---
id: 7e89b582-71cb-45bb-9086-539c72ce75cf
name: PostgreSQL-Column-Enumeration-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.724518+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
sub_techniques: []
tags:
  - '[[tags/PostgreSQL injection]]'
  - '[[tags/PostgreSQL List Columns]]'
  - sql-injection
  - database-enumeration
commands:
  - '[[commands/postgresql-select-columns-from-information-schema]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# PostgreSQL-Column-Enumeration-via-SQL-Injection

## Summary

This procedure demonstrates how to enumerate column names from a specific table in a PostgreSQL database using SQL injection. By injecting a query that targets the information_schema.columns view, attackers can extract schema details to facilitate further exploitation, such as targeted data exfiltration or identifying sensitive fields for privilege escalation.

## Description

In a typical attack scenario, an attacker identifies a SQL injection vulnerability in a web application connected to a PostgreSQL backend. The injection point allows arbitrary SQL execution, enabling queries against system views like information_schema.columns, which contains metadata about all tables and their columns. This technique is particularly useful in reconnaissance phases to map the database structure without direct administrative access. It assumes the application uses a vulnerable parameterized query or lacks input sanitization. Success depends on the injection being blind or error-based, where partial outputs can be inferred from responses. This maps to discovery tactics in MITRE ATT&CK, aiding in broader data collection or execution chains.

## Requirements

1. Valid SQL injection vulnerability in a web application or direct database access point.
2. Knowledge of the target table name (e.g., via prior enumeration of table names).
3. Tools for injecting and observing SQL payloads, such as a proxy like Burp Suite or sqlmap.
4. Network access to the application/database endpoint.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to block injection payloads.
- Use prepared statements or parameterized queries to separate code from user input.
- Enforce the principle of least privilege by limiting database user permissions to read-only on application schemas.
- Monitor database logs for anomalous queries accessing information_schema or unusual SELECT patterns on metadata tables.
- Deploy web application firewalls (WAFs) tuned to detect SQL injection attempts targeting system views.

## Objectives

1. Extract column names from a specified PostgreSQL table to understand the schema.
2. Identify potential sensitive columns (e.g., passwords, credit cards) for targeted attacks.
3. Validate the injection point's capabilities for deeper exploitation.

## Instructions

### Step 1: Identify Injection Point and Test Basic Access

**Context**: Confirm the SQL injection vulnerability exists and can execute SELECT queries. This step ensures the payload can reach the database without errors.

Use a basic injection test like appending ' AND 1=1 -- to a login or search field and observe if the application behaves differently (e.g., true condition passes).

### Step 2: Inject Query to Enumerate Columns

**Context**: Once injection is confirmed, craft and inject the SQL query to retrieve column names for the target table. Replace 'data_table' with the actual table name obtained from prior enumeration (e.g., via querying information_schema.tables).

**Command** ([[commands/postgresql-select-columns-from-information-schema]]):
```sql
SELECT column_name FROM information_schema.columns WHERE table_name='data_table'
```

> This query filters the information_schema.columns view to return only column names for the specified table. In a blind injection scenario, use conditional techniques (e.g., IF statements or time-based delays) to extract results character by character if direct output is not visible. For error-based injection, leverage PostgreSQL's error messages to leak data. Expected output includes a list of column names, such as 'id', 'username', 'password'.

### Step 3: Verify and Extract Results

**Context**: Observe the application's response for leaked data, errors, or behavioral changes indicating success. If using a tool like sqlmap, automate extraction with options like --dump or --schema.

If results are not directly visible, iterate with UNION-based injection to append the query results to a legitimate response:
```sql
' UNION SELECT column_name FROM information_schema.columns WHERE table_name='data_table' --
```

> Success is confirmed if column names appear in the response or if database logs show the query execution without syntax errors.
