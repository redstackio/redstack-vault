---
tags:
  - uuid-discovery
  - network-monitoring
type: procedure
tools:
  - '[[tools/Browser-DevTools]]'
  - '[[tools/Local-Proxy]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/get-conversation-assigned]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.256Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ba8503de-a29d-4a38-a096-ef44f37d8edc
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Discover-Target-User-UUID

## Summary

This procedure extracts a target user's UUID from API requests triggered by UI interactions in the Mail tab, leveraging exposed parameters in conversation assignments for reconnaissance.

## Description

As a low-privilege user, interact with the conversation assignment dropdown to trigger a GET request that includes the target UUID in the query string. Monitor via DevTools or proxy to copy the UUID without direct API abuse. This is a precursor to IDOR exploitation. Target environment: Web app with team collaboration features. Expected: UUID obtained for use in unauthorized updates.

## Requirements

1. Low-privilege 'USER' login
2. Access to Mail tab and dropdown interactions
3. Network monitoring tools configured

## Defense

Defensive measures and detection strategies:

- Avoid exposing UUIDs in client-side requests; use opaque identifiers
- Log and monitor unusual query patterns for user UUIDs
- Implement client-side obfuscation or server-side validation of exposed IDs

## Objectives

1. Identify target user's unique identifier
2. Gather intel for direct object manipulation
3. Validate exposure without alerting defenses

## Instructions

### Step 1: Trigger Request

**Context**: Simulate legitimate usage to expose UUID in network traffic.

**Command** ([[commands/get-conversation-assigned]]):
```bash
# Trigger via UI, monitor GET request
GET https://api.outpost.co/api/v1/conversation/assigned?assignedToUserUuid=da4f313f-e21e-4b5f-b2da-42d9864716f6
```

> Select target user in dropdown; inspect request in DevTools. Expected: UUID in query param.

### Step 2: Extract UUID

**Context**: Copy the identifier from the monitored request.

**Command** (Manual Copy):

Use DevTools Network tab or proxy logs to extract 'da4f313f-e21e-4b5f-b2da-42d9864716f6'.

> Expected: UUID saved for next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/get-conversation-assigned]]

## Tools Used

- [[tools/Browser-DevTools]]
- [[tools/Local-Proxy]]

## Tags

- [[uuid-discovery]]
- [[network-monitoring]]
