---
tags:
  - email-change
  - account-modification
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
updated_at: '2025-12-14T17:31:19.249Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d355f274-90fd-4013-b365-1a43917c26d1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Change-Account-Email

## Summary

This procedure updates the email address associated with a HackerOne account, exploiting the fact that prior reset tokens remain valid.

## Description

After logging in, the user navigates to settings to change the email from a@x.com to b@x.com and verifies it. The vulnerability lies in the system not revoking existing reset tokens, allowing later reuse. This web-based action requires control over both emails and results in an updated account profile.

## Requirements

1. Valid login credentials
2. Access to new email (b@x.com) for verification
3. Active session

## Defense

Defensive measures and detection strategies:

- Invalidate all pending tokens upon email change
- Require re-authentication for sensitive changes
- Monitor for email changes followed by resets

## Objectives

1. Shift primary contact to new email
2. Trigger verification without affecting old tokens
3. Enable token reuse vulnerability

## Instructions

### Step 1: Log In

**Context**: Regain access to perform the change.

**Instructions**: Enter original credentials on the login page to access the dashboard.

> Successful login grants session access.

### Step 2: Update Email

**Context**: Modify the account settings.

**Instructions**: Go to account settings, enter b@x.com as the new email, save, and check b@x.com for the verification link. Click to confirm.

> Account email updates to b@x.com upon verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-change]]
- [[account-modification]]
