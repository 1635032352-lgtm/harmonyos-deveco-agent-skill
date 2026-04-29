# Workflows

## Modify Or Add A Page

1. Inspect `entry/src/main/ets` for page naming, `@Entry`, router registration, `Navigation`, resources, and component folders.
2. Search the relevant ArkUI component or navigation API.
3. Add the page/component in the existing layout. Keep state ownership local unless the project already has a store.
4. Register route/page metadata only where the project already does so.
5. Validate ArkTS imports, resource names, preview/device-only APIs, and navigation back paths.

## Add Permission Or System Capability

1. Search the capability plus `module.json5 requestPermissions`.
2. Add only required permissions to `entry/src/main/module.json5`.
3. Add runtime authorization if the docs require user grant.
4. Handle denied, unavailable, and unsupported-device paths.
5. Re-check privacy wording, reason strings, and AppGallery review implications.

## Configure `module.json5` Or `app.json5`

1. Read the current module/app files and preserve formatting style.
2. Verify field names, nesting, device types, ability names, labels/icons, metadata, and API compatibility in local docs.
3. Keep bundle/module identifiers stable unless the user explicitly asks to rename them.
4. For extension abilities, confirm the exact type and required metadata before editing.

## Integrate A HarmonyOS Kit

1. Search the Kit name with `preparations`, `permissions`, `sample`, and `FAQ`.
2. Check `oh-package.json5` dependencies and whether an SDK/AGC/AppGallery service setup is required.
3. Add permissions/config before code. Keep Kit calls behind a small service/helper if multiple pages use them.
4. Add clear failure paths for missing login, permission denial, service unavailability, or device incompatibility.

## Integrate A HarmonyOS AI Kit

1. Read `ai-kits.md` and choose the narrowest Kit: high-level Vision/Speech/NLP/Intents/Agent Framework first, MindSpore Lite for app-provided models, NNRt/CANN for low-level hardware acceleration.
2. Search the exact Kit and capability name, then open the relevant official doc before writing code. Use `--topic ai` only when the exact name is unknown.
3. Check device, country/region, API level, simulator support, runtime permission, whitelist/entitlement, Huawei account, network, and open-platform/AppGallery setup.
4. Put reusable AI calls behind a service/helper. Keep UI responsible for loading, cancellation, unsupported-device, permission-denied, empty-result, and retry states.
5. For model inference, verify model format, `rawfile` placement, `syscap.json`, Native/N-API boundaries, and target hardware before editing page code.

## Debug Build Or Runtime Errors

1. Capture the exact command and first project-owned error line.
2. Check JSON5 syntax, imports, resource references, API version, dependency versions, hvigor config, signing, and permissions.
3. Search the exact error token and the affected API/config key.
4. Patch the narrow cause, then rerun the same command.

## Build, Sign, And Release

1. Identify debug vs release target and module/product name from `build-profile.json5`.
2. Check signing config, certificate/profile paths, bundle name, and target device type.
3. Prefer DevEco/hvigor commands already used by the project. On this machine, DevEco bundled Node/hvigor may be required.
4. For release, verify permissions, privacy, icons/labels, version fields, and AppGallery packaging requirements.

## Innovation Contest Planning

1. Read `contest-sources.md`.
2. Search contest sources for `Kit`, `工具包`, `一指禅`, `赋能资料`, `设计指南`, and any domain term.
3. Translate contest constraints into a small technical route: user value, required Kit/API, prototype pages, demo data, risks, and validation plan.
4. Treat QQ sheet extracted strings as leads; verify names/links with raw JSON, PDFs, or official docs before final claims.

## HarmonyOS Code Review

Check for HarmonyOS-specific risks: missing permissions, runtime authorization gaps, wrong lifecycle hook, page route mismatch, unsupported API level, hardcoded resources, preview-only assumptions, long-running work on UI thread, missing error handling around Kit/service calls, and release signing/config drift.
