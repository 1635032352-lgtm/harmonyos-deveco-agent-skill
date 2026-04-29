# ArkUI Design System Translation

Use this reference when turning UI/UX direction, design system output, screenshots, or text descriptions into ArkUI / ArkTS implementation.

## Table of Contents

- Design-To-ArkUI Translation Standard
- Minimum ArkUI Design-System Contract
- ArkUI Ownership Rule
- UI/UX System To ArkUI Ownership Matrix
- Product-Ideal to Token Strategy
- Product Temperament to ArkUI Translation
- Design Token Categories
- Token-to-ArkUI Mapping
- Suggested Token Artifact Shape
- ArkUI Translation Checklist
- Layout Guidance
- Screenshot or Spec to ArkUI
- ArkUI Implementation Contract
- Component Split Patterns
- State Matrix
- Device, Dark Mode, and Accessibility Rules
- Design System to ArkTS File Plan
- Anti-Drift Rules
- Ideal-To-ArkUI Packet

## Design-To-ArkUI Translation Standard

A design system is not ready for implementation until it has an ArkUI contract. Before writing ArkTS, define:

- Semantic token names, light/dark values, intended component usage, and fallback behavior.
- Page hierarchy, reusable component boundaries, state ownership, navigation entry points, and resource requirements.
- Layout rules for phone, tablet, foldable, landscape, dynamic text, and overflow scenarios.
- Interaction and motion rules that explain when transitions happen, how long they last, and what state change they communicate.
- Validation criteria linking each visible screen back to product intent, accessibility, and DevEco/device readiness.

Keep this contract API-neutral until local HarmonyOS docs confirm the exact ArkUI APIs, Kits, permissions, or configuration keys needed for implementation.

## Minimum ArkUI Design-System Contract

For product-grade UI work, the design system must be small enough to implement but complete enough to prevent visual drift:

- Color roles: background, surface, elevated surface, text primary/secondary/disabled, action primary/secondary, selected, pressed, border, divider, success, warning, risk, and information.
- Typography roles: page title, section title, body, supporting text, metadata, action label, numeric emphasis, and generated-content text.
- Layout roles: page padding, section gap, component gap, list row padding, fixed action area, safe-area inset, tablet/foldable max content width.
- Shape/elevation roles: control radius, card radius, sheet/dialog radius, border style, subtle shadow, overlay/scrim.
- Motion roles: press feedback, state reveal, route/sheet transition, progress feedback, reduced-motion fallback.
- Accessibility roles: touch target, contrast, focus order, non-color status cue, dynamic text behavior, disabled readability.

Name where each role lands: token module, resource file, component prop, page builder, route/config, or validation note.
## ArkUI Ownership Rule

Every design-system decision must name its ArkUI owner before implementation starts:

- Token owner: existing theme module, feature-local token file, resource color/string/media file, or component prop layer.
- Layout owner: route page, reusable section, primitive component, sheet/dialog, or navigation surface.
- State owner: page state, component state, service/model state, app storage, route params, or resource/config.
- Evidence owner: static review, DevEco build, Preview/device screenshot, exact viewport check, or conditional risk note.

If a color, spacing value, animation, route string, permission, or asset has no owner, treat it as design debt rather than implementation detail.

## UI/UX System To ArkUI Ownership Matrix

Before editing ArkTS, translate UI/UX work into this ownership matrix:

| Design decision | ArkUI / DevEco owner | Validation |
| --- | --- | --- |
| Product tone and density | page shell, layout rhythm, component hierarchy | first viewport review and screenshot/Preview evidence when available |
| Color roles | token module or resource color files | light/dark contrast and disabled/pressed/selected states |
| Typography roles | token module, text builders, component props | long labels, generated text, dynamic text, and small-width behavior |
| Spacing/radius/elevation | token module and reusable components | no card-in-card drift, no one-off shadows, stable dimensions |
| Motion | token module or local transition owner | short state-linked transitions, no ornamental movement |
| Interaction states | page state, component state, services/models | empty/loading/partial/error/blocked/ready/confirmed behavior |
| Navigation | route profile, router helpers, page params | reversible paths, back behavior, deep links if relevant |
| Resources/assets | `resources/base`, rawfile, media, profile entries | file existence, import/resource references, build result |
| Permissions/Kits | `module.json5`, runtime authorization flow, service boundary | local docs search and device/runtime validation |
| Build/signing | `build-profile.json5`, hvigor command, artifact path | signed/unsigned artifact distinction after latest build |

