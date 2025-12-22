---
id: proc-rocket-roomid-001
name: Identify-Rocket-Chat-Room-ID
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.267Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
tags:
  - discovery
  - room-id
  - rocket-chat
platforms:
  - Web
tools:
  - '[[tools/Browser-Web-Inspector]]'
commands: []
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# Identify-Rocket-Chat-Room-ID

## Summary

This procedure extracts the Room ID (RID) from a Rocket.Chat channel or direct message, required for targeted message sending and exploitation of vulnerabilities like CSS injection.

## Description

In Rocket.Chat, rooms and DMs are identified by unique RIDs, visible in network requests or UI elements. Using browser developer tools, attackers inspect traffic to the WebSocket or REST endpoints to retrieve this ID. This is a discovery step in web application attacks, enabling precise targeting. Prerequisites include an authenticated session; outcomes provide the RID for subsequent API calls.

## Requirements

1. Authenticated session in Rocket.Chat
2. Browser with developer tools (e.g., Chrome DevTools)
3. Access to the target room or DM interface

## Defense

Defensive measures and detection strategies:

- Obfuscate internal IDs in client-side code to hinder discovery
- Log and monitor unusual network inspection patterns if possible
- Implement client-side integrity checks to detect tampering

## Objectives

1. Locate and extract the RID for a specific room or DM
2. Prepare for targeted message injection
3. Minimize exposure during reconnaissance

## Instructions

### Step 1: Navigate to Target Room

**Context**: Select the channel or DM to inspect.

No command; click into the desired room in the Rocket.Chat sidebar.

> Expected output: Room chat loads, with messages visible.

### Step 2: Open Network Tab

**Context**: Monitor API calls to capture the RID.

Use [[tools/Browser-Web-Inspector]] to open the Network tab and filter for WebSocket or XHR requests.

> Refresh the room or send a test message. Expected output: Requests show 'rid' parameter, e.g., 'rid: "GENERAL"'.

### Step 3: Inspect UI Elements

**Context**: Alternative method via DOM inspection.

In the Elements tab, search for data attributes or script variables containing the room ID.

> Expected output: RID extracted, such as a hex string or name like 'user123' for DMs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Browser-Web-Inspector]]

## Tags

- [[Discovery]]
- [[room-id]]
- [[rocket-chat]]
