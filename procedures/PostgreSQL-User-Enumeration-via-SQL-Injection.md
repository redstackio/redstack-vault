---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploitation of Remote Services]]'
sub_techniques: []
tags:
  - postgresql
  - sql-injection
  - user-enumeration
  - database-discovery
commands:
  - '[[commands/postgresql-select-users-from-pg-user]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# PostgreSQL-User-Enumeration-via-SQL-Injection

## Summary

This procedure demonstrates how to enumerate valid usernames from a PostgreSQL database by injecting a SQL query to query the pg_user system table. It is typically used after gaining initial access through a SQL injection vulnerability in a web application connected to the database, allowing attackers to identify accounts for further attacks like password spraying or targeted credential attacks.

## Description

PostgreSQL stores user information in the pg_user system catalog table, where the 'usename' column lists all database users. By injecting the query 'SELECT usename FROM pg_user' via a SQL injection point (e.g., in a login form or search parameter), an attacker can extract this information without needing direct database credentials. This technique aids in account discovery during lateral movement or reconnaissance phases, enabling more precise follow-on exploits. It assumes the application has sufficient privileges to query system tables, which is common in misconfigured web apps. Success depends on the injection point allowing read access to system catalogs.

## Requirements

1. Valid SQL injection vulnerability in a web application connected to PostgreSQL (e.g., via UNION-based or error-based injection).
2. Knowledge of the injection point (e.g., URL parameter, POST data).
3. Tool for crafting and sending injected requests, such as [[tools/sqlmap]] or Burp Suite.
4. Network access to the target application.

## Defense

- Implement prepared statements and parameterized queries in all database interactions to prevent SQL injection.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns.
- Limit database user privileges to the minimum required for the application, avoiding SELECT access to system tables like pg_user.
- Monitor database query logs for unusual SELECT statements targeting system catalogs and enable alerting on failed or suspicious injections.

## Objectives

1. Extract a list of valid PostgreSQL usernames from the database.
2. Identify potential high-value accounts (e.g., admins) for targeted attacks.
3. Gather intelligence for subsequent exploitation, such as brute-forcing or privilege escalation.

## Instructions

### Step 1: Identify and Exploit SQL Injection Point

**Context**: Locate a vulnerable input field in the target web application that allows SQL injection, such as a search box or login form. Confirm the vulnerability using a standard payload like ' OR 1=1 -- to bypass authentication or return extra data.

Once confirmed, prepare to inject the user enumeration query. This step assumes a UNION-based injection where you append the query to the original legitimate query.

**Command** ([[commands/postgresql-select-users-from-pg-user]]):

```sql
SELECT usename FROM pg_user
```

> This SQL command queries the pg_user table to retrieve all usernames. In a UNION injection, append it to the application's query, e.g., via a URL parameter: ?id=1 UNION SELECT usename FROM pg_user --. Adjust based on the injection type (e.g., stacked queries with ;). Expected output will be embedded in the application's response, such as a dropdown or error message displaying usernames. If no output appears, try error-based injection to force the database to reveal data in error messages.

### Step 2: Extract and Analyze Results

**Context**: After injection, parse the application's response to collect the returned usernames. This may require tools like Burp Suite to intercept and modify requests.

Use the injected query and observe the response. If the application echoes results (e.g., in a user list page), copy them manually or automate with scripting.

**Command** ([[commands/postgresql-select-users-from-pg-user]]):

```sql
SELECT usename FROM pg_user
```

> Re-execute if needed to confirm. Expected output: A list like 'postgres', 'appuser', 'admin'. Cross-reference with known application users to identify privileged accounts. If the query fails due to privileges, attempt to escalate via other injections.
