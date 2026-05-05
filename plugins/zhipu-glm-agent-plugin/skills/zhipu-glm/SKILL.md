---
name: zhipu-glm
description: Use when the user asks to consult Zhipu GLM, BigModel, 智谱 AI, or GLM models for a second opinion, Chinese drafting, reasoning, code review, summarization, or model comparison through the configured ZHIPUAI_API_KEY.
---

# Zhipu GLM

Use this skill to call Zhipu AI / BigModel GLM models through the local `glm_chat` MCP tool.

## Required Setup

The plugin never stores an API key. The runtime must provide:

```powershell
$env:ZHIPUAI_API_KEY = "your-api-key"
```

Optional environment overrides:

- `ZHIPUAI_MODEL`: default model, initially `glm-4.7`.
- `ZHIPUAI_BASE_URL`: default API base, initially `https://open.bigmodel.cn/api/paas/v4`.
- `ZHIPUAI_TIMEOUT_MS`: request timeout in milliseconds.

## Usage Rules

- Use `glm_chat` for explicit GLM requests or when the user wants an external model's second opinion.
- Do not send secrets, private keys, credentials, or unredacted customer data to GLM.
- Keep prompts scoped. Prefer concise context plus the exact question.
- State that the response came from GLM when using it as an external opinion.
- For current model/API behavior, rely on official BigModel docs or the request result, not memory.

## Tool Defaults

- `model`: `ZHIPUAI_MODEL` or `glm-4.7`.
- `base_url`: `ZHIPUAI_BASE_URL` or `https://open.bigmodel.cn/api/paas/v4`.
- Non-streaming chat completions only.
- `thinking_type` may be `enabled` or `disabled`; omit it when you want the model default.

## Output Handling

When returning GLM output to the user:

- Include the answer content directly.
- Include reasoning content only when the tool returns it and it is useful to the task.
- Include usage metadata only when it helps explain cost, truncation, or debugging.
- If the API call fails, report the status and non-secret error body; never reveal `ZHIPUAI_API_KEY`.
