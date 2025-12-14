---
id: proc-003
tags:
  - api-bypass
  - policy-disclosure
  - hackerone
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-hackerone-api-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.292Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Query-Unauthorized-Program-Policy-via-API

## Summary

This procedure exploits the HackerOne API access control flaw by using a low-privilege API key to retrieve sensitive policy data for an unauthorized program, bypassing UI restrictions and disclosing confidential information.

## Description

The API endpoint https://api.hackerone.com/v1/hackers/programs/{program_handle}/ does not properly enforce group-based permissions, allowing queries to any program handle with a valid API key from the organization. Using the key from a user restricted to one program (e.g., askcmsakmdfksqa_h1r), query an unauthorized program (e.g., askcmsakmdfksqa_h1b) to obtain its policy, which may include sensitive details like scope, rewards, and rules.

## Requirements

1. Low-privilege API key from restricted user
2. Knowledge of unauthorized program handle (e.g., askcmsakmdfksqa_h1b)
3. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Synchronize API authorization with UI RBAC
- Log and alert on API queries to unauthorized resources
- Rate-limit API requests per user/group

## Objectives

1. Demonstrate access control bypass
2. Disclose unauthorized program policy
3. Collect sensitive configuration data

## Instructions

### Step 1: Prepare API Query

**Context**: Set up the HTTP request with authentication.

Use the low-perm API key as the username in basic auth.

### Step 2: Execute Query

**Context**: Send GET request to unauthorized endpoint.

**Command** ([[commands/curl-hackerone-api-query]]):
```bash
curl "https://api.hackerone.com/v1/hackers/programs/askcmsakmdfksqa_h1b/" -X GET -u "██████=" -H 'Accept: application/json'
```

> This command authenticates with the API key, requests JSON, and fetches program details. Expected output is a JSON object with policy data, confirming unauthorized access.

### Step 3: Analyze Response

**Context**: Verify sensitive data leakage.

Parse the JSON for policy fields like 'policy' or 'scope' that should be restricted.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-hackerone-api-query]]

## Tools Used

- [[tools/curl]]

## Tags

- api-bypass
- policy-disclosure
- hackerone
