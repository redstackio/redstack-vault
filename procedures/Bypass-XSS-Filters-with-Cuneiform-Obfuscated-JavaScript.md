---
id: 60d53005-6bc4-4348-942a-68619c4f63b9
name: Bypass-XSS-Filters-with-Cuneiform-Obfuscated-JavaScript
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.921723+00:00'
updated_at: '2023-04-10T20:21:32.228447+00:00'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Bypass using Cuneiform]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
  - xss
  - filter-bypass
  - obfuscation
  - javascript
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Bypass-XSS-Filters-with-Cuneiform-Obfuscated-JavaScript

## Summary

This procedure demonstrates how to bypass web application filters designed to block malicious JavaScript in Cross-Site Scripting (XSS) vulnerabilities by using Cuneiform Unicode encoding to obfuscate the payload. The obfuscated code executes arbitrary JavaScript in the victim's browser, enabling theft of sensitive data like session cookies for session hijacking and unauthorized actions.

## Description

In scenarios involving reflected or stored XSS vulnerabilities, web applications often filter common JavaScript payloads like <script>alert(1)</script> using blacklists or sanitization. This procedure leverages Cuneiform (ancient Unicode characters from U+12000 range) to construct an obfuscated JavaScript expression that evades such filters. The payload builds a function dynamically using string concatenation, boolean coercion, and object properties to execute code without triggering keyword-based detections. Once injected via an XSS vector (e.g., user input field, URL parameter), it runs in the browser context, accessing DOM elements, cookies, and potentially sending data to an attacker-controlled server. This is effective against WAFs or client-side filters that fail to decode or normalize Unicode, leading to account takeover or data exfiltration in web environments.

## Requirements

1. A vulnerable web application with a confirmed XSS vulnerability allowing JavaScript injection (e.g., unescaped user input reflected in HTML).
2. Knowledge of the target filter's behavior (test with basic payloads to confirm Unicode evasion works).
3. A modern web browser (e.g., Chrome, Firefox) for testing and execution; developer tools for console injection.
4. Optional: Proxy tool like Burp Suite to intercept and modify requests for precise payload delivery.

## Defense

- Implement strict input validation and output encoding (e.g., HTML entity encoding) on all user inputs using libraries like DOMPurify.
- Deploy Content Security Policy (CSP) headers to restrict inline script execution and eval() usage (e.g., script-src 'self').
- Use Web Application Firewalls (WAFs) with Unicode normalization and advanced obfuscation detection (e.g., ModSecurity with OWASP CRS).
- Enable browser security features like XSS Auditor (deprecated but similar in modern browsers) and monitor for anomalous JavaScript execution via client-side logging.
- Regularly audit and fuzz inputs with tools like XSStrike to identify bypasses.

## Objectives

1. Inject and execute obfuscated JavaScript code via an XSS vulnerability without triggering filters.
2. Evade detection by using Cuneiform Unicode to hide payload structure.
3. Exfiltrate sensitive victim data, such as session cookies, for further exploitation.

## Instructions

### Step 1: Identify the XSS Injection Point

**Context**: Locate a point in the web application where user input is reflected without proper escaping, such as a search field, comment section, or URL parameter. Test with a basic payload like <script>alert(1)</script> to confirm vulnerability and observe filter behavior.

No specific command; use browser developer tools (F12) to inspect the reflected input and verify execution.

> If the basic payload is blocked, proceed to obfuscation; otherwise, this procedure may not be necessary.

### Step 2: Prepare the Obfuscated Payload

**Context**: Use the Cuneiform-obfuscated JavaScript code to construct a payload that executes arbitrary code. Replace the empty string placeholder in the code with your desired JavaScript (e.g., 'alert(document.cookie)' to steal cookies).

**Code** ([[codes/Cuneiform-Obfuscated-JavaScript-Code-Execution]]):

```javascript
𒀀='',𒉺=!𒀀+𒀀,𒀃=!𒉺+𒀀,𒇺=𒀀+{},𒌐=𒉺[𒀀++],
𒀟=𒉺[𒈫=𒀀],𒀆=++𒈫+𒀀,𒁹=𒇺[𒈫+𒀆],𒉺[𒁹]+=𒇺[𒀀]
+(𒉺.𒀃+𒇺)[𒀀]+𒀃[𒀆]+𒌐+𒀟+𒉺[𒈫]+𒁹+𒌐+𒇺[𒀀]
+𒀟][𒁹](𒀃[𒀀]+𒀃[𒈫]+𒉺[𒀆]+𒀟+𒌐+"(𒀀)")()
```

> Customize by replacing the final empty string (𒀀) with your payload, e.g., for cookie theft: document.cookie. The code uses Unicode variables to build 'Function' constructor and 'eval' equivalent, evading string-based filters.

### Step 3: Inject and Execute the Payload

**Context**: Deliver the obfuscated code through the XSS vector. For reflected XSS, append to a URL parameter; for stored, submit via form. If testing locally, paste into the browser console on the vulnerable page.

No specific command; inject via HTTP request or direct console execution.

> Example injection: If the vuln is in ?q=<input>, use ?q=<script> [obfuscated code] </script>. Monitor network tab for any exfiltration requests.

### Step 4: Verify Execution and Exfiltrate Data

**Context**: Confirm the payload runs by observing effects (e.g., alert popup if testing) and check for data theft (e.g., intercepted cookies sent to attacker server).

Use browser console or proxy to inspect document.cookie post-execution.

> Success: Arbitrary code runs without filter blocks; cookies or other data are accessible or transmitted.
