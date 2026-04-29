# Common Errors

## First Checks

- Confirm DevEco SDK paths: `DEVECO_SDK_HOME`, `OHOS_BASE_SDK_HOME`, `NODE_HOME`.
- Confirm DevEco bundled Node/hvigor is used when the system Node is incompatible.
- Inspect `oh-package.json5`, `oh-package-lock.json5`, `build-profile.json5`, `hvigorfile.ts`, `module.json5`, and `app.json5`.
- Search the exact error plus one context token: API name, config key, module name, permission, or hvigor task.

## Build And Dependency

- `hvigor` task fails before ArkTS compile: check SDK install, hvigor plugin version, build profile product/module name, and Node version.
- Dependency resolution fails: check `oh-package.json5`, registry access, lockfile drift, package name casing, and whether the dependency supports the target API/device.
- API not found or import fails: search import path; HarmonyOS docs may use newer `@kit.*` paths while older projects use legacy imports.
- Resource compile errors: check `$r()` names, file placement under `resources/base`, media filenames, and JSON/XML syntax.

## JSON5 Config

- `module.json5` errors often come from trailing structure mistakes, wrong `abilities` nesting, wrong `requestPermissions` shape, or extension ability metadata.
- `app.json5` errors often involve bundle/version/device config mismatches.
- Signing config errors often involve wrong certificate/profile path, password alias, profile bundle mismatch, or debug/release product mismatch.

## ArkTS / ArkUI

- Type errors: check callback signatures, nullable values, typed arrays/models, and component parameter decorators.
- UI render issues: check builder syntax, required return values, state mutation during build, and conditional layout branches.
- List issues: check stable keys, `ForEach`/`LazyForEach` data source behavior, and item height assumptions.
- Navigation issues: check route registration, page path string, parameter type, and back-stack pattern.

## Runtime

- Permission denied: verify both `module.json5` permission and runtime request/authorization flow.
- Network failure: verify `INTERNET` permission, endpoint scheme/TLS, emulator/device network, and request lifecycle.
- Media/file failure: verify picker/media permission, URI/file access, and release of player/camera resources.
- Kit failure: verify service enablement, account/login, AGC/AppGallery setup, device support, and exact error code docs.

## Local Build Hint

When a project requires DevEco’s bundled tools, use the project’s known command or mirror its environment. On this machine, previous HarmonyOS builds used DevEco SDK under `D:\Program Files\DevEco Studio\sdk\default` and DevEco’s bundled Node/hvigor. Prefer the repo’s own scripts if present.
