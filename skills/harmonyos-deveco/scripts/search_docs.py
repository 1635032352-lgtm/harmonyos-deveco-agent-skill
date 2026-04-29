#!/usr/bin/env python3
"""Search the local HarmonyOS / DevEco / contest documentation index."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCES = SKILL_ROOT / "references"
SQLITE_PATH = REFERENCES / "docs.sqlite"
JSONL_PATH = REFERENCES / "docs-index.jsonl"

TOPIC_ALIASES: dict[str, str] = {
    "arkui": "ArkUI Column Row Stack Flex Grid List ForEach LazyForEach Navigation Tabs TextInput Button Dialog Gesture animation state @State @Builder",
    "arkts": "ArkTS struct @Entry @Component @State @Prop @Link @Provide @Consume @ObservedV2 class interface async Promise import export",
    "module.json5": "module.json5 app.json5 requestPermissions abilities extensionAbilities metadata deviceTypes srcEntry mainElement",
    "permissions": "permission permissions requestPermissions requestPermissionsFromUser authorization privacy reason module.json5 ohos.permission",
    "lifecycle": "UIAbility AbilityStage lifecycle onCreate onDestroy onWindowStageCreate onForeground onBackground Want",
    "routing": "router pushUrl replaceUrl back Navigation NavPathStack page route",
    "network": "Network Kit http request fetch socket WebSocket ohos.permission.INTERNET security config",
    "media": "AVPlayer audio video image camera photoAccessHelper media library picker",
    "storage": "Preferences relationalStore rdb fileIo distributedData cloud storage ArkData",
    "ai": "AI intelligent model inference recognition intent agent speech vision language MindSpore NNRt",
    "distribution": "HAP HAR HSP release AppGallery app packing bundle distribution certificate profile",
    "signing": "signing signature certificate profile p12 csr release debug hapsigntool app signing",
    "hvigor": "hvigor hvigorfile build-profile oh-package assembleHap assembleHqf assembleDevHqf build error DevEco Studio",
    "deveco": "DevEco Studio SDK Node hvigor previewer emulator device run debug build error",
    "kit": "Kit HarmonyOS service Account Map Push Scan Location Wallet AI Ability ArkUI ArkData",
    "contest": "创新赛 极客赛道 Kit 赛题 工具包 一指禅 赋能资料 设计指南 技术咨询 QQ sheet opendoc",
}

SOURCE_ALIASES = {
    "all": None,
    "official": "official",
    "contest": "contest",
    "local": "local-download",
    "official-download": "official-download",
}


def has_cjk(text: str) -> bool:
    return any("\u3400" <= ch <= "\u9fff" for ch in text)


def normalize_fts_query(query: str) -> str:
    parts = re.findall(r"[\w.@#:/%+\-]+|[\u3400-\u9fff]+", query, flags=re.UNICODE)
    safe: list[str] = []
    for part in parts:
        part = part.strip().replace('"', "")
        if part:
            safe.append(f'"{part}"')
    return " OR ".join(safe) if safe else query


def query_terms(query: str) -> list[str]:
    seen: set[str] = set()
    terms: list[str] = []
    for part in re.findall(r"[\w.@#:/%+\-]+|[\u3400-\u9fff]+", query, flags=re.UNICODE):
        part = part.strip().lower()
        if part and part not in seen:
            terms.append(part)
            seen.add(part)
    return terms


def relevance_score(item, terms: list[str], phrase: str) -> int:
    title = str(item["title"] if "title" in item.keys() else item.get("title", ""))
    path = str(item["path"] if "path" in item.keys() else item.get("path", ""))
    content = str(item["content"] if "content" in item.keys() else item.get("content", item.get("snippet", "")))
    title_path = f"{title} {path}".lower()
    haystack = f"{title_path} {content}".lower()
    score = 0
    phrase_l = phrase.strip().lower()
    if phrase_l and phrase_l in title_path:
        score += 120
    if terms and all(term in title_path for term in terms):
        score += 80
    for term in terms:
        if term in title.lower():
            score += 30
        elif term in path.lower():
            score += 20
        elif term in haystack:
            score += 3
    return score


def rerank_results(results: list[dict], query: str) -> list[dict]:
    terms = query_terms(query)
    return sorted(
        results,
        key=lambda item: (-relevance_score(item, terms, query), item.get("rank", 0), item.get("title", "")),
    )


def compact(text: str, limit: int = 260) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:limit] + ("..." if len(text) > limit else "")


def make_snippet(content: str, terms: list[str], limit: int = 360) -> str:
    lowered = content.lower()
    positions = [lowered.find(term.lower()) for term in terms if term]
    positions = [pos for pos in positions if pos >= 0]
    start = max(0, min(positions) - 110) if positions else 0
    return compact(content[start : start + limit], limit)


def selected_columns(conn: sqlite3.Connection) -> str:
    cols = {row[1] for row in conn.execute("PRAGMA table_info(docs)").fetchall()}
    wanted = [
        "title",
        "path",
        "file",
        "url",
        "source",
        "source_kind",
        "catalog",
        "object_id",
        "updated",
        "confidence",
        "notes",
        "topics",
    ]
    return ", ".join(f"d.{name}" for name in wanted if name in cols)


def search_sqlite(query: str, limit: int, source: str | None) -> list[dict]:
    if not SQLITE_PATH.exists():
        return []

    conn = sqlite3.connect(SQLITE_PATH)
    conn.row_factory = sqlite3.Row
    try:
        cols = selected_columns(conn)
        filters = []
        params: list[object] = []
        if source:
            filters.append("d.source = ?")
            params.append(source)
        where_filter = (" AND " + " AND ".join(filters)) if filters else ""

        rows: list[sqlite3.Row] = []
        fts_query = normalize_fts_query(query)
        try:
            rows = conn.execute(
                f"""
                SELECT {cols},
                       snippet(docs_fts, 2, '[', ']', ' ... ', 22) AS snippet,
                       bm25(docs_fts) AS rank
                FROM docs_fts
                JOIN docs d ON d.id = docs_fts.rowid
                WHERE docs_fts MATCH ?{where_filter}
                ORDER BY rank
                LIMIT ?
                """,
                [fts_query, *params, limit],
            ).fetchall()
        except sqlite3.Error:
            rows = []

        if rows and not has_cjk(query):
            return rerank_results([dict(row) for row in rows], query)

        like_terms = [term for term in re.split(r"\s+", query.strip()) if term]
        if not like_terms:
            like_terms = [query.strip()]
        clauses = []
        like_params: list[object] = []
        for term in like_terms:
            clauses.append("(title LIKE ? OR path LIKE ? OR content LIKE ? OR topics LIKE ?)")
            pattern = f"%{term}%"
            like_params.extend([pattern, pattern, pattern, pattern])
        if source:
            clauses.append("source = ?")
            like_params.append(source)

        like_rows = conn.execute(
            f"""
            SELECT {", ".join(name[2:] for name in cols.split(", "))}, content
            FROM docs
            WHERE {" AND ".join(clauses)}
            LIMIT ?
            """,
            [*like_params, limit * 5],
        ).fetchall()
        scored = []
        for row in like_rows:
            score = relevance_score(row, query_terms(query), query)
            scored.append((score, row))
        scored.sort(key=lambda item: item[0], reverse=True)

        results: list[dict] = []
        seen: set[str] = set()
        for score, row in scored[:limit]:
            item = dict(row)
            item["rank"] = -score
            item["snippet"] = make_snippet(row["content"], like_terms)
            item.pop("content", None)
            key = item.get("file") or item.get("url") or item.get("title")
            if key not in seen:
                seen.add(str(key))
                results.append(item)

        if rows:
            for row in rows:
                item = dict(row)
                key = item.get("file") or item.get("url") or item.get("title")
                if key not in seen and len(results) < limit:
                    results.append(item)
                    seen.add(str(key))
        return results
    finally:
        conn.close()


def search_jsonl(query: str, limit: int, source: str | None) -> list[dict]:
    if not JSONL_PATH.exists():
        return []
    terms = [term.lower() for term in re.split(r"\s+", query.strip()) if term]
    results = []
    with JSONL_PATH.open("r", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            if source and record.get("source") != source:
                continue
            haystack = " ".join(
                str(record.get(key, ""))
                for key in ("title", "path", "headings", "symbols", "sample", "topics")
            ).lower()
            score = sum(haystack.count(term) for term in terms)
            if score:
                record["rank"] = -score
                record["snippet"] = compact(record.get("sample", ""))
                results.append(record)
    results.sort(key=lambda item: item["rank"])
    return results[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(description="Search local HarmonyOS, DevEco, ArkTS, ArkUI, and contest docs.")
    parser.add_argument("query", nargs="*", help="Search keywords.")
    parser.add_argument("--limit", type=int, default=8, help="Number of results.")
    parser.add_argument("--json", action="store_true", help="Print JSON lines.")
    parser.add_argument("--source", choices=sorted(SOURCE_ALIASES), default="all", help="Restrict corpus.")
    parser.add_argument("--contest", action="store_true", help="Shortcut for --source contest.")
    parser.add_argument("--topic", choices=sorted(TOPIC_ALIASES), help="Add a HarmonyOS topic query expansion.")
    parser.add_argument("--list-topics", action="store_true", help="Show supported topic names.")
    args = parser.parse_args()

    if args.list_topics:
        for topic in sorted(TOPIC_ALIASES):
            print(topic)
        return 0

    query = " ".join(args.query).strip()
    if args.topic:
        query = f"{query} {TOPIC_ALIASES[args.topic]}".strip()
    if not query:
        parser.error("query is required unless --list-topics is used")

    source = "contest" if args.contest else SOURCE_ALIASES[args.source]
    results = search_sqlite(query, args.limit, source) or search_jsonl(query, args.limit, source)
    if args.json:
        for result in results:
            print(json.dumps(result, ensure_ascii=False))
        return 0 if results else 1

    if not results:
        scope = source or "all sources"
        print(f"No local HarmonyOS docs matched in {scope}. Try fewer keywords, --topic, or --source all.")
        return 1

    for index, result in enumerate(results, start=1):
        print(f"{index}. {result.get('title', '')}")
        print(f"   Source: {result.get('source', '')} / {result.get('source_kind', '')}")
        if result.get("path"):
            print(f"   Path:   {result['path']}")
        if result.get("file"):
            print(f"   File:   {result['file']}")
        if result.get("url"):
            print(f"   URL:    {result['url']}")
        if result.get("confidence"):
            print(f"   Trust:  {result['confidence']} {('- ' + result.get('notes', '')) if result.get('notes') else ''}")
        if result.get("snippet"):
            print(f"   Snip:   {compact(result['snippet'], 340)}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
