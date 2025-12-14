---
id: uuid-3
tags:
  - account-takeover
  - old-credentials
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
updated_at: '2025-12-14T17:32:58.249Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login with Old Password and QR Code for Account Takeover in BCM Messenger

## Summary

This procedure exploits the BCM Messenger vulnerability by logging in with the old password and QR code after a password change, achieving account takeover since the server accepts legacy credentials without invalidation.

## Description

Post-password change, the old password and QR code (with prior private key) remain valid for authentication because the server stores no passwords and does not revoke old private keys. An attacker with access to these old artifacts can log in from another device or session, gaining full control. This targets the authentication endpoint in the mobile app or web client.

## Requirements

1. Access to old password
2. Image or ability to scan old QR code (private key)
3. Separate BCM Messenger instance (e.g., new app install or incognito)

## Defense

Defensive measures and detection strategies:

- Revoke all prior sessions and keys on password changes
- Implement multi-factor authentication beyond QR/password
- Detect and block logins from unrecognized devices

## Objectives

1. Authenticate using pre-change credentials
2. Gain unauthorized account access
3. Demonstrate takeover impact (e.g., read messages, change settings)

## Instructions

### Step 1: Prepare Separate Login Instance

**Context**: Use a clean session to avoid interference from the updated app.

Install BCM Messenger on a new device or use web in incognito mode. Start the login process.

> App prompts for QR code scan and password entry.

### Step 2: Authenticate with Old Credentials

**Context**: Submit old password and scan old QR code to exploit the invalidation flaw.

Scan the original QR code to load the old private key, then enter the old password. Submit for authentication.

> Server accepts credentials; login succeeds, granting account access despite the change.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[old-credentials]]
