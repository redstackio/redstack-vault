---
data: >-
  {"command":"setUrl","params":{"url":"https://example.net"},"source":"QAS","target":"AGL"}
tags:
  - websocket
  - url-loading
type: command
executor: json
platforms:
  - Windows
id: 874949d9-d623-4df9-b948-b267b04a3547
created_at: '2025-12-11T03:47:56.465Z'
updated_at: '2025-12-11T03:47:56.465Z'
verified: false
validated: true
submitted: true
---
# websocket-seturl-example

## Command

```json
{"command":"setUrl","params":{"url":"https://example.net"},"source":"QAS","target":"AGL"}
```

## Description

WebSocket JSON command to instruct AGL to load a specified URL, testing arbitrary loading.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `command` | setUrl | Yes |
| `params.url` | The URL to load | Yes |
| `source` | QAS | Yes |
| `target` | AGL | Yes |

## Examples

### Basic Usage

```json
{"command":"setUrl","params":{"url":"https://example.net"},"source":"QAS","target":"AGL"}
```

## Expected Output

AGL loads the specified URL.

## Related

- [[procedures/Test-Arbitrary-URL-Loading-via-WebSocket]]
