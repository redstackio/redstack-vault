---
tags:
  - account-verification
  - login
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6e70f29e-03fe-4835-af19-bb3afee4f4b2
created_at: '2025-12-13T09:01:26.720Z'
updated_at: '2025-12-13T09:01:26.720Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify Email and Login

## Summary

This procedure involves verifying the email for the newly created account and logging in as the attacker to gain initial access.

## Description

After bypassing signup, the verification email is sent to the victim, who clicks the link, activating the account. The attacker then logs in using the set password, establishing persistence.

## Requirements

1. Access to the verification email
2. Knowledge of the chosen password
3. Web browser for login

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected account creations with restricted domains
- Implement rate limiting on verification emails

## Objectives

1. Activate the unauthorized account
2. Establish login access
3. Prepare for further exploitation

## Instructions

### Step 1: Verify the Email

**Context**: As the victim, confirm the account via email.

Click the confirmation link in the email sent by HackerOne.

> This activates the account.

### Step 2: Log in to the Account

**Context**: As the attacker, access the account.

Navigate to the login page and enter the username and password.

> Successful login grants dashboard access.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- account-verification
- login
