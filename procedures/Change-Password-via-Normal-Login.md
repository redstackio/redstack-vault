---
id: proc-002
tags:
  - broken-authentication
  - password-change
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
updated_at: '2025-12-14T17:31:52.111Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
---

# Change-Password-via-Normal-Login

## Summary

This procedure logs into the Courier account using standard credentials and changes the password through account settings, testing if this action invalidates prior reset tokens.

## Description

Targeting https://www.trycourier.app, this step uses a separate browser session to log in normally after requesting a reset token. The password is updated via the settings page, which should ideally invalidate any pending reset tokens for security. However, in this vulnerability, it does not. This simulates a legitimate user action that an attacker exploits later. Prerequisites: Existing credentials and the prior reset token unused. Outcome: Password changed, but old token remains valid.

## Requirements

1. Valid login credentials for the account
2. New browser tab or incognito mode to avoid session conflicts
3. Access to account settings post-login

## Defense

Defensive measures and detection strategies:

- Automatically expire or invalidate reset tokens on any password modification
- Log password changes and cross-reference with recent reset requests
- Enforce single-session policy or token binding to sessions

## Objectives

1. Perform a standard password update via logged-in session
2. Verify session integrity post-change
3. Highlight failure to invalidate pending tokens

## Instructions

### Step 1: Log In Normally

**Context**: Establish a fresh session without using the reset flow.

Open a new browser tab or incognito window. Navigate to https://www.trycourier.app and log in with the account's email and current password.

### Step 2: Access Account Settings

**Context**: Locate the password change functionality.

Once logged in, go to the account or profile settings section, typically under a user menu.

### Step 3: Update Password

**Context**: Change the password to test token invalidation.

Enter the old password, then set a new one. Confirm and save the changes.

**Expected Output**: Confirmation message that password was updated successfully; login session remains active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[broken-authentication]]
- [[password-change]]

---
