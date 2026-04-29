# ArkUI UI Quality Checklist

Use this checklist before implementing UI, before final review, and when improving an existing HarmonyOS interface.

## Table of Contents

- Ideal-Product Quality Bar
- Pre-Implementation Stop Rule
- Ideal-to-App Failure Signals
- Ideal Software Acceptance Rubric
- Product Fit
- Ideal-to-Implementation Fit
- Information Architecture
- Layout and Responsiveness
- Visual System
- Accessibility
- Interaction Quality
- ArkUI Code Quality
- Page-Size and State-Smell Checks
- Anti-Patterns
- Evidence Honesty
- Validation
- UI Evidence Language
- DevEco Landing And Release Readiness
- Repair Playbook
- Review Finding Priorities
- Pre-Code Gate for Ideal UI Requests
- Submission-Ready UI Evidence Gate

## Ideal-Product Quality Bar

Use this checklist to verify that the implementation still matches the user's intended product, not merely that it compiles:

- The first screen communicates the product's main job, tone, and next action without explanatory clutter.
- Important states are designed before coding: empty, loading, success, error, offline, permission denied, and first-run guidance.
- Visual decisions are expressed through reusable tokens and components instead of one-off values scattered through pages.
- Interaction quality is judged by touch ergonomics, feedback timing, animation restraint, and recovery paths after failure.
- Verification includes build/config checks plus visual evidence when screenshots, previews, or gstack-style QA are practical.

## Pre-Implementation Stop Rule

Before writing ArkTS for a product/UI/interface request, stop if the work lacks all three:

- Product direction: target user, use scene, product temperament, first value, and non-goals.
- ArkUI ownership: tokens, page structure, component split, state matrix, route/resource/config impact, and validation path.
- Evidence plan: what can be verified by docs search, static code review, hvigor/build, signed artifact, screenshot, Preview, or device check.

If only a low-risk detail is missing, write the assumption into the implementation contract and proceed. If the missing detail changes the product shape or evidence claim, ask one direct question.
## Ideal-to-App Failure Signals

Treat these as quality failures even when the page compiles:

- The implementation follows a literal widget request but loses the intended product temperament, audience, or usage scene.
- The UI plan remains prose and never becomes ArkUI token, component, state, route, resource, and validation ownership.
- A large page file carries product logic, repeated UI, hard-coded style, and hidden state without a component/service split.
- Visual acceptance is claimed from static reasoning, a stale screenshot, a nearby viewport, or build success without labeling the evidence conditional.
- DevEco landing claims blur build success, signing success, route/resource correctness, and real device or Preview validation.

## Ideal Software Acceptance Rubric

Use this rubric before claiming a HarmonyOS UI/product task is complete:

| Area | PASS condition | Conditional evidence |
| --- | --- | --- |
| Product feeling | first screen, copy, hierarchy, and interaction rhythm match the Product Ideal Packet | static review only, or unresolved product assumptions |
| UX flow | primary journey, back behavior, state recovery, and safety gates are implemented | plan exists but not all states are exercised |
| ArkUI system | tokens, components, states, and resources have clear owners in code | one-off styles remain but are isolated and documented |
| Responsiveness | target phone widths and any requested tablet/foldable states avoid overlap/clipping | only static layout inspection or nearby viewport evidence |
| Accessibility | readable contrast, usable touch targets, non-color status cues, and reduced motion risk are checked | not checked on device/Preview |
| DevEco correctness | route/resource/config/build/signing claims are verified with current files and commands | build unavailable or signing/device check blocked |
| Evidence honesty | screenshots, build logs, artifact paths, and residual gaps are named precisely | evidence is stale, nearby, or from a different environment |

Do not upgrade a result from conditional to pass because the page "looks likely" or because the build passed. Product feeling, visual evidence, and DevEco build/signing/device evidence are separate gates.
## Product Fit

- The first screen makes the product's core job obvious.
- The screen serves the user's actual workflow rather than a marketing explanation.
- The interface avoids becoming a generic dashboard when the product is a tool.
- Primary and secondary actions are visually distinct.
- Empty states tell the user the next meaningful action.
- The visual tone matches the intended product feeling, audience, and usage pressure.

## Ideal-to-Implementation Fit

- The implementation preserves the user's intended product feeling, not just the requested widget list.
- The main workflow can be described from the user's point of view without mentioning internal services first.
- Design tokens, component boundaries, and state gates are visible in the code, not only in a planning note.
- Screens that generate, compile, save, publish, delete, or otherwise formalize user data have clear preview/confirmation/undo behavior.
- The final report ties major changes back to product promise, UX structure, ArkUI translation, and DevEco validation.

## Information Architecture

