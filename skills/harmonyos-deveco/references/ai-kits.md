# HarmonyOS AI Kit Reference

Use this reference when a task involves HarmonyOS AI capabilities, AI Kit selection, AI-related permissions, model inference, speech, vision, NLP, Intents, Agent Framework, NNRt, or CANN. Search local docs first, then open the specific source file listed here.

## Local Search

```powershell
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "Core Vision Kit OCR textRecognition"
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "SpeechRecognizer MICROPHONE"
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "MindSpore Lite predict"
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "Intents Kit 接入流程"
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "Agent Framework FunctionComponent"
python C:\Users\cjh16\.codex\skills\harmonyos-deveco\scripts\search_docs.py "CANN Kit AIPP 模型推理"
```

Use `--topic ai` for broad exploratory search only. For exact Kit or API names, search the exact name first; adding a broad topic can surface large CANN/model documents ahead of the narrow match.

## Selection Matrix

| Need | Prefer | Why |
| --- | --- | --- |
| OCR, face detection/comparison, subject segmentation, object detection, skeleton detection | Core Vision Kit | Basic visual AI APIs. |
| Liveness, card recognition, document scan, AI image analyzer UI | Vision Kit | Scenario-level visual services and UI components. |
| Speech-to-text or text-to-speech | Core Speech Kit | Basic ASR/TTS APIs. |
| Ready-made reading or AI caption UI | Speech Kit | Scenario-level speech controls. |
| Word segmentation or entity extraction | Natural Language Kit | Lightweight text understanding. |
| Run an app-provided model on device | MindSpore Lite Kit | High-level built-in inference engine; ArkTS and Native routes. |
| Connect an AI framework to hardware acceleration | Neural Network Runtime Kit | Low-level cross-chip inference runtime. |
| Kirin NPU, AIPP, model conversion, custom operator optimization | CANN Kit | Heavy AI optimization and AscendC/operator work. |
| Expose app functions to Xiaoyi dialogue/search/suggestions | Intents Kit | HarmonyOS-level intent standard and smart distribution. |
| Show an in-app entry that launches a Xiaoyi agent | Agent Framework Kit | Function component to open a published agent. |

## Common Engineering Rules

- Confirm device, country/region, API version, simulator support, permission requirements, service entitlement, whitelist, and AppGallery/open-platform setup before coding.
- Prefer high-level Kits first. Use MindSpore Lite for custom models. Use NNRt/CANN only when the task needs low-level acceleration, NPU constraints, or custom operators.
- Keep AI calls behind a small service/helper if multiple pages use them. UI pages should handle loading, cancellation, unsupported-device, permission-denied, service-unavailable, and timeout states.
- For camera/microphone/media/gallery input, verify both `module.json5` declaration and runtime authorization.
- Do not assume simulator support. Most AI Kits here require real devices; Core Speech says its capability supports simulator from `6.0.0(20)`, but verify the target API/device.
- For AI results, design confidence, empty-result, retry, privacy, and content-safety behavior. Do not treat model output as deterministic truth.

## Agent Framework Kit

Purpose: provide a standard Function component that launches a specific Xiaoyi agent from within an app.

Use when:

- The app already has an agent created on Xiaoyi/open platform and associated with the app.
- The UI needs an icon or button entry to open the agent dialog.

Core docs:

- `references/docs/harmonyos-guides/harmony-agent-framework-kit-guide.md`
- `references/docs/harmonyos-guides/hmaf-introduction.md`
- `references/docs/harmonyos-guides/hmaf-function.md`

Key APIs/imports:

```ts
import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
```

Implementation notes:

- Create and associate the agent before app integration.
- Ensure the device is logged into a Huawei account and online.
- Use `FunctionController.isAgentSupport(context, agentId)` before rendering when support may vary.
- `FunctionComponent` needs `agentId` and `onError`; `options.title` and `options.queryText` shape the entry.
- Subscribe to `agentDialogOpened` and `agentDialogClosed` when the page needs lifecycle state.
- Constraints from local docs: Phone/Tablet; China mainland only; simulator unsupported.

## CANN Kit

Purpose: Kirin NPU-oriented heterogeneous AI compute framework for model optimization, model conversion, AIPP, on-device deployment, single operator, and AscendC custom operators.

Use when:

