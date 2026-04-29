#!/usr/bin/env python3
"""Build a combined local index for HarmonyOS official docs and contest sources."""

from __future__ import annotations

import argparse
import dataclasses
from html.parser import HTMLParser
import json
import re
import shutil
import sqlite3
from pathlib import Path
from typing import Any, Iterable


SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCES = SKILL_ROOT / "references"
DOCS_DIR = REFERENCES / "docs"
DEFAULT_SOURCE_ROOT = Path(r"D:\harmonyOS文档")
DEFAULT_CONTEST_ROOT = DEFAULT_SOURCE_ROOT / "innovation_contest_sources"

TEXT_SUFFIXES = {".md", ".markdown", ".html", ".htm", ".json", ".txt", ".log", ".py"}
CONTEST_RAW_SUFFIXES = {".json", ".pdf", ".md", ".txt"}

CONTEST_META: dict[str, dict[str, str]] = {
    "registration": {
        "title": "2026 HarmonyOS 创新赛报名链接",
        "url": "https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101773710117484023",
        "kind": "huawei-page",
    },
    "kit-list": {
        "title": "2026 HarmonyOS 创新赛极客赛道赛题 Kit 清单",
        "url": "https://docs.qq.com/pdf/DUWFJQkZ5ZkJTcW56",
        "kind": "qq-pdf",
    },
    "one-finger": {
        "title": "2026 HarmonyOS 创新赛极客赛道一指禅",
        "url": "https://docs.qq.com/pdf/DUWRsbHBFS1NjZWpY",
        "kind": "qq-pdf",
    },
    "toolkit": {
        "title": "2026 创新赛极客赛道工具包",
        "url": "https://docs.qq.com/sheet/DUU53eExYcXJuWXV3?aidPos=detail&no_promotion=1&is_blank_or_template=blank&tab=BB08J2",
        "kind": "qq-sheet",
    },
    "team-square": {
        "title": "2026 创新赛极客赛道组队广场",
        "url": "https://docs.qq.com/sheet/DUWR3cGp0TnJzSk1k?aidPos=detail&no_promotion=1&is_blank_or_template=blank&tab=BB08J2",
        "kind": "qq-sheet",
    },
    "enablement": {
        "title": "开发者赋能资料",
        "url": "https://docs.qq.com/sheet/DUVdVUnFzZU1naFd2?aidPos=detail&no_promotion=1&is_blank_or_template=blank&tab=BB08J2",
        "kind": "qq-sheet",
    },
    "design-guide": {
        "title": "HarmonyOS 设计指南",
        "url": "https://developer.huawei.com/consumer/cn/design/",
        "kind": "huawei-page",
    },
    "tech-qa": {
        "title": "2026 创新赛极客赛道技术咨询问题记录",
        "url": "https://docs.qq.com/sheet/DUXNORWtDZU1uSG5U?aidPos=detail&no_promotion=1&is_blank_or_template=blank&tab=BB08J2",
        "kind": "qq-sheet",
    },
}

TOPIC_KEYWORDS: dict[str, tuple[str, ...]] = {
    "ArkUI": ("ArkUI", "Column", "Row", "List", "ForEach", "LazyForEach", "Navigation", "TextInput", "组件", "布局"),
    "ArkTS": ("ArkTS", "@State", "@Prop", "@Entry", "@Component", "interface", "class", "状态"),
    "module.json5": ("module.json5", "requestPermissions", "abilities", "extensionAbilities", "app.json5"),
    "permissions": ("permission", "permissions", "权限", "授权", "requestPermissions", "ohos.permission"),
    "lifecycle": ("UIAbility", "AbilityStage", "onCreate", "onWindowStageCreate", "生命周期"),
    "routing": ("router", "Navigation", "NavPathStack", "pushUrl", "replaceUrl", "路由"),
    "network": ("http", "request", "Network", "WebSocket", "INTERNET", "网络"),
    "media": ("AVPlayer", "audio", "video", "image", "camera", "媒体", "图片"),
    "storage": ("Preferences", "relationalStore", "rdb", "fileIo", "ArkData", "存储"),
    "AI": (
        "AI",
        "智能",
        "模型",
        "MindSpore",
        "识别",
        "意图",
        "Agent Framework",
        "FunctionComponent",
        "CANN",
        "AIPP",
        "Core Speech",
        "SpeechRecognizer",
        "textToSpeech",
        "Core Vision",
        "OCR",
        "textRecognition",
        "Intents Kit",
        "Natural Language",
        "textProcessing",
        "Neural Network Runtime",
        "NNRt",
        "Speech Kit",
        "AICaption",
        "TextReader",
        "Vision Kit",
        "DocumentScanner",
        "CardRecognition",
    ),
    "distribution": ("HAP", "HAR", "HSP", "AppGallery", "release", "发布", "上架"),
    "signing": ("signing", "signature", "certificate", "profile", "签名", "证书"),
    "hvigor": ("hvigor", "hvigorfile", "build-profile", "oh-package", "assemble", "构建"),
    "DevEco Studio": ("DevEco Studio", "SDK", "previewer", "emulator", "真机", "构建错误"),
    "Kit": ("Kit", "Account", "Map", "Push", "Scan", "Location", "Wallet", "Service"),
    "contest": ("创新赛", "极客赛道", "赛题", "工具包", "一指禅", "赋能", "技术咨询"),
}


