---
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T11:44:22.456050+00:00'
updated_at: '2023-05-26T18:25:43.673947+00:00'
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

# Reflected-XSS-With-Single-Quote-and-Backslash-Escaped

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in a web application's search functionality where user input is reflected inside a JavaScript string, and single quotes (') and backslashes (\) are escaped. By crafting a payload that closes the existing script tag and injects a new one, an attacker can execute arbitrary JavaScript code, such as displaying an alert with document cookies to demonstrate unauthorized access to sensitive data.

## Description

Reflected XSS occurs when untrusted user input is immediately rendered in the response without proper encoding, allowing attackers to inject malicious scripts. In this scenario, the application escapes single quotes and backslashes to prevent string breakage but fails to encode angle brackets (< >) or other HTML entities, enabling tag injection. This technique is commonly used in web penetration testing to identify injection points in search bars or query parameters. The target environment is a web application with client-side JavaScript processing of user input. Successful exploitation leads to JavaScript execution in the victim's browser, potentially enabling session hijacking via cookie theft. This maps to MITRE ATT&CK technique T1059.007 (JavaScript) under the Execution tactic.

## Requirements

1. Direct access to the vulnerable web application via a web browser.
2. The application must have a search functionality that reflects user input in JavaScript without full HTML encoding.
3. Basic knowledge of HTML and JavaScript for payload crafting.
4. Optionally, a web proxy like Burp Suite to intercept and modify requests for more controlled testing.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding using libraries like OWASP ESAPI or DOMPurify to escape HTML entities in all user inputs reflected in JavaScript.
- Use Content Security Policy (CSP) headers to restrict script execution and inline scripts.
- Monitor for anomalous JavaScript execution or alert popups in web application logs and browser consoles.
- Employ Web Application Firewalls (WAFs) to detect and block common XSS payloads, including script tag breakouts.

## Objectives

1. Identify the reflection point in the application's JavaScript code.
2. Confirm escaping behavior for single quotes and backslashes.
3. Inject a payload to break out of the string context and execute arbitrary JavaScript.
4. Demonstrate impact by stealing or displaying sensitive data like cookies.

## Instructions

### Step 1: Test for Input Reflection

**Context**: Begin by submitting a benign input to locate where and how the search query is reflected in the page, confirming it's inside a JavaScript string context.

**Instructions**: Open the web application in a browser, navigate to the search functionality, and enter a random alphanumeric string such as "test123abc". Submit the search and inspect the resulting page.

> Right-click on the page and select "View Page Source" (or use browser developer tools: press F12, go to Elements tab, and search for the input string). Look for the string reflected within JavaScript, e.g., `var searchQuery = "test123abc";`.

### Step 2: Verify Escaping Mechanism

**Context**: Confirm that single quotes and backslashes are escaped, which prevents simple string breakage but may allow HTML tag injection if angle brackets are not encoded.

**Instructions**: Submit an input containing a single quote, such as "test'123", and a backslash, such as "test\123". Re-inspect the page source to observe the escaping, e.g., `var searchQuery = "test\'123";` or similar.

> This step ensures the payload will need to avoid quote-based breakage and instead use tag closure.

### Step 3: Inject Breakout Payload

**Context**: Craft and submit a payload that closes the existing `<script>` tag (if present) and opens a new one to execute malicious JavaScript. Reference the pre-defined payload for script tag breakout.

**Instructions**: In the search box, enter the following payload: `</script><script>alert(document.cookie)</script>`. Submit the search.

> This payload first closes any open script tag with `</script>`, then injects a new `<script>` tag containing `alert(document.cookie)`, which executes to display the victim's cookies in an alert box. For customization, replace `alert(document.cookie)` with other JavaScript, such as sending data to an attacker-controlled server.

Use [[codes/Reflected-XSS-Payload-Script-Tag-Breakout]] for the exact payload string.

### Step 4: Validate Execution

**Context**: Observe the effects of the injected script to confirm successful exploitation and assess potential impact.

**Instructions**: After submission, check for the alert popup displaying cookie data. If using a proxy, intercept the request to modify or repeat the payload.

> Successful execution indicates the vulnerability is exploitable. Document the cookies or any exfiltrated data for reporting.
