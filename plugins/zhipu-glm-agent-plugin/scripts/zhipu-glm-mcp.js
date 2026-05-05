#!/usr/bin/env node
'use strict';

const DEFAULT_BASE_URL = 'https://open.bigmodel.cn/api/paas/v4';
const DEFAULT_MODEL = 'glm-4.7';
const SERVER_NAME = 'zhipu-glm';
const SERVER_VERSION = '0.1.0';

let inputBuffer = '';

process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => {
  inputBuffer += chunk;
  let newlineIndex;
  while ((newlineIndex = inputBuffer.indexOf('\n')) !== -1) {
    const line = inputBuffer.slice(0, newlineIndex).replace(/^\uFEFF/, '').replace(/\r$/, '');
    inputBuffer = inputBuffer.slice(newlineIndex + 1);
    if (line.trim()) {
      handleLine(line).catch(err => {
        writeError(null, -32603, safeError(err));
      });
    }
  }
});

process.stdin.on('end', () => process.exit(0));

async function handleLine(line) {
  let message;
  try {
    message = JSON.parse(line);
  } catch (err) {
    writeError(null, -32700, `Parse error: ${safeError(err)}`);
    return;
  }

  if (!message || typeof message !== 'object') {
    writeError(null, -32600, 'Invalid request');
    return;
  }

  if (message.id === undefined) {
    await handleNotification(message);
    return;
  }

  try {
    const result = await handleRequest(message.method, message.params ?? {});
    writeMessage({ jsonrpc: '2.0', id: message.id, result });
  } catch (err) {
    writeError(message.id, -32603, safeError(err));
  }
}

async function handleNotification(_message) {
  // `notifications/initialized` does not require a response.
}

async function handleRequest(method, params) {
  switch (method) {
    case 'initialize':
      return {
        protocolVersion: params.protocolVersion ?? '2024-11-05',
        capabilities: { tools: {} },
        serverInfo: { name: SERVER_NAME, version: SERVER_VERSION },
        instructions: 'Use glm_chat to ask Zhipu AI / BigModel GLM models. The server reads ZHIPUAI_API_KEY from the environment and never prints it.',
      };
    case 'ping':
      return {};
    case 'tools/list':
      return { tools: [glmChatTool()] };
    case 'tools/call':
      return callTool(params);
    default:
      throw new Error(`Unsupported MCP method: ${method}`);
  }
}

function glmChatTool() {
  return {
    name: 'glm_chat',
    description: 'Call Zhipu AI / BigModel GLM chat completions with a prompt or explicit messages.',
    inputSchema: {
      type: 'object',
      properties: {
        prompt: {
          type: 'string',
          description: 'Simple user prompt. Use this when explicit messages are not needed.',
        },
        messages: {
          type: 'array',
          description: 'Explicit chat messages. Each item must include role and content.',
          items: {
            type: 'object',
            properties: {
              role: { type: 'string', enum: ['system', 'user', 'assistant', 'tool'] },
              content: {
                description: 'Message content string, or BigModel multimodal content array.',
                anyOf: [
                  { type: 'string' },
                  { type: 'array' },
                  { type: 'object' },
                ],
              },
            },
            required: ['role', 'content'],
          },
        },
        system: {
          type: 'string',
          description: 'Optional system message prepended before prompt/messages.',
        },
        model: {
          type: 'string',
          description: 'GLM model name. Defaults to ZHIPUAI_MODEL or glm-4.7.',
        },
        thinking_type: {
          type: 'string',
          enum: ['enabled', 'disabled'],
          description: 'Optional GLM thinking.type setting.',
        },
        temperature: {
          type: 'number',
          description: 'Sampling temperature.',
        },
        max_tokens: {
          type: 'integer',
          description: 'Maximum output tokens.',
        },
        request_id: {
          type: 'string',
          description: 'Optional caller-provided request id.',
        },
      },
      anyOf: [
        { required: ['prompt'] },
        { required: ['messages'] },
      ],
    },
  };
}

async function callTool(params) {
  if (params.name !== 'glm_chat') {
    return toolError(`Unknown tool: ${params.name}`);
  }

  try {
    const args = params.arguments ?? {};
    const result = await callGlm(args);
    return {
      content: [{ type: 'text', text: result }],
    };
  } catch (err) {
    return toolError(safeError(err));
  }
}

