---
id: eeb8e4ff-45db-4769-b2c6-3cae7221a210
name: Reflected-XSS-Using-AngularJS-Sandbox-Escape
type: procedure
verified: true
submitted: true
created_at: '2020-08-26T07:03:16.684782+00:00'
updated_at: '2023-05-26T18:08:43.878378+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - angularjs
  - owasp
  - web-applications
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Reflected-XSS-Using-AngularJS-Sandbox-Escape

## Summary

This procedure demonstrates how to exploit reflected XSS vulnerabilities in AngularJS applications by escaping the built-in sandbox protections. By injecting a crafted payload that leverages AngularJS directives like ng-focus and filters such as orderBy, attackers can bypass restrictions and execute arbitrary JavaScript, such as alerting document cookies, to steal session data or perform further attacks.

## Description

AngularJS applications often use sandboxing to prevent XSS by restricting what JavaScript can execute within expressions. However, older versions (pre-1.6) have known sandbox escape techniques that allow attackers to break out and run malicious code. This procedure targets reflected XSS where user input is echoed back in the response without proper sanitization, specifically within JavaScript template contexts. The attack involves testing for reflection, crafting a payload to escape the sandbox, and injecting it to trigger execution. It is commonly used against legacy web applications built with AngularJS, leading to session hijacking or data exfiltration. Prerequisites include identifying an input field that reflects user-supplied data into an AngularJS context, such as search boxes or form fields.

## Requirements

1. Access to a web application with AngularJS (version <1.6 recommended for sandbox escape) and a reflected input field.
2. Modern web browser with developer tools enabled for inspecting source and testing payloads.
3. Optional: Intercepting proxy like Burp Suite to capture and modify requests if the application uses POST or complex forms.
4. Basic knowledge of HTML, JavaScript, and AngularJS directives.

## Defense

Defensive measures and detection strategies:

- Upgrade to AngularJS 1.6+ or modern frameworks like Angular/React with built-in XSS protections.
- Implement Content Security Policy (CSP) to block inline scripts and restrict eval-like functions.
- Sanitize all user inputs using Angular's $sanitize service or server-side escaping.
- Monitor for anomalous JavaScript execution via Web Application Firewall (WAF) rules targeting Angular directives in payloads.
- Enable browser security features like XSS Auditor and strict CSP headers.

## Objectives

1. Identify if user input is reflected in AngularJS template contexts without escaping.
2. Craft and inject a sandbox escape payload to execute JavaScript.
3. Verify execution by alerting sensitive data like document cookies.

## Instructions

### Step 1: Test for Input Reflection

**Context**: Begin by submitting a benign string to check if the application reflects user input directly into the page source, particularly within JavaScript or AngularJS template areas. This confirms the vulnerability exists without triggering defenses.

Use the browser's search or input field to submit a unique test string like "TESTREFLECT123". Then, inspect the page source (right-click > View Page Source) to locate the reflected string.

> Look for the string appearing inside AngularJS expressions (e.g., {{'TESTREFLECT123'}}) or HTML attributes processed by Angular.

### Step 2: Verify Non-Escaping in JavaScript Templates

**Context**: Once reflection is confirmed, examine the source more closely to ensure the input is not properly escaped or sanitized within JavaScript contexts, such as ng-bind or template strings. This step identifies if the sandbox is active but escapable.

Reload the page after submission and use browser developer tools (F12 > Elements tab) to search for the test string. Check if it appears in unsafe positions like inside <script> tags or Angular filters without HTML entity encoding.

> If the string is reflected raw (e.g., not as &quot;TESTREFLECT123&quot;), proceed to payload crafting. AngularJS sandbox may still block direct <script>alert(1)</script>, but escapes are possible.

### Step 3: Craft and Inject Sandbox Escape Payload

**Context**: Construct a payload that uses AngularJS events (e.g., ng-focus) combined with unsafe filters like orderBy to escape the sandbox and execute code. This bypasses restrictions on global functions like alert.

Reference the payload from [[codes/AngularJS-Sandbox-Escape-XSS-Payload]] and inject it into the input field. For example, in a search box, enter the full payload and submit.

To trigger, click on the input field to fire the ng-focus event, which processes the expression and executes the alert with document.cookie.

> The payload leverages $event.path to access DOM nodes and orderBy filter to invoke constructor functions indirectly, escaping sandbox limits.

### Step 4: Verify Execution and Extract Data

**Context**: After injection, confirm the payload executes by observing the alert dialog. This validates the XSS and allows capturing sensitive information like cookies for session takeover.

If an alert pops up displaying cookie data, the exploit succeeded. Use developer tools (Console tab) to further interact or exfiltrate data via additional payloads.

> Success is indicated by the alert firing without errors. If blocked, iterate on payload variations or check Angular version.
