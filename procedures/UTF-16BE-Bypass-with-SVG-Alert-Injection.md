---
id: 7fc92ec9-b7fd-498f-92e3-a5e57d2fd842
name: UTF-16BE-Bypass-with-SVG-Alert-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.078673+00:00'
updated_at: '2023-04-10T20:21:44.993577+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/Bypass using UTF-16be]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
  - xss
  - bypass
  - utf-16be
  - svg
commands: []
platforms:
  - Web
tools: []
validated: true
---

# UTF-16BE-Bypass-with-SVG-Alert-Injection

## Summary

This procedure demonstrates a Cross-Site Scripting (XSS) bypass technique using UTF-16BE encoding to evade input filters that do not handle this encoding properly. The payload injects an SVG element with an onload event that triggers a JavaScript alert, confirming the vulnerability. This is useful for testing web applications for reflected or stored XSS in environments where standard payloads are blocked.

## Description

UTF-16BE (UTF-16 Big Endian) encoding represents Unicode characters using 16-bit words with the most significant byte first. Many web filters focus on ASCII or UTF-8, overlooking UTF-16 variants, allowing attackers to smuggle payloads past sanitization. The SVG-based payload exploits the fact that SVG elements can execute JavaScript via event handlers like onload when rendered in a browser. This technique targets input fields, search boxes, or URL parameters in web applications. Upon successful injection, the browser parses the SVG and executes the alert, proving arbitrary JavaScript execution. This is particularly effective against filters that strip common XSS patterns like <script> but miss encoded SVG tags. The procedure assumes a vulnerable endpoint that reflects user input without proper decoding or normalization.

## Requirements

1. Access to a web application with a vulnerable input field that reflects user input (e.g., search box, comment form).
2. Knowledge of the application's input filtering to confirm it does not decode or block UTF-16BE.
3. A browser or proxy tool like Burp Suite to craft and send requests with the encoded payload.
4. Basic understanding of URL encoding and character set manipulation.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation that normalizes and decodes multiple encodings (UTF-8, UTF-16, etc.) before sanitization using libraries like OWASP Java Encoder or DOMPurify.
- Deploy Content Security Policy (CSP) headers to restrict inline script execution and SVG sources, e.g., script-src 'self'; object-src 'none'.
- Use Web Application Firewalls (WAFs) like ModSecurity with rules to detect encoded payloads and SVG event handlers.
- Educate developers on encoding-aware filtering and conduct regular XSS testing with tools like XSStrike.
- Monitor application logs for suspicious inputs containing null bytes (%00) or unusual encodings.

## Objectives

1. Encode an SVG-based XSS payload in UTF-16BE to bypass filters.
2. Inject the payload into a vulnerable web input and achieve JavaScript execution.
3. Confirm the XSS vulnerability by triggering a browser alert dialog.

## Instructions

### Step 1: Prepare the UTF-16BE Encoded Payload

**Context**: Start by obtaining the encoded version of the SVG payload. The base payload is <svg/onload=alert()>, which creates an SVG element that executes alert() on load. Encoding it in UTF-16BE introduces null bytes (\x00) between characters, evading ASCII-focused filters. Use the pre-encoded snippet provided in [[codes/UTF-16BE-Encoded-SVG-XSS-Payload]] to ensure accuracy.

**Code** ([[codes/UTF-16BE-Encoded-SVG-XSS-Payload]]):

```javascript
%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E%00
\x00<\x00s\x00v\x00g\x00/\x00o\x00n\x00l\x00o\x00a\x00d\x00=\x00a\x00l\x00e\x00r\x00t\x00(\x00)\x00>
```

> This encoded string represents the SVG tag in UTF-16BE. The %00-prefixed version is URL-encoded for HTTP transmission, while the \x00 version is for direct string insertion. Copy the appropriate format based on your injection method.

### Step 2: Identify and Target the Vulnerable Input

**Context**: Locate an input field in the web application that echoes user input without escaping, such as a search parameter (?q=) or form field. Test with benign inputs to confirm reflection. Use a proxy to inspect requests and ensure the input is not sanitized for multi-byte encodings.

**Instructions**: Navigate to the target page (e.g., http://vulnerable-site.com/search?q=) and prepare to submit the payload in the reflected parameter.

> If using a browser console or developer tools, you can also inject via DOM manipulation, but focus on HTTP parameters for realism.

### Step 3: Inject the Encoded Payload

**Context**: Submit the UTF-16BE encoded payload into the vulnerable input. The server should reflect it back in the response, and the browser will decode and render the SVG, triggering the onload event.

**Instructions**: Append or post the encoded payload to the input field. For a GET request example:

http://vulnerable-site.com/search?q=%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E%00

Use a tool like curl or Burp Repeater to send the request if manual browser submission fails due to encoding issues.

> Ensure the request Content-Type allows the encoding, or force UTF-16BE in the payload if the app supports it. Observe the response for the reflected input.

### Step 4: Verify Execution

**Context**: Load the page with the injected payload and check for JavaScript execution. Success is indicated by the alert dialog popping up, confirming the bypass and XSS vulnerability.

**Instructions**: Refresh or submit the form and monitor the browser for the alert('') box. If no alert appears, inspect the page source to see if the payload was reflected intact (look for the null bytes).

> If the payload is stripped, iterate by testing variations like wrapping in quotes or using different event handlers (e.g., onclick). Escalate to more complex payloads like stealing cookies if alert succeeds.
