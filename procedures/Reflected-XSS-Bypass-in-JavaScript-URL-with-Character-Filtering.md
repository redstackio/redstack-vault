---
id: 0a59e028-bb6a-44a5-8ac4-0dd8d6b24a72
name: Reflected-XSS-Bypass-in-JavaScript-URL-with-Character-Filtering
type: procedure
verified: true
submitted: true
created_at: '2020-08-26T16:07:50.179064+00:00'
updated_at: '2023-05-26T18:22:59.250655+00:00'
platforms:
  - Web
tags:
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Reflected XSS]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
commands:
  - '[[commands/curl-test-xss-payload]]'
tools: []
codes:
  - '[[codes/JavaScript-XSS-Payload-for-Filter-Bypass]]'
validated: true
---

# Reflected-XSS-Bypass-in-JavaScript-URL-with-Character-Filtering

## Summary

This procedure demonstrates how to identify and exploit a reflected XSS vulnerability in a JavaScript URL context where certain characters are filtered by the application or WAF. By experimenting with alternative JavaScript function calls and payload constructions, an attacker can bypass these filters to execute arbitrary JavaScript code, such as displaying an alert popup to confirm the vulnerability.

## Description

Reflected XSS occurs when user input is reflected back in the server's response without proper sanitization, allowing injection of malicious scripts. In this scenario, the application filters special characters like quotes or angle brackets in URL parameters (e.g., postID), preventing standard payloads like <script>alert(1)</script>. To bypass, craft payloads that use alternative syntax for JavaScript execution, such as throwing errors with onerror handlers or leveraging object properties. This technique is common against basic WAFs or application-level filters and targets web applications processing URL parameters in JavaScript contexts. Success confirms code execution on the victim's browser, potentially leading to session hijacking or data theft.

## Requirements

1. Access to a web application with a reflected parameter (e.g., postID in URL) that is processed in JavaScript.
2. A browser with developer tools or a proxy tool like Burp Suite for intercepting and modifying requests.
3. Network access to the target application (no authentication required for public endpoints).
4. Basic knowledge of JavaScript and URL encoding.

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict inline script execution.
- Sanitize and encode all user inputs, especially URL parameters reflected in JavaScript.
- Use WAF rules to detect anomalous payloads, such as onerror or throw statements.
- Monitor for JavaScript errors or unexpected popups in application logs.

## Objectives

1. Identify filterable characters in the reflected parameter.
2. Construct a bypass payload to execute JavaScript code.
3. Verify execution via an alert or other observable effect.
4. Confirm the vulnerability for further exploitation.

## Instructions

### Step 1: Identify the Reflected Parameter

**Context**: Examine the target URL to locate user-controllable parameters that are reflected in the response, such as postID=1. This establishes the injection point.

**Command** (No specific command; use browser URL bar):

Navigate to the target URL, e.g., https://target.com/page?postID=1, and inspect the response source to confirm reflection.

> View the page source or use browser dev tools (F12) to search for 'postID' and verify it appears unsanitized in JavaScript code.

### Step 2: Test for Basic Injection

**Context**: Inject a single quote (') to break out of the string context and observe if it causes a JavaScript error, indicating reflection without proper escaping.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl "https://target.com/page?postID=1'" -v
```

> This sends a request with postID=1' and checks the response for errors like "Invalid blog postID". A JavaScript console error confirms reflection.

### Step 3: Bypass Character Filtering

**Context**: If quotes are filtered, prepend an ampersand (&) before the quote to alter the parsing, allowing breakout from the filtered context.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl "https://target.com/page?postID=1&'" -v
```

> Observe the response; the & may confuse the filter, allowing the quote to close the string and inject subsequent code.

### Step 4: Inject and Execute Bypass Payload

**Context**: Use a crafted JavaScript payload that avoids filtered characters by using throw statements, onerror handlers, and object manipulations to execute an alert.

**Code** ([[codes/JavaScript-XSS-Payload-for-Filter-Bypass]]):

Embed the payload in the URL parameter.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl "https://target.com/page?postID=1&"},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:'" -v
```

> The payload executes alert(1337) if successful. In a browser, load the URL and check for the popup.

### Step 5: Verify Execution

**Context**: Confirm the payload triggered JavaScript execution by observing the alert or inspecting the browser console for errors/indicators.

No command; use browser observation.

> Success is indicated by the alert popup or console logs showing code execution.
