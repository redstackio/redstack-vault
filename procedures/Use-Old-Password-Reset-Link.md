---
tags:
  - token-reuse
  - bypass
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
updated_at: '2025-12-14T17:31:11.411Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 8e58416b-ff05-4b96-bb26-2069a493bfe3
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Use-Old-Password-Reset-Link

## Summary

This procedure attempts to access a previously generated password reset link after an email change, exploiting the token's unexpected persistence.

## Description

The scenario tests the core vulnerability: reset tokens tied to old emails remain valid. Target is the reset endpoint. Requires the saved link and logout state. Outcome: Access to reset form without new email control, leading to takeover potential.

## Requirements

1. Saved reset link from original email
2. Logged-out state
3. Web browser

## Defense

Defensive measures and detection strategies:

- Expire tokens on email updates or after fixed time
- Validate token against current user email
- Monitor for token usage post-account changes

## Objectives

1. Load reset form with old token
2. Confirm no invalidation occurred
3. Proceed to password update

## Instructions

### Step 1: Log Out

**Context**: Clear any active session to simulate external access.

Click logout from the dashboard.

> Return to login page.

### Step 2: Access Old Link

**Context**: Use the persisted token to reach the reset page.

Paste and navigate to the saved reset URL (e.g., https://secret.app/reset?token=abc123).

> Page loads without 'invalid token' error, prompting for new password.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-reuse]]
- [[bypass]]
