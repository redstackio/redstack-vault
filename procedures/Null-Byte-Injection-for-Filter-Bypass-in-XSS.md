---
id: d81ce74b-cea3-4538-bd53-e55acee07a0d
name: Null-Byte-Injection-for-Filter-Bypass-in-XSS
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.096782+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/JavaScript|T1059.007 -
    JavaScript]]
sub_techniques: []
tags:
  - '[[tags/Bypass using UTF-32]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
  - null-byte
  - xss
  - injection
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Null-Byte-Injection-for-Filter-Bypass-in-XSS

## Summary

Null Byte Injection is a technique to bypass input sanitization filters in web applications by appending null bytes (%00) to malicious payloads, causing the filter to terminate processing early and allow the payload to pass. This is commonly used in Cross-Site Scripting (XSS) attacks to inject executable scripts, such as JavaScript alerts or more complex payloads, enabling attackers to steal session cookies, redirect users, or execute arbitrary code in the victim's browser.

## Description

In web applications, filters often sanitize user inputs to prevent attacks like XSS by stripping or escaping dangerous characters. Null Byte Injection exploits string termination behavior in languages like C/C++ or certain parsers (e.g., PHP before version 5.3), where a null byte signals the end of a string. By injecting multiple null bytes followed by encoded malicious content (e.g., URL-encoded SVG with onload JavaScript), the filter processes only up to the null byte, ignoring the rest. This allows the full payload to reach the application or browser.

This procedure targets reflected or stored XSS vulnerabilities in input fields, search boxes, or file uploads where filters are in place but vulnerable to null byte truncation. Success leads to script execution in the victim's context, potentially compromising accounts or exfiltrating data. It requires identifying filter weaknesses, often through trial-and-error with tools like Burp Suite for interception and modification.

## Requirements

1. Access to a web application with user input fields (e.g., search, comments, profile updates) protected by input filters.
2. Knowledge of the application's backend language or parser (e.g., PHP, ASP.NET) to confirm null byte vulnerability.
3. Ability to intercept and modify HTTP requests, such as via a proxy tool like Burp Suite.
4. Basic understanding of URL encoding and XSS payloads.

## Defense

- Implement strict input validation that rejects or strips null bytes (%00) and multi-byte encodings like UTF-32 at the application layer.
- Use parameterized queries and output encoding (e.g., HTML entity encoding) for all user inputs to prevent XSS.
- Deploy Web Application Firewalls (WAFs) configured to detect null byte patterns and anomalous encodings in payloads.
- Regularly update frameworks and libraries to versions immune to null byte issues (e.g., PHP 5.3+ with proper string handling).
- Enable Content Security Policy (CSP) headers to restrict script execution from inline or untrusted sources.

## Objectives

1. Bypass input filters to inject a malicious XSS payload.
2. Execute JavaScript in the victim's browser to demonstrate compromise (e.g., alert popup).
3. Potentially steal sensitive data like cookies or session tokens for further exploitation.

## Instructions

### Step 1: Identify Vulnerable Input Field

**Context**: Locate an input field in the web application that accepts user data and is filtered but potentially vulnerable to null byte truncation. Test basic XSS payloads first to confirm filtering is active.

Manually enter a simple XSS test like `<script>alert(1)</script>` into fields such as search boxes or forms. Observe if the filter blocks it (e.g., by escaping or removing tags). If blocked, proceed to null byte testing.

**Expected Output**: The basic payload is sanitized or rejected, confirming the presence of a filter.

### Step 2: Craft Null Byte Payload

**Context**: Construct a payload using multiple null bytes (%00) followed by the encoded malicious content. This tricks the filter into terminating early, allowing the payload to pass to the output rendering stage.

Use the provided code snippet [[codes/UTF-32-Encoded-SVG-XSS-Payload]] as the base payload. This is an SVG element with onload attribute triggering a JavaScript alert, encoded with UTF-32 null bytes for evasion.

**Code** ([[codes/UTF-32-Encoded-SVG-XSS-Payload]]):

```js
%00%00%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E
```

Append this directly to the input field or as a URL parameter (e.g., ?search=%00%00...).

**Expected Output**: The payload is accepted without sanitization errors.

### Step 3: Inject and Intercept Request

**Context**: Submit the crafted payload through the vulnerable input using a proxy to monitor the request and response. This allows modification if initial attempts fail.

Configure a proxy like Burp Suite to intercept traffic. Submit the form or query with the null byte payload. In the intercepted request, ensure the payload is correctly URL-encoded if needed, then forward it.

**Expected Output**: The server processes the request without rejection, and the response includes the unsanitized payload.

### Step 4: Verify Execution

**Context**: Check if the payload executes in the browser, confirming the bypass. Look for the alert popup or inspect the rendered HTML.

Load the page with the injected payload in a browser. If successful, the JavaScript alert should trigger. Use browser developer tools (F12) to inspect the DOM for the injected SVG element.

**Expected Output**: JavaScript alert box appears, or console logs show execution.

**Success Indicators**:
- Payload appears in the response without truncation before the null bytes.
- No filter errors or blocks during submission.
- Script executes, demonstrating full bypass.
