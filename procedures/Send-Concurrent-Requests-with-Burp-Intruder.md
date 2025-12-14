---
tags:
  - race-condition
  - toctou
  - concurrent-requests
  - burp-intruder
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/claim-credential-graphql-mutation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.928Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a18d0856-3095-4062-a132-8fc0637694b4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Concurrent-Requests-with-Burp-Intruder

## Summary

This procedure uses Burp Suite's Intruder to send multiple concurrent GraphQL claim requests, exploiting the TOCTOU race condition to bypass synchronization and claim additional credentials.

## Description

After the initial claim, the system's state update lags, allowing concurrent requests to check the availability before the update completes. By firing 22 identical mutations simultaneously, this exploits the race to acquire extra test accounts for the same program, demonstrating a business logic flaw in credential allocation.

## Requirements

1. Burp Suite Professional with Intruder enabled.
2. Captured initial request from the previous procedure.
3. Valid authentication and team_id.
4. Stable network to handle concurrent HTTPS requests.

## Defense

Defensive measures and detection strategies:

- Enforce atomic operations or mutex locks in the claim handler.
- Implement idempotency checks using clientMutationId to reject duplicates.
- Log and alert on high concurrency from single sessions.

## Objectives

1. Trigger the race condition with parallel requests.
2. Achieve at least one additional successful claim.
3. Validate the vulnerability's exploitability.

## Instructions

### Step 1: Capture and Configure Request

**Context**: Intercept the initial successful claim request in Burp Proxy and forward it to Intruder.

No command; use Burp UI to set positions (none needed for identical payloads).

### Step 2: Launch Concurrent Attack

**Context**: Configure Intruder for 22 threads to send the claim mutation rapidly.

**Command** ([[commands/claim-credential-graphql-mutation]]):

Use the same mutation as initial, but replay 22 times via Intruder (no bash equivalent; Burp-specific).

> In Burp Intruder, set attack type to "Null payloads" for identical requests, threads=22, and launch. Expected: Mixed responses with varying success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/claim-credential-graphql-mutation]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- burp-intruder
- concurrent
- race-exploit
