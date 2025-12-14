---
tags:
  - csrf
  - discovery
  - endpoint-testing
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.445Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 089a9fce-ebca-4434-b002-304c2d9d102d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Discover-Inconsistent-Response-in-al_groups-Endpoint

## Summary

This procedure identifies a CSRF vulnerability in VK.com's al_groups.php by testing response differences between admin and non-admin access to group public boxes, revealing information leakage.

## Description

The al_groups.php endpoint at https://vk.com/al_groups.php?act=to_public_box&al=1&gid=<group_id> returns a silent, commented-out response for group admins but an explicit 'Access Error' for others. This inconsistency allows cross-origin detection without authentication tokens, exploiting lack of CSRF protection and frame-embedding restrictions. Prerequisites include a VK account with a test group and browser access.

## Requirements

1. Logged-in VK.com account with owned group (e.g., GID 147481259)
2. Browser developer tools for inspecting responses
3. Non-owned group ID for comparison (e.g., GID 111)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on sensitive endpoints
- Enforce consistent error responses (e.g., uniform silent failures)
- Set X-Frame-Options: DENY and strict CSP to block embedding

## Objectives

1. Confirm vulnerability through response testing
2. Document behavior for exploitation planning
3. Identify lack of protections

## Instructions

### Step 1: Test Admin Response

**Context**: Load the endpoint with an owned group ID to observe silent behavior.

Navigate to https://vk.com/al_groups.php?act=to_public_box&al=1&gid=147481259 in a browser or use curl:

```bash
curl "https://vk.com/al_groups.php?act=to_public_box&al=1&gid=147481259" -H "Cookie: your_vk_session_cookie"
```

> Inspect response: Expect empty or commented-out content (silent).

### Step 2: Test Non-Admin Response

**Context**: Load with a non-owned group to trigger error.

Use:

```bash
curl "https://vk.com/al_groups.php?act=to_public_box&al=1&gid=111" -H "Cookie: your_vk_session_cookie"
```

> Expect 'Ошибка доступа' in response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Discovery]]
