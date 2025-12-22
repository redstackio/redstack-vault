---
id: a61fcfb4-4044-4418-9826-f65cab39c725
name: DB2-Current-Server-Query
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.726585+00:00'
updated_at: '2023-04-10T20:21:59.021854+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
  - >-
    [[techniques/Exploitation-of-Remote-Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/DB2]]'
  - '[[tags/Database-Discovery]]'
  - '[[tags/SQL-Injection]]'
commands:
  - '[[commands/db2-select-current-server]]'
platforms:
  - Database
  - DB2
tools: []
validated: true
---

# DB2-Current-Server-Query

## Summary

The DB2 Current Server Query procedure retrieves the name of the currently connected server in a DB2 database environment. This is useful during reconnaissance to confirm the database connection details, identify the infrastructure setup, and assess the scope of access, particularly when exploiting SQL injection vulnerabilities in web applications connected to DB2.

## Description

In database exploitation scenarios, understanding the current server context is crucial for mapping the target's infrastructure. This procedure involves executing a specific SQL query against a DB2 instance, often via an SQL injection point in a vulnerable application. The query targets system views to extract server information without requiring elevated privileges. It helps attackers verify connectivity in multi-server setups and plan further actions like lateral movement or data enumeration. This technique assumes initial access through a SQL injection vulnerability and focuses on passive discovery to avoid alerting defenses.

## Requirements

1. Valid SQL injection point in a web application or direct access to execute SQL queries against the DB2 database.
2. Knowledge of the injection vulnerability, such as an unparameterized query in user input fields.
3. Basic tools for testing injections, like a browser or proxy (e.g., Burp Suite).
4. DB2 database version supporting sysibm.sysdummy1 view (most versions do).

## Defense

- Implement prepared statements and parameterized queries to prevent SQL injection.
- Enforce least privilege access to database views and system tables.
- Monitor database logs for anomalous queries accessing system information.
- Use web application firewalls (WAFs) to detect and block injection attempts.

## Objectives

1. Retrieve the name of the current DB2 server to confirm connection context.
2. Identify potential multi-server environment details for further reconnaissance.
3. Assess access level by verifying successful query execution without errors.

## Instructions

### Step 1: Identify SQL Injection Point

**Context**: Locate a user input field vulnerable to SQL injection, such as a login form or search box, that interacts with the DB2 backend. Test for injection by appending a single quote (') and observing errors indicating SQL parsing issues. This step ensures you have a viable entry point for injecting the query.

**Command** ([[commands/db2-select-current-server]]):

Use a tool like sqlmap or manual payload crafting to test and confirm the injection. For manual testing:

```sql
' UNION SELECT 1 FROM sysibm.sysdummy1--
```

> This basic union-based injection confirms writability and readability from system tables. Expected output: No syntax errors and successful query execution, possibly displaying a dummy value like '1'.

### Step 2: Craft and Inject the Current Server Query

**Context**: Once the injection point is confirmed, modify the payload to include the specific query for the current server. This extracts infrastructure details without disrupting the application flow. Use union-based injection to append the query to the original legitimate query.

**Code** ([[codes/db2-select-current-server-sql]]):

```sql
select current server from sysibm.sysdummy1
```

> Integrate this into the injection payload, e.g., `' UNION SELECT current server FROM sysibm.sysdummy1--`. This step reveals the server name, helping verify the target environment. Expected output: The server name (e.g., 'DBSERVER01') returned in the response, confirming successful injection and access to system views.

### Step 3: Verify and Interpret Output

**Context**: Analyze the response from the injected query to confirm the server details and check for any access restrictions. If the output is truncated or error-prone, adjust the payload (e.g., using subqueries). This validates the procedure's success and informs next steps like version enumeration.

No specific command here; review the application response.

> Look for the server name in the HTML output or error messages. If successful, note the server for logging or further queries. Expected output: Clear server identifier without database errors. If errors occur (e.g., permission denied), the access level is limited to read-only on certain views.
