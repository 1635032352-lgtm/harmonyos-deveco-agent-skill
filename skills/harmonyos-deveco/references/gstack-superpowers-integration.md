# GStack, Superpowers, UI/UX, and HarmonyOS Integration

Use this reference when the user wants combined product thinking, UI/UX design, process control, visual QA, and HarmonyOS implementation.

## Table of Contents

- Product-Ideal Request Routing
- Shared Workflow Promise
- Trigger Behavior for Ideal-to-Implementation Requests
- Default Companion Combination
- Progress Reporting For Long Windows
- Single Shared Contract
- Role Boundaries
- Recommended Orchestration
- Installed-Tool Behavior
- Handoff Contracts
- Request-Type Pipelines
- Validation Matrix
- Multi-Window Handoff Discipline
- Boundaries
- Security Boundary For AI-Enabled HarmonyOS Apps
- Companion Skill Availability Rule
- Companion Sequencing Shortcut

## Product-Ideal Request Routing

When the user asks to design an ideal HarmonyOS product, route the work by responsibility:

- Use brainstorming/spec/plan discipline to clarify the product feeling, target user, scenario, non-goals, and acceptance criteria before edits.
- Use UI/UX design intelligence to choose visual direction, design tokens, component behavior, accessibility, and interaction quality.
- Use harmonyos-deveco to translate the design into ArkUI tokens, page structure, ArkTS components, routes, resources, permissions, signing/build requirements, and device validation.
- Use gstack-style visual QA when practical to compare intended design against rendered evidence, screenshots, responsive behavior, and regressions.

If one companion skill is unavailable, keep the same checkpoint manually and label the evidence as static rather than tool-backed.

## Shared Workflow Promise

The user's expected combined flow is a single path, not four independent tool invocations:

`superpowers brainstorming/spec -> ui-ux-pro-max design system -> harmonyos-deveco ArkUI/DevEco landing -> gstack visual QA when available -> superpowers verification discipline`

Use the path when the request is phrased as "my ideal software", "product feeling", "HarmonyOS UI", "ArkUI landing", "DevEco runnable project", or "make this app feel high quality". The final answer should explain the current phase and evidence state, not merely list which tools were mentioned.

## Trigger Behavior for Ideal-to-Implementation Requests

When a HarmonyOS request combines product feeling, UI design, and implementation, run the companion-style checkpoints even if the user does not name every tool:

- Brainstorming/spec checkpoint: clarify the product promise, target user, scene, non-goals, first valuable action, and acceptance criteria.
- UI/UX checkpoint: define visual direction, token roles, component behavior, accessibility, responsive behavior, dark mode, and interaction rhythm.
- ArkUI translation checkpoint: map the design to tokens, pages, components, states, routes, resources, permissions/config impact, and validation gates.
- Implementation checkpoint: edit ArkTS/ArkUI/DevEco files with project conventions and verified platform details.
- Verification checkpoint: run build/checks when practical, collect visual evidence when available, and label any unverified device/viewport result as conditional.

This keeps the work from collapsing into either generic product advice or ungrounded ArkTS code. `harmonyos-deveco` remains responsible for the final HarmonyOS implementation contract and DevEco validation.
## Default Companion Combination

When the user explicitly wants `ui-ux-pro-max` + `gstack` + `superpowers` + `harmonyos-deveco`, use a single shared contract rather than four separate reports:

- Superpowers contributes the thinking sequence: brainstorm, spec, plan, TDD when useful, and verification discipline.
- UI/UX contributes the product-grade visual system: tone, layout, tokens, accessibility, responsive behavior, and interaction rhythm.
- HarmonyOS-Deveco converts that system into ArkUI ownership: files, tokens, components, states, routes, resources, permissions/config, build, signing, and device gates.
- GStack contributes visual evidence when a runnable or previewable surface exists: screenshots, viewport notes, visual diffs, and QA findings.

The final implementation report should read as one path from ideal capture to HarmonyOS evidence, not as unrelated tool outputs.

## Progress Reporting For Long Windows

For staged HarmonyOS work, keep progress updates synchronized with the real phase:

- Reading context: name the prompt/report inputs and what constraint they carry forward.
- Planning: name the Product Ideal Packet and ArkUI Landing Contract gaps.
- Editing: name the file group being changed and the ownership reason.
- Verifying: name the command, screenshot, artifact, or static review being used.
- Reporting: write a `.txt` when the phase requires it, with PASS/CONDITIONAL PASS/FAIL/BLOCKED language tied to evidence.

Do not leak API keys, provider keys, signing passwords, token values, private certificates, or local secret paths beyond high-level field presence. Client apps must not call real model provider keys directly.

## Single Shared Contract

Use one shared contract to prevent companion workflows from drifting apart:

