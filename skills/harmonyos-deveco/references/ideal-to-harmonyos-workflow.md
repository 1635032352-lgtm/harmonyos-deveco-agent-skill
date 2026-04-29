# Ideal-to-HarmonyOS Workflow

Use this reference when the user wants to turn a vague product idea, ideal-software feeling, UI concept, screenshot, or design plan into a high-quality HarmonyOS / DevEco Studio app.

## Table of Contents

- Purpose
- Durable User Need
- One-Sentence Trigger Contract
- Reusable User Intent Signals
- Ideal Software Landing Definition
- Ideal Capture Interview Pattern
- Product Ideal Packet Template
- Product Realization Outputs
- Operating Principles
- Ideal Capture Packet
- Workflow
- Handoff Artifacts
- Output Contract
- Readiness Gates
- Quality Gates
- Conversation-to-Skill Distillation

## Purpose

This workflow moves from product taste to implementation without skipping the product thinking. The goal is not merely to write ArkTS; it is to capture the user's intended product feeling, clarify the interaction model, translate it into ArkUI architecture, and then build and verify it as a HarmonyOS app.

## Durable User Need

This section captures reusable product-realization preferences without copying any chat transcript.

## Chat-Derived Durable Need Pattern
Treat vague product requests as a request for a product partner plus HarmonyOS engineer in one loop. The durable pattern is:

- The user wants the agent to capture the product feeling that exists in their head, not merely translate a screen into ArkTS.
- The agent should clarify product temperament, target user, situation, information architecture, visual direction, and interaction rhythm before implementation.
- The agent should transform fuzzy intent into an implementation-ready ArkUI contract: tokens, pages, components, states, navigation, resources, permissions, build mode, signing needs, and validation evidence.
- Staged prompt files or window names are continuity signals. Preserve prior conclusions, then verify the current code, SDK, build, and device facts before raising completion status.
- Reusable decisions belong in the skill, references, project docs, or implementation artifacts. Raw chat excerpts do not belong in the skill.

This workflow exists for requests that begin as a product feeling rather than a finished spec. The durable need is to help the user externalize the ideal software in their head, clarify what quality means, and convert that into concrete HarmonyOS screens, components, state, navigation, resources, build checks, and device validation.

## One-Sentence Trigger Contract

If the user says any variant of "help me design the software in my head and make it a HarmonyOS app", treat the sentence as permission to run the full product-realization path:

1. Capture the ideal product feeling and reject generic page-building.
2. Clarify product temperament, target user, scene, non-goals, first value, and acceptance evidence.
3. Turn the ideal into UX structure, UI/UX design-system roles, and ArkUI ownership.
4. Implement only after tokens, pages, components, states, routes, resources, and validation gates have owners.
5. Verify with docs search, static checks, hvigor/build evidence, signing/artifact evidence, and exact visual/device evidence where available.

This shortcut should not become a long interview by default. Ask only the missing question that would change the product shape; otherwise state assumptions and proceed.

Reusable rules:

- Treat product temperament, target user, usage scene, visual direction, interaction rhythm, and non-goals as implementation inputs, not decorative notes.
- Convert vague intent into information architecture, UI states, ArkUI token decisions, reusable components, route/resource requirements, and acceptance criteria.
- Use companion design, workflow, and QA skills when available, while keeping HarmonyOS API truth, DevEco configuration, and ArkTS/ArkUI implementation responsibility inside `harmonyos-deveco`.
- Never paste raw chat history into skill content or deliverables; preserve only reusable product constraints and implementation rules.
- For multi-window or staged delivery, phase reports are source material: read them, verify what is still true, keep PASS/CONDITIONAL PASS/FAIL language precise, and avoid treating earlier signed artifacts or screenshots as proof for newer code.

## Reusable User Intent Signals

When the user says the software exists "in my head", "ideal", "product feeling", "interface quality", or asks to move from idea to a runnable HarmonyOS app, treat these as signals for a product-realization workflow:

