---
type: code
language: javascript
verified: true
tags:
  - websocket
  - server
  - nodejs
platforms:
  - Linux
  - macOS
  - Windows
validated: true
---

# NodeJS-WebSocket-Server-Creation

## Code

```javascript
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });
```

## Description

This code snippet initializes a WebSocket server using the 'ws' library, binding it directly to a port for accepting connections. It is used to simulate a vulnerable endpoint in security testing, such as for CSWSH demonstrations, without additional HTTP server wrapping.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| port | Port number for the WebSocket server | 8080 |

## Usage

Include this at the top of a Node.js script (server.js) after installing 'ws'. Combine with connection handlers to process messages. Run with 'node server.js' to start listening. Ideal for lab setups where Origin validation is intentionally omitted to test hijacking attacks.

## Detection

- Node.js processes listening on non-standard ports with 'ws' module loaded.
- Network traffic showing WebSocket upgrades without corresponding HTTP handshakes.
- Process listings revealing 'node server.js' with WebSocket imports.

## Related

- [[procedures/Perform-Cross-Site-WebSocket-Hijacking]]