1. Product Ideal Packet from brainstorming/spec: promise, audience, scene, temperament, non-goals, first value, acceptance evidence.
2. UI/UX System Packet from design work: visual direction, token roles, component behavior, accessibility, dark mode, responsive behavior, and motion.
3. ArkUI Landing Contract from harmonyos-deveco: pages, components, services/models, state matrix, routes, resources, permissions/config, signing/build impact.
4. Visual Evidence Packet from gstack or equivalent QA: screenshots, viewport/device notes, defects, reproduction steps, and conditional gaps.
5. Verification Packet from superpowers-style verification: tests/builds, docs searched, artifacts, device checks, and final PASS/CONDITIONAL PASS/FAIL language.

Do not let any packet remain prose-only. Every packet should either map to files, commands, artifacts, screenshots, or a clearly labeled open question.
## Role Boundaries

### harmonyos-deveco

Owns HarmonyOS / DevEco project structure, ArkTS / ArkUI implementation, `module.json5`, `app.json5`, `build-profile.json5`, `oh-package`, hvigor, permissions, resources, routes, signing, build, device validation, and translation from product/design intent into ArkUI pages, components, state, and services.

### ui-ux-pro-max

Use when available or explicitly requested for professional UI/UX direction: design system decisions, color, typography, layout, accessibility, component behavior, interaction details, and visual polish. The expected handoff is product mood, audience, design tokens, page/component hierarchy, state list, responsive rules, and accessibility rules.

### gstack

Use when available or explicitly requested for design review, browser/preview-like visual QA where applicable, screenshot capture, visual comparison, responsive checks, QA loops, and bug reports. The expected handoff is screenshots or QA findings, viewport/device notes, reproduction steps, and visual defects mapped to screens/components.

### superpowers

Use when available or explicitly requested for brainstorming, spec writing, planning, TDD flow, and verification discipline. The expected handoff is a clear product spec, acceptance criteria, non-goals, test plan, and verification checklist.

## Recommended Orchestration

For ideal-software or UI-first HarmonyOS work:

1. Use superpowers-style brainstorming/spec to capture the user's ideal and constraints.
2. Use ui-ux-pro-max-style design thinking to create the visual and interaction system.
3. Use harmonyos-deveco to translate that system into ArkUI tokens, pages, components, services, resources, routes, and build steps.
4. Use gstack-style review/QA to verify visual quality, responsive behavior, screenshots, and regressions when applicable.
5. Return to harmonyos-deveco for ArkTS fixes, DevEco build, signing, permissions, resources, and final validation.
6. Keep a single implementation contract so companion-tool output does not fragment into unrelated advice.

If these tools are not available in the current runtime, preserve the same role boundaries manually: brainstorm/spec first, design system second, ArkUI translation third, implementation fourth, verification last.


## Installed-Tool Behavior

When companion skills are installed and available, prefer using their specialized workflows instead of re-implementing them inside harmonyos-deveco. When they are not available in the current runtime, keep the same responsibilities manually and say which evidence is static rather than tool-backed.

- Use superpowers-style flow for brainstorming, spec, plan, TDD, and verification gates.
- Use ui-ux-pro-max-style flow for product-grade UI/UX system decisions.
- Use gstack-style flow for screenshots, visual comparison, viewport checks, and QA evidence when there is a runnable preview surface.
- Keep HarmonyOS API truth, ArkUI implementation, DevEco config, signing, permissions, resources, routes, and hvigor validation inside harmonyos-deveco.

If a companion skill is named by the user but not available in the current runtime, continue with the same role boundary manually and say that the companion skill itself was not loaded.

If a staged HarmonyOS delivery spans prompt files, completion reports, QA windows, build/signing windows, or device-verification windows, keep the implementation contract cumulative and evidence-based: later phases must re-check the facts they rely on instead of inheriting confidence.
## Handoff Contracts

Superpowers to harmonyos-deveco:

- Product spec or brainstorming summary.
- Acceptance criteria and non-goals.
- Test/verification plan.
- TDD or implementation sequence when applicable.

ui-ux-pro-max to harmonyos-deveco:

- Product category and audience.
- Visual direction and interaction tone.
- Design tokens and component rules.
- Accessibility, responsive, and motion guidance.

harmonyos-deveco to gstack:

- URL or preview surface when available.
- Screens/pages to inspect.
- Viewports/form factors to test.
- Known risks and acceptance checks.

GStack to harmonyos-deveco:

- Visual defect summary.
- Screenshot references or viewport notes.
- Interaction steps.
- Severity and expected behavior.

Integrated contract back to the user:

- What ideal was captured.
- What UI/UX system was chosen.
- How it maps to ArkUI tokens, components, state, routes, and resources.
- What was implemented or what is ready to implement.
- What was verified by build, docs search, visual evidence, or static inspection.
- What remains conditional because the exact Preview/device/viewport/signing check was unavailable.

