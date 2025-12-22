---
id: 50160d32-16f6-4c36-980e-9c84344e0d7c
name: >-
  Reflected XSS With Angle Brackets And Double Quotes HTML Encoded & Single
  Quotes Escaped
type: procedure
verified: true
submitted: true
created_at: '2020-08-26T17:40:53.986734+00:00'
updated_at: '2023-05-26T15:54:46.452082+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Reflected XSS]]'
  - '[[tags/Web Applications]]'
  - xss
  - bypass
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Reflected-XSS-Bypass-With-Backslash-Escaped-Single-Quotes

## Summary

This procedure demonstrates how to bypass a reflected XSS filter that HTML-encodes angle brackets and double quotes while escaping single quotes with backslashes. By crafting a payload that leverages the backslash escaping to break out of a JavaScript string context, an attacker can inject and execute arbitrary JavaScript code, such as displaying an alert box, in the victim's browser.

## Description

In vulnerable web applications, user input from a search box or similar parameter is reflected into a JavaScript context without proper sanitization. The application or its Web Application Firewall (WAF) may encode angle brackets (< >) and double quotes (") to prevent HTML and attribute breakout, and escape single quotes (') by prefixing them with a backslash (\'). A standard payload like '); alert(1);// would fail because the single quote becomes \', keeping the input trapped inside the string. To bypass this, use a payload starting with \' to consume the escape, followed by a comment and the malicious code, such as \'-alert(1)/*/. This technique exploits the incomplete escaping to achieve code execution. It is commonly tested against OWASP Top 10 A7: Cross-Site Scripting vulnerabilities in web applications using client-side JavaScript.

## Requirements

1. Access to a vulnerable web application with a reflected input field (e.g., search box) that echoes user input into a JavaScript string.
2. A modern web browser (e.g., Chrome, Firefox) with developer tools enabled for inspecting network responses and page source.
3. No special privileges required; assumes unauthenticated access to the input endpoint.
4. Optional: A proxy tool like Burp Suite for intercepting and modifying requests, though browser dev tools suffice for manual testing.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive output encoding in JavaScript contexts using functions like encodeURIComponent() or libraries such as DOMPurify.
- Deploy Content Security Policy (CSP) headers to restrict inline script execution and eval().
- Use Web Application Firewalls (WAFs) with updated rules for XSS payload variations, including backslash escapes.
- Sanitize all user inputs server-side and avoid direct reflection into JavaScript without validation.
- Monitor for anomalous JavaScript execution via client-side logging or browser security features like XSS Auditor.

## Objectives

1. Identify if the application escapes single quotes with backslashes in JavaScript contexts.
2. Craft and inject a bypass payload to execute arbitrary JavaScript.
3. Verify successful code execution through visual indicators like alert popups.
4. Demonstrate potential for further exploitation, such as stealing cookies or session tokens.

## Instructions

### Step 1: Verify Input Reflection

**Context**: Confirm that the search input is reflected into a JavaScript string context, which is necessary for this bypass to apply.

Navigate to the vulnerable search page and enter a random alphanumeric string (e.g., "test123") in the search box. Submit the form and use browser developer tools (F12 > Network tab) to inspect the response. Check the page source or console for the reflected input.

Expected: The input appears inside a JavaScript string, such as var query = "test123";

### Step 2: Test Standard Single Quote Escaping

**Context**: Determine if single quotes are escaped with backslashes, confirming the filter behavior this bypass targets.

Enter a test payload like "test'payload" in the search box and submit. Inspect the response in developer tools to observe how the single quote is handled.

Expected: The reflected output shows the single quote escaped as \\, e.g., var query = "test\\'payload"; preventing string breakout.

### Step 3: Inject Bypass Payload

**Context**: Use the backslash to counter the escape and inject executable JavaScript, breaking out of the string context.

Replace the input with the bypass payload: \\-alert(1)/*/. Submit the search form.

In the browser console or page source, the payload should resolve to '; alert(1); // after escaping, executing the alert.

Expected: An alert popup displays with the message "1", confirming JavaScript execution.

### Step 4: Validate and Escalate

**Context**: Ensure the execution is reliable and explore further payloads for real-world impact.

Repeat the injection with variations, such as \\-alert(document.cookie)/*/ to exfiltrate cookies. Inspect the alert output or network tab for any data leakage.

Expected: Successful alerts or data extraction without additional escaping issues.

## Expected Output

Upon successful execution in Step 3, a browser alert dialog appears with the number 1. In developer tools, the injected script executes without syntax errors, and the page may log the event in the console.
