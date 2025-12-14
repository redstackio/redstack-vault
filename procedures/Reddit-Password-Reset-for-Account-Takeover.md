---
tags:
  - password-reset
  - account-takeover
  - reddit
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:06.303Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 71430701-7e76-4469-858c-bc3c098737a6
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Reddit-Password-Reset-for-Account-Takeover

## Summary

This procedure abuses Reddit's password reset mechanism, combined with email control and enumerated usernames, to hijack a victim's account by resetting their password.

## Description

Using the victim's username from enumeration, the attacker requests a password reset, which sends a link to the shared email. The attacker then uses the link to set a new password, gaining full access to the account's private information, chats, and settings. The target is the password reset endpoint, assuming email control from prior steps. Outcomes include complete account compromise without knowing the original password.

## Requirements

1. Enumerated victim username
2. Control over the associated email
3. Web browser

## Defense

Defensive measures and detection strategies:

- Require additional verification (e.g., 2FA, security questions) for resets
- Invalidate old sessions and notify users on reset attempts
- Rate limit reset requests per username/email
- Audit logs for resets on multi-account emails

## Objectives

1. Trigger reset for the specific victim account
2. Intercept and use the reset token
3. Achieve persistent access to victim data

## Instructions

### Step 1: Submit Reset Request

**Context**: Initiate the reset using known details.

**Action**:
Navigate to `https://www.reddit.com/password`, enter username `user1` and email `account@gmail.com`, submit.

> Request accepted; reset email sent.

### Step 2: Retrieve Reset Link

**Context**: Access the recovery mechanism.

**Action**:
Check inbox for the password reset email from Reddit.

> Contains a clickable link or temporary password.

### Step 3: Complete Reset and Takeover

**Context**: Change the password to gain control.

**Action**:
Click the link, enter a new attacker-controlled password, confirm, then log in with new credentials.

> Password updated; full access to account, including private messages and settings.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- password-reset
- account-takeover
- reddit
