# HarmonyOS DevEco Codex Skill

Codex skill package for HarmonyOS / DevEco Studio work. It turns product ideas, UI plans, screenshots, ArkUI implementation tasks, build errors, signing checks, and device evidence requests into small, explicit checkpoints.

## What Is Included

- `skills/harmonyos-deveco/`: the main Codex skill, references, scripts, and OpenAI agent metadata.
- `prompts/harmonyos-*.md`: slash prompt shims for low-friction commands.
- `.codex-plugin/plugin.json`: plugin manifest for Codex plugin packaging.
- `scripts/install.ps1`: local installer for skills and prompt shims.
- `scripts/validate-package.ps1`: repository structure validator.

Large generated documentation caches are intentionally not committed:

- `skills/harmonyos-deveco/references/docs/`
- `skills/harmonyos-deveco/references/contest/raw/`
- `skills/harmonyos-deveco/references/docs.sqlite`
- `skills/harmonyos-deveco/references/docs-index.jsonl`

Regenerate those locally if you need offline HarmonyOS doc search.

## Slash Commands

| Command | Purpose |
| --- | --- |
| `/harmonyos-ideal` | Capture product promise, target user, scene, temperament, non-goals, and evidence target. |
| `/harmonyos-ux` | Map first viewport, core journey, pages, states, entry points, and safety gates. |
| `/harmonyos-system` | Produce ArkUI-ready design tokens, accessibility, dark mode, motion, and component roles. |
| `/harmonyos-arkui` | Convert product/UI/design context into an ArkUI Landing Contract. |
| `/harmonyos-implement` | Make focused ArkTS/ArkUI changes in a DevEco project. |
| `/harmonyos-verify` | Check build, signing, Preview, device, route, permission, and artifact evidence. |
| `/harmonyos-report` | Write a concise handoff report with changed files, evidence, and remaining risks. |
| `/harmonyos-fix` | Debug build/runtime/signing/permission/resource/navigation errors. |
| `/harmonyos-contest` | Plan HarmonyOS innovation contest work with contest-aware Kit/API constraints. |
| `/harmonyos-all` | Run the full path only when the user explicitly wants it. |

## Install Locally

From this repository root:

```powershell
.\scripts\install.ps1
```

To install into a custom Codex home:

```powershell
.\scripts\install.ps1 -CodexHome "C:\Users\you\.codex"
```

The installer copies:

- `skills/harmonyos-deveco` to `$CodexHome\skills\harmonyos-deveco`
- `prompts/harmonyos-*.md` to `$CodexHome\prompts`

Restart or reopen Codex if newly added slash prompts are not visible immediately.

## Optional Local Docs Index

If you have a local HarmonyOS documentation corpus, rebuild the searchable index from the repository root:

```powershell
python .\skills\harmonyos-deveco\scripts\build_local_index.py --source-root "D:\harmonyOS文档"
```

Then use:

```powershell
python .\skills\harmonyos-deveco\scripts\search_docs.py "module.json5 permissions"
```

The generated docs and indexes are ignored by Git by default.

## Validate Before Publishing

```powershell
.\scripts\validate-package.ps1
```

Expected result:

```text
PACKAGE_CHECK PASS
```

## Publish To GitHub

```powershell
git init
git add .
git commit -m "feat: add HarmonyOS DevEco Codex skill"
git branch -M main
git remote add origin https://github.com/1635032352-lgtm/harmonyos-deveco-codex-skill.git
git push -u origin main
```

If the remote repository does not exist yet, create an empty GitHub repository named `harmonyos-deveco-codex-skill` first, then run the remote/push commands.
