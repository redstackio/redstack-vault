---
type: procedure
description: >-
  Detect SQL injection vulnerabilities in a web application using sqlmap with a
  captured HTTP request file and mobile user-agent simulation to bypass certain
  protections.
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - sql-injection
  - sqlmap
  - web-vulnerability
  - detection
commands:
  - '[[commands/sqlmap-detect-sqli-with-request-file-mobile]]'
tools:
  - '[[tools/sqlmap]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Detect-SQL-Injection-with-Sqlmap-Using-Request-File-and-Mobile-User-Agent

## Summary

This procedure uses the sqlmap tool to detect SQL injection vulnerabilities in a web application by loading a captured HTTP request file that includes a potentially vulnerable parameter. It simulates a mobile device user-agent to potentially evade web application firewalls or other detection mechanisms that target desktop browsers, allowing for more stealthy testing of injection points.

## Description

SQL injection (SQLi) is a critical web vulnerability where untrusted input is concatenated into SQL queries, enabling attackers to manipulate database operations, extract sensitive data, or execute arbitrary commands. Sqlmap automates the detection and exploitation of SQLi flaws by analyzing HTTP requests and injecting payloads. In this procedure, a request file (typically captured via tools like Burp Suite) is used to replay the exact request context, ensuring accurate testing of specific endpoints. The --mobile flag spoofs a mobile user-agent (e.g., mimicking an iOS or Android browser), which can bypass filters tuned for standard desktop traffic. This approach is useful in red team engagements targeting mobile-responsive web apps or when initial scans with default agents fail due to user-agent-based blocking. The procedure focuses on detection but can extend to exploitation if vulnerabilities are confirmed. Prerequisites include network access to the target and a properly formatted request file pointing to the injectable parameter.

## Requirements

1. Network access to the target web application (e.g., via VPN or direct connectivity).
2. A captured HTTP request file (e.g., in Burp Suite format) containing the vulnerable parameter and endpoint.
3. Sqlmap tool installed on a Linux-based system like Kali.
4. Basic knowledge of HTTP requests and SQL injection payloads.

## Defense

- Implement prepared statements and parameterized queries in application code to separate SQL logic from user input.
- Use web application firewalls (WAFs) with SQLi rules enabled, including user-agent validation to detect anomalous traffic.
- Employ input sanitization and output encoding for all user-supplied data interacting with the database.
- Monitor application logs for suspicious SQL patterns or failed queries, and enable database auditing for injection attempts.

## Objectives

1. Identify SQL injection vulnerabilities in the specified HTTP request endpoint.
2. Confirm the injectable parameter and assess the vulnerability severity (e.g., blind, error-based, or union-based).
3. Gather evidence of successful injection without full exploitation, such as boolean responses or time delays.

## Instructions

### Step 1: Prepare the Request File

**Context**: Capture or create an HTTP request file that includes the target endpoint and the parameter suspected of being vulnerable to SQLi. This ensures sqlmap tests the exact request context, including headers, cookies, and POST data.

Use a proxy tool like Burp Suite to intercept a legitimate request to the target, save it as a .req file, and identify the injectable parameter (e.g., 'id=1' in a GET or POST field).

**Expected Output**: A file like 'sqli.req' with the full HTTP request, including the vulnerable parameter marked for testing (sqlmap will auto-detect, but you can specify with --data or --string).

### Step 2: Run Sqlmap Detection with Mobile User-Agent

**Context**: Execute sqlmap using the prepared request file, specifying a safe URL for baseline testing and enabling mobile simulation to mimic a mobile browser, which may evade desktop-specific defenses. The --safe-freq controls the delay between tests to avoid rate-limiting.

**Command** ([[commands/sqlmap-detect-sqli-with-request-file-mobile]]):
```bash
sqlmap -r sqli.req --safe-url=http://target.example.com/ --mobile --safe-freq=1
```

> This command loads the request from 'sqli.req', uses 'http://target.example.com/' as a non-injectable baseline for comparison, enables mobile user-agent spoofing, and waits 1 second between tests. Sqlmap will probe for SQLi by injecting payloads and analyzing responses for anomalies like errors, delays, or data leaks.

**Expected Output**: Sqlmap outputs a summary of tested parameters, injection techniques (e.g., boolean-based blind, time-based blind), and payloads that succeeded. For example:
```
[INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Apache 2.4.29, PHP 7.2.0
back-end DBMS: MySQL >= 5.0
[INFO] retrieved in 5 queries: current user is 'webapp@localhost'
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1' AND 1236=1236--
```

### Step 3: Analyze and Verify Results

**Context**: Review sqlmap's output to confirm vulnerability details, such as the injection type and affected database. If detected, note the parameter and technique for further exploitation or reporting.

Manually verify by replaying a confirmed payload in the request file using a tool like curl, observing database errors or unexpected behavior.

**Expected Output**: Confirmation of vulnerable parameters with risk level (e.g., 'Payload confirmed') and suggestions for next steps like --dbs or --tables if exploitation is authorized.

**Success Indicators**:
- Sqlmap identifies at least one injectable parameter with a specific technique.
- No false positives confirmed by manual testing.
- Mobile user-agent successfully applied without blocking (check logs for WAF hits).
