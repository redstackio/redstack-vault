---
id: ff430666-de0e-40b1-bf26-eecb32c06e77
name: MySQL-Injection-Current-Queries
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.745365+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - mysql-injection
  - sql-injection
  - processlist-enumeration
  - database-reconnaissance
commands: []
platforms:
  - Web
  - MySQL
tools: []
validated: true
---

# MySQL-Injection-Current-Queries

## Summary

This procedure demonstrates how to exploit a SQL injection vulnerability in a MySQL-backed web application to enumerate current database queries and connections using the INFORMATION_SCHEMA.PROCESSLIST table. By injecting a UNION SELECT statement, an attacker can extract details on active threads, states, and query information (info field), revealing ongoing database operations, user sessions, and potentially sensitive query contents without direct database access.

## Description

SQL injection remains a prevalent vulnerability in web applications that fail to properly sanitize user inputs, allowing attackers to append or modify SQL queries. This procedure targets MySQL databases specifically, leveraging the INFORMATION_SCHEMA.PROCESSLIST view to list all active client connections and server threads. The 'state' column indicates the current operation (e.g., 'executing', 'waiting for table metadata'), while the 'info' column shows the actual SQL query being executed. This reconnaissance can expose administrative queries, reveal database schema indirectly, or identify other users' activities. It is typically used in the initial access or discovery phase of an attack to map the database environment and identify further exploitation opportunities, such as hijacking sessions or extracting data from running queries. The technique assumes a blind or error-based SQL injection point, often in search fields, login forms, or URL parameters.

## Requirements

1. Identification of a SQL injection vulnerability in the web application (e.g., via tools like [[tools/sqlmap]] or manual testing with single quotes).
2. Knowledge of the number of columns in the original query to match the UNION SELECT (determined through ORDER BY testing or error messages).
3. Network access to the vulnerable web endpoint.
4. Basic understanding of MySQL syntax and injection payloads.
5. Optional: A proxy like [[tools/Burp-Suite]] to intercept and modify requests.

## Defense

- Use prepared statements and parameterized queries in application code to separate SQL logic from user input.
- Implement web application firewalls (WAFs) to detect and block common injection patterns, such as UNION SELECT or references to INFORMATION_SCHEMA.
- Enable MySQL query logging and monitor for anomalous access to system tables like PROCESSLIST.
- Apply least privilege to database users, restricting access to INFORMATION_SCHEMA for application accounts.
- Regularly audit and patch web applications using frameworks that include built-in SQLi protections (e.g., OWASP guidelines).

## Objectives

1. Enumerate active database connections and their states to understand ongoing operations.
2. Extract the 'info' field to reveal executed SQL queries, potentially exposing sensitive data or logic.
3. Identify vulnerabilities for further exploitation, such as targeting specific user sessions or queries.
4. Gather intelligence on the database environment without triggering obvious alerts.

## Instructions

### Step 1: Confirm SQL Injection Vulnerability

**Context**: Before injecting payloads, verify the endpoint is vulnerable to SQL injection. This step ensures the application echoes errors or delays that confirm input manipulation affects the backend query.

Test with a single quote or boolean-based payload to cause a syntax error or observable change.

> Manually craft a request to the vulnerable parameter (e.g., a search field: `?search='`) and observe for MySQL error messages like "You have an error in your SQL syntax" or union-based column mismatches.

**Expected Output**: Database error revealing MySQL version or syntax issues, confirming injection point.

### Step 2: Determine Query Column Count

**Context**: UNION SELECT requires matching the number of columns in the original query. Use ORDER BY to probe this incrementally (e.g., start with ORDER BY 1, increase until error).

Inject payloads like `?id=1' ORDER BY 1--` up to `ORDER BY N--` until an error occurs, indicating the column count (N-1).

**Expected Output**: Successful responses up to the correct count; error like "Unknown column" beyond it.

### Step 3: Inject UNION SELECT to Dump Processlist

**Context**: Once columns are matched (assume 4 for this example), inject the UNION SELECT to pull from INFORMATION_SCHEMA.PROCESSLIST. This step extracts state and info for all threads, providing a snapshot of current queries.

Use the following payload in the vulnerable parameter:

**Code** ([[codes/MySQL-Union-Select-Processlist-Dump]]):

```sql
union SELECT 1,state,info,4 FROM INFORMATION_SCHEMA.PROCESSLIST #
```

> This payload appends a union to the original query, selecting dummy values for the first and last columns, 'state' for the second, and 'info' (the current query) for the third. The # comments out the rest of the original query. Expected output will display in the application's response, showing rows like ID, 'executing', 'SELECT * FROM users', etc.

For a concatenated one-shot dump of all states and infos:

**Code** ([[codes/MySQL-Union-Select-Processlist-Dump]]):

```sql
-- Dump in one shot example for the table content.
union select 1,(select(@)from(select(@:=0x00),(select(@)from(information_schema.processlist)where(@)in(@:=concat(@,0x3C62723E,state,0x3a,info))))a),3,4 #
```

> This uses a variable (@) to concatenate all state:info pairs into a single field, separated by <br>, allowing bulk extraction in one response. It leverages MySQL's user-defined variables for accumulation during the subquery.

**Expected Output**: Application response rendering the dumped data, e.g., a table or text showing multiple states and queries like "executing: SELECT password FROM users WHERE id=1".

### Step 4: Analyze and Validate Results

**Context**: Review the extracted data for actionable intelligence, such as admin queries or long-running operations that could be exploited further.

Parse the output manually or with a script to separate states and infos. Verify no errors in the injection by checking for complete rows without original query data leakage.

**Expected Output**: List of active connections with queries; success if at least one non-trivial query (e.g., not the injected one) is visible.

### Step 5: Clean Up and Evade Detection

**Context**: After enumeration, test for logging by injecting a time-based payload (e.g., SLEEP(5)) to check for delays, then cease activity to avoid alerts.

Monitor application logs if accessible, or use non-persistent payloads.

**Expected Output**: No immediate bans or errors post-exploitation, confirming low detection.
