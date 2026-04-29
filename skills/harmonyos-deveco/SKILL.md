---
name: harmonyos-deveco
description: Use when building, designing, modifying, debugging, packaging, signing, or validating HarmonyOS / DevEco Studio apps; when translating ideal product ideas, UI/UX concepts, screenshots, or design systems into ArkUI/ArkTS; or when verifying HarmonyOS APIs, permissions, routes, resources, hvigor builds, signed HAPs, and device evidence.
---

# HarmonyOS DevEco

## Core Mission

Use this skill as a HarmonyOS product-realization partner: help the user turn an ideal software feeling into a concrete, high-quality DevEco Studio app. The work is not complete at "ArkTS code exists"; it should preserve product temperament, target user, usage scene, UI/UX system, ArkUI ownership, build/signing correctness, and honest device or Preview evidence.

For product/UI/interface requests, do not force the full path into one painful turn. Prefer the smallest slash-command checkpoint that advances the work:

`/harmonyos-ideal -> /harmonyos-ux -> /harmonyos-system -> /harmonyos-arkui -> /harmonyos-implement -> /harmonyos-verify -> /harmonyos-report`

Use `/harmonyos-all` only when the user explicitly wants the whole path in one run or has already supplied enough staged context.

Keep the detailed rules in references. Load only the reference needed for the current phase.

## Request Intent Distillation
This skill is for product realization, not just ArkTS generation. When the user says the software exists in their head, or asks for an ideal HarmonyOS product, distill the request into:

- product temperament, target user, use scene, main job, emotional tone, quality bar, and non-goals;
- information architecture, core workflow, entry discoverability, states, and interaction rhythm;
- visual direction and design-system roles that can become ArkUI tokens, components, resources, and motion;
- HarmonyOS landing facts: routes, permissions, resources, build mode, signing path, and device evidence.

Do not copy raw chat into the skill or project docs. Preserve reusable decisions, implementation contracts, and verification evidence.

## First Moves

1. Inspect the project before editing: `oh-package.json5`, `build-profile.json5`, `hvigorfile.ts`, `AppScope/app.json5`, `entry/src/main/module.json5`, `entry/src/main/ets`, `entry/src/main/resources`, and existing router/store/helper files.
2. If the task is product/UI/interface/ideal-software work, do not jump straight to ArkTS. Run the **Ideal-to-HarmonyOS Workflow** first, then implement only after product feel, information architecture, UI system, ArkUI translation, and verification path are clear.
3. Identify the app model, API version, module name, bundle name, permissions, signing profile, navigation style, state pattern, and current ArkTS/ArkUI conventions.
4. Search local docs before answering concrete API, Kit, config, compatibility, permission, signing, route, or build-error questions. Do not rely on memory for HarmonyOS APIs.
5. Open only the relevant reference file and the top search hits. Keep this skill as a lookup system, not a large preloaded manual.

## Request Routing

- Slash-command request: run only the named checkpoint unless the user asks to continue. Each checkpoint must leave a reusable artifact for the next one.
- Vague ideal-product request: read `references/ideal-to-harmonyos-workflow.md`; produce or infer a Product Ideal Packet before any code.
- UI/UX or visual-quality request: read `references/arkui-design-system.md` and `references/arkui-ui-quality-checklist.md`; translate design decisions into ArkUI owners.
- Companion workflow request mentioning `ui-ux-pro-max`, `gstack`, or `superpowers`: read `references/gstack-superpowers-integration.md`; use one shared contract instead of separate reports.
- Build, signing, permission, Kit, route, resource, SDK, or hvigor request: use local docs search and the DevEco debugging references before changing product code.
- Screenshot/design/text-to-code request: extract observed layout, inferred states, token roles, component split, route/resource needs, and validation gaps before editing ArkTS.

## Pain-Free Slash Commands

These slash commands are lightweight entry points into the same skill, not separate standards. They exist so the user can ask for one non-painful slice instead of the entire ideal-to-release pipeline.

