---
id: e638b29e-490a-4140-8350-4842f131c657
name: Oracle-SQL-List-Tables-and-Columns
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.244903+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Data-from-Information-Repositories|T1213 - Data from
    Information Repositories]]
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - oracle
  - sql-injection
  - database-discovery
  - schema-enumeration
commands:
  - '[[commands/oracle-sql-list-all-tables]]'
  - '[[commands/oracle-sql-list-tables-with-owner]]'
  - '[[commands/oracle-sql-list-password-columns]]'
platforms:
  - Oracle Database
tools: []
validated: true
---

# Oracle-SQL-List-Tables-and-Columns

## Summary

This procedure demonstrates how to use SQL injection in an Oracle database to enumerate tables and columns, focusing on identifying potential sensitive data such as password-related fields. It involves executing targeted SQL queries to extract schema information, which can reveal valuable assets like user credentials for further exploitation.

## Description

In a SQL injection attack against an Oracle database, attackers can inject malicious SQL code into vulnerable input fields to query the database schema. This procedure outlines injecting queries to list all tables, retrieve table owners, and identify columns containing 'PASS' in their names, which often indicate password storage. This discovery technique helps map the database structure, locate sensitive data repositories, and plan subsequent data extraction or privilege escalation. It assumes the attacker has identified a blind or error-based SQLi vulnerability allowing query execution and response observation, either through union-based injection, time-based delays, or out-of-band channels.

## Requirements

1. Confirmed SQL injection vulnerability in a web application connected to an Oracle database.
2. Ability to inject and execute arbitrary SQL queries (e.g., via UNION SELECT or subquery).
3. Tools for crafting and sending payloads, such as [[tools/sqlmap]] or Burp Suite.
4. Basic knowledge of Oracle system views like ALL_TABLES and ALL_TAB_COLUMNS.

## Defense

- Implement strict input validation and sanitization to block SQL injection attempts.
- Use prepared statements and parameterized queries in application code to separate SQL logic from user input.
- Enable database logging for anomalous queries and monitor for schema enumeration patterns.
- Apply least privilege to database accounts used by applications, restricting access to system views.

## Objectives

1. Enumerate all accessible tables in the Oracle database to understand the schema.
2. Identify table owners to scope data ownership and potential access controls.
3. Locate columns likely containing sensitive information, such as passwords, for targeted extraction.
4. Gather intelligence for deeper attacks, like dumping credential data.

## Instructions

### Step 1: List All Tables

**Context**: Begin by querying the ALL_TABLES view to retrieve a list of all tables accessible to the current database user. This provides an overview of the database structure without revealing ownership details initially.

**Command** ([[commands/oracle-sql-list-all-tables]]):
```sql
SELECT table_name FROM all_tables;
```

> This query returns a simple list of table names. Inject this into a vulnerable parameter using UNION or subquery techniques. Observe the response for table names, which may appear in error messages, union results, or delayed responses in blind SQLi.

### Step 2: List Tables with Owners

**Context**: Expand on the previous step by including the OWNER column from ALL_TABLES. This helps identify which schema or user owns each table, aiding in privilege assessment and targeting high-value schemas like SYS or application owners.

**Command** ([[commands/oracle-sql-list-tables-with-owner]]):
```sql
SELECT owner, table_name FROM all_tables;
```

> The output will show pairs of owner and table names. In an injection scenario, concatenate results or use multiple injections to extract this data systematically. Verify by checking for known sensitive schemas.

### Step 3: Identify Password-Related Columns

**Context**: Target potential credential storage by querying ALL_TAB_COLUMNS for columns with 'PASS' in the name. This filters for fields like PASSWORD, PASSHASH, or USERPASS, prioritizing them for further dumping or cracking.

**Command** ([[commands/oracle-sql-list-password-columns]]):
```sql
SELECT owner, table_name FROM all_tab_columns WHERE column_name LIKE '%PASS%';
```

> Results list owners and tables containing matching columns. Success is indicated by returned rows; if none, broaden the search (e.g., '%PWD%'). Use this to chain into data extraction procedures.
