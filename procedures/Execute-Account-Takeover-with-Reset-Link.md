---
id: proc-takeover-link-001
tags:
  - account-takeover
  - credential-abuse
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
updated_at: '2025-12-14T17:33:06.220Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Execute Account Takeover with Reset Link

## Summary

This procedure uses the intercepted password reset link to change the victim's RubyGems account password, achieving full unauthorized access.

## Description

The reset link bypasses normal authentication due to its token-based nature. Accessing it allows setting a new password, granting control over the account for actions like publishing gems or accessing private repositories. This completes the takeover chain started by the MITM interception. Expected outcome: Login with new credentials and account control.

## Requirements

1. Valid, unexpired reset link from interception
2. Web browser access to rubygems.org
3. Desired new password meeting RubyGems policy

## Defense

Defensive measures and detection strategies:

- Shorten reset token lifetimes (e.g., 15 minutes)
- Require additional verification (e.g., 2FA) on reset completion
- Alert on password changes from unusual IPs

## Objectives

1. Access the reset form via the link
2. Set a new password
3. Verify and maintain account access

## Instructions

### Step 1: Access Reset Link

**Context**: Navigate to the link to load the password change form.

No command required; paste the link into a browser.

> The page should show a form to enter a new password.

### Step 2: Change Password and Submit

**Context**: Update credentials to gain control.

No command required; enter new password twice and submit.

> Receive confirmation: "Your password has been changed successfully."

### Step 3: Login with New Credentials

**Context**: Validate takeover by accessing the account.

No command required; go to https://rubygems.org/sign_in and login.

> Successful dashboard access confirms control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[password-reset-abuse]]
