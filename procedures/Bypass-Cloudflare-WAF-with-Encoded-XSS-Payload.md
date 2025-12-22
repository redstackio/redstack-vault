---
type: procedure
description: >-
  Bypasses Cloudflare's WAF protection using an encoded XSS payload to execute
  JavaScript on the target server.
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - xss
  - waf-bypass
  - cloudflare
  - cross-site-scripting
commands:
  - '[[commands/curl-inject-xss-payload]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Bypass-Cloudflare-WAF-with-Encoded-XSS-Payload

## Summary

This procedure demonstrates how to bypass Cloudflare's Web Application Firewall (WAF) using an encoded cross-site scripting (XSS) payload. The technique involves crafting an HTML link with obfuscated JavaScript that evades WAF filters, allowing execution of arbitrary code in the victim's browser to potentially steal session data or perform other malicious actions.

## Description

Cloudflare's WAF often blocks standard XSS payloads like 'javascript:alert(document.domain)' by signature matching. This procedure uses HTML entity encoding and tab/newline obfuscation to disguise the payload, exploiting parsing differences between the WAF and the target application. It is applicable in reflected or stored XSS scenarios on web applications protected by Cloudflare, such as search fields, URL parameters, or user-generated content areas. Success depends on the target application's failure to properly decode and sanitize inputs. The payload executes JavaScript to access the document domain, which can be extended to exfiltrate cookies or perform further actions.

## Requirements

1. Network access to a Cloudflare-protected web application with a potential XSS vulnerability (e.g., reflected input in a URL parameter).
2. Tools for web interception and manipulation, such as [[tools/Burp-Suite]].
3. Basic knowledge of HTML encoding and JavaScript execution in browsers.
4. A testing environment or permission to test the target (e.g., bug bounty program).

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) headers to restrict script execution.
- Use advanced WAF rules with decoding normalization to detect obfuscated payloads.
- Sanitize and encode all user inputs server-side, validating against allowlists.
- Monitor for anomalous JavaScript execution via client-side logging or browser security features.
- Regularly audit web applications for XSS vulnerabilities using automated scanners.

## Objectives

1. Evade Cloudflare WAF filters to inject an XSS payload.
2. Execute JavaScript in the victim's browser context.
3. Demonstrate potential for data theft or session hijacking.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate a parameter or input field in the target application that reflects user input without proper sanitization, such as a search query or redirect URL. Use [[tools/Burp-Suite]] to map the application and test for reflection.

Navigate to the target site and identify endpoints like '/search?q=<input>'. Confirm reflection by inputting a benign string like 'test' and checking if it appears in the response.

### Step 2: Prepare the Encoded XSS Payload

**Context**: Use the pre-encoded payload to obfuscate the JavaScript, preventing WAF detection. This step references the standalone code snippet for the payload.

Reference the [[codes/HTML-Link-with-Encoded-JavaScript-XSS]] code and copy the HTML link. The encoding uses HTML entities (&Tab; for tabs, &NewLine; for line breaks) to break WAF signatures while allowing browser parsing.

### Step 3: Inject the Payload

**Context**: Deliver the payload to the vulnerable input. This can be done manually via browser or automated with a request tool. Use [[commands/curl-inject-xss-payload]] for testing in a non-interactive way.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -X GET "https://target.example.com/search?q=<a href=\"j&Tab;a&Tab;v&Tab;asc&NewLine;ri&Tab;pt&colon;&lpar;a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;(document.domain)&rpar;\">X</a>" -v
```

> This command sends the encoded payload in a GET request to a reflected parameter. The -v flag provides verbose output to inspect the response. If using Burp Suite, intercept the request, modify the parameter, and forward it.

### Step 4: Verify Execution

**Context**: Check if the payload executes by observing the alert or any side effects. In a real attack, extend to data exfiltration.

Load the modified URL in a browser. If successful, an alert box should display the document domain. Inspect browser console for errors or network requests indicating execution.

**Expected Output**: Browser alert showing the domain (e.g., "target.example.com"), or console log confirming JavaScript ran without WAF blocking the request (HTTP 200 response).
