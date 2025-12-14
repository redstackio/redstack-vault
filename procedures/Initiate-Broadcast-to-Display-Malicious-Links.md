---
id: proc-initiate-broadcast-links-2024
tags:
  - xss
  - broadcast-trigger
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Malicious File]]'
updated_at: '2025-12-13T23:55:06.480Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Malicious File]]'
---
# Initiate Broadcast to Display Malicious Links

## Summary

This procedure starts the Chaturbate broadcast to render the forged app links in the chat header, making them visible to victims.

## Description

After crafting apps, initiating the broadcast populates the chat header with <a> tags containing the malicious javascript: URIs from app_info_json. Victims must access the room to see and potentially click the links.

## Requirements

1. Apps created with malicious names
2. Broadcaster dashboard access
3. Victim account for room entry

## Defense

Defensive measures and detection strategies:

- Preview app links before rendering in headers
- Rate-limit or review broadcaster app creations
- Alert on javascript: schemes in chat elements

## Objectives

1. Expose malicious links to victims
2. Ensure room is publicly accessible
3. Prepare for user interaction trigger

## Instructions

### Step 1: Start Broadcast

**Context**: From broadcaster interface, begin streaming.

**Instructions**: Click 'Start Broadcast' or equivalent to activate the room.

### Step 2: Access Room as Victim

**Context**: Use a separate account to enter the room and view header.

**Instructions**: Log in as victim, navigate to the broadcast room URL.

> Expected output: Malicious app links display in chat header. Success: Links visible and clickable without page errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Malicious File]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[broadcast-trigger]]
