---
id: d1cbf8c9-6514-4a74-9aca-91099adb1663
name: Bypass-Quotes-in-Script-Tag-for-XSS-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.451487+00:00'
updated_at: '2023-04-10T20:21:48.171648+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/T1059.007 -
    JavaScript|T1059.007]]
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/xss]]'
  - '[[tags/filter-bypass]]'
  - '[[tags/web-injection]]'
  - '[[tags/Bypass quotes in script tag]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
commands:
  - '[[commands/Inject-XSS-Payload-via-URL-Parameter]]'
platforms:
  - Web
tools: []
validated: true
---

# Bypass-Quotes-in-Script-Tag-for-XSS-Injection

## Summary

This procedure demonstrates how to bypass quote filters in HTML script tags to inject malicious JavaScript code via Cross-Site Scripting (XSS), enabling execution of arbitrary code in the victim's browser. It targets web applications that echo user input into script contexts without proper escaping, allowing attackers to steal session tokens, cookies, or perform actions on behalf of the user.

## Description

In web applications, user input reflected into JavaScript contexts within <script> tags can lead to XSS if not sanitized. Filters may block direct <script> tags or quotes, but attackers can bypass them by closing existing script tags prematurely and injecting new ones. This technique uses payloads that break out of quoted strings (e.g., foo="text" + input) by injecting a closing quote, script tag, and alert or other JS. The target environment is typically PHP or server-side rendered pages with unsanitized GET/POST parameters. Success results in JavaScript execution, such as displaying an alert or exfiltrating data. Prerequisites include identifying a reflection point via reconnaissance.

## Requirements

1. Access to a web application with a reflected input parameter in a script context (e.g., via URL query string).
2. Knowledge of the application's structure, such as parameter names and echo locations.
3. Tools like a browser developer console or curl for testing payloads.
4. No authentication required if the vulnerability is unauthenticated.

## Defense

- Implement strict input validation and output encoding (e.g., htmlspecialchars with ENT_QUOTES flag in PHP) for all user inputs in script contexts.
- Use Content Security Policy (CSP) headers to restrict inline scripts and eval().
- Employ Web Application Firewalls (WAFs) to detect and block common XSS payloads, including encoded variants.
- Regularly scan with tools like OWASP ZAP or Burp Suite for XSS vulnerabilities.

## Objectives

1. Identify and exploit a reflected XSS vulnerability in a script tag context.
2. Bypass quote-based filters using tag closure techniques.
3. Execute JavaScript to demonstrate impact, such as alerting or data theft.
4. Validate successful injection without triggering application errors.

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Examine the web page source to locate where user input is echoed into a <script> tag, such as in a variable assignment like foo="text" + input. Confirm the input is not escaped.

Use browser dev tools or view source to inspect. No command needed here; manual inspection.

**Expected Output**: Identification of the parameter (e.g., ?test=) and its reflection point.

### Step 2: Craft and Test Basic Payload

**Context**: Construct a payload to close the open quote and script tag, then inject a new <script> with alert(1). This breaks out of the string context.

**Command** ([[commands/Inject-XSS-Payload-via-URL-Parameter]]):
```bash
curl "http://localhost/bla.php?test=</script><script>alert(1)</script>"
```

> This sends the payload via GET. The payload closes the existing script tag and injects a new one. If vulnerable, the page will execute alert(1) when loaded in a browser.

**Expected Output**: HTTP response containing the injected script, and in a browser, a pop-up alert box.

### Step 3: Verify Execution and Escalate

**Context**: Load the payload in a browser to confirm JS execution. For escalation, replace alert(1) with data exfiltration, e.g., sending document.cookie to an attacker server.

Modify the payload as needed and reload. Use proxy tools like Burp Suite to intercept and adjust.

**Expected Output**: Successful alert or network request to attacker endpoint confirming data theft.

