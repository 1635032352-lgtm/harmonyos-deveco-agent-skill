#!/usr/bin/env python3
"""Build the HarmonyOS DevEco skill reference corpus from Huawei document APIs."""

from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import html
from html.parser import HTMLParser
import json
import re
import sqlite3
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


API_BASE = "https://svc-drcn.developer.huawei.com/community/servlet/consumer/cn/documentPortal"
PUBLIC_DOC_PREFIX = "https://developer.huawei.com/consumer/cn/doc/"
DOC_HOME = "https://developer.huawei.com/consumer/cn/doc/"
USER_AGENT = "HarmonyOS-deveco-skill-builder/1.0"


@dataclasses.dataclass
class DocNode:
    order: int
    catalog: str
    object_id: str
    title: str
    path: list[str]
    url: str
    doc_id: str = ""


@dataclasses.dataclass
class BuiltDoc:
    node: DocNode
    title: str
    updated: str
    markdown: str
    headings: list[str]
    symbols: list[str]
    url: str
    file: str


class FetchError(RuntimeError):
    pass


class MarkdownHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.in_pre = False
        self.in_code = False
        self.skip_depth = 0

    def emit(self, text: str) -> None:
        if self.skip_depth:
            return
        self.parts.append(text)

    def newline(self, count: int = 1) -> None:
        self.emit("\n" * count)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {key.lower(): value or "" for key, value in attrs}
        tag = tag.lower()
        if tag in {"script", "style"}:
            self.skip_depth += 1
        elif tag in {"p", "div", "section", "article", "blockquote"}:
            self.newline(2 if tag == "section" else 1)
        elif tag in {"br"}:
            self.newline()
        elif re.fullmatch(r"h[1-6]", tag):
            level = int(tag[1])
            self.newline(2)
            self.emit("#" * level + " ")
        elif tag == "li":
            self.newline()
            self.emit("- ")
        elif tag == "pre":
            self.newline(2)
            self.emit("```\n")
            self.in_pre = True
        elif tag == "code" and not self.in_pre:
            self.emit("`")
            self.in_code = True
        elif tag == "tr":
            self.newline()
        elif tag in {"td", "th"}:
            self.emit(" | ")
        elif tag == "img":
            alt = attrs_dict.get("alt") or "image"
            src = attrs_dict.get("src") or ""
            if src:
                self.emit(f"![{alt}]({html.unescape(src)})")
        elif tag == "a" and attrs_dict.get("href") and attrs_dict.get("href").startswith("#"):
            return

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style"} and self.skip_depth:
            self.skip_depth -= 1
        elif re.fullmatch(r"h[1-6]", tag):
            self.newline(2)
        elif tag in {"p", "div", "section", "article", "blockquote", "ul", "ol", "table"}:
            self.newline()
        elif tag == "pre":
            self.emit("\n```\n")
            self.in_pre = False
        elif tag == "code" and self.in_code and not self.in_pre:
            self.emit("`")
            self.in_code = False

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if self.in_pre:
            self.parts.append(data)
        else:
            self.parts.append(re.sub(r"\s+", " ", data))

    def markdown(self) -> str:
        text = "".join(self.parts)
        text = re.sub(r"\[h([1-6])\]\s*", lambda m: "#" * int(m.group(1)) + " ", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{4,}", "\n\n\n", text)
        lines = [line.rstrip() for line in text.splitlines()]
        return "\n".join(lines).strip() + "\n"


def request_json(url: str, payload: dict[str, Any], timeout: int = 60, retries: int = 3) -> dict[str, Any]:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": USER_AGENT,
            "Origin": "https://developer.huawei.com",
            "Referer": DOC_HOME,
        },
    )
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                charset = resp.headers.get_content_charset() or "utf-8"
                return json.loads(resp.read().decode(charset, errors="replace"))
        except (urllib.error.URLError, json.JSONDecodeError) as exc:
            last_error = exc
            time.sleep(1.5 * attempt)
    raise FetchError(f"POST {url} failed: {last_error}")


def public_url(catalog: str, object_id: str) -> str:
    return urllib.parse.urljoin(PUBLIC_DOC_PREFIX, f"{catalog}/{object_id}")


def get_catalog_tree(catalog: str, seed: str, lang: str, show_hide: str) -> dict[str, Any]:
    result = request_json(
        f"{API_BASE}/getCatalogTree",
        {"language": lang, "catalogName": catalog, "objectId": seed, "showHide": show_hide},
    )
    if str(result.get("code")) != "0":
        raise FetchError(f"getCatalogTree({catalog}) failed: {result.get('message')}")
    return result["value"]


