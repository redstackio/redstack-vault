---
id: 16126e3b-de51-4d40-a4cf-a3cd7b76d6ff
name: Filter-Bypass-with-Exotic-Payloads-for-XSS
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.577470+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - xss
  - filter-bypass
  - defense-evasion
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Filter-Bypass-with-Exotic-Payloads-for-XSS

## Summary

This procedure demonstrates techniques for bypassing web application filters designed to prevent Cross-Site Scripting (XSS) attacks by using exotic payloads that incorporate null bytes, vertical tabs, or slashes to evade event handler restrictions. These methods allow attackers to inject and execute JavaScript code in a victim's browser, potentially leading to session hijacking, data theft, or further exploitation.

## Description

Cross-Site Scripting (XSS) vulnerabilities enable attackers to inject malicious scripts into web pages viewed by other users. Filters often block common event handlers like 'onerror' to prevent execution, but they can be bypassed using obfuscation techniques such as inserting null bytes (\x00), vertical tabs (\x0b), or slashes (/) into attribute names. This procedure targets reflected or stored XSS scenarios in web applications with weak input sanitization. It assumes the attacker has identified an injectable input field (e.g., search box, comment form) and uses browser developer tools or a proxy like Burp Suite to test payloads. Successful bypass results in arbitrary JavaScript execution, such as displaying an alert or stealing cookies. This is particularly effective against applications using regex-based filters that do not account for Unicode or control characters.

## Requirements

1. Access to a web application with a suspected XSS vulnerability (e.g., via direct interaction or controlled environment like DVWA).
2. Knowledge of the target's filter patterns, such as blocking 'onerror=' but allowing variations.
3. Browser with developer tools (e.g., Chrome DevTools) or a web proxy like [[tools/Burp-Suite]] for intercepting and modifying requests.
4. Basic understanding of HTML and JavaScript event handlers.

## Defense

- Implement comprehensive input validation and output encoding using libraries like OWASP ESAPI or DOMPurify to sanitize user inputs.
- Deploy Content Security Policy (CSP) headers to restrict inline script execution and limit script sources.
- Use Web Application Firewalls (WAFs) like ModSecurity with updated rulesets to detect obfuscated payloads, including control characters and unusual attribute formats.
- Regularly audit and fuzz inputs with tools like XSStrike to identify bypass opportunities.

## Objectives

1. Identify and evade specific filter rules blocking XSS event handlers.
2. Inject executable JavaScript payloads into vulnerable web inputs.
3. Trigger script execution in the victim's browser context.
4. Achieve arbitrary code execution, such as alerting a message or exfiltrating data.

## Instructions

### Step 1: Identify Injectable Context

**Context**: Locate an input field or parameter that reflects user input without proper sanitization, such as a search query or URL parameter. Use manual testing or fuzzing to confirm reflection.

Inspect the page source or use a proxy to observe how input is rendered (e.g., in an <img> tag src or alt attribute).

> If the input appears in a context where event handlers can be attached (e.g., <img src='userinput'>), proceed to payload injection. Otherwise, explore other vectors like script tags.

### Step 2: Test Standard XSS Payload

**Context**: Attempt a basic payload to confirm vulnerability and identify the filter's behavior. This establishes a baseline before applying bypasses.

Submit a simple payload like <img src='x' onerror='alert(1)'> and observe if it's blocked (e.g., 'onerror' stripped or escaped).

> Expected: If blocked, the alert does not trigger, and source shows sanitized output. Document the exact filter pattern (e.g., 'onxxx=' blocked).

### Step 3: Apply Exotic Bypass Payloads

**Context**: Use obfuscated variations to evade the filter. Reference the provided code snippet for ready-to-use payloads.

Inject payloads from [[codes/XSS-Filter-Bypass-with-Null-Byte-and-Slash]] into the vulnerable input. For example, in a reflected search field:

```html
<img src='1' onerror\x00=alert(0) />
```

Or:

```html
<img src='1' onerror/=alert(0) />
```

Test each variation (null byte, vertical tab, slash) iteratively, encoding if necessary for URL parameters (e.g., %00 for null byte).

> Explanation: The null byte (\x00) or vertical tab (\x0b) terminates the filter's regex match prematurely, allowing the event handler to execute. The slash (/) confuses parsers expecting strict attribute syntax. Expected output: JavaScript alert(0) pops up, confirming execution. If no alert, check for additional filters like WAF blocking and adjust encoding.

### Step 4: Verify and Escalate

**Context**: Confirm successful execution and expand to more impactful actions, such as stealing cookies or keylogging.

Replace alert(0) with document.cookie or a more complex script. Use the browser console to inspect the reflected output post-submission.

> If successful, the payload executes client-side. For escalation, chain with other techniques like sending data to an attacker-controlled server. Decision point: If bypass fails, try case variations (e.g., OnError) or alternative events (onload).
