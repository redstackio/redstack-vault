---
id: 307965b1-0091-4162-8eca-8a4e84d46d97
name: Exotic Payloads for Bypassing XSS Filters
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.557840+00:00'
updated_at: '2023-04-10T20:21:31.881649+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - bypass-parenthesis-semi-colon
  - cross-site-scripting
  - filter-bypass
  - exotic-payloads
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Exotic Payloads for Bypassing XSS Filters

## Summary

This procedure demonstrates how to bypass XSS filters using exotic JavaScript payloads that leverage error handling mechanisms like onerror to execute code without relying on standard script tags or common patterns blocked by filters. These payloads are particularly useful against input sanitization that strips parentheses, semicolons, or direct script injections, enabling attackers to trigger alerts or execute arbitrary JavaScript in the victim's browser context.

## Description

Cross-Site Scripting (XSS) attacks inject malicious scripts into web pages viewed by other users, allowing theft of session cookies, keystroke logging, or page defacement. Filters often block obvious payloads like <script>alert(1)</script> by removing tags, attributes, or specific characters. Exotic payloads evade these by using native JavaScript error throwing (e.g., throw statements) combined with global event handlers like onerror to evaluate code indirectly. This technique targets reflected or stored XSS in web applications with weak sanitization, such as search fields, comment sections, or URL parameters. Success leads to code execution in the browser, potentially compromising user sessions or data. Map to MITRE ATT&CK: Execution (TA0002) via JavaScript (T1059.007). Use in red team exercises to test WAF rules or client-side protections.

## Requirements

1. Access to a vulnerable web application with reflected or stored XSS (e.g., unescaped user input in HTML output).
2. Knowledge of the target's filter rules, such as blocks on semicolons, parentheses, or script tags (test via manual fuzzing).
3. A testing environment like Burp Suite or browser developer tools to inject and observe payloads.
4. Basic JavaScript understanding to adapt payloads if needed.

## Defense

- Implement strict input validation and output encoding (e.g., HTML entity encoding for user inputs).
- Deploy Content Security Policy (CSP) headers to restrict inline scripts and eval execution.
- Use Web Application Firewalls (WAFs) with updated XSS rulesets and regularly test with tools like XSStrike.
- Sanitize inputs server-side and enable browser security features like XSS Auditor (deprecated but similar in modern browsers).

## Objectives

1. Bypass XSS filters using error-based exotic payloads to execute JavaScript without blocked syntax.
2. Evade detection by avoiding common patterns, enabling successful code injection.
3. Achieve arbitrary code execution to steal sensitive data like cookies or session tokens.

## Instructions

### Step 1: Identify Injection Point and Test Basic Filters

**Context**: Locate a point where user input is reflected back unsanitized (e.g., search query, profile field). Test for filter behaviors by injecting simple payloads like <script>alert(1)</script> to confirm blocks on tags or characters like ; and ().

If basic payloads fail, proceed to exotic ones. No specific command needed; use browser or proxy tools manually.

**Expected Output**: Confirmation of filter evasion if an alert pops or console logs the execution.

### Step 2: Inject Exotic Payload Using Error Throwing

**Context**: Use the exotic script injection payloads that throw errors to trigger onerror, evaluating code without direct script execution. These bypass filters stripping parentheses or semicolons by using comma-separated throws or prototype pollution.

**Code** ([[codes/XSS-Exotic-Script-Injection-Payloads]]):

Embed one of the following payloads in the injection point (e.g., as a URL parameter or form input):

```javascript
// From @garethheyes
<script>onerror=alert;throw 1337</script>
<script>{onerror=alert}throw 1337</script>
<script>throw onerror=alert,'some string',123,'haha'</script>

// From @terjanq
<script>throw/a/,Uncaught=1,g=alert,a=URL+0,onerror=eval,/1/g+a[12]+[1337]+a[13]</script>

// From @cgvwzq
<script>TypeError.prototype.name ='=/',0[onerror=eval]['/-alert(1)//']</script>
```

> These payloads set onerror to a function (e.g., alert or eval) before throwing an error, executing the handler. The first set uses simple throws; the second obfuscates with regex and URL properties; the third pollutes TypeError prototype. Replace 'alert' with actual payloads like document.cookie for exfiltration. Observe in browser console for errors triggering the execution.

**Expected Output**: An alert dialog (for testing) or silent execution of the payload, such as logging to console or sending data to an attacker server.

### Step 3: Verify Execution and Escalate

**Context**: Confirm the payload executed by checking for the alert or network requests. Escalate by replacing alert with data exfiltration (e.g., fetch to attacker endpoint with document.cookie).

Monitor browser network tab or console for success. If blocked, iterate by combining with other bypasses like case variations or encoding.

**Expected Output**: Evidence of code run, such as popped alert, console output, or received data on attacker side.

### Step 4: Clean Up and Document

**Context**: Remove test payloads from the application if in a controlled environment. Note successful payloads for reporting vulnerabilities.

No tools required; document findings in a report.
