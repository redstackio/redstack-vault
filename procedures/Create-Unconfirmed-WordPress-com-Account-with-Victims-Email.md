---
tags:
  - account-creation
  - wordpress-com
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
updated_at: '2025-12-14T17:31:42.764Z'
sub_techniques: []
id: 967ec42a-1b92-4a2f-b241-775bb1530501
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Unconfirmed-WordPress-com-Account-with-Victims-Email

## Summary

This procedure creates a WordPress.com account using the victim's email without verifying it, setting up for the invitation-based bypass.

## Description

The account is registered but left unconfirmed, allowing login with chosen credentials. Since the attacker doesn't control the email, normal verification can't occur, but the later invitation acceptance circumvents this. This step plants the fake account for hijacking.

## Requirements

1. Knowledge of victim's email
2. Web browser
3. No access to victim's email needed

## Defense

Defensive measures and detection strategies:

- Enforce email confirmation before any actions
- Detect registrations with unverified emails attempting logins
- Log suspicious account patterns

## Objectives

1. Register account with victim's email
2. Enable login without verification
3. Position for invite exploitation

## Instructions

### Step 1: Register Account

**Context**: Use victim's email for signup.

Go to wordpress.com/signup, input victim's email (e.g., victim@company.com), choose username and password, submit.

> Account created; confirmation email sent to victim (ignored by attacker).

### Step 2: Login Without Confirmation

**Context**: Access the account in unverified state.

Use the credentials to log in; note the unconfirmed status in settings.

> Dashboard accessible but with limitations until verified.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-creation
- wordpress-com
