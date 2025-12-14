---
id: 123e4567-e89b-12d3-a456-426614174004
name: websocket-test-js
type: command
executor: javascript
data: >-
  const ws = new WebSocket('ws://target.com/ws'); ws.onopen = function(event) {
  console.log('Connected'); }; ws.onerror = function(error) {
  console.log('Error:', error); };
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.960Z'
platforms:
  - Web
tags:
  - websocket
  - testing
verified: false
validated: true
submitted: true
---

# websocket-test-js

## Command

```javascript
const ws = new WebSocket('ws://target.com/ws');
ws.onopen = function(event) { console.log('Connected'); };
ws.onerror = function(error) { console.log('Error:', error); };
```

## Description

This JavaScript command tests a WebSocket connection from a browser console or script, checking for successful handshake to detect CSWSH vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ws://target.com/ws` | Target WebSocket URL | Yes |
| `onopen` | Event handler for connection success | No |
| `onerror` | Event handler for failures | No |

## Examples

### Basic Usage

```javascript
const ws = new WebSocket('ws://target.com/ws');
ws.onopen = function(event) { console.log('Connected'); };
```

### Advanced Usage

```javascript
const ws = new WebSocket('wss://target.com/secure-ws');
ws.onopen = function() { console.log('Secure connection'); };
ws.onerror = function(error) { console.error('Secure error:', error); };
```

## Expected Output

Console log: 'Connected' on success, or 'Error: [details]' on failure indicating protections.

## Related

- [[Related Procedure: Test-WebSocket-for-CSWSH-Vulnerability]]
