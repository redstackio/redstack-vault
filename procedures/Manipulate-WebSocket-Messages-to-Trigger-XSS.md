---
id: 22538c12-55db-48df-8378-9e387d14c377
name: Manipulate-WebSocket-Messages-to-Trigger-XSS
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T14:42:03.772376+00:00'
updated_at: '2023-05-26T18:23:38.347176+00:00'
platforms:
  - Web
tags:
  - web-applications
  - web-sockets
  - xss
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Manipulate-WebSocket-Messages-to-Trigger-XSS

## Summary

This procedure demonstrates how to intercept and modify WebSocket messages using a proxy tool like Burp Suite to inject a cross-site scripting (XSS) payload, triggering a JavaScript alert in the target application. It targets web applications that use WebSockets for real-time communication, such as chat features, where insufficient input validation allows reflected XSS via manipulated messages.

## Description

WebSockets enable bidirectional communication between client and server, often used in modern web apps for features like live chat or notifications. If the application echoes user messages without proper sanitization, an attacker can intercept outgoing WebSocket frames, replace the message content with malicious JavaScript, and forward it. Upon receipt and rendering by the server or other clients, the payload executes, potentially leading to session hijacking, data theft, or further exploitation. This technique is effective against applications vulnerable to reflected or DOM-based XSS in WebSocket-handled data. Prerequisites include network access to the target app and a proxy configured to intercept WebSocket traffic.

## Requirements

1. Access to a web browser and the target web application with WebSocket functionality (e.g., a chat interface).
2. Burp Suite or similar proxy tool installed and configured to intercept HTTPS/WebSocket traffic (requires CA certificate installation in the browser).
3. Basic knowledge of WebSocket protocol and JavaScript for payload crafting.
4. Target application must be vulnerable to unsanitized message reflection.

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) headers to restrict inline JavaScript execution.
- Sanitize and encode all WebSocket message contents on both client and server sides using libraries like DOMPurify.
- Monitor WebSocket traffic for anomalous payloads using web application firewalls (WAFs) like ModSecurity.
- Enable logging of WebSocket messages and alert on suspicious patterns, such as script tags or onerror handlers.

## Objectives

1. Intercept a legitimate WebSocket message to understand the frame structure.
2. Inject an XSS payload into the message content to test for reflection vulnerabilities.
3. Trigger JavaScript execution in the target application to confirm the vulnerability.
4. Demonstrate the potential for broader exploitation, such as alert popups leading to code execution.

## Instructions

### Step 1: Establish WebSocket Connection and Send Test Message

**Context**: Interact with the target application's WebSocket-enabled feature (e.g., chat window) to initiate a connection and generate a capturable message. This step ensures the proxy can intercept the traffic.

Configure your browser to route traffic through Burp Suite Proxy. Navigate to the target application and locate the WebSocket interface, such as a chat input field.

Type and send a benign test message, like "Hello", to trigger a WebSocket frame.

> This action establishes the connection and populates the proxy's history with a sample frame for modification.

### Step 2: Intercept and Identify the WebSocket Message

**Context**: Use the proxy tool to capture the outgoing WebSocket message from the test input, allowing inspection of the frame structure.

In Burp Suite, navigate to the Proxy > WebSockets history tab. Locate the recent message frame corresponding to the test input (identified by timestamp or content). Select the frame to view its details, including the opcode (typically 1 for text) and payload.

> Successful interception shows the raw WebSocket frame, often in JSON or plain text format, ready for editing.

### Step 3: Modify the Message with XSS Payload

**Context**: Alter the message payload to include a malicious JavaScript snippet that will execute if reflected without sanitization. This tests for XSS vulnerability in the WebSocket handler.

In the selected WebSocket frame, edit the message content field. Replace the benign text with the XSS payload: `<img src=1 onerror='alert(1)'>`. Ensure the frame structure remains intact (e.g., preserve headers or JSON keys if applicable).

> The payload uses an invalid image source to trigger the onerror event, executing alert(1) to demonstrate code injection.

### Step 4: Forward the Modified Message and Observe Execution

**Context**: Send the tampered frame to the server to check if the application processes and renders it, leading to payload execution.

Click 'Forward' or 'Send to Server' in the proxy interface to transmit the modified frame. Switch to the browser and observe the application's response, such as the chat window updating with the injected content.

> If vulnerable, a JavaScript alert popup with '1' appears, confirming XSS execution via the WebSocket channel.

## Expected Output

Successful execution results in the target application rendering the modified message, triggering the alert(1) popup. In Burp, the history shows the forwarded frame and any response frames from the server echoing the payload. No errors in the proxy or browser console indicate clean transmission.
