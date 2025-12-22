---
tags:
  - algolia
  - api-key
  - verification
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-add-object-to-test-index]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:10.460Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d767994e-c5c2-4569-ac7b-a4041ddcce37
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-API-Key-on-Intended-Index

## Summary

This procedure tests the restricted API key on its intended index to confirm it grants the expected permissions without issues, establishing a baseline for bypass attempts.

## Description

Using the created API key, send a batch addObject request to the 'test' index. This verifies the key works as scoped, adding sample records like user data, and returns a success response with a task ID.

## Requirements

1. Valid restricted API key
2. Algolia application ID
3. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Log all API operations with key details
- Alert on unexpected object additions
- Validate request origins and payloads

## Objectives

1. Confirm key functionality on scoped index
2. Add test objects for later verification
3. Identify any initial permission issues

## Instructions

### Step 1: Prepare Request Payload

**Context**: Construct a JSON payload for adding an object to the 'test' index.

No command; prepare data:

```json
{"requests":[{"action":"addObject","body":{"firstname":"John","lastname":"Doe","zip_code":null}}]}
```

> Ensure the payload matches the addObject action.

### Step 2: Execute Verification Request

**Context**: Send POST to the batch endpoint for 'test' index using the key.

**Command** ([[commands/curl-add-object-to-test-index]]):

```bash
curl "https://c1-in-2.algolianet.com/1/indexes/test/batch" -H "x-algolia-api-key: 0580d14b1c12e191b078f193b5e0e3ce" -H "x-algolia-application-id: FTCHS7XZX2" -H "Content-Type: application/json" --data '{"requests":[{"action":"addObject","body":{"firstname":"John","lastname":"Doe","zip_code":null}}]}'
```

> This adds the object if permissions are correct; expect 200 OK with {"taskID": NNN}.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-add-object-to-test-index]]

## Tools Used

- [[tools/curl]]

## Tags

- [[algolia]]
- [[api-key]]
- [[verification]]
