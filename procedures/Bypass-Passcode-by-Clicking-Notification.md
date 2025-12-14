---
tags:
  - bypass
  - notification-click
  - access-control
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1418]]'
updated_at: '2025-12-14T17:24:44.671Z'
sub_techniques: []
id: 4d970728-eb8b-4728-8388-2474178def24
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[T1418]]'
---
# Bypass-Passcode-by-Clicking-Notification

## Summary

This procedure exploits the vulnerability by tapping the incoming message notification on a locked Nextcloud Talk Android app, bypassing the passcode and granting direct access.

## Description

The core exploit: the app's notification handler fails to enforce passcode checks when launched from push, due to improper access control. Requires physical access; outcome is unauthorized app entry, exposing chats and Nextcloud files.

## Requirements

1. Locked Talk app with passcode (User B)
2. Incoming notification from message
3. Physical device access

## Defense

Defensive measures and detection strategies:

- Update to patched app version
- Disable app notifications or use secure launchers
- Monitor device for unexpected app opens

## Objectives

1. Launch app via notification
2. Avoid passcode prompt
3. Access sensitive content

## Instructions

### Step 1: Observe Notification

**Context**: Wait for push on locked device.

Ensure device is locked; notification appears for new message.

### Step 2: Tap Notification

**Context**: Trigger bypass.

Directly tap the notification banner or in notification shade.

**Expected Output**: App opens to chat without passcode entry.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[T1418]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[lock-screen-bypass]]
- [[android-vulnerability]]
