---
tags:
  - nextcloud
  - talk
  - media-enable
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
updated_at: '2025-12-14T17:29:09.807Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: 36b89eba-186e-46b2-9ae6-aa036004ce6a
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Audio Capture]]'
  - '[[Video Capture]]'
---
# Participant-Joins-and-Enables-Media

## Summary

This procedure details the participant joining the call and enabling their camera and microphone, setting the vulnerable state.

## Description

The participant must join and activate media voluntarily to allow the later revocation and reactivation exploit. This step relies on user action but is part of the attack narrative to establish prior enablement.

## Requirements

1. Invitation to the call
2. Participant account authentication
3. Device with camera/microphone

## Defense

Defensive measures and detection strategies:

- Prompt users to confirm media access on join
- Default media to off
- Log media enablement events

## Objectives

1. Join the active call
2. Activate camera and microphone
3. Make media state active for exploitation

## Instructions

### Step 1: Join the Call

**Context**: Accept and enter the call.

User B opens the invitation in Talk app and clicks join.

### Step 2: Enable Media Devices

**Context**: Turn on camera and mic.

Click camera icon to enable video; repeat for microphone. Verify via preview.

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
- [[media-enable]]
