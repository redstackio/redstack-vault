---
id: ecb3f6c4-feae-41e5-b184-1be9518e4026
name: Cloudflare-XSS-Bypass-via-SVG-Onload-Alert
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.346853+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
  - '[[techniques/Disable or Modify Tools|T1562.001 - Disable or Modify Tools]]'
sub_techniques: []
tags:
  - '[[tags/22nd August 2019]]'
  - >-
    [[tags/Cloudflare XSS Bypasses by [@Bohdan
    Korzhynskyi](https://twitter.com/bohdansec)]]
  - '[[tags/Common WAF Bypass]]'
  - '[[tags/Cross Site Scripting]]'
  - xss
  - waf-bypass
  - cloudflare
commands:
  - '[[commands/curl-inject-svg-xss]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Cloudflare-XSS-Bypass-via-SVG-Onload-Alert

## Summary

This procedure demonstrates how to bypass Cloudflare's Web Application Firewall (WAF) using a specially crafted SVG onload payload to execute arbitrary JavaScript, such as an alert, in a reflected XSS vulnerability. It exploits encoding tricks to evade WAF filters, allowing client-side code execution on the victim's browser without triggering Cloudflare's detection rules.

## Description

Cloudflare WAF protects web applications from common attacks like XSS by inspecting and blocking malicious payloads. However, certain encodings and attribute manipulations in SVG elements can slip past these filters. This technique involves injecting an SVG tag with an onload event that uses HTML entity encoding (%26nbsp; for &nbsp;) to disguise the alert function call. When reflected back in the page (e.g., via a search parameter or user input field), the browser parses and executes the JavaScript, popping an alert box with a custom message. This can be extended to steal cookies, session tokens, or perform further actions like keylogging. The target environment is any web application behind Cloudflare with a reflected XSS vulnerability in an HTML context that renders user input without proper sanitization.

## Requirements

1. Access to a web application protected by Cloudflare with a reflected XSS vulnerability (e.g., unsanitized input in search, comments, or URL parameters).
2. Ability to control input injection, such as through a GET/POST parameter or form field.
3. Tools for testing injection, such as a browser developer console, curl, or a proxy like Burp Suite.
4. Knowledge of the target's input reflection point (e.g., a parameter that echoes back HTML).

## Defense

- Implement strict input validation and output encoding (e.g., using HTML entity encoding) to prevent HTML/SVG injection.
- Deploy a robust Content Security Policy (CSP) that blocks inline scripts and restricts script sources.
- Regularly update Cloudflare WAF rulesets and monitor for bypass attempts via web application firewall logs.
- Use client-side sanitization libraries like DOMPurify to strip dangerous tags and attributes before rendering.

## Objectives

1. Identify a reflection point in the target application where user input is rendered as HTML.
2. Craft and inject an SVG-based XSS payload that evades Cloudflare's filtering.
3. Achieve JavaScript execution on the victim's browser to demonstrate compromise (e.g., alert popup).
4. Extend the payload for data exfiltration or session hijacking if successful.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate a parameter or form field in the Cloudflare-protected application that reflects user input directly into the HTML body without sanitization. This could be a search query, error message, or profile field. Use reconnaissance to test for reflection.

**Instructions**: Navigate to the target site and test inputs like <script>alert(1)</script> to confirm basic XSS, noting if Cloudflare blocks it. If blocked, proceed to SVG variant.

**Expected Output**: Input echoed back in the page source, confirming reflection.

### Step 2: Craft the SVG Onload Payload

**Context**: Use the pre-defined SVG payload to bypass WAF filters. The encoding (%26nbsp;) represents a non-breaking space to disrupt pattern matching while preserving functionality.

**Code** ([[codes/SVG-Onload-Alert-XSS-Payload]]):

```html
<svg/onload=%26nbsp;alert`bohdan`+
```

**Instructions**: Replace 'bohdan' with your desired alert message or further JS payload (e.g., document.cookie for cookie theft). Ensure the payload is URL-encoded if injected via GET parameters.

**Expected Output**: The payload appears in the page source without alteration.

### Step 3: Inject and Test the Payload

**Context**: Deliver the payload to the reflection point to trigger execution. Use curl for automated testing or a browser for manual verification.

**Command** ([[commands/curl-inject-svg-xss]]):

```bash
curl -G "http://target.com/search" --data-urlencode "q=<svg/onload=%26nbsp;alert`bohdan`+" -v
```

**Instructions**: Submit the payload via the vulnerable parameter (e.g., ?q= for search). Observe the response in a browser by visiting the crafted URL. If using Burp Suite, intercept and modify the request to fine-tune encoding.

**Expected Output**: The page loads with an alert box displaying 'bohdan' upon rendering the SVG element.

### Step 4: Verify and Escalate

**Context**: Confirm execution and assess for further impact, such as accessing localStorage or sending data to an attacker-controlled server.

**Instructions**: Check browser console for errors and network tab for any blocked requests. If successful, modify the payload to exfiltrate data, e.g., alert`document.domain` or fetch to an external endpoint.

**Expected Output**: No WAF blocks in Cloudflare logs; successful JS execution without errors.

**Success Indicators**:
- Alert box appears without Cloudflare challenge or block.
- Page source shows the injected SVG intact.
- No 403/429 errors from WAF.
