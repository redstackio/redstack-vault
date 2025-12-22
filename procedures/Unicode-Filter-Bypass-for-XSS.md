---
type: procedure
description: >-
  Uses Unicode character transformations to bypass input validation filters in
  web applications, enabling XSS payload injection.
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - unicode-bypass
  - filter-bypass
  - injection
commands:
  - '[[commands/curl-test-unicode-xss-payload]]'
tools: []
platforms:
  - web-applications
  - javascript
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Unicode-Filter-Bypass-for-XSS

## Summary

This procedure demonstrates how to bypass web application input filters using Unicode characters that normalize or transform into dangerous ASCII equivalents, such as angle brackets for script tags in XSS attacks. By encoding payloads with visually similar or case-variant Unicode, attackers can evade blacklisting or normalization filters, leading to successful code injection and execution in the victim's browser.

## Description

Unicode filter bypass exploits the fact that many web applications perform incomplete normalization on input, allowing characters like the fullwidth less-than sign (U+FF1C, encoded as %EF%BC%9C) to transform into the standard less-than sign (<) during processing. This technique is particularly effective against XSS filters that block direct use of <script> or onload attributes but fail to handle Unicode variants. The attack targets client-side rendering in browsers, where JavaScript execution can steal cookies, session tokens, or perform actions on behalf of the user. It requires identifying filter weaknesses through testing and crafting payloads that survive sanitization. Success results in arbitrary JavaScript execution, enabling data exfiltration or session hijacking in vulnerable web apps.

## Requirements

1. Access to a web application with input fields vulnerable to XSS (e.g., search boxes, comments, or profile fields).
2. Knowledge of URL encoding and Unicode normalization (e.g., via browser dev tools or proxy like Burp Suite).
3. A testing environment or proxy to intercept and modify requests.
4. Basic understanding of JavaScript for payload construction.

## Defense

- Implement strict input validation using libraries like DOMPurify that handle Unicode normalization (e.g., NFKC form).
- Deploy a Web Application Firewall (WAF) configured to detect encoded payloads and Unicode evasions.
- Enforce Content Security Policy (CSP) to restrict inline script execution.
- Regularly audit and update sanitization routines to cover common Unicode bypass vectors.

## Objectives

1. Craft and inject a Unicode-encoded XSS payload that bypasses filters.
2. Achieve JavaScript execution in the victim's browser to demonstrate compromise.
3. Extract sensitive data like cookies or session information.

## Instructions

### Step 1: Identify and Apply Unicode Transformations for Basic Symbols

**Context**: Start by transforming common XSS symbols using Unicode equivalents that normalize to <, >, ', and ". This step prepares the core elements of an <svg onload=alert()> payload, evading filters that block direct ASCII usage.

**Code** ([[codes/fullwidth-to-ascii-unicode-transformations]]):

Use the provided transformations to encode your payload. For example, replace < with %EF%BC%9C (U+FF1C) and > with %EF%BC%9E (U+FF1E).

**Expected Output**: An encoded string like %CA%BA%EF%BC%9E%EF%BC%9Csvg%20onload=alert%28/XSS/%29%EF%BC%9E/ that decodes to "><svg onload=alert('XSS')>/ during browser processing.

### Step 2: Test the Encoded Payload Injection

**Context**: Inject the transformed payload into the target input field via a GET or POST request. Use a tool like curl to simulate submission and observe if the filter allows it through, leading to execution.

**Command** ([[commands/curl-test-unicode-xss-payload]]):
```bash
curl -G "http://www.example.net/something" --data-urlencode "input=%CA%BA%EF%BC%9E%EF%BC%9Csvg onload=alert%28/XSS/%29%EF%BC%9E"
```

> This command sends the Unicode-encoded payload to the vulnerable endpoint. Monitor the response for successful injection (e.g., the alert fires in a browser test) or errors indicating filter blocking.

**Expected Output**: HTTP response containing the injected payload without sanitization, or a browser popup with 'XSS' if tested interactively.

### Step 3: Apply Case Transformations for Additional Evasion

**Context**: If the application is case-sensitive in filtering (e.g., blocks 'svg' but not 'SVG'), use Unicode characters that change case to bypass. This builds on Step 1 for more resilient payloads.

**Code** ([[codes/case-sensitive-unicode-bypass-transformations]]):

Incorporate characters like ſ (%C5%BF) which uppercases to S, or ı (%C4%B1) which uppercases to I, to alter tag names like <svg> to <ſvg> that becomes <SVG> post-processing, evading case-specific blocks while preserving functionality.

**Expected Output**: Payload like <ſvg onload=alert(1)> renders as <SVG ONLOAD=ALERT(1)>, executing if the filter checks lowercase only.

### Step 4: Verify and Iterate

**Context**: After injection, verify execution by checking for the alert or network requests. If blocked, iterate by combining transformations or testing in a proxy.

**Expected Output**: Successful XSS trigger, such as a JavaScript alert or logged exfiltration attempt.

**Success Indicators**:
- Payload renders without stripping symbols.
- JavaScript executes (e.g., alert box appears).
- No server-side errors from filter rejection.