| Command | Use When | Output |
| --- | --- | --- |
| `/harmonyos-ideal` | The idea is fuzzy, emotional, or still "in the user's head". | Product Ideal Packet: promise, target user, scene, temperament, first value, non-goals, safety boundaries, and evidence target. |
| `/harmonyos-ux` | Product direction exists but the flow, pages, states, or navigation are unclear. | UX Map: first viewport, core journey, page inventory, state matrix, entry points, back paths, and preview/confirmation/undo rules. |
| `/harmonyos-system` | The app needs visual direction or a design system before ArkUI code. | ArkUI-ready design system: semantic color, type, spacing, radius, elevation, motion, accessibility, dark mode, and component roles. |
| `/harmonyos-arkui` | A product/UI/design packet exists and needs to become implementation ownership. | ArkUI Landing Contract: tokens, page structure, component split, state owners, routes, resources, permissions/config, and validation plan. |
| `/harmonyos-implement` | The ArkUI contract is clear enough to edit the DevEco project. | Focused ArkTS/ArkUI changes that follow local project conventions and keep build/config impacts explicit. |
| `/harmonyos-verify` | Code, config, routes, permissions, build, signing, Preview, or device evidence must be checked. | Evidence matrix with exact commands, artifacts, timestamps, PASS/CONDITIONAL PASS/BLOCKED status, and smallest next verification step. |
| `/harmonyos-report` | A phase is done and needs a concise handoff. | Completion report tying product ideal, UX, ArkUI ownership, changed files, validation evidence, and remaining risks together. |
| `/harmonyos-fix` | Build/runtime/signing/permission/resource/navigation errors appear. | Root-cause note, matched docs/search terms, minimal patch plan, rerun command, and remaining blockers. |
| `/harmonyos-contest` | The app is for the HarmonyOS innovation contest. | Contest-aware route: user value, relevant Kit/API candidates, prototype pages, demo data, source constraints, and validation plan. |
| `/harmonyos-all` | The user explicitly wants the full path or provides staged inputs for all phases. | Run the checkpoints in order, but pause or label assumptions when a missing decision would change product shape, architecture, or evidence. |

Command rules:

- One command equals one checkpoint. Do not silently expand `/harmonyos-ideal` into implementation or `/harmonyos-implement` into release readiness.
- If a previous checkpoint artifact is missing, infer only low-risk defaults. Ask one direct question only when the answer changes product shape, architecture, permissions, signing, or acceptance evidence.
- Preserve the original evidence honesty rules. `/harmonyos-report` cannot upgrade a static review into Preview, device, signed HAP, or submit-ready proof.
- If the user gives a non-command request, choose the nearest slash checkpoint internally and name it in the response.

## Ideal-to-HarmonyOS Workflow

Use this workflow for requests like "help me design the software in my head", "design a HarmonyOS interface", "turn this UI plan into ArkUI", "implement this product page in ArkTS", "make my ideal software a runnable HarmonyOS project", or "improve this HarmonyOS app's interface quality, interaction, and architecture".

Do not preserve raw chat history in this skill. Distill recurring user intent into durable inputs: product temperament, target user, usage scene, visual direction, interaction rhythm, implementation artifacts, and verification gates.

Default stance for product/UI requests:

- Treat the request as product realization, not only ArkTS output.
- When the user provides staged prompt files, window reports, or phase labels, treat them as orchestration artifacts: read the specified inputs, preserve previous phase conclusions, execute the requested phase, and write the requested report without silently upgrading conditional evidence.
- Capture the intended product feeling before selecting widgets.
- Make the design system executable by translating it into ArkUI tokens, components, states, routes, resources, and validation gates.
- Keep visual/device evidence honest: do not call a viewport, Preview, device, signing, or build check complete unless it was actually run in that exact environment.

