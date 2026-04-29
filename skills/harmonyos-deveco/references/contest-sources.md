# Innovation Contest Sources

Use this file first when the user asks about the HarmonyOS innovation contest, contest project planning, Kit selection, design constraints, enablement materials, toolkits, or technical Q&A.

## Source Inventory

Archive root: `D:\harmonyOS文档\innovation_contest_sources`

Raw copies inside this skill: `C:\Users\cjh16\.codex\skills\harmonyos-deveco\references\contest\raw`

| Topic | Source URL | Local material |
| --- | --- | --- |
| 2026 HarmonyOS 创新赛报名链接 | `https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101773710117484023` | `html/registration.html`, `text/registration.txt`, `markdown/registration.md` |
| 赛题 Kit 清单 | `https://docs.qq.com/pdf/DUWFJQkZ5ZkJTcW56` | `pdf/kit-list.pdf`, `json/kit-list.pdf-data.json`, `html/kit-list.html`, `markdown/kit-list.md` |
| 一指禅 | `https://docs.qq.com/pdf/DUWRsbHBFS1NjZWpY` | `pdf/one-finger.pdf`, `json/one-finger.pdf-data.json`, `html/one-finger.html`, `markdown/one-finger.md` |
| 极客赛道工具包 | `https://docs.qq.com/sheet/DUU53eExYcXJuWXV3?aidPos=detail&no_promotion=1&is_blank_or_template=blank&tab=BB08J2` | `json/toolkit.opendoc.json`, `text/toolkit.strings.txt`, `markdown/toolkit.md`, `html/toolkit.html` |
| 组队广场 | `https://docs.qq.com/sheet/DUWR3cGp0TnJzSk1k?aidPos=detail&no_promotion=1&is_blank_or_template=blank&tab=BB08J2` | `json/team-square.opendoc.json`, `text/team-square.strings.txt`, `markdown/team-square.md`, `html/team-square.html` |
| 开发者赋能资料 | `https://docs.qq.com/sheet/DUVdVUnFzZU1naFd2?aidPos=detail&no_promotion=1&is_blank_or_template=blank&tab=BB08J2` | `json/enablement.opendoc.json`, `text/enablement.strings.txt`, `markdown/enablement.md`, `html/enablement.html` |
| HarmonyOS 设计指南 | `https://developer.huawei.com/consumer/cn/design/` | `html/design-guide.html`, `text/design-guide.txt`, `markdown/design-guide.md` |
| 技术咨询问题记录 | `https://docs.qq.com/sheet/DUXNORWtDZU1uSG5U?aidPos=detail&no_promotion=1&is_blank_or_template=blank&tab=BB08J2` | `json/tech-qa.opendoc.json`, `text/tech-qa.strings.txt`, `markdown/tech-qa.md`, `html/tech-qa.html` |

## Search Strategy

Run contest-only search before answering contest-specific questions:

```powershell
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "创新赛 Kit" --source contest
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "技术咨询 构建错误" --source contest
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "设计指南 HarmonyOS" --source contest
```

Use official docs after contest search to verify APIs, config fields, permissions, and sample code:

```powershell
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "Kit name permissions sample" --source official
```

## Reliability Rules

- Treat QQ sheet `*.opendoc.json` as preserved raw evidence, but not clean final prose.
- Treat `text/*.strings.txt` and generated `markdown/*.md` for QQ sheets as noisy search material; they may contain layout bytes, mojibake, duplicated strings, and partial rows.
- Do not quote garbled strings as facts. Use them to discover names, links, and topics, then verify against PDFs, raw JSON, official docs, or the source URL.
- PDFs are preserved as original files. If PDF text extraction is unavailable, rely on path/title/adjacent metadata and manually inspect the PDF when the exact content matters.
- If a source requires login or authenticated export, say the local archive is incomplete and ask the user for an exported CSV/XLSX/PDF if exact rows are needed.

## Project Advice Pattern

When turning contest material into a project plan, answer in this order:

1. Contest fit: target user, scenario, and which Kit/tool/design constraint supports it.
2. Technical route: ArkUI pages, data model, Kit/API integration, permissions, storage/network/media needs.
3. Prototype slice: smallest demo that proves the contest value.
4. Risk list: unclear source rows, device/API dependency, signing/service enablement, privacy permission, performance.
5. Validation: local build, real device test, contest material cross-check, and demo script.