@dataclasses.dataclass
class Record:
    source: str
    source_kind: str
    title: str
    path: str
    file: str
    url: str
    catalog: str
    object_id: str
    updated: str
    confidence: str
    notes: str
    topics: str
    content: str


class TextHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in {"script", "style", "noscript"}:
            self.skip_depth += 1
        elif tag.lower() in {"p", "div", "section", "article", "br", "li", "tr", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style", "noscript"} and self.skip_depth:
            self.skip_depth -= 1
        elif tag.lower() in {"p", "div", "section", "article", "li", "tr", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)

    def text(self) -> str:
        return compact("\n".join(self.parts), 250000)


def compact(text: str, limit: int = 0) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:limit] if limit and len(text) > limit else text


def read_text(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "cp936"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def repair_mojibake(text: str) -> str:
    if not any(token in text for token in ("鍒", "璧", "楦", "寮€", "瑙")):
        return text
    variants = [text]
    for encoding in ("gb18030", "cp936"):
        try:
            repaired = text.encode(encoding, errors="ignore").decode("utf-8", errors="ignore")
            if len(repaired) > 20:
                variants.append(repaired)
        except UnicodeError:
            pass
    return "\n".join(dict.fromkeys(variants))


def parse_frontmatter(markdown: str) -> tuple[dict[str, str], str]:
    if not markdown.startswith("---"):
        return {}, markdown
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", markdown, flags=re.DOTALL)
    if not match:
        return {}, markdown
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
    return meta, markdown[match.end() :]


def title_from_markdown(content: str, fallback: str) -> str:
    for line in content.splitlines():
        match = re.match(r"^#\s+(.+)$", line.strip())
        if match:
            return match.group(1).strip()
    return fallback


def html_to_text(text: str) -> str:
    parser = TextHTMLParser()
    parser.feed(text)
    return parser.text()


def flatten_json_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        if value.strip():
            yield value.strip()
    elif isinstance(value, dict):
        for key, child in value.items():
            if isinstance(key, str) and key.strip():
                yield key.strip()
            yield from flatten_json_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from flatten_json_strings(child)


def json_to_text(path: Path) -> str:
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError:
        return read_text(path)
    strings: list[str] = []
    seen: set[str] = set()
    for item in flatten_json_strings(data):
        item = compact(item)
        if item and item not in seen:
            strings.append(item)
            seen.add(item)
    return "\n".join(strings)


def pdf_to_text(path: Path) -> tuple[str, str]:
    notes = "PDF text extraction unavailable; raw PDF is indexed by title/path only."
    for module_name in ("pypdf", "PyPDF2"):
        try:
            module = __import__(module_name)
            reader_cls = getattr(module, "PdfReader")
            reader = reader_cls(str(path))
            parts = [(page.extract_text() or "") for page in reader.pages]
            text = "\n".join(parts).strip()
            if text:
                return text, f"PDF text extracted with {module_name}."
        except Exception:
            continue
    return "", notes


def infer_topics(text: str) -> str:
    found = []
    lowered = text.lower()
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(keyword.lower() in lowered for keyword in keywords):
            found.append(topic)
    return ", ".join(found)


def official_records() -> list[Record]:
    records: list[Record] = []
    if not DOCS_DIR.exists():
        return records
    for md in sorted(DOCS_DIR.rglob("*.md")):
        raw = read_text(md)
        meta, body = parse_frontmatter(raw)
        title = meta.get("title") or title_from_markdown(body, md.stem)
        path = meta.get("path") or " / ".join(md.relative_to(DOCS_DIR).parts)
        content = compact(body, 300000)
        file_path = str(md)
        records.append(
            Record(
                source="official",
                source_kind="huawei-doc",
                title=title,
                path=path,
                file=file_path,
                url=meta.get("source", ""),
                catalog=meta.get("catalog", "harmonyos-guides"),
                object_id=meta.get("objectId", md.stem),
                updated=meta.get("updated", ""),
                confidence="high",
                notes="Generated from Huawei developer documentation API into local Markdown.",
                topics=infer_topics(f"{title} {path} {content}"),
                content=content,
            )
        )
    return records


def local_download_records(source_root: Path) -> list[Record]:
    output_dir = source_root / "output"
    records: list[Record] = []
    if not output_dir.exists():
        return records
    for path in sorted(output_dir.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".html", ".htm", ".txt", ".md", ".json"}:
            continue
        raw = read_text(path)
        content = html_to_text(raw) if path.suffix.lower() in {".html", ".htm"} else raw
        content = repair_mojibake(content)
        rel = str(path.relative_to(source_root))
        title = path.stem.replace("_", " ")
        records.append(
            Record(
                source="official-download",
                source_kind=path.suffix.lower().lstrip("."),
                title=title,
                path=f"本地官方下载快照 / {rel}",
                file=str(path),
                url="",
                catalog="local-output",
                object_id=path.stem,
                updated="",
                confidence="medium",
                notes="Local downloaded HTML/text snapshot from D:\\harmonyOS文档\\output; asset-only files are excluded.",
                topics=infer_topics(f"{title} {content}"),
                content=compact(content, 250000),
            )
        )
    return records


def contest_key(path: Path) -> str:
    name = path.name
    for key in CONTEST_META:
        if name.startswith(key):
            return key
    return path.stem.split(".")[0]


def contest_text(path: Path) -> tuple[str, str, str]:
    suffix = path.suffix.lower()
    if suffix in {".html", ".htm"}:
        return html_to_text(read_text(path)), "medium", "HTML page text extracted locally."
    if suffix in {".md", ".markdown", ".txt"}:
        return read_text(path), "medium", "Text extracted by the contest downloader; QQ sheet strings may be noisy."
    if suffix == ".json":
        note = "Raw JSON preserved; string extraction may include QQ sheet layout noise and must not be treated as absolute fact."
        return json_to_text(path), "low" if "opendoc" in path.name else "medium", note
    if suffix == ".pdf":
        text, note = pdf_to_text(path)
        return text, "medium" if text else "low", note
    return "", "low", "Unsupported text extraction."


def contest_records(contest_root: Path) -> list[Record]:
    records: list[Record] = []
    if not contest_root.exists():
        return records
    for path in sorted(contest_root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".md", ".html", ".htm", ".json", ".txt", ".pdf"}:
            continue
        key = contest_key(path)
        meta = CONTEST_META.get(key, {"title": path.stem, "url": "", "kind": "contest-file"})
        text, confidence, notes = contest_text(path)
        text = repair_mojibake(text)
        rel = str(path.relative_to(contest_root)).replace("\\", "/")
        anchor = f"{meta['title']} {key} HarmonyOS 创新赛 极客赛道 Kit 工具包 一指禅 设计指南 技术咨询 QQ sheet opendoc"
        if not text:
            text = anchor
        else:
            text = f"{anchor}\n{text}"
        records.append(
            Record(
                source="contest",
                source_kind=meta.get("kind", "contest-file"),
                title=meta["title"],
                path=f"创新赛资料 / {meta['title']} / {rel}",
                file=str(path),
                url=meta.get("url", ""),
                catalog="innovation-contest",
                object_id=key,
                updated="",
                confidence=confidence,
                notes=notes,
                topics=infer_topics(f"{anchor} {text}"),
                content=compact(text, 250000),
            )
        )
    return records


def copy_contest_raw(contest_root: Path) -> int:
    if not contest_root.exists():
        return 0
    raw_dir = REFERENCES / "contest" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    copied = 0
    for path in sorted(contest_root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in CONTEST_RAW_SUFFIXES:
            continue
        if path.parent.name in {"html"}:
            continue
        rel = path.relative_to(contest_root)
        target = raw_dir / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        copied += 1
    return copied


def headings(content: str) -> list[str]:
    result = []
    for line in content.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+)$", line.strip())
        if match:
            result.append(match.group(2).strip())
    return result[:30]


def symbols(content: str) -> list[str]:
    found = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?\b", content))
    return sorted(token for token in found if len(token) >= 4 and not token.startswith("http"))[:80]


def write_indexes(records: list[Record]) -> None:
    REFERENCES.mkdir(parents=True, exist_ok=True)
    jsonl_path = REFERENCES / "docs-index.jsonl"
    sqlite_path = REFERENCES / "docs.sqlite"

    with jsonl_path.open("w", encoding="utf-8") as handle:
        for record in records:
            sample = compact(record.content, 1400)
            handle.write(
                json.dumps(
                    {
                        "source": record.source,
                        "source_kind": record.source_kind,
                        "title": record.title,
                        "path": record.path,
                        "file": record.file,
                        "url": record.url,
                        "catalog": record.catalog,
                        "objectId": record.object_id,
                        "updated": record.updated,
                        "confidence": record.confidence,
                        "notes": record.notes,
                        "topics": record.topics,
                        "headings": headings(record.content),
                        "symbols": symbols(record.content),
                        "sample": sample,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    if sqlite_path.exists():
        sqlite_path.unlink()
    conn = sqlite3.connect(sqlite_path)
    try:
        conn.execute(
            """
            CREATE TABLE docs (
              id INTEGER PRIMARY KEY,
              source TEXT,
              source_kind TEXT,
              title TEXT,
              path TEXT,
              file TEXT,
              url TEXT,
              catalog TEXT,
              object_id TEXT,
              updated TEXT,
              confidence TEXT,
              notes TEXT,
              topics TEXT,
              content TEXT
            )
            """
        )
        conn.execute("CREATE VIRTUAL TABLE docs_fts USING fts5(title, path, content, source, topics)")
        for index, record in enumerate(records, start=1):
            conn.execute(
                "INSERT INTO docs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    index,
                    record.source,
                    record.source_kind,
                    record.title,
                    record.path,
                    record.file,
                    record.url,
                    record.catalog,
                    record.object_id,
                    record.updated,
                    record.confidence,
                    record.notes,
                    record.topics,
                    record.content,
                ),
            )
            conn.execute(
                "INSERT INTO docs_fts(rowid, title, path, content, source, topics) VALUES (?, ?, ?, ?, ?, ?)",
                (index, record.title, record.path, record.content, record.source, record.topics),
            )
        conn.commit()
    finally:
        conn.close()


def write_summary(records: list[Record], source_root: Path, contest_root: Path, copied_raw: int) -> None:
    counts: dict[str, int] = {}
    kinds: dict[str, int] = {}
    for record in records:
        counts[record.source] = counts.get(record.source, 0) + 1
        kinds[record.source_kind] = kinds.get(record.source_kind, 0) + 1

    lines = [
        "# Docs Build Summary",
        "",
        f"- Total records: {len(records)}",
        f"- Source root scanned: `{source_root}`",
        f"- Contest root scanned: `{contest_root}`",
        f"- Contest raw files copied into `references/contest/raw`: {copied_raw}",
        f"- JSONL index: `docs-index.jsonl`",
        f"- SQLite FTS index: `docs.sqlite`",
        "",
        "## Records By Source",
        "",
    ]
    for source, count in sorted(counts.items()):
        lines.append(f"- {source}: {count}")
    lines.extend(["", "## Records By Kind", ""])
    for kind, count in sorted(kinds.items()):
        lines.append(f"- {kind}: {count}")
    lines.extend(
        [
            "",
            "## Extraction Notes",
            "",
            "- Official docs are generated Markdown copies under `references/docs` and indexed as high-confidence local documentation.",
            "- `D:\\harmonyOS文档\\output` currently contains HTML snapshots plus image assets; image assets are intentionally excluded from the text index.",
            "- QQ sheet `*.opendoc.json` files are preserved as raw sources. Extracted strings can contain layout bytes or mojibake and should be used as search clues, not final facts.",
            "- PDF extraction uses optional local Python PDF libraries when available; otherwise the index retains titles, paths, URLs, and adjacent downloader metadata.",
            "",
        ]
    )
    (REFERENCES / "docs-build-summary.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build local HarmonyOS skill search indexes.")
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--contest-root", type=Path, default=DEFAULT_CONTEST_ROOT)
    parser.add_argument("--skip-official", action="store_true")
    parser.add_argument("--skip-local-output", action="store_true")
    parser.add_argument("--skip-contest", action="store_true")
    parser.add_argument("--no-copy-contest-raw", action="store_true")
    args = parser.parse_args()

    records: list[Record] = []
    if not args.skip_official:
        records.extend(official_records())
    if not args.skip_local_output:
        records.extend(local_download_records(args.source_root))
    if not args.skip_contest:
        records.extend(contest_records(args.contest_root))

    if not records:
        print("No records found; index was not written.")
        return 1

    copied_raw = 0
    if not args.no_copy_contest_raw and not args.skip_contest:
        copied_raw = copy_contest_raw(args.contest_root)

    write_indexes(records)
    write_summary(records, args.source_root, args.contest_root, copied_raw)
    print(f"Indexed {len(records)} records.")
    print(f"Official: {sum(1 for r in records if r.source == 'official')}")
    print(f"Official downloads: {sum(1 for r in records if r.source == 'official-download')}")
    print(f"Contest: {sum(1 for r in records if r.source == 'contest')}")
    print(f"Contest raw copied: {copied_raw}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