If a row cannot be filled, keep the work in planning or label the assumption explicitly.

## Product-Ideal to Token Strategy

When the source is a vague product feeling, not a finished design file, derive tokens from product qualities before selecting component details:

- Calm or focused products usually need restrained contrast, predictable spacing, quiet feedback, and clear primary action hierarchy.
- Operational or expert tools usually need dense but organized information, stable dimensions, fast scan paths, and conservative motion.
- Premium or emotionally warm products need careful typography, surface layering, content pacing, and accessible contrast rather than decorative noise.
- Playful products can use richer motion and illustration, but state clarity, touch targets, and buildability still define quality.

Translate these choices into semantic roles. Do not hard-code "brand blue on one page" or "special card shadow in this builder" unless the project already has a local pattern for it.

## Product Temperament to ArkUI Translation

Use product feeling as an implementation constraint:

- Calm/focused: fewer competing colors, clear primary action, restrained elevation, predictable spacing, short state-linked motion.
- Operational/expert: denser information, stable dimensions, strong scan paths, compact controls, conservative animation, clear error recovery.
- Warm/premium: careful typography, surface layering, content pacing, accessible contrast, polished empty/error states.
- Playful: richer illustration or motion only where it improves meaning; keep touch targets, state clarity, and buildability strict.

Do not accept a technically correct page as complete if the token choices contradict the stated product temperament.
## Design Token Categories

Define tokens semantically, not by page-specific names. Prefer a token layer that reads like a design system: surface, text, action, feedback, spacing, shape, motion, density, and responsive behavior.

### Color

Recommended roles include app background, primary surface, muted surface, elevated surface, overlay, primary text, secondary text, tertiary text, inverse text, disabled text, primary action, secondary action, selected background, pressed state, border, divider, success, warning, risk, and information.

Dark mode rules:

- Do not simply invert colors.
- Preserve contrast between surface layers.
- Re-check disabled, input hint, border, and selected states.
- Use semantic roles so switching themes is centralized.
- Verify the exact HarmonyOS theme/dark-mode mechanism with local docs search when implementing app-wide behavior.

### Typography

Define page title, section title, body, supporting text, caption/metadata, button label, and numeric or metric emphasis when needed.

Rules:

- Do not scale font size directly with viewport width.
- Avoid negative letter spacing.
- Prevent long labels from overflowing buttons, chips, or toolbar controls.
- Use wrapping, line limits, or detail expansion for generated text.

### Spacing, Radius, and Elevation

Use a small spacing scale such as 4, 8, 12, 16, 20, 24, and 32. Use small radius for chips and controls, medium radius for cards, and larger radius only for sheets or brand-specific surfaces. Keep elevation subtle and avoid stacking card-in-card effects.

Rules:

- Do not put UI cards inside other cards unless the inner card is a repeated item or modal content.
- Use stable dimensions for toolbars, lists, cards, counters, and chip rows.
- Use responsive constraints rather than viewport-scaled typography.
- Avoid one-note palettes and decoration-only surfaces.

### Motion

Motion should explain state, not decorate the page. Use short enter transitions, progress feedback, state-change emphasis, and gentle reveal only when they improve comprehension. Avoid long ornamental animations, transitions that hide loading or errors, and motion that moves controls under the user's finger.

## Token-to-ArkUI Mapping

Map design-system decisions into implementation artifacts before page edits:

- **Colors:** central token class/module, resource colors when the project uses resources, pressed/disabled/selected/error/success roles, and dark-mode alternatives.
- **Typography:** named text roles for page title, section title, body, support text, metadata, button label, and numeric emphasis.
- **Spacing:** small scale for page padding, section gap, component gap, list item padding, and bottom-safe-area action spacing.
- **Shape/elevation:** radius and shadow roles by surface type; avoid ad hoc card styling in pages.
- **Motion:** duration/easing roles for route entry, state reveal, button press, progress, and sheet/dialog changes.
- **Components:** tokenized props for buttons, chips, cards, rows, empty states, forms, sheets, dialogs, tabs, and navigation surfaces.
- **Resources:** media, icons, static strings, route profile entries, permission declarations, and any generated assets.

Do not assert exact ArkUI API names or theme hooks from memory. When implementation requires a concrete API, search the local docs first.

