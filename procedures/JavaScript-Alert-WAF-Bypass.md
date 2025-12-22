---
id: 71407a3d-2ed7-4595-b829-596ab937777f
name: JavaScript-Alert-WAF-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.624751+00:00'
updated_at: '2023-04-10T20:21:36.725557+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/T1059.007 -
    JavaScript|T1059.007]]
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/Common WAF Bypass]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Fortiweb WAF Bypass by @rezaduty - 9th July 2019]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# JavaScript-Alert-WAF-Bypass

## Summary

This procedure demonstrates how to bypass web application firewalls (WAFs) configured to block XSS payloads by using Unicode encoding on a JavaScript alert payload. It allows execution of client-side JavaScript in vulnerable web applications, such as reflected or stored XSS contexts, to confirm code injection or perform further actions like stealing cookies or session tokens.

## Description

In scenarios where a web application is protected by a WAF like FortiWeb, direct injection of XSS payloads (e.g., <script>alert('XSS')</script>) may be blocked due to signature-based detection. This technique obfuscates the payload using Unicode escape sequences (\uXXXX), which the WAF may not normalize or detect, but the browser decodes and executes. The target environment is typically a web application with unsanitized user inputs, such as search fields, URL parameters, or form submissions. Success enables JavaScript execution in the victim's browser, potentially leading to session hijacking, keylogging, or phishing. Prerequisites include identifying a reflection point via manual testing or tools like Burp Suite.

## Requirements

1. Access to a web application with a reflected or stored XSS vulnerability protected by a WAF.
2. Knowledge of the WAF's blocking patterns, often tested via trial-and-error with common payloads.
3. A browser or proxy tool (e.g., Burp Suite) to inject and observe the encoded payload without triggering blocks.
4. Basic understanding of HTML and JavaScript to customize the alert message or extend to more malicious actions.

## Defense

Defensive measures and detection strategies:

- Regularly update WAF rules to detect Unicode-normalized payloads and enable decoding normalization (e.g., in ModSecurity or FortiWeb).
- Implement content security policy (CSP) headers to restrict inline script execution and eval/alert functions.
- Enforce strict input validation, output encoding (e.g., HTML entity encoding), and sanitization on all user inputs using libraries like DOMPurify.
- Monitor web logs for suspicious patterns like high-frequency alert executions or unusual Unicode sequences in requests.

## Objectives

1. Evade WAF detection by obfuscating the XSS payload.
2. Execute JavaScript code in the target browser to confirm bypass and potential impact.
3. Demonstrate or exploit client-side execution for information disclosure or further attacks.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate a point in the web application where user input is reflected back without proper sanitization, such as a search parameter or comment field. Test with a benign payload like <script>alert(1)</script> to confirm XSS but expect WAF block.

Use browser developer tools or a proxy to inspect requests and responses for reflection.

**Expected Output**: The payload is blocked (e.g., 403 Forbidden or sanitized output), confirming WAF presence and vulnerability.

### Step 2: Encode the Payload Using Unicode Escapes

**Context**: Transform the standard XSS payload into Unicode to bypass WAF signatures. This step obfuscates characters like <, >, and h1 to prevent pattern matching while ensuring browser decoding.

Reference the encoded payload in [[codes/Unicode-Encoded-XSS-Alert-Payload]]:

```javascript
><h1 onclick=alert('1')>
```

Replace '1' with a custom message if needed (e.g., 'XSS' or document.cookie for testing theft).

**Expected Output**: The encoded string appears as garbled text in the request but decodes correctly in the HTML response.

### Step 3: Inject and Test the Encoded Payload

**Context**: Submit the encoded payload via the identified input point (e.g., URL parameter ?q=encoded_payload or form field). Observe if the WAF allows passage and the browser executes the alert.

Inject using a tool like curl or directly in the browser:

For example, in a URL: http://target.com/search?q=%u003e%u003c%u0068%u0031%20onclick=alert('1')%u003e

Monitor the response for the alert popup.

**Expected Output**: A JavaScript alert box displays '1' (or custom message) without WAF blocking the request.

### Step 4: Verify and Escalate if Successful

**Context**: Confirm execution by checking browser console for errors or using the alert to exfiltrate data (e.g., alert(document.cookie)). If successful, extend to more advanced payloads like beaconing to an attacker server.

Test data theft by modifying the payload to alert(document.domain) or similar.

**Expected Output**: Alert shows sensitive data like cookies or domain, indicating full client-side control.

**Success Indicators**:
- No WAF block (200 OK response).
- Alert executes without errors.
- Data exfiltration possible if extended.