- The user wants help externalizing the product, not a detached code sample.
- Product feel, target user, usage scene, visual direction, and interaction rhythm are first-order requirements.
- The output should become concrete UI, interaction, information architecture, ArkUI structure, ArkTS files, resources, routes, build steps, and validation evidence.
- Companion skills may be part of the expected workflow: `superpowers` for brainstorming/spec/plan/TDD/verification, `ui-ux-pro-max` for professional design-system quality, and `gstack` for visual comparison, screenshots, responsive QA, and regression evidence where a runnable surface exists.
- If the user asks for "exact" visual validation, exact means exact: do not substitute a nearby viewport, different device, or static reasoning without labeling the result conditional.
- If the user asks for a runnable, signed, or submit-ready HarmonyOS result, evidence must include the latest relevant build command, signed/unsigned artifact distinction, artifact timestamp, and any device/Preview gap.

Use these signals to choose the workflow automatically. Do not wait for the user to say "use the skill" when the request is clearly about HarmonyOS UI/product design or DevEco landing.
## Ideal Software Landing Definition

For this skill, "ideal software" means the user's internal product standard has been converted into buildable HarmonyOS evidence, not merely described in prose. A request is ready to leave the ideal phase only when it has:

- A product feeling and target user clear enough to reject a technically valid but wrong-feeling UI.
- A first-screen priority and core workflow clear enough to choose page structure and navigation.
- A design system clear enough to become ArkUI tokens, components, states, resources, and motion rules.
- A DevEco landing path clear enough to name build, signing, route/resource/config, and device or Preview validation gates.

If any of these are missing, continue ideal capture or state a labeled assumption before writing ArkTS.

## Ideal Capture Interview Pattern

Use a short, product-shaping interview instead of a long intake form. Ask only questions whose answers would materially change the UI, workflow, architecture, or acceptance evidence.

High-signal prompts:

- "Who is opening this app, under what pressure, and what should feel easier after the first minute?"
- "What should the first screen make obvious without tutorial text?"
- "Should the product feel calm, operational, premium, warm, playful, expert, or something else?"
- "What must this product not become, even if that feature seems useful?"
- "Which action needs preview, confirmation, undo, or a formal write gate?"
- "What would convince you this is the software in your head rather than a generic HarmonyOS demo?"

If the user already provided enough context, do not pause for all questions. State the inferred Product Ideal Packet and proceed to the ArkUI Landing Contract.

## Product Ideal Packet Template

Use this compact structure when the user has a fuzzy idea and wants progress in the same turn:

- Product promise: the user outcome the app should make easier.
- Target user and scene: who opens it, when, and under what pressure.
- Temperament: the app's felt quality, such as calm, expert, focused, warm, operational, or playful.
- First viewport: what the user must immediately understand or do.
- Main path: the shortest path from open to value.
- Non-goals: what the product must not become, especially content that should not be forced onto Home.
- Safety boundaries: preview, confirmation, undo, or formal-write gates.
- Quality evidence: screenshots, Preview/device checks, build/signing artifacts, or labeled static review.

After this packet is clear enough, convert it into the ArkUI Landing Contract rather than writing a separate design essay.

## Product Realization Outputs

For ideal-to-HarmonyOS requests, produce outputs that become implementation inputs:

- Product Ideal Packet: promise, audience, scene, temperament, first value, non-goals, and quality bar.
- UX Map: page inventory, navigation paths, core journey, state matrix, interaction rhythm, and safety gates.
- Design System Packet: token roles, component behavior, accessibility, dark mode, responsive rules, and motion intent.
- ArkUI Landing Contract: files, routes, resources, permissions/config, state owners, services/models, build/signing impact, and validation plan.
- Evidence Report: build/test commands, docs search, screenshots/Preview/device checks, signed/unsigned artifacts, and residual risks.

The output should not be a freestanding design essay. Each design decision should name where it will land in ArkUI/ArkTS or how it will be verified.
## Operating Principles

