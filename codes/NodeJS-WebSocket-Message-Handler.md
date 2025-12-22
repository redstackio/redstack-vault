---
type: code
language: javascript
verified: true
tags:
  - websocket
  - handler
  - nodejs
platforms:
  - Linux
  - macOS
  - Windows
validated: true
---

# NodeJS-WebSocket-Message-Handler

## Code

```javascript
wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });
  ws.send('something');
});
```

## Description

This code defines event listeners for incoming WebSocket connections: it logs received messages to the console and immediately sends a static response ('something') back to the client. Used in vulnerable server setups to echo or respond with data that can be exfiltrated in CSWSH attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (none) | No configurable variables; response message is hardcoded | 'something' |

## Usage

Append this after WebSocket server creation in a Node.js script. It activates on each new connection, logging inputs and sending outputs. In testing, this allows attackers to observe hijacked messages and confirm exfiltration of the response.

## Detection

- Console output or logs showing unexpected 'received' messages from cross-origin clients.
- WebSocket traffic patterns with immediate static responses indicating lack of auth checks.
- EDR alerts on Node.js scripts handling real-time bidirectional comms without validation.

## Related

- [[procedures/Perform-Cross-Site-WebSocket-Hijacking]]
