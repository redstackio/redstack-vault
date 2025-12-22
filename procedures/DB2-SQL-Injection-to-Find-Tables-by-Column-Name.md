---
id: 3523d7db-da95-4e12-8096-e82f46670b33
name: DB2-SQL-Injection-to-Find-Tables-by-Column-Name
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.840684+00:00'
updated_at: '2023-04-10T20:22:04.805069+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Exploitation-of-Remote-Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/DB2]]'
  - '[[tags/SQL-Injection]]'
  - '[[tags/Database-Enumeration]]'
  - '[[tags/Column-Discovery]]'
commands:
  - '[[commands/db2-query-tables-by-column-name]]'
platforms:
  - Databases
  - DB2
tools: []
validated: true
---

# DB2-SQL-Injection-to-Find-Tables-by-Column-Name

## Summary

This procedure demonstrates how to use SQL injection in a vulnerable DB2 database to enumerate tables containing a specific column name, such as 'username'. It leverages a direct query against system tables to discover database schema details, aiding in further reconnaissance or data extraction during an attack.

## Description

In a typical attack scenario, an attacker identifies a SQL injection vulnerability in a web application or direct DB2 interface connected to an IBM DB2 database. By injecting a crafted SQL query, the attacker can query the sysibm.syscolumns system table to retrieve table names (tbname) where a given column name exists. This technique is part of database enumeration and is useful for mapping the database structure to target sensitive data like user credentials or configuration tables. The target environment is an undersecured DB2 instance, often exposed via web apps without proper input sanitization. Expected outcomes include a list of relevant table names, enabling subsequent queries for data exfiltration. This maps to discovery tactics by revealing internal database layout without legitimate access.

## Requirements

1. Access to a vulnerable input point in a DB2-connected application (e.g., login form, search field) susceptible to SQL injection.
2. Knowledge of the target column name (e.g., 'username') from prior reconnaissance or error messages.
3. A SQL client or injection tool like [[tools/sqlmap]] or Burp Suite for manual injection.
4. Network connectivity to the DB2 server (default port 50000).

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and parameterized queries to prevent SQL injection.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns.
- Regularly audit database logs for queries accessing system tables like sysibm.syscolumns.
- Limit application privileges to read-only on user tables, denying access to system catalogs.

## Objectives

1. Identify all tables in the DB2 database containing a specified column name.
2. Gather schema information for targeted data extraction.
3. Validate the injection point and query execution without triggering alerts.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user-controllable input field (e.g., a search box or authentication form) that interacts with the DB2 backend. Test for SQL injection vulnerability by appending a single quote (') and observing errors revealing DB2 syntax.

**Command** ([[commands/db2-test-injection-point]]):

This step uses a basic test, but proceed to the main query if confirmed.

> If an error like "SQL0101N" appears, the point is injectable. No specific command here; use manual input like "test'".

### Step 2: Craft and Inject the Enumeration Query

**Context**: Once the injection is confirmed, replace or append the vulnerable parameter with the SQL query to query sysibm.syscolumns. This step targets the column name 'username' but can be adapted (e.g., replace with 'password' or 'email'). The query selects table names where the column matches, bypassing normal application logic.

**Code** ([[codes/DB2-Select-Tables-By-Column-Name]]):

Embed this SQL in the injection point, such as in a UNION-based injection: "' UNION SELECT tbname FROM sysibm.syscolumns WHERE name='username'--".

**Command** ([[commands/db2-query-tables-by-column-name]]):
```sql
select tbname from sysibm.syscolumns where name='username'
```

> This command executes the core query. In a web injection, wrap it in a subquery or UNION to avoid syntax errors. Expected output includes table names like 'USERS' or 'ADMIN_ACCOUNTS' if they contain the 'username' column.

### Step 3: Interpret and Verify Results

**Context**: Analyze the returned table names to confirm success. If no results, try variations like case-insensitive (e.g., 'USERNAME') or check for schema prefixes. Use the discovered tables for follow-on queries, such as "SELECT * FROM [tbname]".

> Success is indicated by a list of table names. If empty, the column may not exist or access is restricted. Log the output for further enumeration.