- Pages have clear ownership.
- Navigation paths are reversible.
- Modal or sheet content is not used as a substitute for missing page structure.
- Long-range planning, settings, and diagnostics are not forced into Home.
- Destructive or formal-write actions use preview, confirmation, or undo when appropriate.
- Chat-style UI is not used for structured workflows unless conversation is the product's core interaction.

## Layout and Responsiveness

- 375px and 390px widths do not overlap, truncate critical text, or require horizontal scroll.
- Tablet and foldable layouts preserve hierarchy and do not stretch text too wide.
- Dynamic or generated text uses wrapping, line limits, or disclosure.
- Buttons and chips have stable dimensions.
- Important controls meet practical touch target expectations, approximately 44px where possible.
- Lists, cards, boards, and counters have stable dimensions during loading and state changes.
- Safe-area, keyboard, and bottom action behavior are accounted for on form-heavy screens.

## Visual System

- Colors are semantic and centralized.
- Typography roles are consistent across pages.
- Spacing and radius follow a small scale.
- Elevation is subtle and not stacked excessively.
- Icons match platform style and button meaning.
- UI does not rely on decorative gradients, blobs, or unrelated visual noise.

## Accessibility

- Text contrast is sufficient in normal and dark modes.
- Touch targets are usable.
- State is not communicated by color alone.
- Dynamic content has text labels.
- Disabled states remain readable.
- Motion is not required to understand the UI.

## Interaction Quality

- Loading states are visible and do not look broken.
- Error states include problem, likely cause, and recovery action.
- Partial states preserve user work.
- Undo or restore exists for high-impact changes.
- Preview-before-apply is used for generated plans, schedules, and destructive edits.
- Gestures have visible alternatives when they perform important actions.

## ArkUI Code Quality

- Page files do not mix unrelated services, data transforms, and repeated UI.
- Repeated UI is extracted to components.
- Hard-coded colors, spacing, and text styles are minimized.
- State ownership is explicit: page state, component state, service state, storage state, resources/config, or route params.
- Imports are clean and consistent.
- Route names are registered and navigable.
- Resources are stored in the right resource directories.
- Domain logic stays in services/models; pages compose UI and call narrow service interfaces.

## Page-Size and State-Smell Checks

Flag these as maintainability risks during UI implementation:

- A route page becomes the owner of unrelated services, persistence, generated-content transforms, and repeated visual blocks.
- Empty/loading/error/ready/blocked states are handled by scattered booleans instead of a clear state matrix.
- A component silently reads app-level storage or route params instead of receiving explicit props or service state.
- The same card, row, chip, button, or prompt panel appears in multiple places with copied style values.
- A visual fix adds a new hard-coded value instead of extending tokens or existing components.

Prefer extracting feature sections, state-heavy widgets, and services in the same style as the local project.

## Anti-Patterns

- Product/UI request implemented immediately as ArkTS without clarifying product intent.
- Chat bubbles used for structured planning flows.
- Home screen filled with roadmap, task backlog, or admin controls.
- Domain-specific pages implemented as long if/else chains.
- Long forms shown all at once with no blocking/optional split.
- Generated text inserted into fixed-height controls.
- Low-quality animation used to hide unclear hierarchy.
- Build, signing, permission, or Kit details asserted from memory.
- Design system pasted as comments but not represented in ArkUI tokens/components.
- One-off route params, storage keys, and style constants scattered across unrelated pages.
- Layout that works only on one phone width.
- Treating browser-style visual QA as a substitute for a DevEco build or device check.
- Treating a successful hvigor build as proof that the product feeling and interaction quality are correct.
- Claiming exact viewport, Preview, device, signing, permission, or build validation when the exact check was not performed.
- Reporting a stale signed HAP or old screenshot as validation for a newer UI or runtime change.
- Letting generated or AI-assisted workflows write formal user data without a preview, confirmation, or undo boundary.

## Evidence Honesty

Use precise result language:

- PASS: the requested behavior or visual condition was checked in the requested environment and no blocking issue was found.
- CONDITIONAL PASS: nearby evidence, static inspection, or a different environment suggests low risk, but the exact requested check was not completed.
- FAIL: the requested behavior or visual condition was checked and a blocking issue remains, or the app cannot build/run enough to verify it.

For visual acceptance, record:

- Device or Preview surface.
- Physical resolution and virtual viewport when available.
- Pixel ratio/density when relevant.
- Screenshot path or capture method.
- Page/state name, scroll position, keyboard/safe-area state, light/dark mode, and exact width such as 375vp or 390vp.
- Whether the conclusion is visual evidence, static ArkUI/layout reasoning, or build evidence.

Never use a successful build as visual proof, and never use a 376vp screenshot as exact 390vp evidence. It can be supporting risk analysis only.

## Validation