1. Clarify before coding when the task is product, UI, interaction, or experience oriented.
2. Keep the user's ideal product feeling visible through technical decisions.
3. Convert fuzzy ideas into concrete screens, states, components, navigation, resources, and validation gates.
4. Separate product intent, design system, ArkUI translation, implementation, and DevEco verification.
5. Do not invent HarmonyOS APIs. Verify concrete platform details with local docs search or official docs.
6. Treat "looks like the software in my head" as an acceptance criterion covering product feel, information rhythm, interaction confidence, and build correctness.
7. Prefer a few high-leverage questions over a long intake form; when ambiguity is low-risk, proceed with explicit assumptions.
8. Keep validation typed and honest: product/design confidence, ArkUI/static checks, DevEco build checks, and device/Preview/screenshot evidence are different kinds of evidence.

## Ideal Capture Packet

Use this compact packet to turn a vague software idea into implementable product direction:

- **Promise:** what the app does for the user in one sentence.
- **Audience:** who uses it, their environment, and their pressure level.
- **Moment:** the opening scene and the first valuable action.
- **Feeling:** the intended product temperament, such as quiet, utilitarian, warm, premium, focused, playful, or expert.
- **Boundary:** what the product must not become, especially what should not be pushed onto Home.
- **Workflow:** the primary path, fallback path, and any preview/confirmation/undo gate.
- **Visual direction:** density, layout rhythm, imagery/icon needs, motion tone, and dark-mode expectation.
- **Implementation surface:** pages, components, services, state, resources, routes, permissions, build, and device validation.

Do not store the user's raw brainstorming text in the skill. Extract durable product rules and implementation constraints.

## Workflow

### 1. Capture the Product Ideal

Extract or infer these decisions from the user and existing context:

- Product promise: what the app helps the user accomplish.
- Target user: who uses it and under what pressure.
- Primary scene: when, where, and why the app is opened.
- Desired feeling: calm, professional, playful, operational, premium, low-pressure, focused, or another concrete tone.
- First screen: what must be visible immediately.
- Main workflow: the shortest path from opening the app to user value.
- Non-goals: what the app must not become.
- Quality bar: what would make the user recognize the intended software.

Ask concise clarifying questions only when a missing decision would change the product shape. Otherwise, make a defensible assumption and label it.

For this user's recurring preference, bias toward product-grade software rather than isolated demo pages, calm but high-quality interaction, concrete UI/state/navigation/build artifacts, preview/confirmation boundaries for generated or high-impact actions, and focused home screens that do not absorb every long-term plan or diagnostic panel.

### 2. Convert Ideal Into UX Structure

Define the user-facing structure before ArkTS edits:

- Information architecture: pages, tabs, sheets, dialogs, and navigation paths.
- Core journeys: first run, normal use, review/edit, error recovery, and any high-impact confirmation flow.
- State model: empty, loading, partial, error, success, blocked, and low-confidence states when relevant.
- Content hierarchy: primary, secondary, folded, deferred, and hidden content.
- Interaction rules: taps, long presses, gestures, forms, confirmations, undo, preview-before-apply, and back behavior.
- Responsive behavior: small phones, common phones, tablet/foldable, and landscape when relevant.

Decision checkpoints:

- First viewport: the one thing the user should understand or do immediately.
- Main path: number of taps from open to value.
- State safety: behavior for empty, partial, blocked, failed, and confirmed states.
- Scope boundary: what belongs on Home, what gets its own page, and what stays folded.
- Formal-write boundary: actions that require preview, confirmation, undo, or later integration.

### 3. Form the Design System

Produce or reuse a UI system with semantic roles:

- Color roles for background, surfaces, text, action, feedback, borders, disabled, and selected states.
- Typography roles for title, section, body, supporting text, metadata, action labels, and numeric emphasis.
- Spacing, radius, elevation, density, and component rhythm.
- Motion language tied to state and interaction.
- Accessibility requirements: contrast, target size, readable disabled states, state labels, and non-color status cues.
- Dark mode behavior and large-screen adaptation.
- Resource and asset requirements.

