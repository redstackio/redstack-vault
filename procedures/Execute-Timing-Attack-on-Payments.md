---
tags:
  - timing-attack
  - oracle
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/perform-timing-attack]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:53.621Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 134199dc-e320-4bd1-b56c-e6032a7794ca
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Execute-Timing-Attack-on-Payments

## Summary

This procedure leverages response time differences in the Payments backend to perform a timing attack, inferring the existence and approximate count of matching Payment objects based on injected filters.

## Description

When filters return no matches, the backend responds quickly (~400ms); matches cause delays (~2000ms) due to array handling vs. single record expectation, leading to 500 errors. This side-channel attack on the REST interface (/payments) discloses sensitive data without direct content access, applicable to GraphQL-backed web apps.

## Requirements

1. Ability to send rapid GraphQL queries (scripting recommended)
2. Timing measurement tool (e.g., custom script or proxy)
3. Baseline timings established

## Defense

Defensive measures and detection strategies:

- Implement constant-time query execution
- Add noise/jitter to response times
- Detect high-volume similar queries via WAF

## Objectives

1. Differentiate match/no-match via RTT
2. Estimate object counts from delay magnitude
3. Infer backend behavior anomalies

## Instructions

### Step 1: Measure Response Times

**Context**: Send queries with known match/no-match params and record timings.

**Command** ([[commands/perform-timing-attack]]):
```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dsecurity%26") { ... on User { id } } }
```

> No matches: ~400ms. Repeat 10x for average.

### Step 2: Test Matching Parameters

**Context**: Use params known to match (e.g., from public data) to observe delay.

**Command** ([[commands/perform-timing-attack]]):
```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dfransrosen%26") { ... on User { id } } }
```

> Matches (2 objects): ~2000ms, 500 error due to array mismatch.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/perform-timing-attack]]

## Tools Used


## Tags

- timing-oracle
- side-channel
- enumeration