def collect_nodes(catalog: str, tree: list[dict[str, Any]]) -> list[DocNode]:
    nodes: list[DocNode] = []
    order = 0

    def walk(items: list[dict[str, Any]], parents: list[str]) -> None:
        nonlocal order
        for item in sorted(items, key=lambda value: value.get("catalogIndex", 0)):
            name = str(item.get("nodeName") or "").strip()
            path = parents + ([name] if name else [])
            object_id = str(item.get("relateDocument") or "").strip()
            if object_id:
                order += 1
                nodes.append(
                    DocNode(
                        order=order,
                        catalog=catalog,
                        object_id=object_id,
                        title=name or object_id,
                        path=path,
                        url=public_url(catalog, object_id),
                        doc_id=str(item.get("relateDocId") or ""),
                    )
                )
            children = item.get("children") or []
            if isinstance(children, list):
                walk(children, path)

    walk(tree, [])
    deduped: dict[tuple[str, str], DocNode] = {}
    for node in nodes:
        deduped.setdefault((node.catalog, node.object_id), node)
    return list(deduped.values())


def extract_body(raw_html: str) -> str:
    match = re.search(r"<body[^>]*>(.*?)</body>", raw_html, flags=re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else raw_html.strip()


def html_to_markdown(raw_html: str) -> str:
    parser = MarkdownHTMLParser()
    parser.feed(extract_body(raw_html))
    return parser.markdown()


def extract_headings(markdown: str) -> list[str]:
    headings = []
    for line in markdown.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+)$", line.strip())
        if match:
            title = re.sub(r"\s+", " ", match.group(2)).strip()
            if title and title not in headings:
                headings.append(title)
    return headings[:40]


def extract_symbols(markdown: str) -> list[str]:
    symbols = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?\b", markdown))
    useful = [s for s in symbols if len(s) >= 4 and not s.startswith("http")]
    return sorted(useful)[:80]


def safe_name(value: str) -> str:
    value = re.sub(r"[^0-9A-Za-z._-]+", "-", value).strip("-")
    return value[:120] or "document"


def build_one(node: DocNode, docs_dir: Path, lang: str, force: bool) -> BuiltDoc:
    target = docs_dir / node.catalog / f"{safe_name(node.object_id)}.md"
    target.parent.mkdir(parents=True, exist_ok=True)

    if target.exists() and not force:
        markdown = target.read_text(encoding="utf-8", errors="replace")
        content_for_index = re.sub(r"^---.*?---\s*", "", markdown, flags=re.DOTALL)
        return BuiltDoc(
            node=node,
            title=node.title,
            updated="",
            markdown=content_for_index,
            headings=extract_headings(content_for_index),
            symbols=extract_symbols(content_for_index),
            url=node.url,
            file=str(target.relative_to(docs_dir.parents[0])).replace("\\", "/"),
        )

    result = request_json(f"{API_BASE}/getDocumentById", {"objectId": node.object_id, "language": lang})
    if str(result.get("code")) != "0":
        raise FetchError(f"getDocumentById({node.object_id}) failed: {result.get('message')}")

    value = result.get("value") or {}
    content = (value.get("content") or {}).get("content") or ""
    markdown = html_to_markdown(content)
    title = str(value.get("title") or node.title or node.object_id)
    updated = str(value.get("displayUpdateTime") or value.get("updatedDate") or "")
    source_url = public_url(str(value.get("catalogName") or node.catalog), str(value.get("fileName") or node.object_id))
    doc_path = " / ".join(part for part in node.path if part)

    full_markdown = "\n".join(
        [
            "---",
            f"title: {title}",
            f"catalog: {node.catalog}",
            f"objectId: {node.object_id}",
            f"path: {doc_path}",
            f"source: {source_url}",
            f"updated: {updated}",
            "---",
            "",
            f"# {title}",
            "",
            f"Source: {source_url}",
            "",
            markdown,
        ]
    )
    target.write_text(full_markdown, encoding="utf-8")
    return BuiltDoc(
        node=node,
        title=title,
        updated=updated,
        markdown=markdown,
        headings=extract_headings(markdown),
        symbols=extract_symbols(markdown),
        url=source_url,
        file=str(target.relative_to(docs_dir.parents[0])).replace("\\", "/"),
    )


