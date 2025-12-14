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
updated_at: '2025-12-14T17:30:58.980Z'
skill_level: low
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5c150452-d0f3-4e96-8e90-dedd8f42f94c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Request Password Reset to New Email

## Summary

This procedure initiates a password reset using the validated attacker-controlled email, sending a one-time login link to enable unauthorized access.

## Description

Phabricator's password reset feature allows sending recovery links to any validated email. With the new email active, the attacker requests a reset, receiving the link directly. This exploits the trust in validated emails, leading to session generation without original credentials.

## Requirements

1. Validated email in the account
2. Access to Phabricator's auth/reset page
3. Control over the target email

## Defense

Defensive measures and detection strategies:

- Limit resets to primary emails only
- Require 2FA confirmation for reset requests
- Alert on resets to secondary emails

## Objectives

1. Generate one-time login link
2. Bypass credential requirements
3. Gain temporary access

## Instructions

### Step 1: Access Reset Form

**Context**: Start the recovery process.

**Instructions**: Navigate to Phabricator's password reset page (e.g., /auth/request/).

> Enter the target username or email.

### Step 2: Select New Email and Submit

**Context**: Direct link to controlled email.

**Instructions**: Choose the newly added email as the recovery address and submit.

> Link sent to controlled inbox.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[reset-abuse]]
- [[phabricator]]
