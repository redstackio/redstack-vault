---
id: hijack-password-reset-takeover
tags:
  - password-reset
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.528Z'
skill_level: low
impact_level: critical
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Hijack Password Reset for Takeover

## Summary

This procedure uses the hijacked email to initiate and complete IRCCloud's password reset process, allowing the attacker to set a new password and gain full control of the victim's account.

## Description

With the email confirmed, the attacker requests a password reset using the victim's username or original email. The reset link arrives in the attacker's inbox, which they follow to change the password. This leads to complete account compromise, including access to IRC sessions, messages, and settings. The logic flaw enables this because email changes are usable for resets pre-full confirmation in some flows.

## Requirements

1. Confirmed control over the account's email
2. Knowledge of victim's username (from phishing or public info)
3. Access to IRCCloud reset endpoint

## Defense

Defensive measures and detection strategies:

- Require additional auth (e.g., 2FA) for password resets
- Invalidate sessions on email changes
- Send notifications to original email for resets
- Monitor for rapid successive changes (email then password)

## Objectives

1. Request and intercept password reset token
2. Change password to attacker-controlled value
3. Achieve persistent access to the account

## Instructions

### Step 1: Initiate Password Reset

**Context**: Start the reset flow using the compromised email.

**Instructions**: Visit https://www.irccloud.com/reset-password, enter victim's username, submit request.

**Expected Output**: Reset email sent to attacker's inbox with temporary link.

### Step 2: Complete Reset

**Context**: Use the link to set new password.

**Instructions**: Click link in email, enter new password (e.g., attackerpass123), confirm.

**Expected Output**: Password updated; login successful with new credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access
- [[Impact]] Impact

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[account-takeover]]
