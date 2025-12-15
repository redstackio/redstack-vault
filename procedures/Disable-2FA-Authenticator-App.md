---
tags:
  - 2fa-disable
  - business-logic
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 871ab679-be36-43da-8c39-b0b78293cd59
created_at: '2025-12-14T17:24:45.455Z'
updated_at: '2025-12-14T17:24:45.455Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Disable-2FA-Authenticator-App

## Summary

This procedure deactivates the authenticator app 2FA on Legal Robot, triggering the flawed email notification.

## Description

Disabling 2FA requires verification via current code, then removes the method. The root cause lies in the backend logic that assumes U2F presence without checking enablement. Outcome: 2FA off, but notification misstates status.

## Requirements

1. Logged-in account with active 2FA
2. Access to authenticator app for verification code

## Defense

Defensive measures and detection strategies:

- Add confirmation dialogs for 2FA disable
- Log disable events with user IP/session data
- Validate all 2FA methods before sending notifications

## Objectives

1. Remove app-based 2FA
2. Initiate automated email flow
3. Expose logic error in notification

## Instructions

### Step 1: Access Disable Option

**Context**: Locate 2FA management.

Go to settings > security > 2FA. Select disable for authenticator app.

### Step 2: Verify and Disable

**Context**: Confirm removal.

Enter current app code and submit. Confirm 2FA is now off.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-disable]]
- [[business-logic]]
