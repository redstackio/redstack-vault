---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - DB2
  - SQL-Injection
  - Database-Discovery
  - Column-Enumeration
commands:
  - '[[commands/db2-select-columns-from-sysibm-syscolumns]]'
tools: []
platforms:
  - Databases
  - DB2
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
---

# DB2-SQL-Injection-to-List-Table-Columns

## Summary

This procedure demonstrates how to use SQL injection in a vulnerable DB2 database to enumerate column names, table associations, and data types from system catalog tables like sysibm.syscolumns. By injecting a crafted SELECT query, an attacker can map the database schema, enabling further targeted queries for data exfiltration or privilege escalation.

## Description

DB2 databases, like other relational databases, store metadata about their structure in system tables such as sysibm.syscolumns, syscat.columns, and sysstat.columns. A SQL injection vulnerability in a web application or API connected to DB2 allows an attacker to append malicious SQL payloads to user inputs, bypassing authentication and executing arbitrary queries. This procedure focuses on retrieving column details to understand the database layout, which is crucial for identifying sensitive tables (e.g., user credentials or financial data). The technique leverages the LISTAGG function or direct SELECT to concatenate and extract information without disrupting the application's normal flow. It applies to scenarios where the application fails to sanitize inputs, such as search fields or login forms. Success provides a blueprint for subsequent attacks, like dumping specific tables.

## Requirements

1. Valid SQL injection point in a DB2-backed application (e.g., via a vulnerable parameter in a web form).
2. Basic knowledge of SQL syntax and DB2 system tables.
3. Tools for injecting and observing responses, such as a browser with developer tools or [[tools/sqlmap]].
4. Network access to the target application and database.

## Defense

- Implement strict input validation and sanitization to block SQL injection attempts, using whitelisting for expected inputs.
- Use parameterized queries or prepared statements in application code to separate SQL logic from user data.
- Enable database logging and monitoring for anomalous queries, such as SELECTs on system tables from unexpected sources; integrate with SIEM for alerts on schema enumeration patterns.
- Apply least privilege to database accounts used by applications, restricting access to system catalogs.

## Objectives

1. Inject a SQL payload to query DB2 system tables for column metadata.
2. Extract column names, associated tables, and data types to map the database schema.
3. Identify potential targets for further data extraction or manipulation.

## Instructions

### Step 1: Identify Injection Point and Test Vulnerability

**Context**: Locate a parameter vulnerable to SQL injection (e.g., a search box) and confirm it allows DB2-specific payloads by observing error messages or delayed responses indicating SQL execution.

Use manual testing or automated tools to append a single quote (') and observe if it breaks the query, confirming injectability.

### Step 2: Inject Query to Enumerate Columns

**Context**: Craft and inject the SQL query to select from sysibm.syscolumns, which holds column details across all tables. This step retrieves essential metadata without needing prior table knowledge. Alternative tables like syscat.columns (for current schema) or sysstat.columns (for statistics) can be substituted for broader or narrower scopes.

**Command** ([[commands/db2-select-columns-from-sysibm-syscolumns]]):

```sql
select name, tbname, coltype from sysibm.syscolumns -- also valid syscat and sysstat
```

> Append this payload to the vulnerable parameter, e.g., in a URL: `search='; [payload] --`. The comment (--) neutralizes the rest of the original query. Expected output includes a list of columns with their table names and types (e.g., CHAR, INTEGER). If the response is truncated, use LISTAGG to concatenate results: `select LISTAGG(name, ',') from sysibm.syscolumns`. Verify by checking for database-specific errors or partial data leaks in the application response.

**Code** ([[codes/DB2-SQL-Query-to-List-Table-Columns]]):

Embed the code snippet directly into the injection point as needed for customization.

### Step 3: Analyze and Iterate on Results

**Context**: Parse the returned data to identify high-value tables (e.g., those with 'user' or 'password' columns). Use the insights to craft follow-up injections, such as selecting from specific tables.

Review the output for patterns, like sensitive data types (VARCHAR for credentials), and document the schema for chaining with other procedures like data dumping.
