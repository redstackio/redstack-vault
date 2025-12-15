---
tags:
  - idor
  - graphql
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 1782f466-3a98-454f-ba81-bb7e3b9984be
created_at: '2025-12-14T17:25:30.151Z'
updated_at: '2025-12-14T17:25:30.151Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Decode-and-Obtain-Target-Team-Member-ID

## Summary

This procedure decodes the base64-encoded team_member_id from the captured request and retrieves other team members' IDs from a public JSON endpoint to identify exploitation targets.

## Description

HackerOne encodes team_member_ids in base64 as Global IDs (e.g., 'gid://hackerone/TeamMember/43794'). Decoding reveals the numeric ID. Public endpoints like https://hackerone.com/<program_handle>/team_members.json expose lists of team_member_ids, enabling IDOR targeting. This step assumes the captured request from prior procedure and focuses on enumeration without authentication for public data.

## Requirements

1. Captured GraphQL request with team_member_id
2. Base64 decoder (built-in browser tools or online)
3. Knowledge of target program handle (e.g., 'parrot_sec')

## Defense

Defensive measures and detection strategies:

- Remove or restrict public exposure of team_member_ids in JSON endpoints
- Implement ID obfuscation beyond base64 (e.g., UUIDs)
- Log access to public team endpoints for anomaly detection

## Objectives

1. Extract numeric ID from own request
2. Enumerate victim IDs publicly
3. Prepare for request substitution

## Instructions

### Step 1: Decode Own team_member_id

**Context**: Convert base64 to reveal the internal reference format.

Take the value (e.g., 'Z2lkOi8vaGFja2Vyb25lL1RlYW1NZW1iZXIvNDM3OTQ=') and base64-decode it to 'gid://hackerone/TeamMember/43794'.

### Step 2: Retrieve Victim IDs

**Context**: Access public endpoint to list team members.

Visit https://hackerone.com/<program_handle>/team_members.json (e.g., https://hackerone.com/parrot_sec/team_members.json).

Parse the JSON for 'team_member_ids' array, extracting base64 values or IDs.

> Expected JSON structure: {"team_member_ids": ["id1", "id2"]}. Note numeric parts for substitution.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[graphql]]
- [[Discovery]]
