---
tags:
  - rest-api
  - 403-forbidden
  - contrast
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-rest-user-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:59.506Z'
sub_techniques: []
id: 12f2bb8f-290e-4319-9a56-fd1fdfbad7d8
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Test-REST-API-Access-with-Deactivated-Token

## Summary

This procedure tests REST API access with a deactivated user's token to confirm proper enforcement of restrictions, contrasting with GraphQL bypass.

## Description

REST endpoints like /api/v4/user enforce :access_api checks, returning 403 for deactivated users. This highlights the GraphQL-specific vulnerability.

## Requirements

1. Deactivated token
2. Access to REST endpoint
3. curl

## Defense

Defensive measures and detection strategies:

- Ensure consistent policy enforcement across APIs
- Monitor 403 responses for patterns

## Objectives

1. Attempt user endpoint access
2. Verify denial
3. Validate expected behavior

## Instructions

### Step 1: Query User Endpoint

**Context**: Test basic REST access.

**Command** ([[commands/curl-rest-user-access]]):
```bash
curl --header "Authorization: Bearer jKSvxhuDN-Noag6N-w7R" "http://gitlab.joaxcar.com/api/v4/user"
```

> Returns 403 with deactivation message.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-rest-user-access]]

## Tools Used

- [[tools/curl]]

## Tags

- rest
- forbidden
- test
