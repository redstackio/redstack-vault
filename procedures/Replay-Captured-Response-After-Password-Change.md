---
tags:
  - replay-attack
  - authentication-bypass
  - account-takeover
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Interceptor]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Forge Web Credentials]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:30.612Z'
sub_techniques: []
id: 265032cb-c7d8-4868-ba5a-03d78e1aab51
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Forge Web Credentials]]'
  - '[[Valid Accounts]]'
---
# Replay-Captured-Response-After-Password-Change

## Summary

This procedure exploits the vulnerability by attempting login with the old password post-victim password change and replaying the captured 2FA backup code response via proxy to bypass authentication and achieve account takeover.

## Description

After the victim changes their password, the old password fails, but the server does not invalidate prior 2FA responses. The attacker uses a proxy to submit the old password login, intercepts the failure response, and replaces it with the saved 2FA success response. This forges valid credentials. Target: Basecamp login endpoint; prerequisites: captured response and proxy. Outcome: Unauthorized access.

## Requirements

1. Saved HTTP response from 2FA success
2. HTTP proxy for interception and modification
3. Knowledge of timing for victim's password change

## Defense

Defensive measures and detection strategies:

- Invalidate all authentication artifacts on password reset
- Bind sessions to password versions or timestamps
- Monitor for response anomalies or proxy-like traffic patterns

## Objectives

1. Trigger password failure response
2. Replay 2FA response to forge success
3. Gain persistent account access

## Instructions

### Step 1: Attempt Login with Old Password

**Context**: Initiate the login to get the failure point.

**Instructions**: Configure proxy, go to sign-in page, submit email and old password.

> Expected output: Proxy shows failed response (e.g., 401 or error indicating invalid password).

### Step 2: Intercept and Replace Response

**Context**: Modify the response to mimic 2FA success.

**Instructions**: In proxy, drop the real failure response, load the saved 2FA response, and forward it to the browser (match headers like Set-Cookie, body).

> Expected output: Browser receives success, redirects to dashboard.

### Step 3: Verify Takeover

**Context**: Confirm control.

**Instructions**: Interact with dashboard, change settings if needed.

> Expected output: Full account functionality; old password no longer works for victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Forge Web Credentials]] Forge Web Credentials
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy-Interceptor]]

## Tags

- [[replay-attack]]
- [[authentication-bypass]]
- [[account-takeover]]