async function callGlm(args) {
  const apiKey = process.env.ZHIPUAI_API_KEY;
  if (!apiKey) {
    throw new Error('Missing ZHIPUAI_API_KEY. Set it in the environment before starting the plugin.');
  }

  const baseUrl = stripTrailingSlash(process.env.ZHIPUAI_BASE_URL || DEFAULT_BASE_URL);
  const model = stringArg(args.model) || process.env.ZHIPUAI_MODEL || DEFAULT_MODEL;
  const messages = normalizeMessages(args);

  const body = {
    model,
    messages,
    stream: false,
  };

  if (args.temperature !== undefined) body.temperature = numberArg(args.temperature, 'temperature');
  if (args.max_tokens !== undefined) body.max_tokens = integerArg(args.max_tokens, 'max_tokens');
  if (args.request_id !== undefined) body.request_id = stringArg(args.request_id);
  if (args.thinking_type !== undefined) {
    const type = stringArg(args.thinking_type);
    if (!['enabled', 'disabled'].includes(type)) {
      throw new Error('thinking_type must be enabled or disabled.');
    }
    body.thinking = { type };
  }

  const timeoutMs = integerArg(process.env.ZHIPUAI_TIMEOUT_MS || 60000, 'ZHIPUAI_TIMEOUT_MS');
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);

  let response;
  let responseText;
  try {
    response = await fetch(`${baseUrl}/chat/completions`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
        'User-Agent': 'zhipu-glm-agent-plugin/0.1.0',
      },
      body: JSON.stringify(body),
      signal: controller.signal,
    });
    responseText = await response.text();
  } finally {
    clearTimeout(timer);
  }

  if (!response.ok) {
    throw new Error(`BigModel API error ${response.status}: ${redact(responseText, apiKey).slice(0, 1200)}`);
  }

  let data;
  try {
    data = JSON.parse(responseText);
  } catch {
    throw new Error(`BigModel API returned non-JSON response: ${redact(responseText, apiKey).slice(0, 1200)}`);
  }

  return formatGlmResponse(data, model);
}

function normalizeMessages(args) {
  const messages = [];
  if (args.system !== undefined) {
    messages.push({ role: 'system', content: stringArg(args.system) });
  }

  if (Array.isArray(args.messages)) {
    for (const msg of args.messages) {
      if (!msg || typeof msg !== 'object') {
        throw new Error('messages items must be objects.');
      }
      const role = stringArg(msg.role);
      if (!['system', 'user', 'assistant', 'tool'].includes(role)) {
        throw new Error(`Unsupported message role: ${role}`);
      }
      if (msg.content === undefined) {
        throw new Error('messages items require content.');
      }
      messages.push({ role, content: msg.content });
    }
  } else if (args.prompt !== undefined) {
    messages.push({ role: 'user', content: stringArg(args.prompt) });
  } else {
    throw new Error('Provide prompt or messages.');
  }

  return messages;
}

function formatGlmResponse(data, model) {
  const choice = Array.isArray(data.choices) ? data.choices[0] : undefined;
  const message = choice?.message ?? {};
  const content = stringifyContent(message.content);
  const reasoning = stringifyContent(message.reasoning_content);
  const usage = data.usage ? JSON.stringify(data.usage) : '';
  const finishReason = choice?.finish_reason ? String(choice.finish_reason) : '';

  const sections = [`model: ${data.model || model}`];
  if (finishReason) sections.push(`finish_reason: ${finishReason}`);
  if (content) sections.push(`content:\n${content}`);
  if (reasoning) sections.push(`reasoning_content:\n${reasoning}`);
  if (usage) sections.push(`usage: ${usage}`);

  if (sections.length <= 2 && !content && !reasoning) {
    sections.push(`raw_response:\n${JSON.stringify(data, null, 2)}`);
  }

  return sections.join('\n\n');
}

function stringifyContent(value) {
  if (value === undefined || value === null) return '';
  if (typeof value === 'string') return value;
  return JSON.stringify(value, null, 2);
}

function stringArg(value) {
  if (typeof value !== 'string') {
    throw new Error('Expected string argument.');
  }
  return value;
}

function numberArg(value, name) {
  const number = Number(value);
  if (!Number.isFinite(number)) {
    throw new Error(`${name} must be a number.`);
  }
  return number;
}

function integerArg(value, name) {
  const number = Number(value);
  if (!Number.isInteger(number)) {
    throw new Error(`${name} must be an integer.`);
  }
  return number;
}

function stripTrailingSlash(value) {
  return String(value).replace(/\/+$/, '');
}

function toolError(text) {
  return {
    content: [{ type: 'text', text }],
    isError: true,
  };
}

function writeMessage(message) {
  process.stdout.write(`${JSON.stringify(message)}\n`);
}

function writeError(id, code, message) {
  writeMessage({
    jsonrpc: '2.0',
    id,
    error: { code, message },
  });
}

function safeError(err) {
  const text = err instanceof Error ? err.message : String(err);
  return redact(text, process.env.ZHIPUAI_API_KEY || '');
}

function redact(text, secret) {
  if (!secret) return String(text);
  return String(text).split(secret).join('[REDACTED]');
}
