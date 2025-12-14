---
tags:
  - idor
  - api
  - unauthenticated
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-trip-config]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:34.951Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 94336014-8e89-4022-b235-031d6d79bd84
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate-Trip-Hash-via-Unauthenticated-Config-Endpoint

## Summary

This procedure exploits an unauthenticated GET endpoint to retrieve configuration data for a specific trip ID, generating a hash that can be used for further manipulation, enabling IDOR attacks on ride-sharing trip data.

## Description

In the context of a ride-sharing platform like Bykea, the /v1/config endpoint lacks authorization checks, allowing any unauthenticated user to query trip configurations using arbitrary trip IDs. This exposes sensitive hashes used in bidding logic, facilitating business logic flaws when chained with other endpoints. The attack targets web APIs and requires only HTTP access, resulting in the ability to prepare for fare manipulation without credentials.

## Requirements

1. Network access to the target API (e.g., https://api.bykea.com)
2. Knowledge of a valid target trip_id (e.g., obtained via enumeration or social engineering)
3. HTTP client like curl for requests

## Defense

Defensive measures and detection strategies:

- Implement authentication and authorization checks (e.g., JWT validation) on all API endpoints handling user-specific data
- Rate-limit requests to config endpoints and monitor for anomalous trip_id queries
- Use input validation to restrict trip_id to owned resources only

## Objectives

1. Retrieve trip configuration hash without authentication
2. Enable chaining to bidding manipulation
3. Expose IDOR vulnerability in trip data access

## Instructions

### Step 1: Query Trip Config

**Context**: Send an unauthenticated GET request to the config endpoint with the target trip_id to obtain the hash.

**Command** ([[commands/curl-get-trip-config]]):
```bash
curl -X GET "https://api.example.com/v1/config?trip_id=TARGET_TRIP_ID" -H "Accept: application/json"
```

> This command fetches the JSON response containing the trip config. Look for the 'hash' field in the output (e.g., {"trip_id": "12345", "hash": "abc123def"}). Success is indicated by a 200 OK response; failure may return 404 if the trip_id is invalid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-trip-config]]

## Tools Used


## Tags

- idor
- api
- unauthenticated
