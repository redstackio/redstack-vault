---
id: proc-003
tags:
  - security-settings
  - account-access
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:48.242Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Account Security Settings

## Summary

After logging into the unauthorized account, this procedure navigates to the security settings to access 2FA configuration without additional verification.

## Description

The /account/security endpoint is reachable post-login, allowing modification of authentication settings on unverified accounts, which is the core flaw enabling the attack.

## Requirements

1. Valid login credentials from prior registration
2. Web browser session

## Defense

Defensive measures and detection strategies:

- Require email verification before accessing security features
- Implement session checks for sensitive endpoints

## Objectives

1. Reach security configuration page
2. View 2FA enablement options
3. Prepare for unauthorized 2FA setup

## Instructions

### Step 1: Login and Navigate to Account Section

**Context**: Use the new account credentials to log in, then proceed to security settings.

No command; click login, enter credentials, and navigate to https://www.xvideos.com/account/security.

> The page loads with editable security options, including 2FA, without prompting for email confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[navigation]]
- [[settings]]
