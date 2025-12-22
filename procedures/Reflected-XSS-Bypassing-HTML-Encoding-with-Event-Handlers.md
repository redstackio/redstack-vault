---
id: d46dfca7-55a5-468c-ba98-7ca3466592e9
name: Reflected-XSS-Bypassing-HTML-Encoding-with-Event-Handlers
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T10:05:07.024482+00:00'
updated_at: '2023-05-26T01:29:19.129287+00:00'
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
  - injection
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Browser-Developer-Tools]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Reflected-XSS-Bypassing-HTML-Encoding-with-Event-Handlers

## Summary

This procedure demonstrates how to exploit a reflected XSS vulnerability in a web application where angle brackets (< >) are HTML-encoded, preventing direct script injection. By leveraging event handlers like onmouseover, an attacker can bypass the encoding in an HTML attribute context (e.g., within a single-quoted attribute) to execute JavaScript, such as displaying an alert box. This technique is useful for confirming XSS in applications with partial input sanitization and can lead to session hijacking or data theft in real scenarios.

## Description

Reflected XSS occurs when user input is immediately echoed back in the server's response without proper sanitization, allowing malicious scripts to execute in the victim's browser. In this case, the application HTML-encodes angle brackets, blocking tags like <script>, but fails to encode or filter event handler attributes. The input is reflected within a single-quoted HTML attribute, such as a search result div. To bypass, craft a payload that closes the attribute with a double quote, injects an event handler (e.g., onmouseover), and executes JavaScript while commenting out any trailing code. This targets OWASP Top 10 A7: Cross-Site Scripting and maps to MITRE ATT&CK T1059.007 for JavaScript execution in a web context. The technique requires access to a vulnerable search or input field and works in modern browsers.

## Requirements

1. A web browser with developer tools enabled (e.g., Chrome DevTools) for inspecting page source and testing payloads.
2. Access to the vulnerable web application, typically via a URL with a reflected input field like a search box.
3. Optional: A proxy tool like Burp Suite to intercept and modify requests/responses for precise payload testing.
4. No special credentials needed if the vulnerability is unauthenticated; otherwise, valid session cookies.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding using libraries like OWASP ESAPI or DOMPurify to neutralize event handlers and JavaScript.
- Use Content Security Policy (CSP) headers to restrict inline scripts and event handlers (e.g., script-src 'self').
- Employ Web Application Firewalls (WAFs) like ModSecurity to detect and block common XSS patterns, including event handler injections.
- Enable browser security features like XSS Auditor (deprecated in Chrome) or monitor for anomalous JavaScript execution via client-side logging.
- Regularly scan with tools like OWASP ZAP or Burp Suite Scanner to identify reflection points.

## Objectives

1. Confirm the presence of reflected input in an HTML attribute context.
2. Bypass HTML encoding restrictions using event handlers to execute arbitrary JavaScript.
3. Trigger a proof-of-concept alert to validate exploitation success.
4. Understand how partial sanitization can still lead to XSS vulnerabilities.

## Instructions

### Step 1: Verify Input Reflection

**Context**: Test the input field to confirm that user-supplied data is reflected back in the HTML response, specifically within a single-quoted attribute (e.g., a div title or class). This establishes the injection point and context.

Enter a random innocuous string, such as "test123", into the search box or vulnerable input field and submit it.

Inspect the page source (right-click > Inspect Element or View Page Source) to locate the reflection. Look for the input echoed inside an attribute like <div title='test123'>.

**Expected Output**: The string appears unencoded within single quotes in an HTML attribute, confirming reflection without full sanitization.

### Step 2: Test Attribute Escape

**Context**: Attempt to break out of the single-quoted attribute by injecting a double quote to close it prematurely. This tests if the application allows attribute boundary crossing, setting up for event handler injection.

In the input field, enter a payload like: test" onfocus=alert(1) autofocus="

Submit and inspect the page source again. The payload should close the attribute and potentially inject new attributes if not filtered.

If using a proxy like [[tools/Burp-Suite]], intercept the POST/GET request, modify the parameter, and forward to observe the response.

**Expected Output**: The page source shows the attribute closed with the double quote, and any injected attributes may appear, though JavaScript might not execute yet due to encoding.

### Step 3: Inject Event Handler Payload

**Context**: Since angle brackets are encoded, use an event handler that doesn't require tags, such as onmouseover, to execute JavaScript when the user hovers over the element. Close the attribute properly and comment out trailing content to avoid syntax errors.

Craft and enter the following payload in the input field: test" onmouseover=alert(1)//

The double quote closes the single-quoted attribute, onmouseover injects the event, alert(1) executes the script on hover, and // comments out the rest of the attribute value.

Submit the form and hover over the reflected element (e.g., the search result div).

**Expected Output**: An alert box pops up displaying "1" when hovering, confirming JavaScript execution.

### Step 4: Validate and Escalate

**Context**: Confirm the exploit works consistently and consider escalation paths, such as replacing alert(1) with code to steal cookies (e.g., onmouseover=fetch('/steal?cookie='+document.cookie) ).

Repeat the payload with variations, like using onfocus with autofocus for automatic triggering without hover.

Inspect network requests in developer tools to ensure no additional sanitization blocks the execution.

**Expected Output**: Reliable alert triggering on interaction, with no JavaScript errors in the console.

> **Note**: In a real attack, replace alert(1) with malicious actions like keylogging or phishing forms. Always test in a controlled environment.
