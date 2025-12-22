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
  - '[[commands/curl-baseline-delay]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.833Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 43b65e54-e86f-47ad-b4e7-fbbb8ca32599
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Baseline-Response-Delay-with-SQL-Injection

## Summary

This procedure tests for blind time-based SQL injection by injecting a short WAITFOR DELAY payload into the refresh_token parameter of the /api/v1/token endpoint, measuring response time to establish a baseline for SQL execution confirmation.

## Description

In a typical attack scenario targeting the Informatica tsftp API, unsanitized input in the refresh_token allows SQL concatenation. By appending '; WAITFOR DELAY '0:0:1'-- , the payload introduces a 1-second database delay if executed. This is observed via timed HTTP requests. Prerequisites include network access to the endpoint; no authentication is needed. Expected outcomes: delayed response confirming injection point.

## Requirements

1. Network access to https://tsftp.informatica.com on port 443
2. curl and time utilities installed
3. Basic understanding of HTTP POST requests and SQL syntax

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and prepared statements in API backend
- Use web application firewalls (WAF) to detect SQL keywords like WAITFOR
- Monitor database query logs for anomalous delays or injection patterns

## Objectives

1. Verify SQL injection vulnerability in refresh_token parameter
2. Measure baseline delay to differentiate from normal response times
3. Set foundation for further payload testing without data access

## Instructions

### Step 1: Prepare and Execute Baseline Delay Test

**Context**: Send a POST request to the token endpoint with the short delay payload to inject SQL and time the response.

**Command** ([[commands/curl-baseline-delay]]):
```bash
time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:1'--"
```

> This command uses time to measure execution, curl for the HTTP POST with form-urlencoded data containing the SQL payload. Expected output is a JSON error with ~2-second total time, including the 1-second delay, indicating SQL execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-baseline-delay]]

## Tools Used

- [[tools/curl]]
- [[tools/time]]

## Tags

- sqli
- blind-sqli
- time-based
