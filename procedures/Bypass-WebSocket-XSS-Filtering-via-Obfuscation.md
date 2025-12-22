---
id: 04f4b3a1-5428-4b70-8c06-998a2d1ce361
name: Bypass-WebSocket-XSS-Filtering-via-Obfuscation
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T14:26:01.202086+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - web-applications
  - web-sockets
  - xss
  - bypass
  - injection
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
codes:
  - '[[codes/Basic-IMG-XSS-Payload]]'
  - '[[codes/Obfuscated-JavaScript-XSS-Payload]]'
validated: true
---

# Bypass-WebSocket-XSS-Filtering-via-Obfuscation

## Summary

This procedure demonstrates how to manipulate WebSocket communications in a web application to bypass XSS filtering. By intercepting messages, testing basic payloads that trigger defenses, re-establishing the connection with spoofed headers, and using obfuscated payloads, an attacker can inject malicious JavaScript that evades detection and executes on the client side.

## Description

WebSockets enable real-time bidirectional communication between clients and servers, often used in chat applications or live updates. Many applications implement filtering to block malicious payloads like XSS in WebSocket messages. This procedure exploits weak filtering by first triggering a block with a standard payload to close the connection, then spoofing the client IP via the X-Forwarded-For header to reconnect (potentially bypassing IP-based rate limiting or session checks), and finally sending an obfuscated XSS payload that slips past case-sensitive or pattern-based filters. This technique is effective against applications with incomplete input sanitization on WebSocket channels, leading to client-side code execution. It requires proxy interception tools like Burp Suite and assumes the target uses a proxy-aware backend.

## Requirements

1. Access to a web application with WebSocket-based features (e.g., live chat).
2. Burp Suite or similar proxy tool configured to intercept HTTPS traffic.
3. Valid session or authentication to interact with the WebSocket endpoint.
4. Knowledge of the target's WebSocket URL and message format.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and sanitization for all WebSocket messages, including normalization for obfuscation attempts (e.g., case mixing, encoding).
- Use Content Security Policy (CSP) headers to restrict inline script execution.
- Monitor for anomalous WebSocket connections, including rapid reconnects with varying X-Forwarded-For headers.
- Log and analyze WebSocket traffic for suspicious payloads; employ WAF rules targeting common XSS patterns and obfuscations.
- Enforce strict origin checks and validate client IPs beyond headers.

## Objectives

1. Intercept and analyze normal WebSocket messages to understand the format.
2. Test and trigger defensive filtering to identify blocking mechanisms.
3. Re-establish the WebSocket connection using spoofed headers to reset session state.
4. Inject an obfuscated XSS payload to achieve code execution without detection.

## Instructions

### Step 1: Observe Normal WebSocket Communication

**Context**: Establish a baseline by interacting with the application's WebSocket feature, such as sending a message in a live chat, to capture the legitimate message format and endpoint.

Use [[tools/Burp-Suite]] to monitor traffic without interception initially.

> Interact with the chat interface by sending a benign message (e.g., "Hello"). Note the WebSocket handshake (Upgrade: websocket) and subsequent message frames.

### Step 2: Intercept and Forward to Repeater

**Context**: Capture an outgoing WebSocket message during normal interaction and route it to Burp Repeater for manipulation. This allows isolated testing without disrupting the live session.

Configure [[tools/Burp-Suite]] Proxy to intercept WebSocket traffic.

> With interception enabled, send a message from the application. In the Proxy history, right-click the WebSocket frame and select "Send to Repeater." This opens the message in Repeater for editing.

### Step 3: Test Basic XSS Payload and Observe Block

**Context**: Modify the intercepted message to include a standard XSS payload, send it, and confirm the server's filtering response, which typically closes the connection.

In Burp Repeater, edit the message body to inject the payload from [[codes/Basic-IMG-XSS-Payload]].

> Send the modified message. The server should reject it, log a block (if visible), and terminate the WebSocket connection. Verify in the application that the message does not appear and the chat disconnects.

### Step 4: Re-establish Connection with Spoofed Header

**Context**: After the block closes the connection, reconnect by adding a spoofed X-Forwarded-For header to mimic a new client IP, potentially evading session or rate limits tied to the original IP.

In Burp Repeater or a new tab, initiate a new WebSocket handshake.

> Add the header `X-Forwarded-For: 1.1.1.1` to the initial HTTP request that upgrades to WebSocket. Click "Connect" or send the request. Confirm the connection re-establishes successfully, restoring message sending capability.

### Step 5: Inject Obfuscated XSS Payload

**Context**: With the connection reset, send a modified payload using obfuscation techniques (e.g., mixed case, alternative tags) to bypass regex-based or simple string filters.

Edit the message in Repeater to include the payload from [[codes/Obfuscated-JavaScript-XSS-Payload]].

> Send the message. Observe in the application that the payload is accepted, rendered, and executes (e.g., alert dialog appears), confirming the bypass.
