---
id: 289bcfd4-0013-4e70-a8ec-3120a6132649
name: PostgreSQL-Time-Based-Blind-SQL-Injection-for-Table-Dump
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.881111+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Data from Information Repositories|T1213 - Data from
    Information Repositories]]
sub_techniques: []
tags:
  - postgresql
  - sql-injection
  - time-based
  - blind-sqli
  - table-dump
  - data-exfiltration
commands: []
platforms:
  - Web
  - Linux
  - Database
tools: []
validated: true
---

# PostgreSQL-Time-Based-Blind-SQL-Injection-for-Table-Dump

## Summary

This procedure exploits time-based blind SQL injection vulnerabilities in PostgreSQL databases to extract table names and contents by inferring data from response delays using the pg_sleep function. It is particularly useful in scenarios where error-based or union-based SQLi is not possible, allowing attackers to systematically dump database schema and sensitive data over multiple iterations.

## Description

Time-based blind SQL injection in PostgreSQL relies on injecting conditional logic that triggers a delay (via pg_sleep) only when a specific condition is true, enabling bit-by-bit or character-by-character data extraction based on whether the response is delayed. This procedure focuses on dumping table names from information_schema.tables and can be extended to column names or row data. It targets web applications with unsanitized inputs to PostgreSQL backends, such as login forms or search parameters. Success depends on precise timing measurements (e.g., 5-second delays) and iteration over possible character sets (a-z, 0-9). In a real attack, this could lead to exfiltration of user credentials, financial records, or other sensitive information stored in tables.

## Requirements

1. A vulnerable web application parameter injectable into PostgreSQL queries (e.g., via GET/POST requests).
2. Knowledge of the injection point and basic SQL syntax for PostgreSQL.
3. Tools for sending HTTP requests and measuring response times, such as Burp Suite or curl.
4. A timing baseline for normal responses (typically under 1 second) to distinguish delays.
5. Patience for iterative queries, as dumping a full table name may require 100+ requests per character.

## Defense

- Implement strict input validation, sanitization, and escaping for all user inputs using prepared statements or parameterized queries (e.g., via PDO in PHP or psycopg2 in Python).
- Use web application firewalls (WAFs) like ModSecurity to detect and block SQL injection patterns, including time-based payloads.
- Enable database logging for long-running queries (e.g., pg_sleep > 1 second) and monitor for anomalies using tools like pgBadger.
- Limit database user privileges to least-privilege access, avoiding SELECT on information_schema for application accounts.
- Conduct regular vulnerability scans with tools like sqlmap to identify blind SQLi exposures.

## Objectives

1. Confirm the presence of a time-based blind SQL injection vulnerability.
2. Enumerate and dump table names from the information_schema.tables view.
3. Extend to extract table contents for targeted data exfiltration.
4. Achieve full schema reconnaissance without triggering error messages.

## Instructions

### Step 1: Confirm Time-Based Blind SQL Injection Vulnerability

**Context**: Before dumping data, verify the injection point supports time delays by injecting a basic pg_sleep payload. This establishes a baseline for delayed vs. normal responses. Use a tool like Burp Suite to intercept and modify requests, measuring response times.

**Code** ([[codes/PostgreSQL-Basic-PG-Sleep-Test]]):

```sql
SELECT pg_sleep(5);
```

> Inject this into the vulnerable parameter (e.g., ' OR (SELECT pg_sleep(5))-- ). If the response takes ~5 seconds longer than a normal request, the vulnerability is confirmed. Normal responses should complete in <1 second. Repeat without the sleep to baseline timing.

### Step 2: Enumerate First Character of Table Names

**Context**: Start extracting table names by checking the first character of table_name in information_schema.tables. Iterate over possible characters (a-z, 0-9, _, etc.) using conditional pg_sleep. A delay indicates a match.

**Code** ([[codes/PostgreSQL-Time-Based-Table-Name-Character-Check]]):

```sql
SELECT CASE WHEN SUBSTRING(table_name,1,1)='a' THEN pg_sleep(5) ELSE pg_sleep(0) END FROM information_schema.tables LIMIT 1;
```

> Replace 'a' with each possible character and inject (e.g., via URL parameter: id=1' AND (CASE WHEN SUBSTRING... )-- ). Measure response time for each. A 5-second delay confirms the character. Log matches to reconstruct the name. This step typically requires 30-60 requests for alphanumeric sets.

### Step 3: Iterate for Subsequent Characters and Full Table Name

**Context**: Once the first character is found, advance to the second position (SUBSTRING(table_name,2,1)) and repeat the process. Continue until no more characters match (e.g., end of string inferred by no delay for length checks). Use LIMIT 1 to focus on one table at a time; adjust for multiple tables by adding conditions like table_schema='public'.

**Code** ([[codes/PostgreSQL-Time-Based-Table-Name-Character-Check]]):

```sql
SELECT CASE WHEN SUBSTRING(table_name,2,1)='u' THEN pg_sleep(5) ELSE pg_sleep(0) END FROM information_schema.tables LIMIT 1;
```

> Modify the position (e.g., 2,3,...) and character. To check string length first, use: SELECT CASE WHEN LENGTH(table_name)>=1 THEN pg_sleep(5) ELSE pg_sleep(0) END FROM information_schema.tables LIMIT 1; Increment until no delay. Combine findings to get full names like 'users' or 'admin_table'.

### Step 4: Dump Table Contents Using Time-Based Extraction

**Context**: With table names known, extract row data (e.g., from a 'users' table). Target specific columns like usernames or passwords, using similar conditional logic on column values. This extends the technique to actual data exfiltration.

**Code** ([[codes/PostgreSQL-Time-Based-Column-Value-Check]]):

```sql
SELECT CASE WHEN SUBSTRING((SELECT username FROM users LIMIT 1),1,1)='a' THEN pg_sleep(5) ELSE pg_sleep(0) END;
```

> Adapt the query to the target table/column (e.g., replace 'username' with actual column). Iterate positions and characters as in previous steps. For multiple rows, add OFFSET or conditions. Exfiltrate data by logging matches externally or via out-of-band channels if available.

### Step 5: Verify and Exfiltrate Dumped Data

**Context**: Reconstruct the extracted data into readable format and validate against known schema. If large, chain with encoding techniques for exfiltration over web responses.

> Manually compile character results into full strings (e.g., via a script tracking requests). Test by injecting a known SELECT query if possible. For exfiltration, base64-encode results if direct output is blocked, or use DNS/HTTP channels for blind scenarios.
