---
tags:
  - nextcloud
  - talk
  - call-setup
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Audio Capture]]'
  - '[[Video Capture]]'
updated_at: '2025-12-14T17:29:09.817Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: cd92cf60-0f5c-4e47-84fe-1d05e7e2eac8
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Audio Capture]]'
  - '[[Video Capture]]'
---
# Create-Call-as-Moderator

## Summary

This procedure outlines how a moderator creates a new call in Nextcloud Talk to initiate the environment for permission-based attacks.

## Description

In the context of exploiting Nextcloud Talk vulnerabilities, creating a call as the moderator establishes the session where permission management can be manipulated. This step requires authenticated access to a Nextcloud instance with the Talk app enabled. The outcome is a ready call room for adding participants and managing media permissions.

## Requirements

1. Authenticated moderator account in Nextcloud
2. Talk app installed and active in the instance
3. Web browser access to the Nextcloud dashboard

## Defense

Defensive measures and detection strategies:

- Limit moderator roles to trusted users only
- Monitor call creation logs for anomalous patterns
- Enable user notifications for call invitations

## Objectives

1. Set up a controlled call environment
2. Prepare for participant addition and permission changes
3. Ensure moderator controls are active

## Instructions

### Step 1: Access Talk App

**Context**: Log in and navigate to the Talk interface to begin call creation.

Log in to Nextcloud as User A (moderator). From the app launcher or main menu, select the Talk app.

### Step 2: Initiate New Call

**Context**: Create the call room using the interface controls.

Click the "New call" or equivalent button. Select video call mode if prompted. The call room is generated automatically.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Audio Capture]] Audio Capture
- [[Video Capture]] Video Capture

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[talk]]
- [[call-setup]]
