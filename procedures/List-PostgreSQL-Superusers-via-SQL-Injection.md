---
type: procedure
description: >-
  Exploit SQL injection in PostgreSQL-backed web applications to enumerate
  superuser accounts.
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.549012+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - postgresql
  - sql-injection
  - database-discovery
commands:
  - '[[commands/postgresql-select-superusers-from-pg-user]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# List-PostgreSQL-Superusers-via-SQL-Injection

## Summary

This procedure outlines how to exploit SQL injection vulnerabilities in web applications connected to a PostgreSQL database to execute a query that lists all superuser accounts. Superusers in PostgreSQL have administrative privileges, making this information valuable for identifying high-privilege targets for further exploitation, such as privilege escalation or data exfiltration.

## Description

SQL injection (SQLi) occurs when user input is not properly sanitized, allowing attackers to append or modify SQL queries executed by the database. In PostgreSQL, the system catalog table `pg_user` stores user information, including the `usesuper` boolean flag that indicates superuser status. By injecting a payload that selects `usename` from `pg_user` where `usesuper` is TRUE, an attacker can retrieve a list of database administrators. This technique is typically used during reconnaissance in web application penetration testing or red team engagements targeting database-backed services. The attack assumes the application uses a vulnerable parameter (e.g., login form, search field) and that the database user has sufficient permissions to query system tables. Success enables discovery of admin accounts for subsequent attacks like credential dumping or lateral movement within the database environment.

## Requirements

1. Access to a web application vulnerable to SQL injection, interacting with a PostgreSQL backend.
2. Identification of an injectable parameter (e.g., via error-based or union-based SQLi testing).
3. Basic knowledge of SQL syntax and PostgreSQL system catalogs.
4. Tools for crafting and sending HTTP requests (manual via browser dev tools or proxy like Burp Suite; not required but recommended for complex injections).
5. Network access to the target application (e.g., over HTTP/HTTPS).

## Defense

- Implement prepared statements and parameterized queries to prevent SQL injection.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns.
- Apply least privilege principles: Limit application database users to read-only access on necessary tables, excluding system catalogs like `pg_user`.
- Enable PostgreSQL logging for failed queries and monitor for unusual SELECTs on system tables.
- Regularly audit database users and revoke unnecessary superuser privileges.

## Objectives

1. Identify and exploit an SQL injection point in the target application.
2. Execute a query to retrieve superuser usernames from the PostgreSQL `pg_user` table.
3. Compile a list of database administrators for targeting in further attacks.
4. Verify the output to confirm superuser discovery without alerting defenses.

## Instructions

### Step 1: Identify SQL Injection Vulnerability

**Context**: Locate a parameter in the web application that is vulnerable to SQL injection. This could be a login form, search box, or URL parameter. Test for vulnerability by appending a single quote (`'`) or other SQL metacharacters and observing errors or unexpected behavior.

**Instructions**: Send a test payload like `username=admin' OR '1'='1` to a login endpoint. If the application returns a database error (e.g., PostgreSQL syntax error) or bypasses authentication, an injection point is confirmed. Use error-based SQLi to extract database version and confirm PostgreSQL backend.

**Expected Output**: Database error messages revealing PostgreSQL details, such as "ERROR: syntax error at or near \"\"" or version info like "PostgreSQL 13.0".

### Step 2: Craft and Execute Superuser Enumeration Query

**Context**: Once the injection point is confirmed, construct a payload to execute the superuser listing query. This step unions the malicious SELECT with the original query or uses a subquery/time-based technique if union is not feasible. The goal is to force the database to run the `SELECT usename FROM pg_user WHERE usesuper IS TRUE` query and return results in the application response.

**Command** ([[commands/postgresql-select-superusers-from-pg-user]]):

```sql
SELECT usename FROM pg_user WHERE usesuper IS TRUE;
```

**Instructions**: Inject the query via the vulnerable parameter. For union-based SQLi, append: `'; [query] UNION SELECT usename FROM pg_user WHERE usesuper IS TRUE --`. Replace `[query]` with a null or matching column count from the original query (e.g., `UNION SELECT NULL, NULL, (SELECT usename FROM pg_user WHERE usesuper IS TRUE)`). Submit the payload and extract results from the response. If the application echoes query results (e.g., in a user list), superusers will appear inline.

> This command queries the `pg_user` system table, filtering for users with superuser privileges. It returns usernames only, avoiding verbose output. In a successful injection, results integrate into the application's response, such as displaying admin usernames in a dropdown or error message.

**Expected Output**: A list of superuser names, e.g.,

```
usename
---------
postgres
admin_user
```

Or embedded in the web response: "Users: postgres, admin_user".

### Step 3: Validate and Document Results

**Context**: Confirm the extracted accounts are valid superusers and assess their potential for further exploitation. Cross-reference with known application users to identify high-value targets.

**Instructions**: If multiple superusers are listed, note any default or custom names (e.g., `postgres` is common). Test if the injection allows further queries, like checking user roles with `\du` in psql (if direct access is gained later). Document usernames for use in subsequent procedures, such as attempting default credential logins or privilege escalation.

**Expected Output**: Verified list of superusers without errors; no application crashes or alerts triggered.

**Success Indicators**:
- Query executes without syntax errors.
- Superuser names appear in the response.
- No immediate defensive responses (e.g., IP blocks).
