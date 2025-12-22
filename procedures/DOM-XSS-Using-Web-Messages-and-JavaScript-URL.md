---
id: e269fadf-0e12-40ab-b0bd-ec4a904bf7b5
name: DOM-XSS-Using-Web-Messages-and-JavaScript-URL
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T14:51:46.620302+00:00'
updated_at: '2023-05-26T01:22:32.207771+00:00'
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
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# DOM-XSS-Using-Web-Messages-and-JavaScript-URL

## Summary

This procedure demonstrates how to exploit a DOM-based Cross-Site Scripting (XSS) vulnerability triggered via web messages (postMessage) and JavaScript URLs. By crafting a malicious iframe that sends a specially formatted message to the target application, an attacker can execute arbitrary JavaScript, such as alerting document cookies to steal session data.

## Description

DOM-based XSS occurs when client-side JavaScript processes untrusted data insecurely, leading to code injection. In this scenario, the vulnerable application uses an event listener for web messages (window.addEventListener('message')) and unsafely sets location.href based on the message data without validation. An attacker exploits this by posting a message starting with 'javascript:' followed by the payload, using '//http:' to comment out any subsequent URL scheme. This technique is common in web applications with cross-origin communication, such as embedded iframes or third-party integrations. The target environment is a web browser accessing a vulnerable web application, typically tested in a lab like PortSwigger Web Security Academy. Success results in arbitrary JavaScript execution in the victim's context, enabling cookie theft, keylogging, or further attacks.

## Requirements

1. Access to a web browser (e.g., Chrome, Firefox) with developer tools enabled.
2. URL of the vulnerable web application.
3. Ability to load custom HTML content, such as via a local file, phishing page, or controlled domain.
4. No special credentials required, but the victim must visit the attacker's crafted page while authenticated to the target site.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all postMessage data, ensuring the origin is trusted and the data does not contain 'javascript:' schemes.
- Use Content Security Policy (CSP) with 'unsafe-inline' restrictions and frame-ancestors to block unauthorized iframes.
- Implement strict origin checks in message event listeners (e.g., event.origin !== expectedOrigin).
- Monitor browser console for unexpected JavaScript execution and network logs for suspicious postMessage traffic.
- Employ Web Application Firewalls (WAFs) to detect anomalous iframe loads or message patterns.

## Objectives

1. Identify the vulnerable event listener in the application's source code.
2. Craft and deliver a payload that triggers JavaScript execution via web messages.
3. Verify exploitation by executing a proof-of-concept like alerting cookies.

## Instructions

### Step 1: Inspect the Target Application Source

**Context**: Examine the page source to confirm the presence of a vulnerable web message listener that unsafely handles location.href, allowing JavaScript URL injection.

Open the target page in a browser, right-click, and select 'View Page Source' or use developer tools (F12) to inspect the HTML and JavaScript.

Look for code similar to:

```javascript
window.addEventListener('message', function(event) {
    location.href = event.data;
});
```

This lacks origin validation and safe URL handling.

### Step 2: Craft the Malicious Payload

**Context**: Create an iframe that loads the target origin and posts a malicious message to trigger the DOM XSS.

Use the following code snippet as the payload:

**Code** ([[codes/DOM-XSS-Exploit-Using-Web-Messages-and-JavaScript-URL]]):

```html
<iframe src="https://acb11f271e33403880064a21005600ba.web-security-academy.net/" onload="this.contentWindow.postMessage('javascript:alert(document.cookie)//http:','*')"></iframe>
```

Substitute the src attribute with the actual target URL. The payload 'javascript:alert(document.cookie)//http:' executes the alert upon processing, with '//http:' preventing fallback to a benign HTTP redirect.

Save this as an HTML file (e.g., exploit.html) and open it in the browser, or host it on an attacker-controlled server.

### Step 3: Execute and Verify the Exploit

**Context**: Load the crafted page to deliver the payload and observe the execution in the target context.

Visit the exploit page while authenticated to the target application. The iframe will load the target, post the message, and trigger the vulnerable listener.

Monitor the browser for the alert popup displaying cookies, confirming successful XSS execution.

If no alert appears, check the console for errors (e.g., CORS issues) and ensure the target listener is active.
