# Docs Build Summary

This GitHub source package intentionally does not commit generated documentation caches, copied official docs, copied contest raw files, `docs.sqlite`, or `docs-index.jsonl`. The counts below describe the local source environment used when the skill was assembled, not files guaranteed to exist after a fresh clone.

- Total records: 5253
- Source root scanned: `D:\harmonyOS文档`
- Contest root scanned: `D:\harmonyOS文档\innovation_contest_sources`
- Contest raw files copied into `references/contest/raw`: 31
- JSONL index: `docs-index.jsonl`
- SQLite FTS index: `docs.sqlite`

## Records By Source

- contest: 39
- official: 5210
- official-download: 4

## Records By Kind

- contest-file: 3
- html: 4
- huawei-doc: 5210
- huawei-page: 6
- qq-pdf: 10
- qq-sheet: 20

## Extraction Notes

- Official docs are generated Markdown copies under `references/docs` and indexed as high-confidence local documentation.
- `D:\harmonyOS文档\output` currently contains HTML snapshots plus image assets; image assets are intentionally excluded from the text index.
- QQ sheet `*.opendoc.json` files are preserved as raw sources. Extracted strings can contain layout bytes or mojibake and should be used as search clues, not final facts.
- PDF extraction uses optional local Python PDF libraries when available; otherwise the index retains titles, paths, URLs, and adjacent downloader metadata.