For HarmonyOS product work, the design system should land as code, not prose: name the token owner, page/component files, state owners, route/resource/config impacts, and the validation command before implementation starts.

## Suggested Token Artifact Shape

Prefer the smallest token layer that prevents visual drift. A practical HarmonyOS project may use one of these shapes:

- Existing token/theme module: extend it with semantic roles instead of adding a parallel system.
- New feature-local token file: acceptable for a narrow feature when the app has no global design system.
- Resource-backed token values: use when the project already centralizes colors, strings, media, or profiles in resources.
- Component props/builders: use for local variants, but keep values named by role rather than copied as raw numbers.

Token names should describe purpose: `surfacePrimary`, `textSecondary`, `actionPrimary`, `spacingSection`, `radiusControl`, `motionFast`, not `blue1`, `bigGap`, or `homeCardShadow`.

When adding tokens, also name their validation: light/dark contrast, 375vp/390vp behavior, disabled/pressed/selected state, dynamic text behavior, and whether the value is shared across pages.

## ArkUI Translation Checklist

Before coding:

- Identify page files, reusable components, services, and model types.
- Decide which tokens live in an existing token file or a new token module.
- Map every design state to ArkUI state variables or service state.
- Decide which strings or assets belong in resources.
- Confirm route names and navigation parameters.
- Identify target devices, dark-mode scope, and accessibility expectations.

During coding:

- Prefer existing project components and tokens.
- Extract repeated or state-heavy sections into components.
- Keep data transformation in services, not page layout code.
- Keep ArkUI builders small enough to review.
- Use semantic styles and stable layout constraints.
- Keep generated text out of fixed-height controls unless clipping has a visible disclosure path.

After coding:

- Check imports and route registration.
- Check 375px and 390px behavior.
- Check tablet/foldable behavior if the app targets those devices.
- Check dark mode if supported.
- Check touch targets and contrast.
- Run the project build/check command when practical.
- Record unverified design evidence separately from build evidence.

## Layout Guidance

Phone screens should use a single-column flow, reachable primary actions, folded secondary content, and stable list/card dimensions. Avoid dense tables, full calendar grids, and side-by-side diffs on small screens.

Tablet and foldable screens can use master-detail, two-pane preview, or wider content columns when this reduces navigation cost. Preserve the phone journey and avoid overly wide text lines.

Form-heavy screens should group fields by user decision rather than database structure, explain required fields when unclear, progressively disclose optional settings, and preserve entered data when navigating back.

## Screenshot or Spec to ArkUI

When given a screenshot, design file, or text-only UI description:

1. Identify layout structure before visual styling.
2. Extract semantic tokens for color, type, spacing, radius, elevation, and motion.
3. Identify component inventory and reuse opportunities.
4. Identify states missing from the static source.
5. Translate into ArkUI page/component files, services, resources, and route/config changes.
6. Verify platform capabilities and resource handling through local docs search when specific APIs or config are involved.

Do not copy web CSS concepts blindly into ArkUI. Convert them to ArkUI layout, component, and state patterns that fit the local project.

For screenshots, separate observation from inference:

- Observation: visible hierarchy, approximate spacing, repeated components, color relationships, content density, states visible in the screenshot.
- Inference: missing states, route behavior, component props, dark mode, responsive rules, permissions/config impact.
- Verification: what can be checked statically, what needs DevEco Preview/device, and what needs exact viewport screenshots.

If the user asks for exact visual acceptance, record the exact viewport/device used. A nearby viewport can inform risk but cannot be reported as exact evidence.


## ArkUI Implementation Contract

Before writing ArkTS from a product/UI design, produce a compact mapping:

- Tokens: where semantic colors, typography, spacing, radius, elevation, and motion live.
- Pages: route-level page files, route params, lifecycle hooks, and navigation actions.
- Components: reusable blocks, local visual state, props, and slots/builders.
- Services/models: domain state, persistence, transforms, generated plans, and formal-write gates.
- Resources: media, profile route entries, string/color/media resources, and any app/module config impact.
- States: empty, loading, partial, error, ready, blocked, preview, confirmed, and undo/restore when relevant.
- Verification: build command, small-screen checks, dark/accessibility checks, and device/preview evidence if available.

Use this contract to keep the UI implementation from becoming a single large page with scattered hard-coded style values.

