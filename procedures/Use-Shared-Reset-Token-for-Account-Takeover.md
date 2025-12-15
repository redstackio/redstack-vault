---
id: proc-upchieve-takeover-001
tags:
  - account-takeover
  - reset-token
  - email-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.389Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Use-Shared-Reset-Token-for-Account-Takeover

## Summary

This procedure leverages the shared password reset token received in the attacker's email to access and reset the victim's account credentials, achieving full unauthorized access without victim interaction.

## Description

After the modified request, the UPchieve backend sends the same reset token to all emails in the array. The attacker uses this token to load the reset form for the victim's account and sets a new password. This targets web applications with email-based resets in environments using SMTP services, assuming the token is valid for a short window. No additional tools are needed beyond email access.

## Requirements

1. Shared reset token received in attacker's email
2. Valid reset link from the email
3. Web browser for accessing the link
4. Desired new password for the takeover

## Defense

Defensive measures and detection strategies:

- Generate unique tokens per email request
- Expire tokens quickly and invalidate on first use
- Monitor for multiple token deliveries from single requests
- Alert on successful resets from unusual IPs

## Objectives

1. Access the victim's reset form using the intercepted token
2. Change the account password
3. Gain persistent access to the account

## Instructions

### Step 1: Check Emails for Reset Links

**Context**: Confirm receipt of the identical reset emails in both inboxes.

Monitor inboxes; the links will be the same, e.g., https://app.upchieve.org/reset?token=abc123.

> Victim may not check email immediately, giving a window.

### Step 2: Click the Reset Link

**Context**: Use the link to authenticate to the reset process for the victim's account.

Open the link in a browser from the attacker's email.

> This bypasses email ownership verification.

### Step 3: Enter and Submit New Password

**Context**: Complete the reset to control the account.

Input a new password (e.g., newpass123) and confirm; submit the form.

> Success message confirms the change.

### Step 4: Verify Takeover

**Context**: Test access to ensure control.

Log in to https://app.upchieve.org with victim's email and new password.

> Full account functionality available.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[reset-token]]
- [[email-injection]]
