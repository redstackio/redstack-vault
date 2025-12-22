---
tags:
  - parameter-injection
  - graphql
  - url-encoding
type: procedure
tools:
  - '[[tools/ActiveResource]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/inject-query-parameters]]'
  - '[[commands/test-encoding-behavior]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.624Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 84914672-08b3-457d-bfc2-5a861df230e8
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Query-Parameters-via-Global-ID

## Summary

This procedure exploits the absence of encoding in ActiveResource's resource identifier handling to inject URL-encoded query parameters into the backend REST endpoint, altering the Payments index call to filter results.

## Description

By crafting global IDs with encoded query strings (e.g., %3f for ?, %26 for &), the decoded parameters append to the path (e.g., /payments/?core_hacker_username=jobert), enabling unauthorized filtering. This targets GraphQL APIs backed by Ruby/Rails and ActiveResource, leading to potential information disclosure when combined with timing attacks.

## Requirements

1. Valid GraphQL access
2. Known parameter names (e.g., core_hacker_username, core_team_handle from backend schema)
3. Tool to measure request construction (e.g., proxy like Burp)

## Defense

Defensive measures and detection strategies:

- Encode and validate all ID components before ActiveResource calls
- Reject queries with encoded URL characters in IDs
- Log and rate-limit suspicious GraphQL patterns

## Objectives

1. Inject filters into backend index endpoint
2. Confirm parameter decoding and application
3. Prepare for data inference attacks

## Instructions

### Step 1: Craft Injected Global ID

**Context**: Use encoded ? and & to append query params, with trailing %26 to isolate .json.

**Command** ([[commands/inject-query-parameters]]):
```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dsecurity%26") { ... on User { id } } }
```

> Results in GET /payments/?core_hacker_username=jobert&core_team_handle=security%26.json; verify via proxy.

### Step 2: Test Encoding Behavior

**Context**: Highlight root cause by comparing expected vs. actual path handling.

**Command** ([[commands/test-encoding-behavior]]):
```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fsomething%26") { ... on User { id } } }
```

> Actual: /payments/?something&.json; expected: encoded path. Confirms decoding flaw.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/inject-query-parameters]]
- [[commands/test-encoding-behavior]]

## Tools Used

- [[tools/ActiveResource]]

## Tags

- parameter-injection
- url-decoding
- exploitation
