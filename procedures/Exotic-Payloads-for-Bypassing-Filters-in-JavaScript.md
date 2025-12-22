---
id: 96b7933e-805e-4b45-8188-ce1989ae8563
name: Exotic Payloads for Bypassing Filters in JavaScript
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.846676+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/T1059.007 -
    JavaScript|T1059.007 - JavaScript]]
sub_techniques: []
tags:
  - '[[tags/Bypass ";" using another character]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
  - xss
  - filter-bypass
  - javascript
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Exotic Payloads for Bypassing Filters in JavaScript

## Summary

This procedure demonstrates the use of exotic payloads in JavaScript to bypass input filters that block specific characters, such as semicolons (;), commonly used in cross-site scripting (XSS) attacks. By leveraging alternative operators and constructs, attackers can execute arbitrary JavaScript code like alert() without triggering filter rules, enabling exploitation of vulnerable web applications to steal session data or perform other malicious actions.

## Description

Exotic payloads exploit weaknesses in web application filters by substituting blocked characters with visually similar or functionally equivalent alternatives. In JavaScript, semicolons are often filtered to prevent statement termination in injected code, but operators like multiplication (*), division (/), or the comma (,) can serve as separators instead. This technique is particularly effective against reflected or stored XSS vulnerabilities where input is not properly sanitized or encoded.

The target environment is typically a web browser interacting with a vulnerable web application, such as a search field, comment section, or user input form. Success allows execution of JavaScript in the victim's context, potentially leading to session hijacking, keylogging, or phishing. Prerequisites include identifying an injectable point via manual testing or tools like Burp Suite. This procedure maps to MITRE ATT&CK technique T1059.007 for JavaScript execution in a browser context.

## Requirements

1. Access to a vulnerable web application with an XSS-reflective or stored input field.
2. Basic knowledge of JavaScript syntax and operators.
3. A testing environment, such as a local vulnerable app (e.g., DVWA) or a proxy tool like Burp Suite for intercepting and modifying requests.
4. Victim's browser must support JavaScript execution (most modern browsers do).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using HTML entity encoding) to neutralize special characters and operators.
- Deploy Content Security Policy (CSP) headers to restrict inline script execution and eval() usage.
- Use a Web Application Firewall (WAF) configured to detect anomalous JavaScript patterns, such as unusual operator chains or alert() calls.
- Enable browser security features like XSS Auditor (deprecated in some browsers) or monitor for unexpected popups and network requests from scripts.

## Objectives

1. Identify and bypass character-specific filters in web input fields to inject executable JavaScript.
2. Execute arbitrary code, such as displaying an alert or exfiltrating data, in the victim's browser session.
3. Exploit XSS vulnerabilities to achieve session takeover or data theft in web applications.

## Instructions

### Step 1: Identify the Filter and Test Basic Injection

**Context**: Begin by locating an input field vulnerable to XSS and confirming the filter blocks semicolons. Submit a simple payload like `<script>alert('xss')</script>` and observe if it executes. If semicolons are blocked, note the error or sanitization behavior to guide exotic payload selection.

No specific command is required here; use browser developer tools (F12) to inspect the reflected input and verify sanitization.

> Test in a controlled environment to avoid disrupting production systems. Expected outcome: Confirmation of injection point and filter details, such as blocked ';' in statement termination.

### Step 2: Deploy Exotic Payload Using Operator Substitutions

**Context**: Use the exotic payload snippet to chain JavaScript expressions with alternative operators, bypassing semicolon filters. This step injects the payload into the vulnerable field and triggers execution upon reflection or storage.

**Code** ([[codes/JavaScript-Operator-Bypass-Payloads]]):

Embed the following payload in the input field, adjusting as needed for the context (e.g., within a script tag or event handler):

```javascript
'te' * alert('*') * 'xt';
'te' / alert('/') / 'xt';
'te' % alert('%') % 'xt';
'te' - alert('-') - 'xt';
'te' + alert('+') + 'xt';
'te' ^ alert('^') ^ 'xt';
'te' > alert('>') > 'xt';
'te' < alert('<') < 'xt';
'te' == alert('==') == 'xt';
'te' & alert('&') & 'xt';
'te' , alert(',') , 'xt';
'te' | alert('|') | 'xt';
'te' ? alert('ifelsesh') : 'xt';
'te' in alert('in') in 'xt';
'te' instanceof alert('instanceof') instanceof 'xt';
```

> This code demonstrates various operators (* for multiplication, / for division, % for modulus, - for subtraction, + for addition, ^ for bitwise XOR, > and < for comparisons, == for equality, & for bitwise AND, , for comma operator, | for bitwise OR, ? for ternary, in and instanceof for object checks) to separate expressions and execute alert(). Each line attempts to pop an alert with the operator name if the filter allows it. Submit the payload and refresh or interact with the page to trigger. Expected output: One or more alert dialogs displaying operator symbols or names, indicating successful bypass.

### Step 3: Verify Execution and Escalate

**Context**: After injection, verify code execution by checking for alerts or console logs. If successful, replace alert() with malicious actions like document.cookie exfiltration to a controlled server.

Use browser console to log results or monitor network traffic for data leaks.

> Success is confirmed by visible alerts or captured data. If no execution, iterate by combining operators or encoding the payload (e.g., URL encoding).
