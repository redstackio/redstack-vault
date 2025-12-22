---
id: 97d40b7a-67ac-447b-93c5-f12ea1ca23ce
name: ECMAScript6 Filter Bypass Script Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.958753+00:00'
updated_at: '2023-04-10T20:21:36.375102+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
tags:
  - '[[tags/Bypass using ECMAScript6]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
commands:
  - '[[commands/curl-inject-xss-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# ECMAScript6 Filter Bypass Script Injection

## Summary

ECMAScript6 Filter Bypass Script Injection is a technique to evade web application filters designed to prevent cross-site scripting (XSS) attacks by leveraging ES6 features like template literals to inject and execute malicious JavaScript in the context of a trusted third-party site that the target application incorporates or trusts.

## Description

This procedure targets scenarios where direct XSS payloads are blocked by input sanitization or output encoding on the primary target site. Instead, the attacker injects the payload into a third-party resource (e.g., a comment section, user profile, or API response on a site like a forum or social platform) that the target site embeds via iframes, AJAX, or other mechanisms. ES6 template literals (backticks and ${} syntax) allow embedding dynamic expressions that can construct and execute code evasively, bypassing keyword-based filters that block common strings like 'alert' or '<script>'. For example, expressions can be built using String.fromCharCode to avoid direct string matches. Once executed in the target's browser context due to the trusted source, it enables stealing cookies, keystrokes, or performing actions on behalf of the victim. This is particularly effective against legacy filters not updated for modern JavaScript standards.

## Requirements

1. Access to a third-party site trusted by the target application (e.g., via public registration or API).
2. Knowledge of the target's integration with the third-party (e.g., embedding user-generated content).
3. A proxy tool like Burp Suite for intercepting and modifying requests (optional but recommended).
4. Basic understanding of ES6 syntax, particularly template literals and dynamic code construction.

## Defense

- Implement comprehensive input validation and output encoding (e.g., using libraries like DOMPurify) that handle ES6 features.
- Deploy Content Security Policy (CSP) with strict script-src directives to block inline scripts and untrusted sources.
- Use Subresource Integrity (SRI) hashes for third-party resources to prevent tampering.
- Regularly audit third-party integrations and monitor for anomalous script execution via browser logs or WAF rules.

## Objectives

1. Identify and access a trusted third-party injection point.
2. Craft an ES6-based payload that evades filters and executes in the target context.
3. Verify execution by triggering an alert or data exfiltration in the victim's browser.

## Instructions

### Step 1: Identify Third-Party Injection Point

**Context**: Locate a vulnerable input field on a third-party site that the target embeds, such as a comment form or profile bio that gets loaded via JavaScript.

Inspect the target site's source to find embedded third-party URLs, then register or access the third-party to find injectable fields. Use browser developer tools to confirm the content is rendered in the target's DOM.

### Step 2: Craft ES6 Payload Using Template Literals

**Context**: Build a payload that uses ES6 features to construct malicious code dynamically, evading string-based filters.

Use the code snippet [[codes/simple-xss-alert-script]] as a base, but enhance with ES6: for example, `` `alert${String.fromCharCode(40)}document.domain${String.fromCharCode(41)}` `` to build 'alert(document.domain)' without direct strings.

**Code** ([[codes/simple-xss-alert-script]]):
```html
<script>alert('1');</script>
```

> Modify the alert message as needed. This basic payload tests execution; for bypass, wrap in template literals if the injection point supports them (e.g., in a JSON response parsed as JS).

### Step 3: Inject Payload via HTTP Request

**Context**: Submit the payload to the third-party site using a tool to simulate user input.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -X POST -d "comment=$_PAYLOAD" -H "Content-Type: application/x-www-form-urlencoded" $_TARGET_URL
```

> This sends the payload as a form parameter. Replace $_PAYLOAD with the encoded ES6 script (e.g., URL-encoded template literal). Expected output: HTTP 200 response confirming submission, no errors.

### Step 4: Verify Execution in Target Context

**Context**: Trigger the target site to load the third-party content and observe if the script executes.

Visit the target site in a browser, ensure it fetches the injected content, and check for the alert popup or console errors. Use proxy to confirm the payload reaches the DOM unfiltered.

**Expected Output**: Alert box displays '1' (or custom message) in the target's browser, indicating successful bypass and execution.
