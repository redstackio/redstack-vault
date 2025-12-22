---
id: 9029c61d-c0d3-4174-9cc1-23909f9ddbf5
name: Test-for-HTML-Injection-in-User-Input-Fields
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T13:59:51.707927+00:00'
updated_at: '2023-05-26T18:29:16.065509+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - html-injection
  - injection
  - owasp
  - owasp-top-10
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Test-for-HTML-Injection-in-User-Input-Fields

## Summary

This procedure tests web applications for HTML injection vulnerabilities by submitting HTML tags through user input fields, such as search boxes, and observing if the application renders the injected content as HTML rather than escaping it as plain text. Successful injection indicates a potential vulnerability that could lead to cross-site scripting (XSS) or other client-side attacks if combined with JavaScript.

## Description

HTML injection occurs when a web application fails to properly sanitize or encode user-supplied input before inserting it into HTML output. This allows attackers to inject arbitrary HTML tags, which the browser then renders. While HTML injection alone may not execute scripts, it can alter page structure, steal data via forms, or serve as a stepping stone to XSS. This technique targets reflected, stored, or DOM-based injection points in web forms, search fields, or comment sections. It is commonly tested during penetration testing of OWASP Top 10 risks like Injection (A03:2021). The procedure assumes access to the application's frontend and uses manual browser interactions or proxy interception to verify rendering.

## Requirements

1. Valid user access to the web application (no authentication bypass needed for public-facing inputs).
2. A modern web browser (e.g., Chrome, Firefox) for manual testing.
3. Optional: A web proxy like [[tools/Burp-Suite]] to intercept and modify requests for more precise payload delivery.
4. Knowledge of basic HTML tags and browser developer tools for inspecting rendered output.

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user inputs displayed in HTML contexts using libraries like OWASP ESAPI or built-in functions in frameworks (e.g., htmlspecialchars in PHP).
- Use Content Security Policy (CSP) headers to restrict inline HTML and script execution.
- Validate and sanitize inputs server-side, rejecting or escaping HTML tags.
- Monitor application logs for suspicious input patterns containing HTML tags and alert on anomalies.
- Employ Web Application Firewalls (WAFs) with rules for detecting unescaped HTML in inputs.

## Objectives

1. Identify if user input fields are vulnerable to HTML injection by observing tag rendering.
2. Confirm the vulnerability through visual changes in page output and source code inspection.
3. Document the injection point for further exploitation or reporting.

## Instructions

### Step 1: Identify and Baseline the Input Field

**Context**: Locate a user input field (e.g., search box) that echoes input back in the response, such as search results. Enter a neutral test string to establish baseline behavior and confirm the input is reflected.

Enter a simple message like "Test" in the input field and submit it.

Inspect the response page to see if the input is displayed as plain text without alteration.

### Step 2: Submit the Test Input and Observe Baseline Output

**Context**: Verify that the application processes and displays the input correctly without rendering any special formatting, ensuring a controlled baseline for comparison.

Submit the form with the test message.

**Expected Output**: The search results or echoed input appears as plain text, e.g., "Test" without any HTML formatting.

Use browser developer tools (F12) to inspect the HTML source and confirm the input is escaped (e.g., as &lt;p&gt;Test&lt;/p&gt; if in a paragraph).

### Step 3: Inject HTML Payload and Submit

**Context**: Introduce a basic HTML tag to test for injection. This step checks if the application fails to escape the tags, allowing the browser to interpret them as markup.

Enter a payload like "<h1>Test</h1>" in the input field and submit.

If using a proxy like [[tools/Burp-Suite]], intercept the request, ensure the payload is sent as-is in the POST/GET parameters, and forward it.

### Step 4: Verify Rendering and Injection Success

**Context**: Examine the response to determine if the HTML was rendered, indicating a vulnerability. This confirms the injection point and its impact.

Observe the page output: The text "Test" should appear in a large heading (H1) style if injected successfully.

Inspect the HTML source again to see if the tags are unescaped (e.g., <h1>Test</h1> directly in the markup).

**Expected Output**: Visual change in formatting, such as bold/large text, and unescaped tags in the page source.

### Step 5: Test Variations and Escalate if Vulnerable

**Context**: If successful, try additional payloads to assess severity, such as nested tags or combinations that could lead to XSS (e.g., <script>alert(1)</script> if JavaScript is allowed).

Submit variations like "<img src=x onerror=alert(1)>" to check for XSS escalation.

Document the exact payload, input field, and response for reporting.

**Expected Output**: Rendered HTML elements or, if escalated, JavaScript execution (e.g., alert popup).

If no rendering occurs, the input is likely sanitized; test other fields or parameters.
