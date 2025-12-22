---
id: c9acae9f-84f9-46b5-b8e9-ec4e5fd35dd7
name: Akamai-WAF-Bypass-via-Common-XSS-Injection-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.546188+00:00'
updated_at: '2023-04-10T20:21:47.464059+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Scripting|T1064 - Scripting]]'
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
sub_techniques: []
tags:
  - >-
    [[tags/Akamai WAF Bypass by [@zseano](https://twitter.com/zseano) - 18th
    June 2018]]
  - '[[tags/Common WAF Bypass]]'
  - '[[tags/Cross Site Scripting]]'
  - xss
  - waf-bypass
commands:
  - '[[commands/curl-send-xss-payload]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Akamai-WAF-Bypass-via-Common-XSS-Injection-Attack

## Summary

This procedure demonstrates a technique to bypass Akamai Web Application Firewall (WAF) protections by injecting a crafted Cross-Site Scripting (XSS) payload into a vulnerable web application. The payload exploits encoding and parsing quirks to evade detection rules, allowing malicious JavaScript execution in the victim's browser.

## Description

Akamai WAF is a cloud-based security solution that filters HTTP traffic to block common web attacks like XSS. However, certain payloads can bypass its signature-based detection by using URL encoding, attribute manipulation, and incomplete tag closures. This procedure targets reflected or stored XSS vulnerabilities in web apps behind Akamai, where user input is not properly sanitized. The attack injects a script that redirects or executes code, bypassing the WAF to achieve code execution on the client side. This can lead to session hijacking, data theft, or further exploitation. The technique relies on a specific payload that closes an existing script tag and injects a base element to alter page behavior, evading Akamai's pattern matching.

## Requirements

1. Access to a web application protected by Akamai WAF with a known XSS vulnerability (e.g., unsanitized input fields in search, comments, or forms).
2. Knowledge of the target URL and input parameters vulnerable to injection.
3. Tools for sending HTTP requests, such as curl or a browser with developer tools.
4. Network access to the target application (no authentication required for public-facing vulns).

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) headers to restrict script execution and inline JavaScript.
- Use advanced WAF rules with behavioral analysis beyond signatures, including anomaly detection for unusual encodings.
- Sanitize and validate all user inputs server-side, escaping HTML entities and rejecting suspicious patterns.
- Enable web application firewall logging and monitor for encoded payloads or unexpected base/script tags in traffic.
- Regularly scan for XSS vulnerabilities using tools like OWASP ZAP or Burp Suite.

## Objectives

1. Bypass Akamai WAF detection rules to inject malicious XSS payload.
2. Execute arbitrary JavaScript in the victim's browser context.
3. Achieve client-side code execution for data exfiltration or session manipulation.

## Instructions

### Step 1: Identify Vulnerable Input Parameter

**Context**: Locate a parameter in the web application that reflects user input without sanitization, such as a search query or URL parameter. Test basic XSS payloads like `<script>alert(1)</script>` to confirm vulnerability, noting if Akamai blocks them.

Inspect the application using browser developer tools or a proxy to identify the exact endpoint and parameter (e.g., ?q= for search).

### Step 2: Craft and Encode the Bypass Payload

**Context**: Use the specialized XSS payload designed to evade Akamai by closing an existing script tag and injecting a malformed base element. This exploits parsing differences between the WAF and browser.

Reference the payload code: [[codes/XSS-Payload-for-Akamai-WAF-Bypass]].

Replace the placeholder in the payload with the target site URL if needed for redirection.

### Step 3: Inject the Payload via HTTP Request

**Context**: Send the crafted payload to the vulnerable endpoint using an HTTP request. This simulates user input submission and triggers the XSS if the WAF is bypassed.

**Command** ([[commands/curl-send-xss-payload]]):
```bash
curl -X GET "http://target.com/vulnerable-page?q=$_PAYLOAD" -v
```

> This command sends a GET request with the encoded payload in the 'q' parameter. The -v flag provides verbose output to inspect the response. If successful, the response will include the injected script, and executing the page in a browser will trigger the XSS.

### Step 4: Verify Execution

**Context**: Load the vulnerable page with the injected payload in a browser to confirm code execution. Look for the payload's effects, such as a redirect or alert (modify payload for testing).

Open the URL with the payload in a browser and check the developer console for JavaScript errors or execution. If the base tag alters the page's base URL, navigation will confirm success.

**Expected Output**: The browser executes the injected code without WAF blocking; e.g., a redirect to the attacker's site or console log from the script.
