---
id: proc-khan-intercept-burp
tags:
  - request-interception
  - http-manipulation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:24:18.866Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Email-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture, modify, and prepare the POST request to Khan Academy's /api/internal/graphql/requestAuthEmail endpoint for race condition exploitation by downgrading the HTTP version and adding a custom header.

## Description

The race condition arises from a time-of-check-to-time-of-use flaw where the email resource state is checked before sending but can change concurrently. Intercepting the request allows modification to HTTP/1.1 for better Turbo Intruder compatibility and adds a placeholder header. This targets the GraphQL mutation for requesting auth emails, typically sent once but exploitable for multiples.

## Requirements

1. Burp Suite Community Edition installed and running as a proxy
2. Browser configured to proxy traffic through Burp (e.g., 127.0.0.1:8080)
3. Valid session from prior login
4. Target email address ready (e.g., a controlled or test email)

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS-only and prevent HTTP/1.1 downgrades via HSTS
- Log and alert on unusual headers like 'X-Request'
- Implement request signing or idempotency keys to prevent replay

## Objectives

1. Capture the vulnerable GraphQL request
2. Modify protocol and headers for exploitation tool compatibility
3. Forward the prepared request without triggering errors

## Instructions

### Step 1: Trigger the Request

**Context**: Initiate the email send action to generate the interceptable request.

Enter a valid email address in the form and click 'Send confirmation email'.

> Burp Suite intercepts the POST to /api/internal/graphql/requestAuthEmail. Expected output: Raw HTTP request visible in Proxy > Intercept tab.

### Step 2: Modify the Request

**Context**: Adjust the request to enable concurrent sending in Turbo Intruder.

In Burp, change the HTTP version to 1.1 and add header 'X-Request: %s'.

> Expected output: Modified request body includes GraphQL mutation for email auth, with JSON payload like {"query": "mutation..."}.

### Step 3: Forward to Turbo Intruder

**Context**: Prepare for concurrent execution.

Right-click the intercepted request and select 'Send to Turbo Intruder'.

> Expected output: Request loaded in Turbo Intruder interface, ready for scripting.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-interception
- http-manipulation
