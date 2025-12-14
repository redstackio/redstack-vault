---
id: proc-auth-irccloud-ios
tags:
  - ios
  - authentication
  - session-storage
type: procedure
tools:
  - '[[tools/iOS-Data-Protection-Tool]]'
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:39.899Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Authenticate-to-IRCCloud-iOS-App

## Summary

This procedure authenticates a user in the IRCCloud iOS app, causing the session identifier to be stored in an unsecured plist file, setting up the conditions for token extraction.

## Description

In the context of physical access attacks on iOS devices, authenticating to the IRCCloud app writes the session token to com.irccloud.IRCCloud.plist in the app's Preferences folder without applying iOS data protection classes like NSFileProtectionComplete. This makes the token accessible even on a locked device. The procedure assumes the app is installed and the device is accessible; it requires valid credentials if not already logged in.

## Requirements

1. Physical access to the iOS device (unlocked temporarily for login if needed)
2. Valid IRCCloud credentials
3. IRCCloud iOS app installed

## Defense

Defensive measures and detection strategies:

- Apply NSFileProtectionComplete to sensitive files in app development
- Monitor for unusual app authentications on locked devices
- Use device encryption and remote wipe capabilities

## Objectives

1. Store session token in app storage
2. Prepare for extraction without device unlock
3. Enable credential access via physical means

## Instructions

### Step 1: Launch and Authenticate App

**Context**: Open the app to initiate login, which triggers token storage.

No specific command; perform manually:

- Unlock device if necessary, launch IRCCloud app.
- Enter credentials and authenticate.

> Successful authentication stores the token in the plist. Lock the device afterward.

### Step 2: Verify Storage

**Context**: Confirm token presence using tools.

Use [[tools/iOS-Data-Protection-Tool]] to check if files are written:

Connect device and run the tool to inspect app sandbox.

> Output shows plist file created without protection.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/iOS-Data-Protection-Tool]]

## Tags

- ios
- authentication
- session-storage