When `ui-ux-pro-max` is available or explicitly requested, use it to produce the professional UI/UX system. Then translate that system through `references/arkui-design-system.md`.

### 4. Translate to ArkUI Implementation

Map design decisions to HarmonyOS artifacts before coding:

- ArkUI pages and reusable components.
- Token module or existing style constants.
- View models, services, and state ownership.
- Route entries, navigation parameters, and back behavior.
- Resource files for strings, media, colors, profiles, or static assets where the project centralizes them.
- Permission, Kit, module, signing, and build-profile impacts.
- Lifecycle and async loading behavior.
- Validation commands and manual verification path.

The implementation plan should be specific enough that file edits are mechanical: file ownership, page structure, component boundaries, states, data flow, and acceptance checks.

Before editing, check that the plan names the exact ArkUI artifacts to create or change: token module, page file, component file, service/model, route profile, resource asset, permissions/config file, build command, and visual/device checks. If a category is irrelevant, say so rather than leaving it implicit.

### 4.5 Convert Design Decisions Into a Buildable Contract

Before touching ArkTS for UI/product work, create a short implementation contract:

- Product promise and quality bar: the behavior and feeling the UI must express.
- Screen inventory: route-level pages, sheets, dialogs, first viewport priority, and back behavior.
- Token inventory: semantic color, typography, spacing, radius, elevation, motion, density, and dark-mode roles.
- Component inventory: reusable sections, primitives, state-heavy widgets, and page-only blocks.
- State inventory: empty, loading, partial, error, ready, blocked, preview, confirmed, and undo/restore states when relevant.
- HarmonyOS surface: route/resource/config/permission/signing/build impact, with concrete API or config details verified through local docs search when needed.
- Validation plan: build command, small-width checks such as 375vp/390vp when relevant, dark/accessibility checks, device or Preview evidence, and what would remain conditional.

This contract is allowed to be concise. Its purpose is to stop vague UI direction from becoming a large page file with hard-coded style and hidden state.

### 4.6 Source-to-ArkUI Modes

Choose the mode that matches the user's input:

- Text idea: infer Product Ideal Packet, then create UX structure and token roles.
- Screenshot or visual mock: separate observed layout from inferred behavior, missing states, and responsive rules.
- Existing app page: inspect current ArkTS structure, token usage, state ownership, route/resource references, and visual anti-patterns before proposing changes.
- UI/UX design-system output: translate system roles into ArkUI token owners, component props/builders, resources, and validation.
- Submit/demo-ready request: include DevEco landing packet, current build command, signed/unsigned artifact distinction, and exact screenshot/device evidence boundaries.

Each mode must end with file-level ArkUI ownership before implementation starts.

### 4.7 Add the DevEco Landing Packet

When the user wants a runnable, demo-ready, submit-ready, or externally shareable HarmonyOS app, extend the implementation contract with a DevEco landing packet:

- Project identity: current root directory, module name, product name, bundleName, versionCode, versionName, vendor, deviceTypes, and permissions.
- Build surface: exact hvigor command, SDK/Node/JAVA_HOME assumptions when relevant, output directory, and whether the build was debug, release, HAP, HQF, or another target.
- Route/resource surface: new or changed route profile entries, resource files, media assets, rawfiles, strings, colors, and any app/module JSON5 changes.
- Signing surface: whether the current project has a matching `signingConfig`, whether the product points to it, whether required signing material fields exist, and whether signed HAP was actually generated.
- Artifact surface: exact signed HAP path and size, exact unsigned HAP path and size, and whether each file exists after the latest build.
- Device/visual surface: exact Preview/device/viewport/screenshot evidence for visual claims, and clear conditional language for anything not checked in the requested environment.

Do not treat a successful hvigor build as proof of signing, visual quality, or device readiness. Keep build success, signing success, and exact visual evidence as separate facts.

