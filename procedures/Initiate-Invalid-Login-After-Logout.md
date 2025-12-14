---
id: proc-wakatime-invalid-login
tags:
  - logout
  - failed-auth
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.999Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate Invalid Login After Logout

## Summary

This procedure logs out a valid session and attempts an invalid login to trigger an error response, which is intercepted for modification in a replay attack, exploiting the lack of token invalidation in WakaTime.

## Description

After capturing a valid session, the attacker logs out to invalidate the current session context, then submits incorrect credentials to hit the login endpoint. Normally, this returns 400 or 429 due to rate limits, but interception allows replacement with valid data. The environment involves nginx/HTTP/2 backend, where sessions persist indefinitely without revocation.

## Requirements

1. Active Burp Suite proxy with interception enabled
2. Captured valid session from prior step
3. Access to WakaTime logout endpoint
4. Incorrect password for the target account

## Defense

Defensive measures and detection strategies:

- Enforce strict rate limiting tied to IP/session
- Bind sessions to specific user contexts and revoke on logout
- Log and alert on rapid login failures followed by successes

## Objectives

1. Create an interceptable failed response
2. Trigger potential rate limit for bypass demonstration
3. Prepare for session replay

## Instructions

### Step 1: Execute Logout

**Context**: Invalidate the current session to simulate post-logout replay.

Send a request to the logout endpoint (e.g., POST /logout or GET /logout).

> Response: 302 redirect to login or success message. Confirm session cookies are cleared in subsequent requests.

### Step 2: Submit Invalid Login Request

**Context**: Generate a failed auth attempt to intercept the error response.

Use Burp to send POST to /login with wrong password, intercepting the response.

> Request: email=valid@example.com&password=wrong. Expected response: 400 Bad Request or 429 Too Many Requests.

### Step 3: Intercept and Hold Response

**Context**: Pause before forwarding to allow modification.

In Burp Intercept, hold the invalid response.

> Verify headers show no valid session; body indicates auth failure.

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

- logout
- failed-auth
