---
type: procedure
tactics:
  - '[[tactics/Defense-Evasion|TA0005]]'
techniques:
  - '[[techniques/Obfuscated-Files-or-Information|T1027]]'
  - '[[techniques/Command-and-Scripting-Interpreter-JavaScript|T1059.007]]'
sub_techniques: []
tags:
  - jsfuck-bypass
  - cross-site-scripting
  - filter-bypass
  - obfuscation
commands: []
tools: []
platforms:
  - Web
  - Browser
skill_level: intermediate
impact_level: medium
detection_risk: low
verified: true
validated: true
---

# JSFuck-Obfuscation-for-XSS-Payloads

## Summary

This procedure demonstrates how to use JSFuck obfuscation to encode JavaScript payloads, enabling them to bypass basic content filters and detection mechanisms in Cross-Site Scripting (XSS) attacks. By representing standard JavaScript functionality using only six characters ([]()!+), attackers can inject seemingly innocuous strings that execute malicious code in the victim's browser.

## Description

JSFuck is an esoteric encoding technique that constructs valid JavaScript from a minimal character set, making payloads appear as gibberish to human reviewers or simple regex-based filters. In an XSS context, this is used to evade Web Application Firewalls (WAFs) or input sanitization that blocks common keywords like 'alert' or 'document'. The technique maps to MITRE ATT&CK T1027 for obfuscation and T1059.007 for JavaScript execution. It is particularly effective against reflected or stored XSS vulnerabilities where direct script tags are filtered, allowing attackers to steal cookies, session tokens, or perform keylogging in the victim's browser session. The target environment is typically client-side web applications running in modern browsers like Chrome or Firefox.

## Requirements

1. Identification of an XSS vulnerability in a web application (e.g., via reflected input in a search field or stored comment).
2. Basic knowledge of JavaScript and browser developer tools for testing.
3. Access to the vulnerable input point, such as a URL parameter or form field.
4. Optional: A JSFuck encoder tool or manual construction skills for custom payloads.

## Defense

- Implement comprehensive Content Security Policy (CSP) to restrict inline script execution.
- Use advanced WAF rules that detect anomalous JavaScript patterns beyond simple keyword blocking.
- Employ client-side sanitization libraries like DOMPurify to decode and validate inputs.
- Monitor for unusual browser console activity or network requests from obfuscated scripts.

## Objectives

1. Obfuscate a JavaScript payload to bypass input filters in an XSS vector.
2. Inject and execute the obfuscated code in the victim's browser context.
3. Demonstrate payload execution, such as displaying an alert or exfiltrating data.
4. Validate the bypass against common detection mechanisms.

## Instructions

### Step 1: Identify the XSS Injection Point

**Context**: Locate a vulnerable input field or parameter that reflects user input without proper escaping, allowing script execution. Test with a simple payload like <script>alert(1)</script> to confirm the vulnerability.

Use browser developer tools to inspect the reflected input and note any filtering behaviors, such as blocking 'script' tags or 'alert' keywords.

### Step 2: Generate or Select a JSFuck Payload

**Context**: Choose or create a JSFuck-encoded version of your desired JavaScript action. For testing, use a basic alert(1) payload, which pops an alert box to confirm execution without causing harm.

Reference the obfuscated code: [[codes/JSFuck-Alert-One-Payload]]

This code represents alert(1) using only []()!+ characters.

### Step 3: Inject the Obfuscated Payload

**Context**: Insert the JSFuck string into the vulnerable input point, ensuring it executes as JavaScript in the page context. For reflected XSS, append it to a URL parameter; for stored XSS, submit it via a form.

Example injection in a URL: https://vulnerable-site.com/search?q=<script>[JSFuck code here]</script>

If direct <script> tags are blocked, try event handlers like <img src=x onerror="[JSFuck code]">.

### Step 4: Verify Execution and Impact

**Context**: Load the page with the injected payload and observe if the obfuscated code executes. In a real attack, replace alert(1) with actions like document.cookie exfiltration to a controlled server.

Open the browser console to check for errors. Successful execution will trigger the alert without filter blocks.

**Expected Output**: A browser alert dialog displaying '1', confirming the payload ran despite obfuscation.

**Success Indicators**:
- Alert box appears without console errors.
- No WAF blocks or sanitization removes the payload.
- In advanced tests, data exfiltration occurs (e.g., POST to attacker server).
