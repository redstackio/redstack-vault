---
id: proc-gratipay-password-reset
tags:
  - account-takeover
  - password-reset
  - gratipay
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
updated_at: '2025-12-14T17:32:57.821Z'
skill_level: basic
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Perform-Password-Reset-for-Takeover

## Summary

This procedure leverages the controlled primary email to initiate and complete a password reset on the victim's account, achieving full takeover.

## Description

With the victim's email added and verified as primary on the attacker's account, the forgot-password feature sends reset links to it. Controlling the inbox allows the attacker to reset credentials, gaining unauthorized access to payments and data.

## Requirements

1. Verified primary email control
2. Victim's email address
3. Access to reset link delivery

## Defense

Defensive measures and detection strategies:

- Send reset notifications to secondary channels (e.g., SMS)
- Require additional verification for resets
- Monitor for rapid email additions followed by resets

## Objectives

1. Trigger password reset flow
2. Intercept and use reset link
3. Gain full account control

## Instructions

### Step 1: Initiate Reset

**Context**: Start the recovery process.

On the Gratipay login page, use the 'forgot password' link and enter the victim's email.

### Step 2: Receive Reset Email

**Context**: Access the reset mechanism.

Check the controlled email for the reset link.

### Step 3: Complete Reset

**Context**: Change credentials for takeover.

Click the link and set a new password, then log in as the victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Default Accounts]] Default Accounts

## Commands Used


## Tools Used


## Tags

- ato
- reset
