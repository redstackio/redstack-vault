---
id: cc122ec8-c17c-4eab-a786-3cb19c349138
name: Bypass-Space-Filter-in-XSS-with-Exotic-Payloads
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.605251+00:00'
updated_at: '2023-04-10T20:21:49.208510+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial-Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Obfuscated-Files-or-Information|T1027 - Obfuscated Files or
    Information]]
  - '[[techniques/Valid-Accounts|T1078 - Valid Accounts]]'
  - >-
    [[techniques/Command-and-Scripting-Interpreter-JavaScript|T1059.007 -
    Command and Scripting Interpreter: JavaScript]]
sub_techniques: []
tags:
  - '[[tags/Bypass-space-filter]]'
  - '[[tags/Cross-Site-Scripting]]'
  - '[[tags/Filter-Bypass-and-exotic-payloads]]'
commands:
  - '[[commands/xss-payload-bypass-slash]]'
  - '[[commands/xss-payload-bypass-formfeed]]'
  - '[[commands/convert-xss-payload-to-hex]]'
platforms:
  - Web
tools: []
validated: true
---

# Bypass-Space-Filter-in-XSS-with-Exotic-Payloads

## Summary

This procedure demonstrates how to bypass space filters in web applications vulnerable to Cross-Site Scripting (XSS) by using exotic payloads that replace spaces with alternative characters like forward slashes (/) or form feed characters (0x0c, represented as ^L). These techniques allow attackers to inject and execute JavaScript code, such as alert functions, to test for reflected or stored XSS, potentially leading to session hijacking or data theft.

## Description

Space filters are common in web input sanitization to prevent XSS by blocking payloads with spaces between attributes and values. This procedure uses obfuscation to evade such filters: the slash bypass leverages '/' as a space substitute in attribute contexts, while the form feed (0x0c) inserts invisible control characters that parsers ignore but filters may miss. Applicable in reflected, stored, or DOM-based XSS scenarios on web applications with inadequate output encoding. Success enables arbitrary JavaScript execution in the victim's browser, aligning with MITRE ATT&CK techniques for obfuscated information and JavaScript execution.

## Requirements

1. Access to a web application input field vulnerable to XSS (e.g., search box, comment form).
2. Knowledge of the filter's behavior (confirm space blocking via testing).
3. Browser developer tools or a proxy like Burp Suite for inspecting responses.
4. Basic understanding of HTML attributes and JavaScript event handlers.

## Defense

- Implement comprehensive input validation and output encoding (e.g., HTML entity encoding for user inputs).
- Deploy Content Security Policy (CSP) to restrict inline script execution and eval().
- Use Web Application Firewalls (WAFs) trained on obfuscated payloads, including control characters.
- Regularly scan for XSS vulnerabilities with tools like OWASP ZAP or Burp Suite.

## Objectives

1. Evade space-based filters to inject executable JavaScript.
2. Trigger a proof-of-concept alert to confirm XSS.
3. Demonstrate potential for stealing session cookies or performing actions on behalf of the victim.

## Instructions

### Step 1: Test Standard XSS Payload

**Context**: Verify the vulnerability exists and that spaces are being filtered by attempting a basic payload like `<script>alert(1)</script>`. If blocked, proceed to exotic variants.

Observe the application's response in the browser or proxy to confirm filtering.

### Step 2: Inject Slash-Based Payload

**Context**: Use the forward slash (/) as a space substitute in the onerror attribute of an img tag. This bypasses filters expecting traditional spaces while triggering JavaScript on load failure.

**Command** ([[commands/xss-payload-bypass-slash]]):

```html
<img/src='1'/onerror=alert(0)>
```

> Submit this payload into the vulnerable input field. The browser will attempt to load the invalid src='1', failing and executing alert(0). Expected output: A popup alert box displaying '0' if successful.

### Step 3: Inject Form Feed-Based Payload

**Context**: Replace spaces with form feed characters (0x0c, ^L in some notations) in an SVG onload attribute. This inserts non-printable characters that HTML parsers treat as whitespace but may evade regex-based space filters.

**Command** ([[commands/xss-payload-bypass-formfeed]]):

```html
<svg\fonload\=\alert(1)\>
```

> Note: The \f represents the form feed (0x0c) in string literals. Submit this into the input. The SVG loads, executing alert(1). Expected output: Alert popup with '1'.

### Step 4: Verify Obfuscation with Hex Conversion

**Context**: Convert the payload to hexadecimal to understand or generate the exact bytes, useful for crafting in tools or confirming filter evasion.

**Command** ([[commands/convert-xss-payload-to-hex]]):

```bash
echo "<svg^Lonload^L=^Lalert(1)^L>" | xxd
```

> Here, ^L denotes 0x0c. Run this on the attacker machine to view the hex representation. Expected output: Byte dump showing 0x0c in place of spaces, e.g., 00000000: 3c73 7667 0c6f 6e6c 6f61 640c 3d0c 616c  <svg.onload.=.al

### Step 5: Validate Execution and Escalate

**Context**: After successful alert, replace alert() with malicious code, e.g., document.cookie to exfiltrate data.

Monitor network traffic for any data leaks and confirm no errors in console.
