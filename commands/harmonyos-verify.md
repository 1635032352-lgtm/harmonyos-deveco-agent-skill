---
description: Verify HarmonyOS build, signing, routing, permissions, Preview, and device evidence.
---

# HarmonyOS Command Prompt: /harmonyos-verify

Use this prompt to run the `harmonyos-deveco` verification checkpoint.

## Arguments

`$ARGUMENTS`

## Delegation

Apply the `harmonyos-deveco` skill.

- Check only the requested evidence unless the user asks for broader release readiness.
- Produce an evidence matrix with exact commands, artifacts, timestamps, PASS/CONDITIONAL PASS/BLOCKED status, and the smallest next verification step.
- Keep unsigned HAP, signed HAP, signing config, Preview screenshot, device screenshot, and submit-ready status as separate facts.
- Do not claim a device, Preview, signing, or build check passed unless it actually ran in that environment.