1. **Capture the ideal before coding.** Clarify product feeling, target users, usage context, first-run moment, main task, emotional tone, quality bar, and what must not happen. If `superpowers` brainstorming/spec/plan/TDD/verification workflows are installed, available, or explicitly requested, use them to structure this phase.
2. **Create or reuse the design system.** If `ui-ux-pro-max` is installed, available, or explicitly requested, use it for UI/UX system decisions. Otherwise follow `references/arkui-design-system.md` to define colors, typography, spacing, radius, elevation, motion, accessibility, dark mode, and responsive behavior.
3. **Translate design to ArkUI before implementation.** Convert the product plan into ArkUI tokens, page hierarchy, reusable components, state model, navigation, resources, assets, motion, responsive rules, preview/confirmation gates, and validation gates. Read `references/ideal-to-harmonyos-workflow.md` and `references/arkui-design-system.md` when the task has any UI/product ambiguity.
4. **Implement in ArkTS/ArkUI.** Keep UI logic componentized, avoid hard-coded styling drift, and follow project conventions. Verify HarmonyOS APIs, Kits, permissions, routes, resources, build commands, and signing with local docs search before asserting specifics.
5. **Validate with build, signing, and visual QA.** Use DevEco/hvigor checks when practical. Treat unsigned HAP, signed HAP, signing profile, exact device/viewport evidence, and Preview screenshots as separate validation facts. If `gstack` is installed, available, or explicitly requested, use it for design comparison, browser/preview-like QA where applicable, screenshots, responsive checks, and regression evidence. Read `references/gstack-superpowers-integration.md` for orchestration.
6. **Return an implementation contract.** For product/UI work, final outputs should connect the original ideal to concrete screens, ArkUI tokens/components, changed files, validation evidence, and remaining device/API risks.

## When to Read References

- `references/ideal-to-harmonyos-workflow.md`: read for vague software ideas, product feel, UI/UX planning, information architecture, or idea-to-implementation handoffs.
- `references/arkui-design-system.md`: read when defining or translating design tokens, layouts, components, responsive behavior, dark mode, accessibility, or motion into ArkUI.
- `references/arkui-ui-quality-checklist.md`: read before UI implementation, before final review, or when fixing visual/interaction quality issues.
- `references/gstack-superpowers-integration.md`: read when the user mentions `ui-ux-pro-max`, `gstack`, `superpowers`, brainstorming/spec/plan/TDD/verification, visual previews, screenshots, or multi-tool workflow coordination.
- `references/workflows.md` and `references/common-errors.md`: read when the ideal-to-app task reaches DevEco build, release, signing, permissions, SDK path, hvigor, HAP output, or device validation.
- If a companion skill is named but not available in the current runtime, preserve the same checkpoint manually, say it was not loaded, and keep HarmonyOS API/config/build truth inside this skill.

## Product/UI Trigger Rules

Treat mixed requests like `产品理想设计 + HarmonyOS 落地`, `UI/UX design system -> ArkUI`, or `brainstorming -> DevEco runnable app` as first-class triggers for this skill. The expected output is not a loose design note; it is a path from ideal capture to ArkUI artifacts and verification evidence.

Use the ideal workflow automatically when the user asks for any of these outcomes, even if they do not name this skill explicitly:

- "帮我把脑海中的软件设计出来" or similar ideal-product phrasing.
- "帮我设计 HarmonyOS 软件界面" or any HarmonyOS UI/UX/interface request.
- "把这个 UI 方案落到 ArkUI" or design-to-ArkUI translation.
- "用 ArkTS 实现这个产品页面" or product page implementation.
- "把 ideal 软件变成可运行 HarmonyOS 项目" or idea-to-DevEco delivery.
- "优化这个 HarmonyOS 应用的界面质感、交互和架构" or visual/interaction/architecture polish.
- "先不要直接写代码，先帮我澄清产品感觉" or any request to capture product temperament before implementation.
- "从 UI/UX 设计系统到 ArkUI tokens、页面、组件、状态和动效" or design-system-to-code phrasing.
- "把截图/设计稿/文字描述转成 ArkTS 页面" or screenshot/spec/text-to-ArkUI work.

Mode selection:

