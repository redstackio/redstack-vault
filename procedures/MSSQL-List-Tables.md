---
id: 9e79f41a-6268-45f4-bcdb-1249e3cb393b
type: procedure
name: MSSQL-List-Tables
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.715890+00:00'
updated_at: '2023-04-10T20:22:43.807048+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/MSSQL]]'
  - '[[tags/SQL-Injection]]'
  - '[[tags/Database-Enumeration]]'
commands: []
platforms:
  - Database
  - Windows
tools: []
validated: true
---

# MSSQL-List-Tables

## Summary

This procedure outlines how to enumerate tables, columns, and database structures in Microsoft SQL Server (MSSQL) databases using SQL injection techniques. By injecting targeted SQL queries into a vulnerable web application or direct database access, attackers can discover the schema to identify sensitive data locations for further exploitation.

## Description

In SQL injection attacks against MSSQL databases, enumerating tables and columns is a key discovery step to map the database structure. This involves crafting union-based or error-based injections to execute system table queries like those targeting sysobjects or information_schema. The technique exploits insufficient input sanitization in web applications connected to MSSQL, allowing arbitrary query execution. It is typically used after confirming SQLi vulnerability to pivot to data extraction or privilege escalation. Success depends on the database user's permissions, often requiring at least db_datareader role. This procedure assumes a confirmed SQLi point and focuses on safe, comment-terminated queries to avoid breaking the application.

## Requirements

1. Confirmed SQL injection vulnerability in a web application backed by MSSQL.
2. Basic knowledge of SQL syntax and injection payloads (e.g., union select, stacked queries).
3. Tools for crafting and sending requests, such as a browser, curl, or Burp Suite.
4. Network access to the target application; direct MSSQL access if authenticated.
5. Sufficient database permissions to query system views (e.g., public role or higher).

## Defense

- Implement strict input validation and sanitization to block malicious SQL payloads.
- Use parameterized queries or prepared statements in application code to separate SQL from user input.
- Apply least privilege principles: Run database applications with minimal permissions (e.g., no sysadmin role).
- Enable database logging (e.g., SQL Server Audit) to detect anomalous queries to system tables.
- Deploy web application firewalls (WAFs) tuned to detect SQLi patterns targeting schema enumeration.

## Objectives

1. Retrieve a list of user tables in the current or specified database.
2. Enumerate columns and data types for targeted tables to prepare for data extraction.
3. Identify tables across all databases for broader reconnaissance.
4. Gather schema information to support subsequent attacks like data exfiltration.

## Instructions

### Step 1: Confirm SQL Injection and Prepare Payload

**Context**: Before enumerating, verify the injection point allows query execution. Append a comment to test without altering output, then prepare to inject schema queries using union-based injection if the original query returns data.

Identify the number of columns in the original query (e.g., via order by or union select nulls) and craft a payload like: `' UNION SELECT name FROM master..sysobjects WHERE xtype='U' --`

Use the code snippet [[codes/MSSQL-Enumerate-Tables-Columns-and-Databases]] for the base queries.

### Step 2: List User Tables in Current Database

**Context**: This step retrieves all user-created tables (xtype='U') in the current database, excluding system objects, to identify potential data stores like user accounts or logs.

Inject the first query from [[codes/MSSQL-Enumerate-Tables-Columns-and-Databases]] via the vulnerable parameter.

**Expected Output**: A list of table names, such as 'Users', 'Orders', 'Products'.

### Step 3: List Tables in a Specific Database

**Context**: If database names are known (e.g., from error messages), target another database to expand enumeration without switching contexts, useful for multi-DB environments.

Replace 'someotherdb' in the second query from [[codes/MSSQL-Enumerate-Tables-Columns-and-Dabases]] with the target database name and inject.

**Expected Output**: Table names from the specified database.

If access denied, the user lacks cross-database permissions—fall back to current DB.

### Step 4: Enumerate Columns for a Specific Table

**Context**: Once tables are identified, query column names and types to understand data structure, enabling targeted selects (e.g., extracting passwords from a 'Users' table).

Use the third query from [[codes/MSSQL-Enumerate-Tables-Columns-and-Databases]], replacing 'sometable' with a discovered table name, and inject.

**Expected Output**: Columns like 'id (int)', 'username (varchar)', 'password (varchar)'.

### Step 5: List All Tables Across Databases

**Context**: For comprehensive mapping, query the information_schema to get tables from all accessible databases, revealing partitioned or replicated data.

Inject the fourth query from [[codes/MSSQL-Enumerate-Tables-Columns-and-Databases]].

**Expected Output**: Pairs of database and table names, e.g., 'maindb.Users', 'reportsdb.Logs'.

### Step 6: Concatenated Table List (MSSQL 2017+)

**Context**: For quick parsing, aggregate table names into a single delimited string, simplifying automation or logging.

Inject the fifth query from [[codes/MSSQL-Enumerate-Tables-Columns-and-Databases]], adjusting the delimiter (e.g., ', ') as needed.

**Expected Output**: A comma-separated list like 'trace_xe_action_map, trace_xe_event_map, spt_fallback_db'.

If STRING_AGG is unavailable (pre-2017), use FOR XML PATH for concatenation.
