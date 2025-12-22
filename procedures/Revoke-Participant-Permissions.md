---
tags:
  - nextcloud
  - talk
  - permission-revoke
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
updated_at: '2025-12-14T17:29:09.804Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: fb373e27-25a7-4603-91f7-f3f9ba5679f6
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Audio Capture]]'
  - '[[Video Capture]]'
---
# Revoke-Participant-Permissions

## Summary

This procedure explains revoking permissions for a participant in Nextcloud Talk to disable their media.

## Description

Revocation simulates permission withdrawal, disabling active media and setting up the vulnerability for regrant reactivation. Performed via moderator controls during an active call.

## Requirements

1. Active call with participant media enabled
2. Moderator privileges
3. Access to participant settings

## Defense

Defensive measures and detection strategies:

- Require confirmation for permission changes
- Alert users to revocation events
- Audit moderator actions on permissions

## Objectives

1. Disable participant media
2. Revoke access rights
3. Prepare for regrant exploitation

## Instructions

### Step 1: Access Settings

**Context**: Open management for User B.

Click on User B's name or avatar in participants list.

### Step 2: Revoke Permissions

**Context**: Disable cam and mic access.

Select revoke options for all permissions and confirm.

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
- [[permission-revoke]]
