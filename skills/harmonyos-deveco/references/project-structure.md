# DevEco Project Structure

## Common Roots

- `AppScope/app.json5`: app-level bundle metadata, version fields, icon/label, app permissions/features where applicable.
- `build-profile.json5`: products, signing, targets, modules, build options.
- `hvigorfile.ts`: project/module build hooks and hvigor plugin config.
- `oh-package.json5`: project/module dependencies and overrides.
- `oh-package-lock.json5`: resolved dependency graph; do not hand-edit unless the project pattern requires it.
- `entry/`: default application module. Other modules may be HAR/HSP libraries or feature modules.

## Entry Module

- `entry/src/main/module.json5`: module name/type, device types, abilities, extension abilities, metadata, and `requestPermissions`.
- `entry/src/main/ets`: ArkTS source. Typical folders include `pages`, `components`, `entryability`, `entrybackupability`, `model`, `viewmodel`, `common`, `utils`.
- `entry/src/main/resources`: `base/element` strings/colors/media profile files and `base/media` assets. Prefer `$r()` references instead of hardcoded display strings/colors when the project already uses resources.
- `entry/src/ohosTest` or `entry/src/test`: tests when present.

## Config Editing Rules

- Preserve existing JSON5 style, comments, and ordering when possible.
- Never guess permission names or ability fields; search local docs.
- Keep `bundleName`, `moduleName`, ability names, and route names consistent across config and ArkTS.
- Check `compatibleSdkVersion`, `targetSdkVersion`, `runtimeOS`, and device type when a doc/API appears unsupported.
- For signing, inspect both project-level and module-level config because DevEco projects can split signing/product settings.

## Dependency Rules

- Use `ohpm`/`oh-package.json5` patterns already in the project.
- Verify Kit/service dependencies against official docs or contest source links.
- After dependency changes, run or recommend the same install/build flow the project already uses.
