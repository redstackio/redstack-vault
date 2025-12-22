---
tags:
  - password-reset
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.142Z'
sub_techniques: []
id: b4b8d47c-07e8-45af-b1bb-df9b77c1b845
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Trigger-Password-Reset-for-Victim

## Summary

This procedure abuses the forgot password functionality to generate and email a new password to the now-attacker-controlled email address.

## Description

After email update, the attacker visits the forgot password form, enters the victim's username, and submits. The app generates a new password and sends it to the updated email without verification. Target: Web app's reset endpoint. Outcome: New password en route to attacker.

## Requirements

1. Victim's username known
2. Updated email in place from prior step
3. Access to reset page

## Defense

Defensive measures and detection strategies:

- Send reset links, not passwords
- Require email/SMS confirmation for resets
- Rate-limit reset requests per username

## Objectives

1. Generate new password
2. Route it to controlled email
3. Gain login credentials

## Instructions

### Step 1: Access Forgot Password Page

**Context**: Navigate to the reset form.

Visit the forgot password URL on the target site.

> Form loads for username input.

### Step 2: Submit Reset Request

**Context**: Enter username and trigger email.

Input victim's username and submit.

> App processes and emails new password.

### Step 3: Note Generation Time

**Context**: Wait for email delivery.

Monitor for immediate or delayed send.

> Password generated successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[auth-bypass]]
