---
tags:
  - setup
  - channel-creation
  - rocket-chat
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Web
techniques: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 7d954693-43a9-4ac4-ac5c-a23b83a8eed1
created_at: '2025-12-13T23:55:06.263Z'
updated_at: '2025-12-13T23:55:06.263Z'
verified: false
validated: true
submitted: true
---
# Setup-Rocket.Chat-Channel

## Summary

This procedure sets up a target channel or identifies an existing one for delivering malicious messages in Rocket.Chat.

## Description

To exploit messaging vulnerabilities, a channel is needed to post and have victims view the payload. This can be done manually via the UI or by obtaining a RoomId for private rooms.

## Requirements

1. Access to Rocket.Chat UI
2. User permissions to create channels

## Defense

Defensive measures and detection strategies:

- Restrict channel creation to admins
- Log channel creations for review

## Objectives

1. Create or select a channel for message posting
2. Ensure victim access to the channel

## Instructions

### Step 1: Create Channel via UI

**Context**: Use the Rocket.Chat web interface to create a new channel.

**Instructions**: Navigate to http://127.0.0.1:3000, click "Create Channel", name it (e.g., "target-channel"), and save.

> No command needed. Expected: Channel listed in sidebar.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- channel-creation
