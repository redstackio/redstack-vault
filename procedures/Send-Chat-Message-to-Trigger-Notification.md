---
tags:
  - chat-message
  - notification
  - nextcloud-talk
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
techniques: []
updated_at: '2025-12-14T17:24:44.675Z'
sub_techniques: []
id: 70cf1cf2-0c9d-4671-b150-012a12c3d47e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Send-Chat-Message-to-Trigger-Notification

## Summary

This procedure involves sending a chat message from User A to User B via Nextcloud Talk web, generating a push notification on the Android device.

## Description

From the web interface, initiating a chat triggers server-side push to the app, exploiting notification handling flaws. This step assumes logins are complete; outcome is a visible notification on the locked device.

## Requirements

1. Active web session (User A)
2. Chat channel with User B
3. Push notifications enabled on app

## Defense

Defensive measures and detection strategies:

- Disable notifications for sensitive chats
- Monitor for anomalous message patterns

## Objectives

1. Deliver message to User B
2. Generate app notification
3. Prepare for bypass interaction

## Instructions

### Step 1: Open Talk in Web

**Context**: Access chat functionality.

In Nextcloud web, click Talk icon, select User B to start chat.

### Step 2: Send Message

**Context**: Trigger push.

Type and send a message like "Hello".

**Expected Output**: Message sent; notification on device.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[message-sending]]
- [[push-notification]]