- For vague product/UI requests, start with ideal capture and design structure before edits.
- For an approved design/spec, read the relevant reference and translate directly to ArkUI implementation.
- For pure build, signing, permission, Kit, route, or runtime errors, use the normal DevEco debugging flow and verify concrete API/config facts with local docs search.
- For screenshot/design/spec-to-code work, extract layout, tokens, components, missing states, and responsive behavior before writing ArkTS.
- For implementation requests with insufficient product direction, ask only the few questions that would change the product shape; otherwise state assumptions and proceed.
- For requests that combine "design my ideal software" and "make it run", produce a compact implementation contract first, then execute it through ArkTS edits and DevEco validation.
- For visual acceptance work, record the exact tested device, viewport, Preview surface, screenshot source, and build command. If exact evidence is unavailable, report the result as conditional rather than silently upgrading confidence.
- For submit-ready or release-like claims, distinguish `entry-default-unsigned.hap` from `entry-default-signed.hap`, check the current project's `build-profile.json5`, and never infer signing from a successful build alone.
- If DevEco, SDK, signing, device, or Preview validation is blocked by environment, keep the result as `CONDITIONAL PASS` or `BLOCKED`, record the exact command/error/artifact timestamps, and identify the smallest next verification step.

## Pre-Code Gate
For product, UI, interface, or ideal-software requests, do not begin ArkTS edits until you can state both:

- Product Ideal Packet: target user, scene, primary job, product temperament, visual direction, interaction rhythm, non-goals, and success evidence.
- ArkUI Landing Contract: tokens, page structure, component split, state matrix, navigation, resources, permission/config needs, and verification plan.

If the user has already supplied enough context, state the assumptions and proceed. Ask only questions that would change the design direction, architecture, or acceptance evidence.

## Ideal-To-Implementation Contract

For HarmonyOS UI/product work, keep a compact contract visible before and after implementation:

- **Product ideal:** what the user wants the product to feel like, who it serves, when it is opened, and what quality would make it recognizable.
- **UX structure:** first viewport, main path, secondary paths, information architecture, state matrix, and preview/confirmation/undo boundaries.
- **Design system:** semantic color/type/spacing/radius/elevation/motion/accessibility/dark-mode roles, with an ArkUI owner for each.
- **ArkUI plan:** page files, component files, services/models, route/resource/config changes, permission/signing/build impacts, and validation commands.
- **Evidence:** docs searched for concrete APIs/config, exact build/test commands, signed/unsigned artifact state, and screenshot/device/Preview evidence when visual quality is claimed.

Use `references/ideal-to-harmonyos-workflow.md` for the detailed contract, `references/arkui-design-system.md` for token translation, and `references/arkui-ui-quality-checklist.md` for the final quality pass.

## Companion Skill Handshake

When the user wants `ui-ux-pro-max + gstack + superpowers + harmonyos-deveco`, keep the responsibilities explicit:

- `superpowers`: brainstorming/spec/plan/TDD/verification discipline.
- `ui-ux-pro-max`: professional UI/UX system, product tone, color, type, layout, accessibility, interaction quality.
- `harmonyos-deveco`: HarmonyOS truth, ArkUI/ArkTS implementation, `module.json5`, `app.json5`, resources, routes, permissions, hvigor, signing, artifacts, and device/Preview validation.
- `gstack`: visual QA, screenshot comparison, responsive checks, and regression evidence when a runnable or previewable surface exists.

Do not let companion tools invent HarmonyOS APIs, and do not let HarmonyOS implementation skip product ideal capture when the task is experience-oriented. If a companion skill is unavailable, preserve the checkpoint manually and label the evidence as static or conditional.

## Local Search

Use `scripts/search_docs.py` first for official docs and contest archives:

```powershell
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "module.json5 permissions"
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "ArkUI List ForEach" --topic arkui
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "hvigor signing release" --topic signing
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "HarmonyOS innovation contest Kit" --source contest
```

Search result fields:

- `Source`: `official`, `official-download`, or `contest`.
- `Trust`: confidence and extraction notes. Treat QQ sheet extracted strings as noisy clues.
- `File`: local file path to open when a result is relevant.

