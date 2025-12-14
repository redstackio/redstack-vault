---
tags:
  - password-change
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
updated_at: '2025-12-14T17:30:58.976Z'
skill_level: low
impact_level: high
detection_risk: high
sub_techniques: []
id: 9a5c8418-c130-4842-90e8-463bf61e6d4a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Use One-Time Login to Change Password

## Summary

This procedure uses the one-time login link from the reset to access the account and update the password, achieving complete takeover.

## Description

The one-time link provides a temporary authenticated session in Phabricator, allowing direct navigation to settings for password modification. Once changed, the attacker locks out the victim, gaining persistent control. This finalizes the attack chain.

## Requirements

1. Received one-time login link
2. Access to Phabricator interface
3. New password ready

## Defense

Defensive measures and detection strategies:

- Expire one-time links quickly and single-use only
- Require 2FA post-reset login
- Notify on password changes via all emails

## Objectives

1. Log in via temporary link
2. Modify account credentials
3. Secure persistent access

## Instructions

### Step 1: Follow Login Link

**Context**: Activate the temporary session.

**Instructions**: Click the link in the email, which redirects to the Phabricator dashboard.

> Logged in without further auth.

### Step 2: Update Password

**Context**: Change to controlled credentials.

**Instructions**: Go to Settings > Password, enter new password, and save.

> Confirmation of update; original access revoked.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[takeover]]
- [[phabricator]]
