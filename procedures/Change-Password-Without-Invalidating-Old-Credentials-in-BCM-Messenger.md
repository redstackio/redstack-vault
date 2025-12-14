---
id: uuid-2
tags:
  - password-change
  - credential-invalidation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Mobile App
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.250Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Change Password Without Invalidating Old Credentials in BCM Messenger

## Summary

This procedure changes the account password in BCM Messenger, which generates a new QR code with an updated private key locally, but fails to invalidate the old password and prior QR code on the server, leaving legacy credentials vulnerable to exploitation.

## Description

BCM Messenger's password change feature updates the user's password and regenerates the QR code (with a new private key) in the app, but the server does not revoke access for old authentication data. Private keys are managed locally, and without server-side invalidation, old credentials remain valid. This targets the mobile app or web client and requires an active session with the account.

## Requirements

1. Active login session in BCM Messenger
2. Knowledge of current password
3. New password meeting app policies

## Defense

Defensive measures and detection strategies:

- Implement server-side session revocation on password changes
- Log and alert on multiple authentication attempts with varying credentials
- Use token-based auth with expiration and invalidation

## Objectives

1. Update password and generate new QR code
2. Confirm old credentials are not revoked (vulnerability trigger)
3. Maintain access for takeover testing

## Instructions

### Step 1: Navigate to Password Settings

**Context**: Access the account settings to initiate the password update.

In the BCM Messenger app or web interface, go to account settings (typically under profile or security) and select 'Change Password'.

> The app prompts for the current password to verify identity.

### Step 2: Update Password and Generate New QR

**Context**: Enter new password details, triggering local QR regeneration without server invalidation.

Provide the old password for verification, then enter and confirm the new password. Submit the change. The app generates a new QR code with an updated private key.

> Password updated successfully; new QR code displayed for rescanning if needed. Old credentials persist on server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-change]]
- [[credential-invalidation]]