## Request-Type Pipelines

- Vague ideal app: superpowers-style brainstorm, UI/UX design system, ArkUI translation, implementation, hvigor/device/gstack validation.
- UI design only: ideal capture, UI/UX design system, ArkUI implementation plan, no code unless requested.
- Design-to-code: parse design, ArkUI tokens/components/state, implementation, build, visual QA.
- Existing UI polish: quality checklist, targeted ArkUI fixes, build, screenshot/device notes.
- Build/runtime issue: DevEco diagnostic flow first; involve UI/UX tools only if the root cause affects product experience.
- Ideal-to-runnable-app: ideal capture, product spec, design system, ArkUI contract, scoped implementation, route/resource/config validation, hvigor build, and device/visual risks.

For long-running multi-window work, preserve file ownership, route/config changes, known build environment variables, and SDK path fixes. Keep final reports concrete: modified files, service interfaces, user flow, static layout checks, build result, integration notes, and unverified risks.

## Validation Matrix

- Product validation: ideal brief, non-goals, first-screen priority, acceptance criteria.
- Design validation: token roles, responsive behavior, dark mode, accessibility, interaction states.
- ArkUI validation: page split, component boundaries, state ownership, route/resource/config impacts.
- DevEco validation: hvigor build, SDK path, signing profile, permissions, packaged resources, device or preview result.
- Visual QA validation: screenshot/preview evidence where available, viewport notes, regression findings, and static checks when no visual surface exists.

## Multi-Window Handoff Discipline

For long-running product-to-HarmonyOS work that spans multiple chats or named windows, keep each handoff concrete and auditable:

- Carry forward the frozen functional boundaries and non-goals so later build/signing windows do not edit product code.
- Record exact files read, exact output artifacts, exact commands, and exact device/viewport evidence.
- Keep secrets out of reports; for signing, report field presence and artifact state rather than values.
- Distinguish product readiness, UI quality, build success, signing success, and submit readiness.
- If a later window discovers only conditional evidence, preserve the conditional status instead of upgrading the outcome.

## Boundaries

- ui-ux-pro-max owns design intelligence, not HarmonyOS API truth.
- gstack owns visual/browser-style evidence where available, not DevEco build success.
- superpowers owns process discipline, not ArkUI implementation details.
- harmonyos-deveco owns HarmonyOS translation, DevEco correctness, build/signing/permission/resource validation, and final app-side implementation.
- Do not use gstack visual output as proof of DevEco build success.
- Do not let design tools invent HarmonyOS APIs or build configuration details.
- Do not let implementation skip product intent when the task is vague or experience-oriented.
- Do not let a companion workflow produce a large standalone document that never becomes ArkUI tokens, components, state, routes, resources, and validation steps.

## Security Boundary For AI-Enabled HarmonyOS Apps

When the product includes AI planning, generated schedules, model calls, or cloud gateway work:

- Keep real provider API keys on the backend or gateway, never in ArkTS client code, resource files, reports, screenshots, or packages.
- Client code may call a controlled app backend with user/session-scoped authentication, quota, rate limiting, and safe error messages.
- Reports may state that a secret exists, is missing, is environment-backed, or is masked; never print the value.
- Generated plans or schedules should have preview-before-apply, confirmation, undo, or equivalent formal-write safety.
- Cost, quota, timeout, retry, logging, and privacy evidence are separate from UI quality and DevEco build success.

## Companion Skill Availability Rule

The user may mention installed companion skills that are not visible in the current runtime. In that case:

- State briefly that the named companion skill was not loaded in this session.
- Preserve the same checkpoint manually: brainstorming/spec, UI/UX design, ArkUI translation, implementation, or visual QA.
- Do not invent tool outputs, screenshots, or official API facts that were not actually produced.
- Keep the final HarmonyOS implementation contract inside harmonyos-deveco so the work still lands in DevEco/ArkUI artifacts.

## Companion Sequencing Shortcut
For ideal-product HarmonyOS work, use the companion skills in this order unless the user gives a narrower task:

1. superpowers brainstorming or spec flow: capture the product ideal, important constraints, assumptions, and acceptance evidence.
2. ui-ux-pro-max: turn the ideal into a design system, interaction model, accessibility stance, and responsive layout direction.
3. harmonyos-deveco: translate that design into ArkUI tokens, pages, components, state, navigation, resources, permissions, build/signing configuration, and DevEco validation.
4. gstack: when a web mock, screenshot comparison, visual regression, browser preview, or QA evidence loop is useful, generate and compare evidence before changing status.
5. superpowers verification: close with explicit build, test, visual, device, and residual-risk evidence.

HarmonyOS API, Kit, permission, configuration, and hvigor facts remain owned by harmonyos-deveco. Use local docs search first, then official documentation when local evidence is missing or stale.
