---
id: proc-intercept-modify-search-burp
tags:
  - xss
  - reflected-xss
  - waf-bypass
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:26.557Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Intercept-and-Modify-Search-Request-with-Burp-Suite

## Summary

This procedure exploits a reflected XSS vulnerability in a web search form by using Burp Suite to intercept, modify the POST keyword parameter with an encoded JavaScript payload, and forward the request to trigger execution in the victim's browser, bypassing WAF protections.

## Description

The target application at www.█████ reflects user input from the POST 'keyword' parameter directly into the search results page without sanitization. By intercepting the request with Burp Suite, an attacker can inject a payload like `<a+href="ja%0A%0Dvascript:alert(document.domain)">Click</a>`, where %0A%0D encodes newlines to construct a valid javascript: URI in the href attribute, evading WAF rules that block direct 'javascript:' strings. Upon submission and clicking the reflected link, arbitrary JavaScript executes, enabling cookie theft, page modification for phishing, or other client-side attacks. This targets public-facing web applications vulnerable to input reflection.

## Requirements

1. Burp Suite installed and running with proxy interception enabled
2. Network access to the target website (www.█████) via browser configured to route through Burp proxy
3. Basic knowledge of HTTP requests and URL encoding

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and output encoding for all user inputs, especially reflected parameters like search keywords
- Configure WAF to detect and block encoded javascript: URIs, including newline injections (%0A%0D or %0D%0A)
- Monitor for anomalous JavaScript execution in client-side logs or use Content Security Policy (CSP) to restrict inline scripts and unsafe-inline

## Objectives

1. Intercept and tamper with search form POST requests to inject XSS payloads
2. Bypass WAF using encoding techniques to reflect executable JavaScript
3. Demonstrate impact through alert execution, extensible to session hijacking or data exfiltration

## Instructions

### Step 1: Configure and Intercept Request

**Context**: Set up Burp Suite to capture traffic from the target search form.

Configure your browser to use Burp Suite as a proxy (typically localhost:8080). Navigate to www.█████, enter a benign search term (e.g., 'test'), and submit the form. Burp Suite will intercept the POST request.

**Expected Output**: Paused request in Burp's Proxy > Intercept tab, displaying POST /search endpoint with Content-Type: application/x-www-form-urlencoded and keyword=test in the body.

### Step 2: Modify with Malicious Payload

**Context**: Replace the keyword parameter to inject the XSS payload that bypasses WAF.

In the intercepted request, edit the body to change keyword=test to keyword=<a+href="ja%0A%0Dvascript:alert(document.domain)">Click</a>. The %0A%0D inserts newlines after 'ja' to form 'javascript:alert(document.domain)' upon reflection.

**Expected Output**: Updated request body with the encoded payload; no validation errors in Burp.

### Step 3: Forward and Verify Execution

**Context**: Submit the tampered request and interact with the response to confirm XSS.

Click 'Forward' in Burp to send the request. Inspect the response HTML for the reflected anchor tag. Click the 'Click' link in the rendered page.

**Expected Output**: Browser alert box showing the document domain (e.g., 'www.█████'); console may log the execution without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[reflected-xss]]
- [[waf-bypass]]