def write_indexes(built_docs: list[BuiltDoc], references_dir: Path) -> None:
    jsonl = references_dir / "docs-index.jsonl"
    sqlite_path = references_dir / "docs.sqlite"

    with jsonl.open("w", encoding="utf-8") as handle:
        for doc in sorted(built_docs, key=lambda item: item.node.order):
            sample = re.sub(r"\s+", " ", doc.markdown).strip()[:1200]
            record = {
                "title": doc.title,
                "catalog": doc.node.catalog,
                "objectId": doc.node.object_id,
                "path": " / ".join(doc.node.path),
                "file": doc.file,
                "url": doc.url,
                "updated": doc.updated,
                "headings": doc.headings,
                "symbols": doc.symbols,
                "sample": sample,
            }
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    if sqlite_path.exists():
        sqlite_path.unlink()
    conn = sqlite3.connect(sqlite_path)
    try:
        conn.execute(
            """
            CREATE TABLE docs (
              id INTEGER PRIMARY KEY,
              title TEXT,
              path TEXT,
              file TEXT,
              url TEXT,
              catalog TEXT,
              object_id TEXT,
              updated TEXT,
              content TEXT
            )
            """
        )
        conn.execute("CREATE VIRTUAL TABLE docs_fts USING fts5(title, path, content)")
        for index, doc in enumerate(sorted(built_docs, key=lambda item: item.node.order), start=1):
            path = " / ".join(doc.node.path)
            conn.execute(
                "INSERT INTO docs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (index, doc.title, path, doc.file, doc.url, doc.node.catalog, doc.node.object_id, doc.updated, doc.markdown),
            )
            conn.execute(
                "INSERT INTO docs_fts(rowid, title, path, content) VALUES (?, ?, ?, ?)",
                (index, doc.title, path, doc.markdown),
            )
        conn.commit()
    finally:
        conn.close()

    summary = references_dir / "docs-build-summary.md"
    summary.write_text(
        "\n".join(
            [
                "# Docs Build Summary",
                "",
                f"- Documents: {len(built_docs)}",
                f"- JSONL index: `{jsonl.name}`",
                f"- SQLite index: `{sqlite_path.name}`",
                "- Image-heavy content is represented by Markdown image links; images are not bundled into the skill.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build local HarmonyOS guide references for the skill.")
    parser.add_argument("--catalog", default="harmonyos-guides", help="Catalog name.")
    parser.add_argument("--seed", default="start-overview", help="Seed objectId for getCatalogTree.")
    parser.add_argument("--lang", default="cn", help="Document language.")
    parser.add_argument("--show-hide", default="0", choices=["0", "1", "2"], help="Huawei catalog visibility flag.")
    parser.add_argument("--max-pages", type=int, default=0, help="Limit pages for testing.")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent document fetches.")
    parser.add_argument("--force", action="store_true", help="Refetch documents even if Markdown exists.")
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    references_dir = skill_root / "references"
    docs_dir = references_dir / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading catalog tree: {args.catalog} (seed: {args.seed})")
    tree_value = get_catalog_tree(args.catalog, args.seed, args.lang, args.show_hide)
    nodes = collect_nodes(args.catalog, tree_value.get("catalogTreeList") or [])
    if args.max_pages:
        nodes = nodes[: args.max_pages]
    print(f"Document nodes: {len(nodes)}")

    built_docs: list[BuiltDoc] = []
    failures: list[str] = []
    started = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        future_map = {executor.submit(build_one, node, docs_dir, args.lang, args.force): node for node in nodes}
        for done_count, future in enumerate(concurrent.futures.as_completed(future_map), start=1):
            node = future_map[future]
            try:
                doc = future.result()
                built_docs.append(doc)
            except Exception as exc:
                failures.append(f"{node.object_id}: {exc}")
            if done_count == 1 or done_count % 25 == 0 or done_count == len(nodes):
                elapsed = time.time() - started
                print(f"[{done_count}/{len(nodes)}] built={len(built_docs)} failed={len(failures)} elapsed={elapsed:.1f}s")
                sys.stdout.flush()

    if not built_docs:
        print("No documents were built.", file=sys.stderr)
        return 1

    built_docs.sort(key=lambda item: item.node.order)
    print("Writing indexes...")
    write_indexes(built_docs, references_dir)
    if failures:
        fail_path = references_dir / "docs-build-failures.txt"
        fail_path.write_text("\n".join(failures), encoding="utf-8")
        print(f"Failures: {len(failures)} ({fail_path})", file=sys.stderr)
    print(f"Done. Built {len(built_docs)} documents in {references_dir}")
    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
