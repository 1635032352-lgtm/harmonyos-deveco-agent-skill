# HarmonyOS Topic Map

Use this map to choose local-search terms before opening full docs.

## Search Commands

- General official docs: `python scripts/search_docs.py "query"`
- Topic expansion: `python scripts/search_docs.py "query" --topic arkui`
- Contest-only: `python scripts/search_docs.py "query" --source contest`
- Available topics: `python scripts/search_docs.py --list-topics`

## High-Value Topics

- ArkUI UI: `--topic arkui`, search `List ForEach LazyForEach`, `Navigation NavPathStack`, `Column Row Stack Flex`, `TextInput validation`, `Dialog`, `Tabs`, `Gesture`, `animation`.
- ArkTS language: `--topic arkts`, search `@State @Prop @Link`, `@ObservedV2`, `async Promise`, `import export`, `Sendable`, `worker taskpool`.
- Project config: `--topic module.json5`, search `module.json5 requestPermissions`, `abilities`, `extensionAbilities`, `metadata`, `deviceTypes`, `app.json5`.
- Permissions and privacy: `--topic permissions`, search permission name plus `requestPermissionsFromUser`, `reason`, `authorization`, `privacy`.
- Lifecycle: `--topic lifecycle`, search `UIAbility`, `AbilityStage`, `onWindowStageCreate`, `onForeground`, `onBackground`, `Want`.
- Routing/navigation: `--topic routing`, search `router pushUrl`, `replaceUrl`, `Navigation`, `NavPathStack`, page registration.
- Network: `--topic network`, search `http request`, `WebSocket`, `Network Kit`, `INTERNET permission`, TLS/security config.
- Storage/data: `--topic storage`, search `Preferences`, `relationalStore`, `RDB`, `fileIo`, `photoAccessHelper`, `distributedData`.
- Media: `--topic media`, search `AVPlayer`, `audio renderer`, `image`, `camera`, `media library`, `picker`.
- AI: read `ai-kits.md`, then search exact Kit/capability names such as `Agent Framework FunctionComponent`, `CANN AIPP 模型推理`, `Core Speech SpeechRecognizer MICROPHONE`, `Core Vision OCR textRecognition`, `Intents Kit 接入流程`, `MindSpore Lite predict`, `Natural Language getEntity`, `Neural Network Runtime NNRt`, `Speech Kit AI字幕`, `Vision Kit 文档扫描`. Use `--topic ai` only when the exact Kit/API name is unknown.
- Build tools: `--topic hvigor`, search exact error plus `hvigor`, `oh-package`, `build-profile`, `assembleDevHqf`.
- Signing/release: `--topic signing`, search `certificate`, `profile`, `signature`, `release`, `HAP`, `AppGallery`.
- Kits: `--topic kit`, search the Kit name plus `preparations`, `permissions`, `sample`, `FAQ`.
- Contest: `--topic contest` or `--source contest`, search `创新赛 Kit`, `工具包`, `一指禅`, `设计指南`, `技术咨询`.

## Lookup Strategy

Start broad when the exact API name is unknown, then narrow with the component/config/error token. Prefer official docs for API facts and contest sources for competition constraints. If QQ sheet text is garbled, use it only to discover names/links and verify against raw JSON, PDFs, or official pages.
