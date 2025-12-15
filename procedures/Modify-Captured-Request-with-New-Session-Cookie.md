---
tags:
  - request-modification
  - csrf-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-modified-deletion-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.427Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c6ad2f97-3bde-4f97-abaa-d056720e5213
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify Captured Request with New Session Cookie

## Summary

This procedure modifies the intercepted account deletion request by swapping the session cookie to the victim's while keeping the attacker's CSRF token, enabling the bypass.

## Description

Using Burp Suite's Repeater, update the `_gitlab_session` header in the captured POST `/users` request with the second account's cookie. The token remains valid due to lack of reset in Warden during email confirmation, allowing cross-session reuse.

## Requirements

1. Captured request from first procedure
2. New session cookie from second account
3. Burp Suite Repeater tab

## Defense

Defensive measures and detection strategies:

- Bind CSRF tokens to specific sessions/cookies
- Validate token-session pairing on state-changing requests
- Anomaly detection on cookie-token mismatches

## Objectives

1. Replace session cookie in request
2. Preserve authenticity_token
3. Prepare replayable request for deletion

## Instructions

### Step 1: Load in Repeater

**Context**: Import the intercepted request into Burp Repeater.

In Burp, right-click the captured POST and select "Send to Repeater".

### Step 2: Update Cookie and Forward

**Context**: Modify headers to use victim cookie, then test forward.

Edit the Cookie header to `_gitlab_session=new_victim_cookie;`. Keep body unchanged.

**Command** ([[commands/curl-modified-deletion-request]]):
```bash
curl -X POST https://gitlab.com/users \
  -H "Cookie: _gitlab_session=568a0c6e266c55938182945af357dda4;" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "_method=delete&authenticity_token=a57BV%2BO0KhEtRe%2FS9W2%2FIBqZj2bWA8jbfE38VlA4pzN1wBKov8F4UV7gYerBaLOumjqpnIoC2Dsx1jufaAZGsg%3D%3D"
```

> Expected output: 200 OK or redirect on successful prep; no auth error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-modified-deletion-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-forgery
- token-reuse