### 5. Implement and Verify

When implementation is requested:

- Follow existing project style before adding abstractions.
- Use semantic tokens instead of scattered raw styling.
- Keep page files readable and componentized.
- Verify route registrations, imports, resources, permissions, JSON5 configs, and build profile changes.
- Run hvigor/build/test commands when practical.
- If visual quality matters, collect screenshot, preview, or device evidence when available. If unavailable, state the static checks performed.

## Handoff Artifacts

For product/UI work, produce these artifacts before code unless the user explicitly asks to implement immediately:

1. Ideal brief: product promise, target user, primary scene, desired feeling, non-goals, and quality bar.
2. UX structure: pages, navigation, core journey, state matrix, interaction rules, and responsive behavior.
3. Design system summary: color roles, typography, spacing, radius, elevation, motion, accessibility, and dark-mode rules.
4. ArkUI translation: token strategy, page/component split, state/services, resources/routes/config, and validation plan.
5. Implementation result: scoped file changes, build result, visual/device verification notes, and remaining unverified risks.

For implementation windows, preserve a short trace from ideal to code: each significant file change should map back to product feel, workflow, UI system, state safety, or DevEco correctness.


## Output Contract

When using this workflow, the final answer or implementation report should make the chain of reasoning reusable without pasting the original conversation:

- Product ideal captured: promise, audience, use scene, feeling, non-goals, and quality bar.
- UX decisions made: first screen priority, information architecture, navigation, state matrix, and high-impact confirmation/undo gates.
- Design system translated: semantic color/type/spacing/radius/elevation/motion/accessibility/dark-mode rules mapped to ArkUI tokens or existing components.
- Implementation mapped: page files, component files, services/models, resources, routes, permissions/config, and data ownership.
- Validation completed: docs searched for concrete APIs/configs, build command/result, visual/device checks, and unresolved risks.
- Delivery readiness: whether the project is runnable, demo-ready, submit-ready, signed, or still blocked, with artifact paths and remaining gates separated.

If implementation is not requested yet, stop at the ArkUI translation and validation plan. If implementation is requested, keep the report concise but tie each file change back to the product ideal.
## Readiness Gates

Start ArkTS edits only when these are clear enough to implement:

- First viewport priority and primary action.
- Page ownership and route behavior.
- Reusable component boundaries.
- State ownership and persistence model.
- Token strategy and dark-mode behavior when relevant.
- Small-screen and large-screen behavior.
- Validation command or manual verification path.
- Companion-skill responsibility when `ui-ux-pro-max`, `gstack`, or `superpowers` is part of the request.

If one missing item is low-risk, make a labeled assumption. If it is high-risk, ask one direct question.

## Quality Gates

- The first screen matches the product promise.
- The primary action is clear without explanatory wall text.
- UI hierarchy matches the user's real workflow.
- Dynamic states are designed before implementation.
- Small screens do not require horizontal scrolling or dense tables.
- Platform APIs and permissions are verified before being asserted.
- The implementation remains buildable in DevEco/hvigor.
- The final implementation still expresses the original product feeling rather than only the literal widget list.
- Exact visual claims are backed by matching screenshot, Preview, device, or viewport evidence. Otherwise use conditional language and state the verification gap.

## Conversation-to-Skill Distillation

When a future chat reveals a recurring product-building preference, distill it into reusable workflow rules instead of copying the chat text. Preserve these categories:

- Product ambition: what kind of ideal software the user is trying to make real.
- Design intent: product temperament, target user, usage scene, visual direction, and interaction rhythm.
- Implementation contract: ArkUI tokens, page/component split, state ownership, navigation, resources, permissions/config, build, signing, and device validation.
- Evidence rule: exact claims require exact evidence; nearby viewport, static reasoning, or build success must stay conditional.

This keeps the skill reusable across future HarmonyOS products while still carrying forward the user's preference for product-grade design before ArkTS implementation.