- Run local docs search for concrete HarmonyOS APIs, permissions, Kits, and build/signing details.
- Run hvigor/build checks when practical.
- Inspect route/profile JSON after adding pages.
- Verify changed pages at small phone widths and any target large-screen modes.
- Record what could not be verified, especially DevEco Preview, device screenshots, signing, or Hypium tests.
- For UI/UX work, capture screenshot/device/preview evidence when available; if unavailable, state the static checks performed.
- Keep validation evidence typed: product/design validation, ArkUI/static validation, DevEco/build validation, and device/visual validation.

## UI Evidence Language

Use exact wording for evidence claims:

- "Verified on X" only when X was actually run or captured in the latest relevant state.
- "Static review suggests" when the conclusion comes from reading ArkTS/layout/resource files.
- "Conditional pass" when nearby viewport, stale artifact, browser-style QA, or non-device evidence reduces risk but does not match the requested environment.
- "Blocked" when DevEco Preview, device, SDK, signing, or screenshot capture is unavailable.

Never use an old screenshot, a different viewport, or an unsigned artifact to upgrade a current HarmonyOS UI to final or submission-ready.

## DevEco Landing And Release Readiness

- Confirm the current project root before judging build, signing, or artifact state.
- Check root `build-profile.json5` for `app.signingConfigs`, a named config matching the product, `type: HarmonyOS`, and required material fields.
- Check `AppScope/app.json5` for bundleName, vendor, versionCode, and versionName.
- Check `entry/src/main/module.json5` for deviceTypes, abilities, permissions, and route/page metadata impacts.
- Confirm signed and unsigned HAP separately. A successful `assembleHap` can still skip signing.
- Do not report submit-ready unless `entry-default-signed.hap` exists after the latest relevant build.
- Never copy signing material into the project or report password values. Only report whether password fields are configured, hidden, missing, or risky.
- If DevEco GUI signing appears configured but the current project file is unchanged, inspect likely sibling project directories read-only and report paths without migrating secrets.

## Repair Playbook

- Weak hierarchy: reduce competing headings, strengthen the primary action, and group secondary content.
- Generic dashboard feel: re-center the user's main workflow and move admin-like panels away from the first screen.
- Hard-coded style drift: introduce or reuse semantic tokens and replace one-off values gradually.
- Oversized page file: extract feature sections and repeated blocks; move transformation logic into services.
- State confusion: define explicit empty/loading/partial/error/ready/blocked states.
- Text overflow: add wrapping, line limits, disclosure, or stable dimensions; do not shrink fonts with viewport width.
- Low-quality animation: remove ornamental motion and keep short transitions tied to state changes.
- Layout overflow: verify small-phone widths, long generated strings, large font settings, and foldable/tablet behavior.
- Unsafe generated actions: restore preview, confirmation, or undo gates before writing formal schedules, files, or persistent state.

## Review Finding Priorities

- P0: build-breaking behavior, data loss, broken formal-write safety, or broken navigation to critical flows.
- P1: unusable layout on a target device, inaccessible primary action, severe state confusion, or missing permission/config gate.
- P2: hard-coded visual drift, component boundary problems, weak empty/error states, or non-critical overflow risk.
- P3: polish issues, naming clarity, and small consistency improvements.

## Pre-Code Gate for Ideal UI Requests

Before writing ArkTS for ideal-product or UI-quality work, confirm the following are explicit or safely assumed:

- Product feeling, target user, usage scene, and first valuable action.
- First viewport priority, main workflow, non-goals, and formal-write safety boundaries.
- Design token roles, component inventory, state matrix, responsive behavior, dark mode, accessibility, and motion intent.
- ArkUI page/component/service/resource/config ownership and validation plan.

If one missing item would change the product shape, ask one direct question. If it is low risk, proceed with a labeled assumption and verify against this checklist after implementation.

## Submission-Ready UI Evidence Gate
Do not describe a HarmonyOS UI as final, polished, or submission-ready until there is evidence for the relevant surfaces:

- Product fit: the screen hierarchy, copy, primary action, and interaction rhythm match the Product Ideal Packet.
- Visual fit: tokens are applied consistently; there are no one-off colors, unexplained sizes, accidental shadows, or low-quality animation flourishes.
- Layout fit: small phones, common portrait sizes, landscape, tablet, and foldable/adaptive layouts avoid clipping, overlap, hidden CTAs, and unstable scroll regions.
- Accessibility fit: text remains readable, touch targets are large enough, semantic roles and focus order are sane, and dark mode does not reduce contrast.
- HarmonyOS fit: routes, resources, permissions, module/app configuration, signing, and hvigor build mode match the target deliverable.
- Evidence fit: screenshots, logs, build output, signed artifacts, or device observations are named with enough detail that another agent can reproduce the result.

When evidence is incomplete, report the gap directly and avoid upgrading the status beyond what was actually verified.
