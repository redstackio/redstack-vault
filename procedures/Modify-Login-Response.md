---
tags:
  - response-modification
  - auth-bypass
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e58fc9b2-3ed4-4805-bd7b-14cde05a4bba
created_at: '2025-12-14T17:33:11.947Z'
updated_at: '2025-12-14T17:33:11.947Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Modify-Login-Response

## Summary

This procedure alters the HTTP response from the login endpoint to simulate successful authentication, exploiting lack of server-side validation to bypass credential checks.

## Description

By modifying the intercepted response from the login endpoint (e.g., /login on Mars website), an attacker can change status codes, body content, and headers to mimic a valid login. This works due to client-side reliance on server responses without integrity verification. The attack targets web applications and results in an authenticated session without valid credentials, paving the way for account takeover.

## Requirements

1. Intercepted login request from prior procedure
2. Proxy tool active for response editing
3. Knowledge of expected success response format (e.g., via prior testing)

## Defense

Defensive measures and detection strategies:

- Enforce server-side session validation and response signing
- Log and alert on mismatched request-response pairs
- Deploy WAF rules to detect proxy-like modifications

## Objectives

1. Fake successful authentication state
2. Establish client-side session belief in valid login
3. Avoid triggering additional auth flows

## Instructions

### Step 1: Intercept Response

**Context**: After forwarding the request, capture the server's failure response.

In Burp Suite, the response will pause; inspect it (e.g., 401 status, error JSON).

> Note original body (e.g., {"success": false}) and headers.

### Step 2: Edit Response Details

**Context**: Change elements to indicate success.

Set status to 200 OK, modify body to {"success": true, "user_id": "fake"}, and add auth headers if present.

> Ensure JSON is valid to avoid client parsing errors.

### Step 3: Forward Modified Response

**Context**: Release the altered response to the client.

Forward to browser; the application will treat it as a successful login.

> Expected: User redirected to dashboard or session established.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[response-modification]]
- [[auth-bypass]]
- [[web]]
