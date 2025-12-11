---
tags:
  - idor
  - recon
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-extract-group-id]]'
  - '[[commands/curl-craft-admin-request]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 516b2b9d-15ee-4487-9679-318527a555a2
created_at: '2025-12-11T06:10:22.406Z'
updated_at: '2025-12-11T06:10:22.406Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Discover and Extract Group IDs from LINE Accounts

## Summary

This procedure involves discovering and extracting group IDs from LINE Official Accounts by querying accessible endpoints or guessing based on patterns, exploiting the ease of ID predictability to set up for further attacks.

## Description

In the context of LINE Official Accounts, group IDs are not sufficiently obfuscated, allowing attackers to extract them from API responses or guess them systematically. This is a foundational step for IDOR exploitation, targeting web-based administration features with inadequate security controls.

## Requirements

1. Access to LINE API endpoints via public internet
2. Basic web reconnaissance tools like curl
3. Knowledge of LINE account structures

## Defense

Defensive measures and detection strategies:

- Implement proper ID obfuscation and randomization
- Monitor API requests for unusual patterns or guessing attempts

## Objectives

1. Obtain valid group IDs for target accounts
2. Identify patterns for efficient guessing
3. Prepare for privilege escalation

## Instructions

### Step 1: Query Public Endpoints

**Context**: Send requests to LINE endpoints to retrieve account information containing group IDs.

**Command** ([[commands/curl-extract-group-id]]):
```bash
curl -X GET 'https://example.line.endpoint/account/info' -H 'User-Agent: Mozilla/5.0'
```

> This command fetches account details; parse the JSON response for 'group_id' fields.

### Step 2: Guess IDs if Needed

**Context**: If direct extraction fails, use patterns (e.g., incremental IDs) to guess valid ones.

**Command** ([[commands/curl-extract-group-id]]):
```bash
for id in {1..100}; do curl -X GET "https://example.line.endpoint/group/$id"; done
```

> Loop through potential IDs and check for valid responses indicating existing groups.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-extract-group-id]]

## Tools Used

- [[tools/curl]]

## Tags

- [[idor]]
- [[recon]]