- The project has hard performance/power targets and a supported Kirin NPU device.
- The model needs hardware-specific acceleration, AIPP image preprocessing, zero-copy, deep fusion, or custom operator work.
- The user is explicitly asking for CANN, NPU, AscendC, AIPP, OMG model conversion, tiling, or operator migration.

Avoid as first choice when:

- A high-level Kit or MindSpore Lite can solve the feature.
- The target must work in simulator or on devices without Kirin NPU.

Core docs:

- `references/docs/harmonyos-guides/cann-kit-guide.md`
- `references/docs/harmonyos-guides/cannkit-introduction.md`
- `references/docs/harmonyos-guides/cannkit-preparations.md`
- `references/docs/harmonyos-guides/cannkit-model-conversion.md`
- `references/docs/harmonyos-guides/cannkit-aipp.md`
- `references/docs/harmonyos-guides/cannkit-model-inference.md`
- `references/docs/harmonyos-guides/cannkit-app-integration.md`
- `references/docs/harmonyos-guides/cannkit-ascendc-operator-development.md`
- `references/docs/harmonyos-guides/cannkit-supported-operators.md`

Implementation notes:

- Check hardware first. Local docs state CANN Kit only applies to devices with Kirin NPU: Phone, Tablet, PC/2in1, TV; TV is supported from `5.1.0(18)`.
- Simulator is unsupported.
- Typical route: prepare model -> optimize/lightweight if needed -> convert/offline compile -> configure AIPP if image preprocessing benefits -> deploy -> run inference -> profile/debug.
- Use CANN for performance work, not basic image/NLP features that are already exposed through Core Vision, Natural Language, MindSpore Lite, or other high-level Kits.

## Core Speech Kit

Purpose: basic speech AI APIs, including text-to-speech and speech recognition.

Use when:

- The app needs speech-to-text, microphone/file ASR, TTS playback, or generated PCM audio.

Core docs:

- `references/docs/harmonyos-guides/core-speech-kit-guide.md`
- `references/docs/harmonyos-guides/core-speech-introduction.md`
- `references/docs/harmonyos-guides/speechrecognizer-guide.md`
- `references/docs/harmonyos-guides/texttospeech-guide.md`
- `references/docs/harmonyos-guides/corespeechkit-personal-data.md`

Key imports:

```ts
import { speechRecognizer } from '@kit.CoreSpeechKit';
import { textToSpeech } from '@kit.CoreSpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

Implementation notes:

- ASR: create engine -> set `RecognitionListener` -> configure `StartParams` -> call `startListening`.
- TTS: create engine -> configure `SpeakParams` and `SpeakListener` -> call `speak`.
- For microphone ASR, declare `ohos.permission.MICROPHONE` in `module.json5` and request runtime permission.
- Common ASR audio parameters from docs: `pcm`, `16000` sample rate, `1` channel, `16` sample bit.
- Constraints from local docs: Phone/Tablet/PC/2in1; China mainland only; Core Speech capability supports simulator from `6.0.0(20)`.
- Speech recognition supports Chinese Mandarin; short speech up to 60s and long speech up to 8h in the docs.

## Core Vision Kit

Purpose: basic machine vision APIs.

Use when:

- The app needs OCR, face detection, face comparison, subject segmentation, object detection, or skeleton detection.

Core docs:

- `references/docs/harmonyos-guides/core-vision-kit-guide.md`
- `references/docs/harmonyos-guides/core-vision-introduction.md`
- `references/docs/harmonyos-guides/core-vision-text-recognition.md`
- `references/docs/harmonyos-guides/core-vision-face-detector.md`
- `references/docs/harmonyos-guides/core-vision-face-comparator.md`
- `references/docs/harmonyos-guides/core-vision-subject-segmentation.md`
- `references/docs/harmonyos-guides/core-vision-object-detection.md`
- `references/docs/harmonyos-guides/core-vision-skeleton-detection.md`
- `references/docs/harmonyos-guides/corevisionkit-personal-data.md`

OCR import example:

```ts
import { textRecognition } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
```

Implementation notes:

- OCR flow: `textRecognition.init()` -> prepare `PixelMap` -> build `VisionInfo` -> configure `TextRecognitionConfiguration` -> call `recognizeText` -> `release()`.
- Local docs list image quality, size, angle, language, and concurrency restrictions. Check the exact capability doc before coding.
- Core Vision capabilities support multiple users, but the docs warn that the same user cannot concurrently call the same feature.
- Constraints from local docs: Phone/Tablet/PC/2in1; China mainland only; simulator unsupported.

## Intents Kit

Purpose: HarmonyOS-level intent standard for exposing app/meta-service functions to Xiaoyi dialogue, Xiaoyi search, and Xiaoyi suggestions.

Use when:

- The user wants app features to be discoverable/callable from system AI entrances.
- The task mentions smart distribution, intent sharing, intent invocation, local search, skill calling, Xiaoyi suggestions, or app function one-step access.

Core docs:

- `references/docs/harmonyos-guides/intents-kit-guide.md`
- `references/docs/harmonyos-guides/intents-introduction.md`
- `references/docs/harmonyos-guides/intents-access-flow.md`
- `references/docs/harmonyos-guides/intents-habit-rec.md`
- `references/docs/harmonyos-guides/intents-event-rec.md`
- `references/docs/harmonyos-guides/intents-local-rec.md`
- `references/docs/harmonyos-guides/intents-search-rec.md`
- `references/docs/harmonyos-guides/intents-skill-all-rec.md`
- `references/docs/harmonyos-guides/intents-kit-listing-configuration.md`

Implementation notes:

- Main runtime concepts: intent sharing and intent invocation.
- Access workflow in local docs: choose feature/intent -> apply for debug whitelist -> register intent declaration -> implement intent sharing -> implement intent invocation -> end-to-end test -> app market and Xiaoyi/open-platform listing configuration.
- Typical feature categories: habit recommendation, event recommendation, location recommendation, voice skill calling, local search.
- Constraints from local docs: Phone/Tablet/PC/2in1; China mainland only; HarmonyOS 5.0+; simulator unsupported.

## MindSpore Lite Kit

Purpose: built-in lightweight AI engine for on-device model inference/training, with ArkTS and Native development routes.

Use when:

- The app ships or downloads its own model and needs on-device inference.
- The user asks for `.ms` models, model conversion, image classification, custom model deployment, or MindSpore Lite.

Core docs:

- `references/docs/harmonyos-guides/mindspore-lite-kit.md`
- `references/docs/harmonyos-guides/mindspore-lite-kit-introduction.md`
- `references/docs/harmonyos-guides/mindspore-lite-converter-guidelines.md`
- `references/docs/harmonyos-guides/mindspore-guidelines-based-js.md`
- `references/docs/harmonyos-guides/mindspore-guidelines-based-native.md`
- `references/docs/harmonyos-guides/mindspore-asr-based-native.md`
- `references/docs/harmonyos-guides/mindspore-lite-guidelines.md`
- `references/docs/harmonyos-guides/mindspore-lite-train-guidelines.md`
- `references/docs/harmonyos-guides/mindspore-lite-supported-operators.md`

ArkTS import:

```ts
import { mindSporeLite } from '@kit.MindSporeLiteKit';
```

Implementation notes:

- Convert third-party models such as TensorFlow, TensorFlow Lite, Caffe, or ONNX to `.ms`.
- Common ArkTS flow: add model to `entry/src/main/resources/rawfile` -> add `SystemCapability.AI.MindSporeLite` to `entry/src/main/syscap.json` if needed -> create context -> load model -> prepare inputs -> call `predict()` -> parse outputs.
- ArkTS route is fast for validation. Native route is preferred for dynamic shape, `OH_AI_ModelResize`, lower-level performance work, or C/C++ algorithm packaging behind N-API.
- Local docs state Phone/Tablet/PC/2in1/TV support and simulator support.
- MindSpore Lite, NNRt, and CANN relate as layers: MindSpore Lite is high-level inference, NNRt bridges AI frameworks to hardware acceleration, CANN is Kirin NPU compute/backend and optimization layer.

## Natural Language Kit

Purpose: basic natural language understanding.

Use when:

- The app needs word segmentation or entity extraction from short text.

Core docs:

- `references/docs/harmonyos-guides/natural-language-kit-guide.md`
- `references/docs/harmonyos-guides/natural-language-introduction.md`
- `references/docs/harmonyos-guides/natural-language-getwordsegmentation.md`
- `references/docs/harmonyos-guides/natural-language-getentity.md`

Import example:

```ts
import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
```

Implementation notes:

- Entity extraction example: `textProcessing.getEntity(text, { entityTypes: [EntityType.NAME, EntityType.PHONE_NO] })`.
- Supported entity types in the docs include time, location, email, tracking number, flight number, name, phone number, URL, verification code, and ID number.
- Text length is limited; the local introduction lists 1000 characters for segmentation/entity extraction.
- Same-feature concurrent calls from the same user are not supported.
- Constraints from local docs: Phone/Tablet/PC/2in1; China mainland only; simulator unsupported.

## Neural Network Runtime Kit

Purpose: low-level runtime that bridges AI inference frameworks and AI acceleration hardware.

Use when:

- The user works on AI framework integration, direct AI hardware inference acceleration, model compilation/cache, NNRt graph building, or offline model execution.

Core docs:

- `references/docs/harmonyos-guides/neural-network-runtime-kit.md`
- `references/docs/harmonyos-guides/neural-network-runtime-kit-introduction.md`
- `references/docs/harmonyos-guides/neural-network-runtime-guidelines.md`

Implementation notes:

- NNRt can build internal model graphs from framework graphs, compile them to hardware-specific models, execute inference, manage shared memory, select devices, and cache model compilation results.
- It does not provide CPU general inference; it exposes capabilities of underlying AI acceleration hardware.
- It currently supports common synchronous inference patterns in the local docs; verify supported operators and hardware before use.
- Constraints from local docs: strongly hardware dependent; requires supported NPU hardware; simulator unsupported.

## Speech Kit

Purpose: scenario-level speech UI/components.

Use when:

- The app needs ready-made reading or AI caption controls rather than raw ASR/TTS APIs.

Core docs:

- `references/docs/harmonyos-guides/speech-kit-guide.md`
- `references/docs/harmonyos-guides/speech-production.md`
- `references/docs/harmonyos-guides/speech-textreader-guide.md`
- `references/docs/harmonyos-guides/speech-aicaption-guide.md`

Implementation notes:

- Reading control: useful for article/news reading.
- AI caption control: useful for captions when users cannot hear or do not understand source audio.
- Constraints from local docs: Phone/Tablet/PC/2in1; China mainland only; simulator unsupported.
- AI caption constraints in the docs include PCM audio, 16000 sample rate, one channel, 16-bit depth; some models/devices may fail initialization.

## Vision Kit

Purpose: scenario-level visual AI services/components.

Use when:

- The app needs liveness detection, card recognition, document scan, or AI image analyzer UI.

Core docs:

- `references/docs/harmonyos-guides/vision-kit-guide.md`
- `references/docs/harmonyos-guides/vision-introduction.md`
- `references/docs/harmonyos-guides/vision-interactiveliveness.md`
- `references/docs/harmonyos-guides/vision-cardrecognition.md`
- `references/docs/harmonyos-guides/vision-documentscanner.md`
- `references/docs/harmonyos-guides/vision-imageanalyzer.md`
- `references/docs/harmonyos-guides/visionkit-personal-data.md`

Implementation notes:

- Vision Kit capabilities include liveness, card recognition, document scanning, and AI image analyzer.
- Device support differs by capability: local docs list liveness/card/document scan for Phone/Tablet, and AI image analyzer for Phone/Tablet/PC/2in1.
- Local docs list China mainland only and simulator unsupported.
- Do not overlap/cover card/document scanning components with other UI; docs call this out for some capabilities.
- For plain OCR, segmentation, face detection/comparison, object detection, or skeleton detection, prefer Core Vision Kit unless the task specifically needs Vision Kit UI.

## Review Checklist For AI Kit Changes

- Exact Kit chosen for the user need, with reason.
- Official doc searched and relevant source file opened.
- Device/country/API/simulator constraints checked.
- `module.json5` permissions declared when needed.
- Runtime permission flow implemented when user-grant permission is needed.
- Any required whitelist, entitlement, Huawei account, online state, open-platform config, or AppGallery listing step documented.
- Service/helper boundary used for reusable AI logic.
- UI handles loading, cancellation, failure, unsupported device, no result, and retry.
- No hardcoded secrets or cloud API keys in ArkTS client code.
- Model files, raw resources, `syscap.json`, Native/N-API, and `oh-package.json5` changes are consistent with the selected route.
