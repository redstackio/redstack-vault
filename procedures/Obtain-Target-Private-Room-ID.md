---
tags:
  - reconnaissance
  - room-discovery
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:01.563Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ba4f91ba-0b4a-42c6-ac5a-2ec62377c40e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Obtain-Target-Private-Room-ID

## Summary

This procedure identifies the internal ID of a private room in Rocket.Chat, necessary for crafting the injection payload to target specific threads.

## Description

Room IDs in Rocket.Chat are opaque strings (e.g., hex identifiers) stored in MongoDB. Obtain them via network inspection during authorized access, social engineering, or enumeration of API responses. This step assumes prior knowledge or leakage and focuses on extraction for exploitation.

## Requirements

1. Temporary authorized access to the private room or related data
2. Browser developer tools for inspecting API calls
3. Knowledge of the target room's name or participants

## Defense

Defensive measures and detection strategies:

- Obfuscate internal IDs and avoid exposure in client-side code
- Log and alert on unauthorized API queries for room metadata

## Objectives

1. Extract the exact room ID string
2. Validate it corresponds to a private room
3. Prepare for use in regex payload

## Instructions

### Step 1: Access Private Room as Authorized User

**Context**: Log in as an authorized user to interact with the room.

**Instructions**: Navigate to the private room in the Rocket.Chat interface.

### Step 2: Inspect Network Traffic for Room ID

**Context**: Capture the room ID from API requests or URL parameters.

**Instructions**: Open browser dev tools (Network tab), refresh the room, and look for requests to /api/v1/channels.info or similar; extract 'rid' from the response or URL (e.g., /direct/${ROOM_ID}). Alternatively, use console: RocketChat.roomTypes.getRoomType('d').roomName(RocketChat.roomTypes.getRoomType('d').RoomHistory({rid: roomId})) to infer.

**Expected Output**: Room ID like 'abc123def456'.

### Step 3: Verify Privacy

**Context**: Confirm the ID is for a private room.

**Instructions**: As unauthorized user, attempt to query /api/v1/rooms.info?roomId=${ID}; expect access denied.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- reconnaissance
- room-discovery
