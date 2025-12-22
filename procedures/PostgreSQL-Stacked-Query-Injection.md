---
id: 7e257717-ee01-4a1a-9c74-5d3cd36ab7a5
name: PostgreSQL-Stacked-Query-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.910824+00:00'
updated_at: '2023-04-10T20:23:14.029348+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/PostgreSQL injection]]'
  - '[[tags/PostgreSQL Stacked Query]]'
  - sql-injection
  - database-exploitation
commands:
  - '[[commands/curl-send-stacked-sqli-payload]]'
platforms:
  - Web
  - PostgreSQL
tools: []
validated: true
---

# PostgreSQL-Stacked-Query-Injection

## Summary

PostgreSQL Stacked Query Injection exploits vulnerabilities in web applications using PostgreSQL databases by injecting multiple SQL statements separated by semicolons, allowing attackers to execute arbitrary commands beyond the intended single query. This technique bypasses basic input validation to create tables, insert data, or exfiltrate information, commonly used in penetration testing to demonstrate data manipulation or extraction risks.

## Description

In a typical attack scenario, an attacker identifies a web application parameter (e.g., an ID in a URL query string) that is directly concatenated into a SQL query without proper sanitization. By appending a semicolon (;) after the legitimate input and adding a second malicious query, the attacker forces the database to execute both statements. For PostgreSQL, this 'stacked' approach works because the database supports multiple statements per request, unlike some other RDBMS that limit to single queries. This can lead to outcomes like creating unauthorized tables, dumping sensitive data, or escalating privileges if the application runs with elevated database permissions. The target environment is usually a web-facing application on Linux/Unix servers with PostgreSQL as the backend, requiring no special privileges beyond network access to the app.

## Requirements

1. Network access to a vulnerable web application using PostgreSQL as the database backend.
2. Knowledge of the application's input parameters vulnerable to SQL injection (e.g., via error-based or union-based testing).
3. Tools for sending HTTP requests, such as curl, and basic understanding of SQL syntax for PostgreSQL.
4. Optional: A proxy like Burp Suite for intercepting and modifying requests during testing.

## Defense

- Use prepared statements or parameterized queries in application code to separate SQL logic from user input.
- Implement web application firewalls (WAFs) to detect and block common SQL injection patterns, including stacked queries.
- Sanitize and validate all user inputs, escaping special characters like semicolons.
- Regularly audit database permissions to ensure the application user has minimal privileges (e.g., no CREATE TABLE rights).
- Enable PostgreSQL logging for failed queries and monitor for anomalous statement executions.

## Objectives

1. Execute arbitrary SQL commands, such as creating new tables or inserting data, to demonstrate control over the database.
2. Extract sensitive information by stacking SELECT statements to bypass restrictions.
3. Modify existing data to simulate persistence or disruption, highlighting the impact of insufficient input validation.

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: First, confirm the injection point by testing for basic SQL errors or delays. This step verifies that the parameter allows SQL injection, setting the stage for stacked queries.

Use error-based payloads like appending ' OR 1=1-- to observe database errors revealing PostgreSQL specifics.

> If no errors appear, try time-based blind injection with pg_sleep(5) to confirm.

### Step 2: Craft and Send Stacked Query Payload

**Context**: Construct the payload to terminate the original query with a semicolon and append a malicious statement, such as creating a table. This exploits PostgreSQL's support for multiple statements to execute the second query.

**Command** ([[commands/curl-send-stacked-sqli-payload]]):
```bash
curl "http://$_TARGET_HOST/vuln.php?id=$_INJECTION_PAYLOAD" -v
```

> Replace $_TARGET_HOST with the vulnerable application's URL (e.g., target.com) and $_INJECTION_PAYLOAD with the stacked injection like 'injection';create table NotSoSecure (data varchar(200));--. The -- comments out any trailing code. Expected output includes a successful HTTP response without errors, and subsequent database checks (if accessible) confirm the new table creation.

### Step 3: Verify Execution and Insert Data

**Context**: After creation, stack another query to insert data into the new table, confirming full control and demonstrating data persistence.

Modify the payload to: 'injection';insert into NotSoSecure (data) values ('Injected Data');-- and resend using the same command.

> Decision point: If the table already exists, use DROP TABLE first in a stacked query. Success is verified by querying the table (if direct DB access) or observing application behavior changes.

### Step 4: Extract or Escalate

**Context**: Extend the stack to exfiltrate data, such as union-based selects or dumping user tables, to achieve the objective of data collection.

Example stacked payload for extraction: 'injection';SELECT * FROM users INTO OUTFILE '/tmp/dump.txt';-- (requires file write perms).

> Monitor for application errors or use blind techniques if output is not directly visible. If successful, the data is manipulated or exposed.
