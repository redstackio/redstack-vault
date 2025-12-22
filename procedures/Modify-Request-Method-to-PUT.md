---
tags:
  - method-tampering
  - http-modify
  - bypass
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.271Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 2d949bc6-002c-4e98-b152-d2f899101a98
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Request-Method-to-PUT

## Summary

Change the HTTP method of the intercepted POST request to PUT to exploit the lack of method-specific validation, allowing CAPTCHA token reuse.

## Description

The backend flaw treats PUT requests (intended for updates) as creations without re-verifying CAPTCHA, unlike POST. By altering the method while preserving the payload, the server checks only the HTTP 200 status from Google's API (which is always returned, even for invalid tokens) instead of the body. This business logic error in the PHP/WordPress API enables bypass.

## Requirements

1. Intercepted POST request in proxy
2. Proxy tool with request editing capabilities
3. Original token still valid (short-lived, act quickly)

## Defense

Defensive measures and detection strategies:

- Validate HTTP methods strictly on endpoints (e.g., POST only for creates)
- Parse reCAPTCHA response body for 'success': true
- Implement idempotency checks to prevent reuse

## Objectives

1. Tamper method to trigger bypass
2. Confirm acceptance without new CAPTCHA
3. Create unauthorized entry

## Instructions

### Step 1: Edit Request in Proxy

**Context**: Modify the method while keeping payload intact.

In Burp's Intercept tab, change 'POST' to 'PUT' in the request line.

Ensure body remains the same: form data with g-recaptcha-response.

> Expected output: Modified request ready for forwarding.

### Step 2: Forward and Observe Response

**Context**: Send to server and check acceptance.

Click Forward in proxy.

> Expected output: 200 OK response; new request in dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy-Burp-Suite]]

## Tags

- [[method-tampering]]
- [[bypass]]
