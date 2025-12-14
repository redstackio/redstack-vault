---
tags:
  - account-takeover
  - password-reset
type: procedure
tools:
  - '[[tools/Firefox-Multi-Account-Containers]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-validate-reset]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:25:23.464Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 81652f99-94c3-43c2-9097-d0fb255956a0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Validate-Recovery-Email-and-Reset-Password

## Summary

This procedure validates the recovery email using the reset link and sets a new password to achieve full account takeover.

## Description

Using the link from the reset email (e.g., /self?guid=...), confirm the recovery addition and update the password. Any valid session can be used, granting attacker login as victim.

## Requirements

1. Reset link from prior step
2. New password choice
3. Valid session for confirmation

## Defense

Defensive measures and detection strategies:

- Expire reset links quickly and require CAPTCHA
- Log IP changes during resets
- Alert on password changes from new IPs

## Objectives

1. Confirm recovery email control
2. Set attacker-controlled password
3. Gain persistent access to victim account

## Instructions

### Step 1: Access Confirmation Link

**Context**: Open the guid-based link to validate recovery.

Navigate to /self?guid=reset_guid in browser.

### Step 2: Set New Password

**Context**: Update password and login.

Execute [[commands/curl-validate-reset]] if form-based:

```bash
curl -X POST https://target-site.com/self \
  -H "Cookie: session=valid_session" \
  -d "guid=reset_guid&newPassword=attacker_new_pass&confirmPassword=attacker_new_pass" \
  -v
```

> Follow with login using new credentials.

**Expected Output**: Password updated; successful login as victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used

- [[commands/curl-validate-reset]]

## Tools Used

- [[tools/Firefox-Multi-Account-Containers]]

## Tags

- account-takeover
- password-reset
