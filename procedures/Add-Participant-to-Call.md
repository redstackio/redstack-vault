---
tags:
  - nextcloud
  - talk
  - participant-management
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
updated_at: '2025-12-14T17:29:09.813Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: 51f4bb17-1d41-474c-a86b-19e68576b8bf
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Audio Capture]]'
  - '[[Video Capture]]'
---
# Add-Participant-to-Call

## Summary

This procedure describes adding a target participant to an existing call in Nextcloud Talk, enabling subsequent permission manipulations.

## Description

Adding a participant involves using the Talk app's invitation features to include User B in the call. This step is crucial for targeting specific users in the privacy violation attack. Prerequisites include an active call room created by the moderator.

## Requirements

1. Existing call room as moderator
2. Knowledge of target participant's username or email
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Require explicit join confirmations for participants
- Log participant additions and review for unauthorized invites
- Implement role-based access to prevent unwanted additions

## Objectives

1. Include target user in the call
2. Set stage for media enablement
3. Maintain moderator oversight

## Instructions

### Step 1: Open Participant Management

**Context**: Access the controls to add users.

In the call room, click the participants icon or "Invite" button.

### Step 2: Select and Add User

**Context**: Search and confirm addition of User B.

Enter User B's details, select from suggestions, and confirm to send invite.

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
- [[participant-management]]
