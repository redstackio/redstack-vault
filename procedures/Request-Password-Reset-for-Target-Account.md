---
tags:
  - password-reset
  - initial-access
type: procedure
tools:
  - '[[tools/pre_auth_nosqli.py]]'
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
updated_at: '2025-12-14T17:31:30.574Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: bb7b7aee-be5e-4270-a1cd-c5d1a28d416b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Request-Password-Reset-for-Target-Account

## Summary

This procedure initiates a password reset for a target user in Rocket.Chat, generating a reset token in the MongoDB database that can be targeted for extraction via injection.

## Description

In the context of exploiting Rocket.Chat, send a password reset request using the target's email via the API. This stores a temporary reset token in the database, setting up for blind injection to leak it. The endpoint is public, requiring no auth, and works on vulnerable versions like 3.12.1. Expected outcome is a token generation without alerting the user if email delivery is intercepted or ignored.

## Requirements

1. Network access to Rocket.Chat API (port 3000)
2. Target email address (e.g., admin@rocketchat.local)
3. Python with requests library installed

## Defense

Defensive measures and detection strategies:

- Enable email notifications for resets to alert users
- Rate-limit reset requests per IP/email
- Monitor API logs for anomalous reset patterns

## Objectives

1. Generate database-stored reset token
2. Prepare for token extraction
3. Enable account takeover path

## Instructions

### Step 1: Send Reset Request

**Context**: Use the API or script to request reset, triggering token creation.

**Command** ([[commands/run-exploit-script]]):
```bash
python3 pre_auth_nosqli.py 'http://localhost:3000' 'admin@rocketchat.local' --reset-request
```

> This sends a POST to the forgotPassword endpoint, generating the token. Expected output: API response {"success": true}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/pre_auth_nosqli.py]]

## Tags

- password-reset
- initial-access
