---
id: c288905d-f95e-48e7-bce9-2268cdece4c5
name: Bypass-Case-Sensitive-XSS-Filter-with-Exotic-Payloads
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.321398+00:00'
updated_at: '2023-04-10T20:21:39.528380+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - bypass-case-sensitive
  - xss
  - filter-bypass
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Bypass-Case-Sensitive-XSS-Filter-with-Exotic-Payloads

## Summary

This procedure demonstrates how to bypass case-sensitive filters designed to block Cross-Site Scripting (XSS) attacks by using exotic payloads with mixed-case HTML tags and alternative encodings. It targets web applications that fail to normalize case in input validation, allowing injection of JavaScript code to execute arbitrary actions like alerting messages or stealing session data.

## Description

In a typical attack scenario, an attacker identifies an input field (e.g., search box, comment form) in a web application that reflects user input without proper sanitization. If the filter checks for lowercase '<script>' but not mixed-case variations like '<sCrIpt>', the attacker can craft payloads that evade detection. This technique exploits poor input validation to inject and execute JavaScript in the victim's browser, potentially leading to session hijacking, data theft, or further exploitation. The target environment is any web application with reflected or stored XSS vulnerabilities, commonly tested during penetration testing on modern browsers supporting JavaScript.

## Requirements

1. Access to a vulnerable web application with a reflected or stored input field.
2. Knowledge of the filter's behavior, such as case sensitivity (identified via trial-and-error fuzzing).
3. Tools for testing payloads, such as a browser developer console or proxy like Burp Suite.
4. Basic understanding of HTML and JavaScript encoding.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding using libraries like OWASP ESAPI or DOMPurify to normalize case and escape special characters.
- Deploy a Web Application Firewall (WAF) configured to detect mixed-case tags, encoded payloads, and anomalous JavaScript execution.
- Enable Content Security Policy (CSP) headers to restrict inline script execution and monitor for violations.
- Regularly audit and patch web applications, conduct code reviews for sanitization flaws, and log all reflected inputs for anomaly detection.

## Objectives

1. Identify and confirm a case-sensitive XSS filter in the target application.
2. Craft and inject an exotic payload to bypass the filter and execute JavaScript.
3. Verify successful code execution to demonstrate impact, such as displaying an alert or exfiltrating data.

## Instructions

### Step 1: Identify the Injection Point and Filter Behavior

**Context**: Locate a user-controlled input that is reflected back in the page source without proper escaping, and test standard XSS payloads to confirm the filter's case sensitivity.

Submit basic payloads like '<script>alert(1)</script>' and observe if they are blocked. Then try uppercase '<SCRIPT>alert(1)</SCRIPT>' to check for case insensitivity. If lowercase is blocked but mixed case is not, proceed to crafting exotic variants.

**Expected Output**: The application reflects the input but blocks standard lowercase tags, while allowing mixed-case versions to render without sanitization.

### Step 2: Craft the Exotic Payload

**Context**: Use mixed-case variations of HTML tags to evade the case-sensitive filter. This step leverages alternative representations of the '<script>' tag to inject JavaScript.

Reference the payload in [[codes/Case-Insensitive-Script-Tag-XSS-Payload]] and customize the alert message or action as needed (e.g., replace 'alert(1)' with 'alert(document.cookie)' for cookie theft).

**Expected Output**: A valid payload string ready for injection, such as '<sCrIpt>alert(1)</ScRipt>'.

### Step 3: Inject and Test the Payload

**Context**: Submit the crafted payload into the identified injection point and verify execution in the browser.

Enter the payload into the vulnerable input field (e.g., a search parameter) and submit the form. Monitor the page for JavaScript execution, such as a pop-up alert. If using a proxy, intercept and modify the request to ensure the payload reaches the server unaltered.

**Expected Output**: Upon submission, the page reloads and executes the injected script, displaying an alert box with the message '1' or capturing data.

### Step 4: Verify and Escalate

**Context**: Confirm the bypass success and explore further exploitation, such as data exfiltration or chaining with other vulnerabilities.

Check the browser console for errors and network tab for any unexpected requests. If successful, test more advanced payloads like keyloggers or beaconing to an attacker-controlled server.

**Expected Output**: No filter blocks, successful JS execution confirmed via alert or console log, with potential for data theft indicators like outbound requests.
