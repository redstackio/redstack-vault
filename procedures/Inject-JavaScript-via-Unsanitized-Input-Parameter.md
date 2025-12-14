---
id: proc-uuid-001
name: Inject-JavaScript-via-Unsanitized-Input-Parameter
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.406Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - javascript-injection
commands:
  - '[[commands/curl-xss-test]]'
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject JavaScript via Unsanitized Input Parameter

## Summary

This procedure exploits a cross-site scripting (XSS) vulnerability by injecting arbitrary JavaScript into an unsanitized input parameter on a web application, such as a search field on GM.com, leading to execution of malicious code in the user's browser.

## Description

In this attack scenario, a web application fails to properly sanitize or validate user input, allowing attackers to inject JavaScript code that executes in the context of the victim's browser session. The vulnerability was identified on GM.com through a parameter that directly reflected input without escaping, enabling potential session hijacking, data theft, or phishing. Prerequisites include access to the target website and basic knowledge of HTML/JavaScript payloads. Expected outcomes include confirmation of execution via alerts or more advanced actions like cookie exfiltration.

## Requirements

1. Public access to the target website (e.g., GM.com)
2. Browser with developer tools or curl for testing
3. Knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement input validation and sanitization using libraries like DOMPurify
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript execution in web logs

## Objectives

1. Inject and execute JavaScript in the victim's browser
2. Demonstrate potential for stealing session data
3. Validate the vulnerability for reporting or remediation

## Instructions

### Step 1: Identify the Vulnerable Parameter

**Context**: Locate the input field or URL parameter that accepts user input without sanitization, such as a search query on GM.com.

**Command** ([[commands/curl-xss-test]]):
```bash
curl -G "https://www.gm.com/search" --data-urlencode "q=test" -o test.html
```

> This command sends a benign test input and saves the response. Inspect test.html to confirm the input is reflected unsanitized.

### Step 2: Craft and Inject XSS Payload

**Context**: Append a JavaScript payload to the parameter to test for execution.

**Command** ([[commands/curl-xss-test]]):
```bash
curl -G "https://www.gm.com/search" --data-urlencode "q=<script>alert('XSS')</script>" -o xss-test.html
```

> Open xss-test.html in a browser or check for the alert execution. If successful, the script runs, confirming the vulnerability. For real exploitation, replace alert with code to exfiltrate data, e.g., `document.cookie`.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-test]]

## Tools Used


## Tags

- [[xss]]
- [[javascript-injection]]
