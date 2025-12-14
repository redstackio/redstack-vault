---
tags:
  - credential-validation
  - api-testing
  - unauthorized-access
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-wakatime-api-key]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:39.414Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f805ee89-bd30-47a2-8f54-887efe1d1cf7
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Valid Accounts]]'
---
# Validate-Exposed-API-Key-on-WakaTime

## Summary

This procedure tests a discovered API key against the WakaTime API to verify its validity and potential for unauthorized access to user summaries or other resources.

## Description

Once an API key is identified in public sources, such as the leaked waka_edf47c40-cabf-46e7-9f88-f1b44f00431f from a historical URL, this procedure involves crafting requests to protected endpoints like /api/v1/users/current/summaries. A successful response indicates the key remains active, allowing disclosure of personal coding activity data or actions on the user's behalf. Requires only curl and knowledge of the target API structure.

## Requirements

1. The exposed API key value
2. curl installed for HTTP requests
3. Knowledge of the target API endpoint and parameters

## Defense

Defensive measures and detection strategies:

- Rotate API keys immediately upon exposure detection
- Monitor API logs for anomalous access patterns from unknown IPs
- Enforce key rotation policies and usage scoping to limit damage

## Objectives

1. Confirm the API key authenticates requests
2. Assess access level to restricted resources
3. Identify potential data leakage or privilege escalation

## Instructions

### Step 1: Test API Key Authentication

**Context**: Send a request to a protected endpoint with the key to check for successful authentication versus 401 Unauthorized.

**Command** ([[commands/curl-test-wakatime-api-key]]):
```bash
curl "https://wakatime.com/api/v1/users/current/summaries?start=today&end=today&api_key=waka_edf47c40-cabf-46e7-9f88-f1b44f00431f"
```

> This queries today's user summaries. Expected output is JSON data if valid; without the key, it returns 401.

### Step 2: Compare with Invalid Request

**Context**: Verify failure without the key to confirm the key's necessity.

**Command** (curl without key):
```bash
curl "https://wakatime.com/api/v1/users/current/summaries?start=today&end=today"
```

> Should return 401 Unauthorized, validating the key's role in access.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

### Techniques

- [[Credentials In Files]] Credentials In Files
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-test-wakatime-api-key]]

## Tools Used


## Tags

- [[credential-validation]]
- [[api-testing]]
- [[unauthorized-access]]
