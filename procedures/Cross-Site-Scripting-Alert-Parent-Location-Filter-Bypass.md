---
id: b21ca177-b989-47a3-9291-40fb6883ee8a
name: Cross-Site-Scripting-Alert-Parent-Location-Filter-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.659989+00:00'
updated_at: '2023-04-10T20:21:38.483205+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Bypass document blacklist]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
  - xss
  - filter-bypass
  - javascript
commands: []
platforms:
  - Web
  - Browser
tools: []
validated: true
---

# Cross-Site-Scripting-Alert-Parent-Location-Filter-Bypass

## Summary

This procedure demonstrates a Cross-Site Scripting (XSS) attack that bypasses document blacklists by using a JavaScript payload to alert the parent window's location. It injects malicious code into a vulnerable web page, allowing arbitrary code execution in the victim's browser to steal sensitive information like the current URL or session data.

## Description

Cross-Site Scripting (XSS) involves injecting malicious scripts into trusted websites, which execute in the victim's browser context. This technique targets filters that blacklist common XSS payloads by navigating the DOM tree using parentNode properties to access the parent window's location without directly using blacklisted terms like 'document' or 'window'. The payload creates a div element and traverses up three parent nodes to reach the top-level location, displaying it in an alert. This can reveal the full URL, including query parameters or fragments with sensitive data, enabling further attacks like session hijacking. It is effective against reflected or stored XSS vulnerabilities where direct script tags are filtered but DOM manipulation is allowed. The target environment is any web application with insufficient input sanitization, typically in browsers supporting JavaScript.

## Requirements

1. Access to a vulnerable web page with an XSS injection point (e.g., search field, comment section).
2. Knowledge of the DOM structure to ensure the parentNode traversal reaches the intended location.
3. A testing environment or victim browser to observe the alert.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) to prevent script injection.
- Deploy a Content Security Policy (CSP) to restrict inline scripts and eval() usage.
- Regularly scan and patch web applications using tools like OWASP ZAP or Burp Suite to identify XSS vulnerabilities.
- Enable browser security features like XSS Auditor (deprecated in modern browsers) or use HttpOnly and Secure flags on cookies.

## Objectives

1. Bypass document blacklists to inject and execute JavaScript in the victim's browser.
2. Extract and alert the parent window's location to reveal sensitive URL information.
3. Enable further exploitation, such as stealing session tokens or redirecting the user.

## Instructions

### Step 1: Identify Injection Point

**Context**: Locate a user-controlled input field on the target web page that reflects input without proper sanitization, such as a search parameter or form field. Test basic payloads like `<script>alert(1)</script>` to confirm XSS vulnerability, noting any blacklisted keywords.

> If the basic payload is blocked, proceed to the bypass technique. No specific command is needed here; use browser developer tools to inspect the reflected input.

### Step 2: Craft and Inject Bypass Payload

**Context**: Use the specialized JavaScript payload to traverse the DOM and access the parent location, avoiding direct references to blacklisted objects. This step injects the payload into the vulnerable field.

**Code** ([[codes/XSS-Payload-Alert-Parent-Location-Bypass]]):

```javascript
<div id = "x"></div><script>alert(x.parentNode.parentNode.parentNode.location)</script>
window["doc"+"ument"]
```

> This payload creates a div with id 'x', then uses a script tag to alert the location of the third parent node (typically the top window). The bracket notation at the end obfuscates 'document' access. Submit the payload via the injection point (e.g., URL parameter: ?search=<payload>). Expected output is an alert box displaying the parent URL, confirming execution.

### Step 3: Verify Execution and Extract Data

**Context**: Observe the alert in the victim's browser to capture the location data. If successful, the alert reveals the full URL, which can be used for further reconnaissance or data exfiltration.

> Manually note the alerted location. For automation in testing, use browser extensions like XSS Hunter. Success is indicated by the alert popping up without filter blocks.
