---
tags:
  - setup
  - rocket-chat
  - private-room
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.567Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: bd1f0d5b-bf8d-4417-8b62-f65a4219d01c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Private-Thread-in-Rocket-Chat

## Summary

This procedure sets up a private room and thread in Rocket.Chat containing sensitive messages, simulating a target for information disclosure attacks.

## Description

In a Rocket.Chat instance, create a direct message room between two authorized users (e.g., Alice and Bob) and initiate a thread with sensitive content. This establishes the vulnerable data in MongoDB that can later be leaked via injection. The procedure assumes access to the web interface or API and focuses on preparation for exploitation testing.

## Requirements

1. Valid Rocket.Chat credentials with permission to create private rooms
2. Access to the Rocket.Chat web application
3. Two user accounts for the private interaction

## Defense

Defensive measures and detection strategies:

- Enforce strict room creation policies and audit logs for private rooms
- Monitor for unusual thread activity in private channels

## Objectives

1. Establish a private room with threaded messages for targeting
2. Ensure messages contain mock sensitive data
3. Verify isolation from unauthorized users

## Instructions

### Step 1: Create Private Room

**Context**: Start a direct message conversation between two users to form a private room.

**Instructions**: Log in as one user (e.g., Alice), search for the other user (Bob), and initiate a DM. Note the room ID from the URL or network inspection (e.g., /direct/${ROOM_ID}).

### Step 2: Start Thread with Sensitive Messages

**Context**: Post a message and reply to it to create a thread, adding sensitive content.

**Instructions**: Send an initial message in the private room, then reply to it to start the thread. Include details like "Confidential project info: ..." to simulate sensitivity.

**Expected Output**: Thread visible in the private room interface, with messages stored in MongoDB.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- rocket-chat
