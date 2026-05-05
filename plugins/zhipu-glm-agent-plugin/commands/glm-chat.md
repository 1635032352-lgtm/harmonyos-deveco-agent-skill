---
description: Ask Zhipu GLM a focused question through the glm_chat MCP tool.
---

# GLM Chat

Use the `zhipu-glm` skill and call the `glm_chat` MCP tool.

## Arguments

`$ARGUMENTS`

## Instructions

- Treat `$ARGUMENTS` as the user prompt unless the user supplied structured messages.
- Do not include secrets, credentials, private keys, or unredacted customer data.
- Use the default model unless the user names a GLM model explicitly.
- Return the GLM answer and mention which model was used.
