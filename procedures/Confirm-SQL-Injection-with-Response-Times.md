---
id: proc-confirm-sqli-times-2024
tags:
  - sqli
  - validation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/time-based-sqli-sleep-15]]'
  - '[[commands/time-based-sqli-sleep-7]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.438Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-SQL-Injection-with-Response-Times

## Summary

This procedure validates the time-based SQL injection by measuring and comparing response times between injected payloads with different SLEEP durations, confirming the vulnerability's presence.

## Description

By sending payloads with SLEEP(7) and SLEEP(15), attackers measure delays (e.g., 660ms vs 4140ms) to infer successful injection in a blind scenario. This technique relies on MySQL's SLEEP function and is key for verifying SQLi without visible errors.

## Requirements

1. Timing-capable HTTP client (curl with -w flag)
2. Multiple runs for consistency
3. Baseline normal request time

## Defense

Defensive measures and detection strategies:

- Log and alert on response times exceeding thresholds
- Use query timeouts to mitigate delays
- Implement anomaly detection in application logs

## Objectives

1. Measure delay differences
2. Confirm payload execution
3. Quantify vulnerability reliability

## Instructions

### Step 1: Execute Short Delay Payload

**Context**: Run SLEEP(7) to establish shorter baseline.

**Command** ([[commands/time-based-sqli-sleep-7]]):
```bash
curl ... (as above) -w "%{time_total}s\n"
```

> Observe ~660ms total time.

### Step 2: Execute Long Delay Payload

**Context**: Run SLEEP(15) and compare.

**Command** ([[commands/time-based-sqli-sleep-15]]):
```bash
curl ... (as above) -w "%{time_total}s\n"
```

> Observe ~4140ms, confirming injection.

### Step 3: Repeat for Validation

**Context**: Run 3-5 times each to rule out network variance.

**Expected Output**: Consistent delay correlation to SLEEP value.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/time-based-sqli-sleep-15]]
- [[commands/time-based-sqli-sleep-7]]

## Tools Used


## Tags

- sqli
- validation
