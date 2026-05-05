# Zhipu GLM Agent Plugin

Codex and Claude Code plugin for calling Zhipu AI / BigModel GLM chat models through a local MCP server.

## Setup

Set your API key in the environment before starting Codex or Claude Code:

```powershell
$env:ZHIPUAI_API_KEY = "your-api-key"
```

Optional overrides:

```powershell
$env:ZHIPUAI_MODEL = "glm-4.7"
$env:ZHIPUAI_BASE_URL = "https://open.bigmodel.cn/api/paas/v4"
$env:ZHIPUAI_TIMEOUT_MS = "60000"
```

## Tool

The plugin exposes one MCP tool:

- `glm_chat`: calls `POST /chat/completions` on the configured BigModel API base.

Useful arguments:

- `prompt`: simple user prompt.
- `messages`: explicit chat messages.
- `system`: optional system message.
- `model`: override the model.
- `thinking_type`: `enabled` or `disabled`.
- `temperature`: sampling temperature.
- `max_tokens`: maximum output tokens.

## Claude Code

From this plugin directory:

```powershell
claude --plugin-dir .
```

Command:

```text
/zhipu-glm-agent-plugin:glm-chat 用中文总结这段设计方案
```

## Notes

- The plugin does not store API keys.
- Requests are non-streaming.
- Default model is `glm-4.7`, matching the current BigModel chat completion examples.
