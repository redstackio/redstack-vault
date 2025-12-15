---
id: proc-tva-favorites-api-bypass
name: Retrieve-User-Favorites-via-API-Without-Authentication
type: procedure
verified: false
submitted: true
created_at: '2023-10-17T00:00:00Z'
updated_at: '2025-12-14T17:31:52.468Z'
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
  - '[[commands/get-valleyconnect-favorites-api]]'
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

# Retrieve-User-Favorites-via-API-Without-Authentication

## Summary

This procedure accesses the user favorites API in ValleyConnect without authentication, receiving an empty 200 OK response that bypasses intended controls.

## Description

The endpoint /customapi/v1/user/getuserfavorites does not validate sessions, responding to unauthenticated GET requests with empty data. Part of the HTTP/2 JSON-based web API, this reveals access control gaps in public endpoints, useful for mapping user features in offensive testing.

## Requirements

1. HTTPS access to the domain.
2. Basic HTTP client.
3. No authentication artifacts.

## Defense

Defensive measures and detection strategies:

- Require auth headers for user-specific APIs.
- Implement WAF rules to deny unauthenticated calls to /customapi/* paths.

## Objectives

1. Query favorites endpoint.
2. Confirm lack of enforcement.
3. Gather API behavior intel.

## Instructions

### Step 1: Send GET Request to Favorites API

**Context**: Test the endpoint for auth bypass.

**Command** ([[commands/get-valleyconnect-favorites-api]]):
```bash
curl -X GET https://valleyconnect.tva.gov/customapi/v1/user/getuserfavorites
```

> Yields 200 OK with empty string "". Success without auth errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/get-valleyconnect-favorites-api]]

## Tools Used


## Tags

- improper-authentication
- api
- discovery
