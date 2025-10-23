---
id: bb4190d6-5422-4861-b5e2-c5fba78b3d92
name: Handling WebSocket connection
type: command
executor: bash
data: "wss.on('connection', function connection(ws) {\n  ws.on('message', function\
  \ incoming(message) {\n    console.log('received: %s', message);\n  });\n  ws.send('something');\n\
  });"
output: null
created_at: '2023-04-06T03:56:41.344657+00:00'
updated_at: '2023-04-06T03:56:41.360167+00:00'
---

# Handling WebSocket connection

```bash
wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });
  ws.send('something');
});
```


