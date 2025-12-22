---
id: 11535e8b-c784-4905-84fd-6000f359b56c
name: 'Reflected XSS In a Template Literal(Where <>,\,'',\" are Unicode-escaped)'
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T10:26:20.588718+00:00'
updated_at: '2023-05-26T01:28:50.368354+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - injection
  - owasp
  - owasp top 10
  - Reflected XSS
  - Web Applications
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Reflected-XSS-in-JavaScript-Template-Literals-with-Unicode-Escaped-Characters

## Summary

This procedure demonstrates how to exploit a reflected Cross-Site Scripting (XSS) vulnerability in a web application that uses JavaScript template literals, where characters like <>, -, ', and " are Unicode-escaped. By injecting a payload that breaks out of the template literal using backticks and ${}, an attacker can execute arbitrary JavaScript code, such as displaying an alert, to confirm the vulnerability.

## Description

JavaScript template literals, enclosed in backticks (`), allow embedded expressions via ${}. In vulnerable applications, user input reflected into these literals may be escaped for common characters (e.g., < becomes \u003c), but backticks and ${} might not be properly sanitized. This enables attackers to close the template literal early and inject executable JavaScript. The technique is useful in web penetration testing to identify injection flaws in modern JavaScript frameworks like React or Vue.js that mishandle user input in dynamic strings. Success leads to client-side code execution, potentially enabling session hijacking, data theft, or further attacks like keylogging.

## Requirements

1. Access to a vulnerable web application with a reflected input field (e.g., search box) that echoes input into a JavaScript template literal.
2. A modern web browser (e.g., Chrome, Firefox) with developer tools enabled for inspecting reflected input.
3. Optional: A proxy tool like Burp Suite to intercept and modify requests if the application uses POST or complex interactions.
4. Knowledge of the target's URL and the specific input parameter vulnerable to reflection.

## Defense

Defensive measures and detection strategies:

- Implement strict Content Security Policy (CSP) to restrict inline script execution and eval-like functions.
- Sanitize and validate all user inputs, ensuring template literals use safe interpolation methods (e.g., escaping backticks and ${}).
- Use libraries like DOMPurify for output encoding in JavaScript contexts.
- Monitor for anomalous JavaScript execution via browser logs or Web Application Firewall (WAF) rules targeting template literal patterns.
- Enable browser security features like XSS Auditor (deprecated but similar in modern browsers) and strict mode in JS.

## Objectives

1. Confirm reflection of user input within a JavaScript template literal.
2. Identify escape mechanisms for special characters and find a breakout payload.
3. Execute arbitrary JavaScript to demonstrate code injection and vulnerability impact.
4. Validate the attack without causing persistent changes to the application.

## Instructions

### Step 1: Verify Input Reflection

**Context**: Test the input field to confirm that user-supplied data is reflected back in the application's response, specifically within a JavaScript template literal. This establishes the injection point.

Enter a random, non-malicious string (e.g., "test123") into the search box or vulnerable input field and submit the request. Use browser developer tools (F12 > Elements or Network tab) to inspect the page source or response.

Observe the reflected string in the JavaScript code, looking for patterns like `search: ${input}` enclosed in backticks.

### Step 2: Test Template Literal Escaping

**Context**: Probe the application's escaping behavior to understand which characters are blocked, focusing on those that could close or manipulate the template literal structure.

Submit the string "${}" into the input field. Inspect the response to see if the template literal is properly escaped (e.g., backticks or ${} converted to Unicode entities like \u0024{ }).

If escaped, note the pattern; this confirms the vulnerability context but indicates need for a breakout technique.

### Step 3: Inject Breakout Payload

**Context**: Craft and submit a payload that closes the template literal prematurely and injects executable JavaScript, bypassing the Unicode escaping for <>, -, ', and " by avoiding those characters.

Enter the following payload into the input field: `${alert(1)*}`

The `*` acts as a multiplier to close any potential expression context, while `alert(1)` executes the JavaScript. Submit the request and observe the page.

### Step 4: Confirm Execution

**Context**: Verify that the injected JavaScript has executed successfully, indicating a successful XSS exploitation.

Look for the alert dialog box popping up with the number "1". If it appears, the vulnerability is confirmed. Inspect the console (F12 > Console) for any errors or additional output from the execution.

If no alert appears, iterate by trying variations like `${alert(`xss`)}` or using other simple functions like `console.log(1)`, ensuring the payload avoids escaped characters.
