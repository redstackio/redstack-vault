---
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
  - '[[Collection]]'
commands:
  - '[[commands/time-curl-blind-sqli-test]]'
platforms:
  - Web
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 9383cea5-483c-4ecf-954e-3c05dfb02a93
created_at: '2025-12-14T17:26:17.807Z'
updated_at: '2025-12-14T17:26:17.807Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-Blind-SQLi-with-Time-Based-Delay

## Summary

This procedure confirms a blind SQL injection vulnerability by injecting a time-delay payload and measuring response time, useful when no direct output is visible.

## Description

For the TVA API endpoint, a blind injection uses MSSQL's WAITFOR DELAY to pause execution for 10 seconds if the payload is processed. This technique verifies injection without data exfiltration, ideal for confirming control over the query in environments where union fails or output is suppressed.

## Requirements

1. Identified injection point from prior steps
2. Tools to measure HTTP response timing
3. Tolerance for self-signed certs (-k flag)

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to prevent delay functions like WAITFOR
- Monitor for unusual response times in API logs
- Rate-limit requests to detect probing patterns

## Objectives

1. Validate blind injection without visible errors
2. Confirm DBMS support for time-based techniques
3. Assess potential for data exfiltration via conditionals

## Instructions

### Step 1: Prepare Time-Based Payload

**Context**: Craft a payload that injects a delay only if vulnerable.

**Command** ([[commands/time-curl-blind-sqli-test]]):

```bash
time curl -k "https://soa-accp.glbx.tva.gov/api/river/observed-data/-GVDA1'+WAITFOR+DELAY+'0:0:10'--+-"
```

> The 'time' prefix measures total execution; expect ~10s delay if injected.

### Step 2: Interpret Timing

**Context**: Compare against baseline requests.

Run a normal request first for comparison; significant delay indicates success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/time-curl-blind-sqli-test]]

## Tools Used

- [[tools/curl]]
- [[tools/time]]

## Tags

- blind-sqli
- timing-attack
