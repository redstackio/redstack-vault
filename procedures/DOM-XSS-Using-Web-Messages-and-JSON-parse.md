---
id: 5c0b9508-a2e9-43a0-a90b-6f4cf9abce4e
name: DOM-XSS-Using-Web-Messages-and-JSON-parse
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T14:35:36.746931+00:00'
updated_at: '2023-05-26T01:36:09.708027+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - DOM XSS
  - injection
  - owasp
  - owasp top 10
  - Web Applications
commands: []
platforms:
  - Web
tools: []
validated: true
---

# DOM-XSS-Using-Web-Messages-and-JSON-parse

## Summary

This procedure demonstrates how to exploit a DOM-based Cross-Site Scripting (XSS) vulnerability by leveraging the postMessage API to send a malicious web message that gets processed via JSON.parse on the target application, leading to arbitrary JavaScript execution such as alerting document cookies.

## Description

DOM XSS occurs when client-side code unsafely processes data from untrusted sources, such as web messages received via the postMessage event listener. In this scenario, the target application has an event listener that receives messages and parses them using JSON.parse without proper validation, allowing an attacker to inject a malicious payload in the JSON structure. The payload tricks the parser into executing JavaScript, such as revealing sensitive data like cookies. This technique is common in modern web apps using cross-origin communication and maps to MITRE ATT&CK technique T1059.007 (JavaScript) under the Execution tactic. It requires access to a browser and the target application's URL, typically in a lab or vulnerable environment.

## Requirements

1. A modern web browser (e.g., Chrome, Firefox) with developer tools enabled.
2. Access to the target web application's URL where the vulnerable postMessage listener exists.
3. No special privileges needed, but the target must load an iframe or similar context for message passing.
4. Basic knowledge of HTML, JavaScript, and the postMessage API.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all data passed to JSON.parse, ensuring it conforms to expected schemas and rejecting any 'javascript:' URLs or executable code.
- Use structured clone algorithms or safer parsers instead of JSON.parse for untrusted inputs.
- Implement Content Security Policy (CSP) to restrict script execution from unexpected sources.
- Monitor for anomalous postMessage events in browser developer tools or web application firewalls (WAFs).
- Educate developers on secure cross-origin communication practices per OWASP guidelines.

## Objectives

1. Identify the vulnerable postMessage event listener in the target's source code.
2. Craft and deliver a malicious JSON payload via an iframe to trigger DOM XSS.
3. Execute arbitrary JavaScript on the target domain to demonstrate impact, such as stealing cookies.
4. Verify successful exploitation through visible effects like alert popups.

## Instructions

### Step 1: Inspect the Target Application Source

**Context**: Access the vulnerable page and examine its source code to confirm the presence of a postMessage event listener that uses JSON.parse on received messages without validation. This step identifies the injection point for the malicious payload.

Open the target application in your browser, right-click on the page, and select "View Page Source" (or use Ctrl+U). Search for 'postMessage' or 'JSON.parse' to locate the event listener, typically attached to the window.onload or similar event.

**Expected Output**: Source code revealing code like `window.addEventListener('message', function(event) { var data = JSON.parse(event.data); ... })`, confirming the vulnerability.

### Step 2: Analyze the Event Listener Behavior

**Context**: Understand how the application processes incoming messages to craft an effective payload. The listener expects a JSON object with fields like 'type' and 'url', but fails to sanitize the 'url' field, allowing JavaScript injection.

Use the browser's developer tools (F12) to inspect the page elements and console for any dynamic behavior. Note that messages are sent cross-origin but processed if the origin is '*', and the parsed JSON drives actions like loading content from the 'url' field.

**Expected Output**: Confirmation in the console or network tab that messages are received and parsed, potentially logging errors if malformed JSON is sent for testing.

### Step 3: Craft the Malicious Payload

**Context**: Create an HTML snippet using an iframe to send a postMessage with a tampered JSON payload. The payload embeds a 'javascript:' URI in the 'url' field, which gets executed after JSON.parse due to unsafe handling.

Construct the payload as an HTML iframe that loads the target in its src and uses the onload event to post the message. Reference the code snippet [[codes/Iframe-PostMessage-DOM-XSS-Payload]] for the exact structure.

**Expected Output**: A valid HTML string ready for loading, with escaped JSON containing the injection point.

### Step 4: Execute the Payload and Verify Exploitation

**Context**: Load the crafted payload in a new browser tab or frame to trigger the message and observe the XSS execution. This delivers the payload and confirms the vulnerability.

Save the payload as an HTML file (e.g., exploit.html) and open it in the browser, or paste it into the address bar if supported. Monitor for the alert dialog displaying document cookies.

**Expected Output**: A JavaScript alert popup showing the contents of document.cookie from the target domain, indicating successful code execution.
