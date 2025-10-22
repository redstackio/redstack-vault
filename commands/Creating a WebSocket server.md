---
id: d9563421-287a-44a6-9c83-bf6cb00d0441
name: Creating a WebSocket server
type: command
executor: bash
data: 'const WebSocket = require(''ws'');

  const wss = new WebSocket.Server({ port: 8080 });'
output: null
created_at: '2023-04-06T03:56:41.344638+00:00'
updated_at: '2023-04-06T03:56:41.360104+00:00'
---

# Creating a WebSocket server

```bash
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });
```
