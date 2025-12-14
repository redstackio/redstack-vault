---
id: proc-tva-profile-api-bypass
name: Retrieve-Basic-Profile-Info-via-API-Without-Authentication
type: procedure
verified: false
submitted: true
created_at: '2023-10-17T00:00:00Z'
updated_at: '2025-12-14T17:31:52.473Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - improper-authentication
  - api
  - discovery
commands:
  - '[[commands/get-valleyconnect-profile-api]]'
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---

# Retrieve-Basic-Profile-Info-via-API-Without-Authentication

## Summary

This procedure queries the ValleyConnect profile API endpoint without authentication, receiving a 200 OK response with null user details, confirming flawed session handling.

## Description

The API at /customapi/v1/user/getbasicprofileinfo lacks auth validation, returning JSON profile data even for unauthenticated requests. This web API uses HTTP/2 and JSON, accessible publicly. It aids in discovering user session mechanics and potential for further enumeration in a public-facing app scenario.

## Requirements

1. Network access to https://valleyconnect.tva.gov/
2. HTTP client like curl
3. No tokens or cookies needed

## Defense

Defensive measures and detection strategies:

- Add JWT or session token checks to all API routes.
- Rate-limit and log unauthenticated API calls, blocking suspicious patterns.

## Objectives

1. Fetch profile data structure.
2. Validate null session response.
3. Expose API auth weaknesses.

## Instructions

### Step 1: Send GET Request to Profile API

**Context**: Directly query the endpoint to bypass auth.

**Command** ([[commands/get-valleyconnect-profile-api]]):
```bash
curl -X GET https://valleyconnect.tva.gov/customapi/v1/user/getbasicprofileinfo -H "Host: valleyconnect.tva.gov"
```

> Returns 200 OK with {"username":null,"email":null,"orgId":null,"hasRemoteAssistanceGrant":false}. Failure if 401/403 occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/get-valleyconnect-profile-api]]

## Tools Used


## Tags

- improper-authentication
- api
- discovery
