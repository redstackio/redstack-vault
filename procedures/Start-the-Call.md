---
tags:
  - nextcloud
  - talk
  - call-activation
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
updated_at: '2025-12-14T17:29:09.810Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: c5a423b5-1305-4aaa-8a81-da8df3a009ad
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Audio Capture]]'
  - '[[Video Capture]]'
---
# Start-the-Call

## Summary

This procedure covers starting the call session in Nextcloud Talk to activate media-related features.

## Description

Starting the call transitions the room to an active state, enabling permission controls and media streams. This is a prerequisite for the exploitation steps involving media activation.

## Requirements

1. Call room with at least one participant invited
2. Moderator authentication
3. Stable web connection

## Defense

Defensive measures and detection strategies:

- Auto-pause inactive calls after timeouts
- Monitor call start events in audit logs
- Notify users of call activations

## Objectives

1. Activate the call session
2. Enable media permission interfaces
3. Prepare for participant media enablement

## Instructions

### Step 1: Join as Moderator

**Context**: Initiate participation.

Click "Start call" or "Join now" in the call room.

### Step 2: Confirm Active State

**Context**: Verify the call is live.

Check for active indicators like timer or participant list updates.

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
- [[call-activation]]
