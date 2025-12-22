---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - sql-injection
  - mssql-injection
  - database-discovery
  - mssql-list-columns
commands:
  - '[[commands/mssql-list-column-names-for-table]]'
  - '[[commands/mssql-list-column-names-and-types-for-table]]'
  - '[[commands/mssql-list-table-catalog-and-columns]]'
platforms:
  - MSSQL
tools: []
verified: true
validated: true
---

# List-MSSQL-Table-Columns-via-SQL-Injection

## Summary

This procedure uses SQL injection vulnerabilities in Microsoft SQL Server (MSSQL) databases to enumerate column names and types from specific tables or across the database schema. It enables attackers to map the database structure, facilitating further exploitation such as data extraction or targeted queries in reconnaissance or data collection phases.

## Description

In scenarios where a web application is vulnerable to SQL injection, attackers can append specially crafted SQL queries to user inputs to query system tables like syscolumns or information_schema.columns. This reveals metadata about the database, including column names, data types, and associated catalogs, without direct database access. The technique targets MSSQL-specific system views and is particularly useful in blind SQL injection attacks where error messages or time-based responses confirm results. Prerequisites include identifying an injectable parameter (e.g., via UNION-based or error-based SQLi). Outcomes include a detailed schema map, aiding in crafting follow-on attacks like selecting sensitive data from known columns. This maps to discovery tactics by gathering system information through exploitation of remote services.

## Requirements

1. Access to a web application vulnerable to SQL injection (e.g., unparameterized queries in login or search forms).
2. Knowledge of the database backend being MSSQL (confirm via fingerprinting queries like SELECT @@VERSION).
3. Tools for injecting and observing responses, such as a proxy like Burp Suite or sqlmap.
4. Basic understanding of SQL syntax to adapt queries for blind or union-based injection.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation, sanitization, and escaping for all user inputs to prevent injection.
- Use parameterized queries or prepared statements in application code to separate SQL logic from data.
- Employ web application firewalls (WAFs) to detect and block anomalous SQL patterns, such as references to syscolumns or information_schema.
- Enable database logging to monitor queries accessing system tables and alert on unusual schema enumeration attempts.
- Regularly audit and patch applications and databases to address known SQLi vulnerabilities (e.g., via OWASP guidelines).

## Objectives

1. Enumerate column names from a specific table to understand its structure.
2. Retrieve column data types to infer data sensitivity and craft targeted extractions.
3. Map the overall database schema across tables for comprehensive reconnaissance.
4. Enable planning of subsequent attacks, such as data exfiltration from identified columns.

## Instructions

### Step 1: List Column Names for a Specific Table in Current Database

**Context**: This step uses the syscolumns and sysobjects views to retrieve column names for a targeted table in the current database. It's useful for quick enumeration when the table name is known from prior reconnaissance. Inject this query via a vulnerable parameter, often appended after a UNION SELECT to bypass filters.

**Command** ([[commands/mssql-list-column-names-for-table]]):
```sql
SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '$_TABLE_NAME');
```

> Replace $_TABLE_NAME with the target table (e.g., 'users'). In a SQLi payload, this might look like: ' UNION SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'users') --. Expected output includes a list of column names if the injection succeeds, visible in application responses or error messages.

### Step 2: List Column Names and Types for a Specific Table in Master Database

**Context**: This expands on the previous by querying the master database for both names and types, providing more detail on data handling. It's effective for tables in system or user databases and helps identify exploitable fields like passwords or emails based on types (e.g., varchar for strings).

**Command** ([[commands/mssql-list-column-names-and-types-for-table]]):
```sql
SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id = master..sysobjects.id AND master..sysobjects.name = '$_TABLE_NAME';
```

> Substitute $_TABLE_NAME (e.g., 'sometable'). Deliver via SQLi, such as in a stacked query: '; SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id = master..sysobjects.id AND master..sysobjects.name = 'sometable' --. Success yields pairs of column names and types, like 'id int' or 'username varchar(50)'.

### Step 3: List Table Catalog and Column Names Across Database

**Context**: Using the standard information_schema view (ANSI SQL compliant), this step enumerates columns for all tables in the current catalog. It's broader and less MSSQL-specific, ideal for initial schema mapping when table names are unknown. Use in union-based injections to extract multiple results.

**Command** ([[commands/mssql-list-table-catalog-and-columns]]):
```sql
SELECT table_catalog, column_name FROM information_schema.columns;
```

> No table parameter needed; it scans all. Example payload: ' UNION SELECT table_catalog, column_name FROM information_schema.columns --. If successful, output lists catalog names paired with columns, e.g., 'mydatabase, id' and 'mydatabase, email', revealing the full schema.
