---
id: proc-extract-user-id-browser
tags:
  - discovery
  - user-enumeration
  - browser-traffic
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
updated_at: '2025-12-14T17:30:27.009Z'
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
# Extract-User-ID-from-Browser-Traffic

## Summary

This procedure involves inspecting browser network traffic in Rocket.Chat to retrieve the internal _id of the authenticated user, essential for targeting in privilege modification attacks.

## Description

Rocket.Chat exposes user identifiers in API responses and WebSocket messages. By monitoring traffic during normal interactions (e.g., loading channels), attackers can extract the _id without additional permissions. This targets Meteor/DDP-based communications and assumes an active guest session. Expected outcome: Obtain unique user _id for use in escalation scripts.

## Requirements

1. Active guest session from prior login
2. Browser with developer tools (e.g., Chrome DevTools)
3. Basic knowledge of JSON parsing in network payloads

## Defense

Defensive measures and detection strategies:

- Obfuscate or encrypt internal IDs in client-side responses
- Implement client-side traffic monitoring to detect excessive network inspections
- Use server-side logging to track unusual API query patterns

## Objectives

1. Discover internal user identifier for targeted modifications
2. Enable precise role updates without guessing
3. Prepare for escalation by validating _id in context

## Instructions

### Step 1: Open Developer Tools

**Context**: Prepare to capture traffic during application interactions.

No command; open Network tab in browser dev tools.

> Filter for WebSocket or API requests. Expected output: Live capture of requests.

### Step 2: Trigger User Data Exposure

**Context**: Perform an action that reveals user details, such as joining a channel.

Interact with the UI (e.g., send a message).

> Inspect payloads for '_id' field in JSON (e.g., in 'user' object). Expected output: _id like "9HN4Brdmo2Qc2wsiX" extracted.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- discovery
- user-enumeration
