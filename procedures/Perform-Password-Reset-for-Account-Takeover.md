---
tags:
  - password-reset
  - account-takeover
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
updated_at: '2025-12-14T17:33:12.346Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 0f69b77f-7273-4256-a6a1-e6ead01d94fc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Perform-Password-Reset-for-Account-Takeover

## Summary

This procedure exploits the modified victim profile to trigger a password reset, receiving the link on the attacker's email, and resetting credentials to achieve full unauthorized access to the victim's account.

## Description

Following the IDOR-induced profile change, the 'username' (email) now points to the attacker for resets. Initiating a forgot-password flow sends the link to the attacker, who can then set a new password. This completes the takeover chain without any victim-side interaction, potentially allowing data access or further abuse.

## Requirements

1. Successful profile modification from prior step
2. Access to attacker's email inbox
3. Victim's username for reset initiation

## Defense

Defensive measures and detection strategies:

- Send password reset notifications to original email and require secondary verification (e.g., SMS)
- Log and alert on profile email changes, requiring user confirmation
- Implement time-bound reset tokens with IP/session checks

## Objectives

1. Initiate password reset for victim account
2. Receive and use reset link
3. Gain login access with new credentials

## Instructions

### Step 1: Initiate Reset

**Context**: Start the recovery process using victim's details.

On the login page of mtnmobad.mtnbusiness.com.ng, enter the victim's username and request password reset.

### Step 2: Receive Reset Email

**Context**: Confirm redirection to attacker.

Check the attacker's email for the reset link; it should arrive promptly.

### Step 3: Reset Password

**Context**: Change credentials securely.

Click the link, enter a new password, and submit.

### Step 4: Log In to Victim Account

**Context**: Validate takeover.

Use the victim's username with the new password to log in and access the account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[account-takeover]]
