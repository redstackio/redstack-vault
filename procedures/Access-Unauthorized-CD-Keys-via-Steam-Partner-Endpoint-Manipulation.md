---
tags:
  - improper-access-control
  - steam
  - cd-keys
  - api-exploitation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-steam-endpoint-access]]'
platforms:
  - Web
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploitation for Credential Access]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1a338e07-9f0b-4f5f-a078-0c4b9a27c791
created_at: '2025-12-11T06:10:28.601Z'
updated_at: '2025-12-11T06:10:28.601Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1068]]'
  - '[[T1212]]'
---
# Access Unauthorized CD Keys via Steam Partner Endpoint Manipulation

## Summary

This procedure exploits an improper access control vulnerability in the Steam Partner API's /partnercdkeys/assignkeys/ endpoint, allowing authenticated users to download previously-generated CD keys for games they do not have permission to access by manipulating request parameters.

## Description

The vulnerability stems from insufficient permission checks on authenticated requests, enabling users to specify parameters that target unauthorized games and retrieve their CD keys. This can be performed without bypassing audit logs, and the impact includes potential access to all CD keys for any game on the platform. The attack requires authenticated access to partner.steamgames.com and knowledge of game IDs, discovered through testing endpoint parameters.

## Requirements

1. Valid authentication credentials for Steam Partner site
2. Network access to https://partnerandbook.com
3. HTTP client tool like curl

## Defense

Defensive measures and detection strategies:

- Implement strict permission checks on API endpoints for resource access
- Monitor API requests for anomalous parameter usage or access patterns

## Objectives

1. Bypass access controls to download unauthorized CD keys
2. Extract sensitive game activation data
3. Validate successful key retrieval without detection

## Instructions

### Step 1: Authenticate and Prepare Request

**Context**: Obtain authentication cookies or tokens by logging into partner.steamgames.com, then prepare parameters targeting an unauthorized game ID.

**Command** ([[commands/curl-steam-endpoint-access]]):
```bash
curl -X POST 'https://partner.steamgames.com/partnercdkeys/assignkeys/' \
  --cookie 'session_cookie=your_auth_cookie' \
  --data 'game_id=unauthorized_game_id&key_type=download_existing' \
  -o cd_keys.txt
```

> This command sends a POST request with parameters to download existing keys for the specified game, bypassing normal access restrictions. Expected output is a file containing the CD keys.

### Step 2: Validate Retrieved Data

**Context**: Inspect the downloaded file for valid CD key formats and confirm they correspond to the targeted game.

Review the contents of cd_keys.txt for successful extraction.

> Look for key patterns like XXXXX-XXXXX-XXXXX; absence of error messages indicates success.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]
- [[Credential Access]]

### Techniques

- [[Exploitation for Privilege Escalation]]
- [[Exploitation for Credential Access]]

### Sub-Techniques



## Commands Used

- [[commands/curl-steam-endpoint-access]]

## Tools Used



## Tags

- [[improper-access-control]]
- [[commands/curl-steam-endpoint-access]]
- [[cd-keys]]
- [[api-exploitation]]
