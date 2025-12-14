---
tags:
  - sqli
  - blind-sqli
  - time-based
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/time]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-extended-delay]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.830Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b9e019c1-dfa6-4a40-aa9f-cff60d1ec136
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-SQL-Injection-with-Extended-Delay

## Summary

This procedure confirms the blind time-based SQL injection by injecting an extended WAITFOR DELAY payload into the refresh_token parameter, observing a prolonged response time to validate SQL execution and vulnerability severity.

## Description

Building on the baseline test, this targets the same Informatica tsftp API endpoint with a 13-second delay payload: '; WAITFOR DELAY '0:0:13'-- . The significant delay proves the injection point is exploitable for data exfiltration (e.g., via conditional delays for bit extraction) or RCE. Target environment: Web API with SQL Server backend. Outcomes: Clear evidence of vulnerability without data access.

## Requirements

1. Successful baseline test completion
2. curl and time utilities
3. HTTPS access to the target endpoint

## Defense

Defensive measures and detection strategies:

- Parameterize queries to prevent injection
- Rate-limit API requests to detect timing attacks
- Log and alert on unusual response times from the database

## Objectives

1. Validate SQL payload execution with measurable delay
2. Assess potential for advanced exploitation like data leakage
3. Avoid sensitive data access in proof-of-concept

## Instructions

### Step 1: Execute Extended Delay Confirmation

**Context**: Send the POST request with the longer delay to compare against baseline and confirm the vulnerability.

**Command** ([[commands/curl-extended-delay]]):
```bash
time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:13'--"
```

> The command mirrors the baseline but uses a 13-second delay. Expected output: JSON error with ~14-second total time, confirming the injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-extended-delay]]

## Tools Used

- [[tools/curl]]
- [[tools/time]]

## Tags

- sqli
- blind-sqli
- time-based
