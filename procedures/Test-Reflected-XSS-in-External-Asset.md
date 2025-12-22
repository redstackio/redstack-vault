---
tags:
  - xss
  - reflected-xss
  - input-testing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-xss-payload-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.683Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 60f52e2a-29ce-4d7d-8e84-1f368e0a7b03
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-Reflected-XSS-in-External-Asset

## Summary

This procedure tests for reflected Cross-Site Scripting (XSS) vulnerabilities in an external fraud detection asset by injecting malicious payloads into input parameters and observing if they are reflected unsanitized, allowing JavaScript execution in the user's browser.

## Description

In the context of secure.chaturbate.com, the external asset used for fraud detection fails to sanitize input parameters, enabling attackers to inject scripts via URL parameters or form inputs. This can lead to executing arbitrary code in the victim's browser, such as stealing session tokens or redirecting to phishing sites. The procedure involves manual or automated testing of parameters to confirm reflection and execution, typically in a web environment over HTTPS.

## Requirements

1. Access to a web browser with developer tools enabled
2. Network connectivity to secure.chaturbate.com (port 443)
3. Optional: HTTP proxy like Burp Suite for intercepting and modifying requests
4. Basic knowledge of HTML and JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HTML entity encoding) on all user inputs
- Use Content Security Policy (CSP) headers to restrict script execution
- Monitor for anomalous script tags in web traffic using WAF rules
- Regularly scan external assets for XSS vulnerabilities with tools like OWASP ZAP

## Objectives

1. Confirm unsanitized reflection of inputs in the external asset
2. Demonstrate script execution to assess impact like session hijacking
3. Validate the vulnerability for reporting or exploitation

## Instructions

### Step 1: Identify Target Parameters

**Context**: Locate input parameters in the external fraud detection asset by inspecting network requests during site interactions, such as login or transaction flows on secure.chaturbate.com.

Use browser dev tools to monitor requests and note parameters like 'token' or 'user_id' that are reflected in responses.

### Step 2: Inject Test Payload

**Context**: Craft and send a simple XSS payload to test for reflection and execution.

Execute [[commands/curl-xss-payload-test]] to send a GET request with the payload:

```bash
curl -X GET "https://secure.chaturbate.com/external-asset?param=<script>alert('XSS')</script>" -v
```

> This command sends a request to the external asset endpoint with an unsanitized script tag in the 'param' query string. The -v flag provides verbose output to inspect the response headers and body for payload reflection.

If using a browser, append the payload directly to the URL and load the page.

### Step 3: Verify Execution

**Context**: Check the response and browser behavior to confirm the vulnerability.

Inspect the HTML response for the raw payload. In a browser, look for the alert dialog or use console.log in the payload for logging.

**Expected Output**: The script tag appears unescaped in the page source, and JavaScript executes (e.g., alert pops up).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-payload-test]]

## Tools Used


## Tags

- xss
- web-testing
- vulnerability-discovery