GitHub package note: generated docs, raw contest archives, `docs.sqlite`, and `docs-index.jsonl` are intentionally not committed. If local search returns no results after installing from GitHub, rebuild the local index with `scripts/build_local_index.py` against your own HarmonyOS documentation corpus.

## Reference Map

- `references/topic-map.md`: choose search terms and topics for HarmonyOS SDK areas.
- `references/workflows.md`: common project workflows: pages, permissions, Kits, build, signing, release, contest planning.
- `references/project-structure.md`: DevEco Studio project layout and key config files.
- `references/arkts-patterns.md`: ArkTS/ArkUI implementation patterns and code review risks.
- `references/ideal-to-harmonyos-workflow.md`: ideal product capture, UI planning, ArkUI translation, and implementation handoff workflow.
- `references/arkui-design-system.md`: HarmonyOS/ArkUI design token and component translation guidance.
- `references/arkui-ui-quality-checklist.md`: UI quality gates, responsive checks, accessibility, anti-patterns, and validation checklist.
- `references/gstack-superpowers-integration.md`: how to combine ui-ux-pro-max, gstack, superpowers, and this skill without role confusion.
- `references/common-errors.md`: build/runtime/debugging checklist and local hvigor environment hints.
- `references/ai-kits.md`: AI Kit selection and integration notes for Agent Framework, CANN, Core Speech, Core Vision, Intents, MindSpore Lite, Natural Language, NNRt, Speech, and Vision.
- `references/contest-sources.md`: innovation contest source inventory and usage strategy.
- `references/docs-build-summary.md`: generated index counts and extraction limitations.
- `references/docs.sqlite` / `references/docs-index.jsonl`: machine-searchable local index.
- `references/docs/`: generated official Huawei Markdown docs; open only matched files.
- `references/contest/raw/`: copied raw contest PDFs, QQ opendoc JSON, extracted text/markdown snapshots.

## Engineering Rules

- Prefer official DevEco Studio / ArkTS / ArkUI patterns and the project's existing style.
- For ideal/software/UI tasks, produce a design and implementation plan before editing code unless the user explicitly asks for immediate code changes.
- Translate UI decisions into semantic ArkUI tokens, reusable components, page structure, state, navigation, resources, motion, dark mode, accessibility, responsive behavior, and validation steps before writing page code.
- Keep page files focused. Extract repeated UI blocks and state-heavy widgets into components or services that match the local project style.
- Treat hard-coded colors, font sizes, spacing, route strings, oversized page files, hidden state coupling, layout overflow, tiny touch targets, low-contrast text, inaccessible states, and decorative low-quality motion as review risks.
- Keep the user's product ideal as the design acceptance test: a technically correct page is not complete if it misses the intended product feeling, workflow, or quality bar.
- Keep platform capabilities in `module.json5`, `app.json5`, `build-profile.json5`, `oh-package.json5`, resources, and module boundaries instead of scattering config through page code.
- For AI Kit tasks, read `references/ai-kits.md` first, then search the exact Kit/capability name. Use `--topic ai` only for broad exploration.
- For system resources, verify both manifest permission and runtime authorization flow.
- Treat FA model, legacy JS examples, and older API snippets as legacy unless the project already uses them.
- When local docs do not hit, say what is uncertain and propose the verification path instead of inventing API names.
- For build issues, check SDK paths, DevEco bundled Node, hvigor, `oh-package`, `module.json5`, `app.json5`, signing profile, permissions, and API version before changing application logic.
- For signing/release work, do not output `storePassword` or `keyPassword`; report only whether required fields exist, whether a matching `signingConfig` is present, and whether signed/unsigned HAP artifacts were actually generated.

## Contest Rule

If the user is building for the HarmonyOS innovation contest, read `references/contest-sources.md` first, then search with `--source contest`. Use contest Kit lists, design guidance, toolkits, enablement materials, and technical Q&A as constraints when proposing architecture, features, or implementation priorities.

## Validation

For code edits, run the project's existing build/check command when practical. If the build tool is unavailable, inspect ArkTS, JSON5, imports, resource references, permissions, and changed navigation paths, then state what still needs DevEco/device validation.




