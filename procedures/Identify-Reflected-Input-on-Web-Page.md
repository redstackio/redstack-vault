---
id: proc-identify-reflected-input-xss
tags:
  - xss
  - recon
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:15:36.340Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify Reflected Input on Web Page

## Summary

This procedure involves testing web application inputs for reflection without sanitization, specifically targeting pages like payment settings to uncover potential reflected XSS vulnerabilities.

## Description

In the context of the Kartpay merchant portal, this step focuses on the https://merchant.kartpay.com/payment_settings endpoint. By fuzzing or manually testing parameters (e.g., form fields or query strings), attackers identify where user input is echoed back into the HTML response without proper output encoding. This sets the stage for XSS exploitation, allowing arbitrary code injection in authenticated sessions. Prerequisites include valid merchant login credentials and tools for HTTP request manipulation.

## Requirements

1. Authenticated access to the target web application (e.g., merchant portal login)
2. Browser with developer tools or HTTP client like curl
3. Knowledge of common input parameters (e.g., names, descriptions in payment settings)

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user inputs reflected in responses
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous requests with script tags via WAF logs

## Objectives

1. Locate unsanitized reflected parameters
2. Confirm lack of input validation
3. Prepare for payload injection

## Instructions

### Step 1: Access the Target Page

**Context**: Log in to the merchant portal and navigate to the payment_settings page to inspect available input fields.

No command required; use browser to load https://merchant.kartpay.com/payment_settings.

> Expected: Form fields or URL parameters visible for testing.

### Step 2: Test for Input Reflection

**Context**: Submit benign inputs to check if they appear unencoded in the page source.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl -X POST https://merchant.kartpay.com/payment_settings -d "param1=test123" -v
```

> This sends a POST request with a test parameter. Inspect the response body for 'test123' appearing raw, e.g., in an input value or text node without &quot; or &amp; encoding. Success: Reflection confirmed if input mirrors exactly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[web-recon]]
