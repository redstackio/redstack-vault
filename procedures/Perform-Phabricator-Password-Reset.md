---
id: password-reset-uuid
name: Perform-Phabricator-Password-Reset
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.828Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Account Manipulation]]'
sub_techniques: []
tags:
  - password-reset
  - account-takeover
  - phabricator
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---

# Perform-Phabricator-Password-Reset

## Summary

This procedure uses the injected email to initiate and complete a password reset in Phabricator, resulting in full account takeover.

## Description

After email injection, the attacker can request a reset link sent to their controlled email. Phabricator's reset flow allows setting a new password without further checks. Target: Login/reset page. Prerequisites: Injected email confirmed in account.

## Requirements

1. Access to the injected email inbox
2. Victim's username for reset request
3. No additional auth barriers

## Defense

Defensive measures and detection strategies:

- Limit password resets to verified emails only
- Require secondary verification (e.g., security questions)
- Alert on reset attempts from new IPs

## Objectives

1. Receive reset token via email
2. Set new password
3. Achieve persistent access

## Instructions

### Step 1: Initiate Reset

**Context**: Start the reset process.

Visit the login page and click 'Forgot Password', enter victim's username.

> Expected output: Reset request submitted.

### Step 2: Receive and Use Link

**Context**: Access the reset email.

Check attacker's email for the reset link and click it.

> Expected output: Password change form loads.

### Step 3: Set New Password

**Context**: Complete takeover.

Enter new password and submit.

> Expected output: Confirmation, login with new creds succeeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques

None

## Commands Used

None

## Tools Used

None

## Tags

- [[password-reset]]
- [[account-takeover]]
- [[phabricator]]
