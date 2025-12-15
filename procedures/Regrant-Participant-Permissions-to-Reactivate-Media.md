---
tags:
  - nextcloud
  - talk
  - permission-regrant
  - media-reactivation
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
updated_at: '2025-12-14T17:29:09.801Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
id: 2aac43cb-3fec-4dd6-9df1-6f5b10e55d7a
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Audio Capture]]'
  - '[[Video Capture]]'
---
# Regrant-Participant-Permissions-to-Reactivate-Media

## Summary

This procedure exploits the vulnerability by re-granting permissions to remotely reactivate participant media without consent.

## Description

After revocation, re-granting permissions bypasses user confirmation and auto-activates previously enabled devices on the client side, leading to unauthorized surveillance. This is the core exploit in the permission management flaw.

## Requirements

1. Revoked permissions on active participant
2. Moderator access during call
3. Participant device with prior media enablement

## Defense

Defensive measures and detection strategies:

- Implement user confirmation for all permission regrants
- Disable auto-reactivation of media post-revocation
- Monitor for unexpected media streams in logs

## Objectives

1. Re-grant access rights
2. Force remote media activation
3. Capture unauthorized audio/video

## Instructions

### Step 1: Access Permission Controls

**Context**: Reopen settings for User B.

Navigate back to participant management menu.

### Step 2: Regrant All Permissions

**Context**: Apply full access to trigger reactivation.

Select grant options for camera, mic, and all rights; confirm. Observe auto-activation.

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
- [[permission-regrant]]
- [[media-reactivation]]