When a page already has local tokens/components, extend that system instead of adding a parallel one. When no token layer exists, introduce the smallest semantic layer that prevents visual drift across the requested screens.
## Component Split Patterns

Use this split for larger product pages:

- Page shell: route-level state, lifecycle, top-level scroll/navigation, data loading.
- Feature sections: cohesive blocks such as overview, preview, diagnostics, settings, review, and history.
- Reusable primitives: buttons, chips, empty states, metric rows, timeline items, cards, sheets, and dialogs.
- Services/models: persistence, transformation, scheduling, AI/provider contracts, validation, and domain decisions.
- Resource assets: media, icons, route profile entries, and centralized static strings where the project already uses them.

Extract a component when a block is repeated, state-heavy, visually complex, or likely to be reused in a second page. Do not create abstractions for one-line style differences.

## State Matrix

For each screen or critical component, define empty, loading, partial, error, ready, and blocked states. Generated plans, schedules, destructive actions, and formal writes should have preview, confirmation, undo, or an equivalent safety path.

State ownership rule:

- Page state owns route params, current tab/mode, transient input, and local expansion.
- Component state owns local visual toggles and ephemeral interaction state.
- Service/model state owns domain data, persistence, generated plans, accepted decisions, and validation.
- App-level storage owns cross-page or app-level state that must survive route changes.
- Resources/config own static capabilities, route profiles, media, permissions, signing, and build settings.

## Device, Dark Mode, and Accessibility Rules

- Prioritize one main action per phone screen.
- Ensure 375px and 390px widths do not overlap or truncate critical labels.
- Prefer two-pane layouts on tablet/foldable only when they reduce navigation cost.
- Design light and dark modes together.
- Check text, borders, disabled states, selected states, and generated-content contrast.
- Use touch targets that are practically tappable, around 44px or more where possible.
- Do not communicate status only through color.
- Provide visible alternatives for gesture-only interactions when the action matters.
- Verify exact ArkUI API names, theme mechanisms, and permission/config details with local docs search when uncertain.

## Design System to ArkTS File Plan

Before implementation, translate the design system into file-level work:

- Token file or existing theme extension for semantic color, text, spacing, radius, elevation, motion, density, and dark-mode roles.
- Page shell files for route lifecycle, top-level state, scroll structure, and navigation actions.
- Component files for repeated sections, state-heavy widgets, cards, forms, sheets, dialogs, and empty/error states.
- Service/model files for domain transformations, persistence, generated plans, preview-before-apply gates, and formal writes.
- Resource/profile/config files for strings, media, route profiles, permissions, signing/build changes, and device targeting.

If a UI design, screenshot, or text description cannot be mapped to this file plan, keep planning; otherwise ArkTS edits tend to become one large page with hidden state and hard-coded style.

## Anti-Drift Rules

Review ArkTS/ArkUI edits for these drift signals:

- hard-coded hex colors, font sizes, route strings, spacing, radii, or animation durations repeated across pages;
- visual variants encoded as unrelated builders instead of tokenized props or small components;
- generated text placed in fixed-height controls with no disclosure path;
- dark-mode values guessed from light-mode colors without contrast review;
- tablet/foldable layout handled by stretching phone content instead of changing structure;
- permission, Kit, resource, route, or build config details asserted without local docs search;
- page files carrying product logic, persistence, and repeated UI that should live in services/components.

Fix drift by naming owners first, then editing the smallest set of files that restores the design system.

## Ideal-To-ArkUI Packet
Before editing ArkTS for a product-ideal request, prepare a compact packet that can be implemented and reviewed:

- Design tokens: semantic colors with light/dark roles, typography scale, spacing scale, radii, elevation, border, opacity, and motion durations/easing.
- Page structure: route name, page purpose, hierarchy, scroll areas, fixed regions, safe-area behavior, loading/empty/error/success states, and adaptive breakpoints.
- Component split: reusable components, local page-only components, props/state ownership, event callbacks, and resource dependencies.
- Interaction model: primary actions, secondary actions, gestures, focus order, disabled states, pressed/hovered feedback, and transition behavior.
- HarmonyOS contract: module config impact, permissions, resources, device classes, build target, signing expectations, and verification commands.

Use this packet to keep visual taste and implementation details aligned. If the packet reveals missing product direction, resolve that before code changes unless the user explicitly asks for a throwaway prototype.
