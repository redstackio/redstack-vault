---
id: ab835cb7-8549-4da6-935b-ff79388e6a4d
name: PostgreSQL-Database-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.665658+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/PostgreSQL]]'
  - '[[tags/Database-Enumeration]]'
  - '[[tags/SQL-Injection]]'
commands:
  - '[[commands/postgresql-list-databases]]'
platforms:
  - Linux
  - Database
tools: []
validated: true
---

# PostgreSQL-Database-Enumeration

## Summary

PostgreSQL Database Enumeration involves querying the PostgreSQL server's system catalog to list all available databases. This technique is commonly used in penetration testing or attack scenarios to map the database structure, identify potential targets for further exploitation, such as extracting sensitive data from specific databases via SQL injection or direct access.

## Description

In a typical attack scenario, an attacker gains initial access to a PostgreSQL instance, either through SQL injection in a web application, default credentials, or misconfigured remote access. Once connected, they execute queries against the pg_database system table to enumerate database names. This provides insight into the target's data architecture, revealing application databases, user databases, or administrative ones that may contain valuable information. The technique is low-level and relies on standard PostgreSQL internals, making it reliable across versions but detectable through query logging. It maps to the Discovery tactic in MITRE ATT&CK, as it gathers system information to inform subsequent actions like credential access or data exfiltration.

## Requirements

1. Valid connection to the PostgreSQL server (e.g., via psql client, SQL injection payload, or remote access on port 5432).
2. Sufficient privileges (typically any authenticated user can query pg_database, but superuser access reveals more details).
3. Tools like psql (PostgreSQL client) or a SQL injection framework such as sqlmap.
4. Knowledge of SQL syntax and potential injection points if not directly connected.

## Defense

- Enable query logging in PostgreSQL (log_statement = 'all') to monitor enumeration attempts.
- Implement prepared statements and input parameterization in applications to prevent SQL injection.
- Restrict database access using role-based permissions; revoke unnecessary SELECT rights on system catalogs.
- Use network firewalls to limit PostgreSQL exposure (e.g., bind to localhost or specific IPs) and enable SSL for connections.

## Objectives

1. Identify all databases on the PostgreSQL instance to map the target's data landscape.
2. Determine which databases may hold sensitive information for targeted follow-up queries.
3. Facilitate planning for deeper exploitation, such as table enumeration or data extraction.

## Instructions

### Step 1: Connect to the PostgreSQL Instance

**Context**: Establish a connection to the target PostgreSQL server using the psql client or inject the query via a vulnerable application. This step assumes you have credentials or an injection vector; replace placeholders with actual values.

If using psql directly:
```bash
psql -h $_HOST -U $_USERNAME -d postgres
```

> Enter the password when prompted. Successful connection is indicated by the psql prompt: `postgres=#`.

### Step 2: Execute Database Enumeration Query

**Context**: Run the SQL query to select database names from the pg_database system table. This reveals all databases visible to the current user, including system ones like 'postgres' and 'template1'.

**Command** ([[commands/postgresql-list-databases]]):
```sql
SELECT datname FROM pg_database;
```

> This query targets the 'datname' column in pg_database, which lists database names. It executes quickly and returns a simple list. If injected via a web app, wrap it in a UNION SELECT to bypass filters.

### Step 3: Analyze and Verify Results

**Context**: Review the output for user-created databases (ignore system ones). If no custom databases appear, check user privileges with `SELECT current_user; SELECT version();` to confirm access level.

**Expected Output** (from Step 2):
```
  datname  
-----------
 postgres
 template1
 template0
 myapp_db
 sensitive_data
(5 rows)
```

> Success is confirmed by a list of database names. Use this to pivot, e.g., connect to 'myapp_db' with `\c myapp_db` in psql or inject `SELECT * FROM information_schema.tables WHERE table_schema = 'public';` for table enumeration.

**Success Indicators**:
- Query executes without errors (e.g., no 'permission denied').
- List includes target-specific databases beyond defaults.
- No anomalies in PostgreSQL logs if testing in a controlled environment.
