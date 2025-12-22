---
id: proc-uuid-3
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
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:58.022Z'
skill_level: low
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Password-Reset-Using-Attackers-Email

## Summary

This procedure completes the account takeover by using the previously added unverified email to initiate and complete a password reset, granting the attacker full control of the victim's Vimeo account in under a minute.

## Description

Once the attacker's email is added, the reset process treats it as a valid recovery option. The attacker initiates the reset using the victim's username, receives the link via their controlled email, and sets a new password. This exploits the lack of verification in the prior step, targeting web-based recovery flows. Expected outcomes include exclusive access to all account features, such as video uploads and settings.

## Requirements

1. Attacker's email successfully added to victim's account
2. Access to Vimeo's password reset page
3. Victim's username or original email for reset initiation

## Defense

Defensive measures and detection strategies:

- Limit password resets to verified primary emails only
- Require MFA for reset confirmations
- Alert users to suspicious reset attempts via multiple channels

## Objectives

1. Trigger password reset email to attacker's inbox
2. Change the account password to attacker-controlled value
3. Achieve persistent access to the compromised account

## Instructions

### Step 1: Initiate Password Reset

**Context**: Start the recovery process to route the link to the added email.

Go to Vimeo's login page, click 'Forgot Password?', and enter the victim's username or primary email.

> The system sends the reset link to all associated emails, including the attacker's unverified one.

### Step 2: Complete Reset with Attacker's Email

**Context**: Use the received link to set a new password.

Check the attacker's email inbox for the reset link, click it, and enter a new strong password (e.g., NewPass123!).

> Account is now controllable by the attacker; login succeeds with the new credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[account-takeover]]
