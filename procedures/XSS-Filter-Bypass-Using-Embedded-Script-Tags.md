---
id: aee23567-9d9f-4b9b-b9c4-1e7e761ef2a5
name: XSS-Filter-Bypass-Using-Embedded-Script-Tags
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.725566+00:00'
updated_at: '2023-04-10T20:21:45.694422+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - filter-bypass
  - javascript
commands: []
platforms:
  - Web
tools: []
validated: true
---

# XSS-Filter-Bypass-Using-Embedded-Script-Tags

## Summary

This procedure demonstrates a technique to bypass web application filters that sanitize or block direct <script> tags by embedding a malicious script within a string literal inside another script tag. This allows execution of JavaScript code, such as an alert, to confirm XSS vulnerability without triggering basic filter rules.

## Description

Cross-Site Scripting (XSS) vulnerabilities enable attackers to inject and execute malicious scripts in users' browsers. Many web applications implement filters to strip out <script> tags to prevent XSS. This bypass exploits incomplete sanitization by placing a closing </script> tag, followed by a new <script> tag containing the payload, inside a string variable declaration within an outer <script> tag. The filter may remove outer tags but leave the inner string intact, allowing the browser to parse and execute the embedded script. This is effective against filters that do not deeply parse string contents. The technique targets reflected or stored XSS in input fields, search boxes, or user profiles on web applications.

## Requirements

1. Access to a web application with a potential XSS vulnerability where user input is reflected without proper sanitization.
2. Knowledge of the filter's behavior, such as through testing with tools like Burp Suite to observe how inputs are processed.
3. A modern web browser for testing payload execution.
4. Optional: Proxy tool like [[tools/Burp-Suite]] to intercept and modify requests.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding using libraries like DOMPurify or OWASP ESAPI to escape all user inputs.
- Deploy a Content Security Policy (CSP) with strict script-src directives to block inline scripts and restrict execution to trusted sources.
- Use Web Application Firewalls (WAFs) like ModSecurity to detect and block anomalous JavaScript patterns, including embedded tag bypasses.
- Enable browser security features like XSS Auditor (deprecated in modern browsers) or rely on Content-Security-Policy headers.
- Regularly scan for XSS with automated tools like OWASP ZAP and monitor application logs for suspicious script executions.

## Objectives

1. Identify and bypass script tag filters to inject executable JavaScript.
2. Confirm XSS vulnerability by executing a proof-of-concept payload like alert(1).
3. Escalate to data exfiltration or session hijacking if successful.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user input field (e.g., search box, comment form) where input is reflected back in the HTML without proper escaping. Test basic payloads like <script>alert(1)</script> to confirm filtering is in place but incomplete.

Inspect the page source or use developer tools to see how the input is rendered.

### Step 2: Craft the Bypass Payload

**Context**: Use the embedded script technique to evade the filter. The payload starts with an outer <script> tag declaring a string variable that contains the bypass sequence.

Reference the code snippet: [[codes/XSS-Bypass-Payload-Embedded-Script-In-String]]

Inject the following payload into the vulnerable input field:

```html
<script>foo="text </script><script>alert(1)</script>";</script>
```

This declares a variable 'foo' with a string that includes a closing tag for the outer script, followed by a new script tag with the alert.

### Step 3: Submit and Verify Execution

**Context**: Submit the form or parameter containing the payload and observe the response. If the filter strips outer tags but leaves the string, the browser will execute the inner alert(1).

Use browser developer tools (F12) to monitor the console for errors or network requests. If using a proxy, intercept the request to ensure the payload is transmitted correctly.

**Expected Output**: A pop-up alert box displaying '1' confirms successful execution. In the page source, the payload may appear mangled by the filter, but the script runs.

### Step 4: Escalate if Successful

**Context**: Once confirmed, replace alert(1) with more advanced payloads, such as fetching external scripts or stealing cookies via document.cookie sent to an attacker-controlled server.

Test variations like using different string delimiters (e.g., single quotes) if double quotes are filtered.
