# ArkTS And ArkUI Patterns

## Component Shape

- Follow the project’s existing `@Entry`, `@Component`, `struct`, `build()` style.
- Keep reusable UI as small components with explicit `@Prop`, `@Link`, callbacks, or model objects.
- Avoid broad globals unless the project already has a store/event bus.
- Keep async/service work outside visual builder expressions; update state from handlers/lifecycle methods.

## State

- Use `@State` for page-owned mutable UI state.
- Use `@Prop` for one-way parent-to-child data.
- Use `@Link` for two-way child editing of parent state when the project already uses it.
- Use observed models only when needed for nested mutation; verify `@Observed`, `@ObjectLink`, or V2 decorators against the project API level.
- Do not mutate state inside repeated builder code in a way that can loop/rebuild unexpectedly.

## Layout

- Prefer the existing mix of `Column`, `Row`, `Stack`, `Flex`, `Grid`, `List`, and `Navigation`.
- For dynamic collections, search docs for `ForEach` vs `LazyForEach` and keep stable keys.
- Define empty, loading, error, and permission-denied states for user-facing data.
- Keep resource strings/colors/images in `resources` when the project already localizes or themes.

## Routing And Lifecycle

- If the project uses `router`, register and call paths consistently.
- If it uses `Navigation`/`NavPathStack`, keep path names and parameter models typed and centralized.
- Put app/window setup in `UIAbility`/`AbilityStage` only when the feature genuinely belongs there.
- Check lifecycle hooks before adding network, media, sensor, or background behavior.

## Interop And Kits

- Verify import paths from local docs, especially `@kit.*` vs older module imports.
- Encapsulate Kit access behind helpers when it requires permissions, service availability checks, or repeated error handling.
- Keep device/emulator limitations explicit in code comments only when they affect behavior.

## Review Hotspots

- Missing `INTERNET` or runtime permission.
- Wrong resource key or route string.
- API-level mismatch with decorator/import/component.
- Heavy synchronous work in UI event handlers.
- Mutating list data without stable keys.
- Assuming Previewer behavior equals real device behavior.
