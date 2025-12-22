---
id: 6b94984d-102a-4ebe-9ba9-4f81e1f06c3b
name: SQLite-Schema-Extraction-via-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.970932+00:00'
updated_at: '2023-04-10T20:24:32.288824+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/SQLite Injection]]'
  - '[[tags/Database Schema Extraction]]'
  - '[[tags/SQL Injection]]'
commands:
  - '[[commands/sqlite-select-schema-sql]]'
platforms:
  - Web
tools: []
validated: true
---

# SQLite-Schema-Extraction-via-Injection

## Summary

This procedure outlines how to extract the schema of an SQLite database through SQL injection vulnerabilities in a web application. By injecting a targeted SQL query, an attacker can retrieve the SQL statements defining tables, indexes, and other structures, providing insights into the database layout for further exploitation such as data extraction or privilege escalation.

## Description

SQLite databases are commonly embedded in web applications for lightweight data storage. A SQL injection vulnerability allows arbitrary SQL commands to be executed against the backend database. This procedure focuses on dumping the schema using the built-in `sqlite_schema` table, which stores CREATE statements for all database objects. This technique is useful in reconnaissance phases to map data structures, identify sensitive tables (e.g., users, credentials), and plan subsequent attacks like targeted data dumping. It assumes a classic SQLi vulnerability where user input is concatenated into queries without sanitization. Success depends on the injection point allowing read access to system tables.

## Requirements

1. Access to a web application with a confirmed SQL injection vulnerability targeting an SQLite backend.
2. Knowledge of SQL injection payloads and error-based or union-based exploitation techniques.
3. Tools for crafting and sending HTTP requests, such as [[tools/Burp-Suite]] or curl.
4. Basic understanding of SQLite syntax and web application architecture.

## Defense

- Implement parameterized queries or prepared statements to prevent injection.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns.
- Regularly audit database access logs for unauthorized schema queries.
- Limit database user privileges to deny access to system tables like `sqlite_schema`.

## Objectives

1. Confirm the ability to execute arbitrary SQL via injection.
2. Retrieve the full database schema including table and index definitions.
3. Analyze the schema to identify potential targets for data exfiltration.

## Instructions

### Step 1: Identify and Confirm SQL Injection Point

**Context**: Locate an input field (e.g., login form, search box) vulnerable to SQL injection and confirm it targets an SQLite database. Use error-based or time-based payloads to verify injectability and database type.

**Command** (use a generic SQLi test like [[commands/sqlmap-test-injection]] or manual payload):

```sql
' OR 1=1 --
```

> Inject this into the vulnerable parameter and observe if it alters query behavior (e.g., bypasses login or returns all records). For SQLite confirmation, inject `'; SELECT sqlite_version() --` and check for version output in errors or responses. If successful, proceed; otherwise, try different payloads or points.

### Step 2: Craft and Inject Schema Extraction Query

**Context**: Use the confirmed injection point to execute a query that selects from the `sqlite_schema` table. This reveals CREATE statements for all objects, helping map the database structure without needing direct DB access.

**Command** ([[commands/sqlite-select-schema-sql]]):

```sql
SELECT sql FROM sqlite_schema;
```

> Append this to your injection payload, e.g., in a UNION-based attack: `' UNION SELECT sql FROM sqlite_schema --`. Send via POST/GET request to the endpoint. The response should include SQL CREATE statements if the injection succeeds. Use tools like Burp to capture and modify requests. If the output is truncated, iterate with LIMIT clauses (e.g., `LIMIT 10 OFFSET 0`).

### Step 3: Analyze Retrieved Schema

**Context**: Parse the dumped schema to understand table names, columns, and relationships. Look for sensitive tables like `users` or `credentials`.

No specific command needed; manually review output.

> Expected schema output includes lines like `CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);`. Document table structures and plan next steps, such as dumping specific tables with `SELECT * FROM table_name`. Verify completeness by checking for indexes and views.

### Step 4: Verify and Mitigate Exposure

**Context**: Ensure the extraction is complete and test for further access. This step confirms success and identifies if additional injections are possible.

**Command** (follow-up query):

```sql
SELECT name FROM sqlite_schema WHERE type='table';
```

> Inject this to list table names only. Cross-reference with full schema. Success is indicated by a complete list without errors.
