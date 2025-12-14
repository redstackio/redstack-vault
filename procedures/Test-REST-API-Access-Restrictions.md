---
tags:
  - api-test
  - rest
  - access-control
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-rest-namespace-access-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:59.911Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a93b19cc-e10d-442e-b529-2054bf987986
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-REST-API-Access-Restrictions

## Summary

This procedure tests GitLab's REST API to confirm it properly restricts access to private namespaces, even with an unauthorized token, contrasting with the GraphQL vulnerability.

## Description

GitLab's REST API (/api/v4/namespaces/{id}) requires valid authentication and authorization. Using a token from another user simulates unauthorized access, expecting a 404 response. This targets namespace ID 16048 (example private user) on gitlab.com, verifying that privacy settings are enforced here but not in GraphQL.

## Requirements

1. curl tool installed
2. Valid PRIVATE-TOKEN from a non-owner user
3. Known namespace ID (e.g., 16048)

## Defense

Defensive measures and detection strategies:

- Rate-limit API calls and log unauthorized token usage
- Audit tokens for scope and expiration

## Objectives

1. Confirm REST API access denial
2. Highlight GraphQL discrepancy
3. Validate token-based restrictions

## Instructions

### Step 1: Prepare Token

**Context**: Obtain a token from an unrelated user account.

No command; generate via GitLab user settings.

> Token should have read access but not to target namespace.

### Step 2: Query Namespace

**Context**: Attempt access to private namespace via REST.

**Command** ([[commands/curl-rest-namespace-access-test]]):
```bash
curl --header "PRIVATE-TOKEN: anotherUserToken" 'https://gitlab.com/api/v4/namespaces/16048'
```

> Command sends GET request with header; expects 404 JSON error, confirming restriction.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-rest-namespace-access-test]]

## Tools Used

- [[tools/curl]]

## Tags

- api-test
- rest
- access-control
