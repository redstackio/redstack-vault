---
id: c4dc100b-12cb-4c4e-b57b-eb43a5d1bdd4
name: List-Tables-via-DB2-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.810846+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/DB2]]'
  - '[[tags/SQL-Injection]]'
  - '[[tags/Database-Enumeration]]'
  - '[[tags/List-Tables]]'
commands:
  - '[[commands/db2-select-table-names-from-tables]]'
  - '[[commands/db2-select-table-names-from-systables]]'
platforms:
  - Database
  - DB2
tools: []
validated: true
---

# List-Tables-via-DB2-SQL-Injection

## Summary

This procedure demonstrates how to exploit SQL injection vulnerabilities in IBM DB2 database-backed applications to enumerate and list all table names in the database. By injecting specific SQL queries into vulnerable input fields, an attacker can retrieve schema information, enabling further reconnaissance, data exfiltration, or privilege escalation.

## Description

DB2 SQL injection targets applications that fail to properly sanitize user inputs interacting with IBM DB2 databases. This procedure focuses on using two key system catalog queries to list tables: one targeting the SYSTABLES view for all database tables and another targeting the TABLES view for schema-specific tables. These queries can be injected via UNION-based or error-based techniques in web forms, APIs, or other input points. The technique assumes the application uses DB2 as the backend and exposes injectable endpoints. Successful execution reveals table names, which can be used to identify sensitive data stores like user credentials or configuration tables. This is commonly used in web application penetration testing or red team engagements to map database structures without direct DB2 access.

## Requirements

1. Access to a vulnerable web application or API endpoint that interacts with a DB2 database.
2. Ability to inject SQL payloads, typically through unsanitized input fields like search boxes, login forms, or URL parameters.
3. Knowledge of the application's query structure to craft effective UNION-based injections.
4. A tool like Burp Suite or sqlmap for intercepting and modifying requests (optional but recommended).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to block SQL keywords and patterns.
- Use parameterized queries or prepared statements in application code to separate SQL logic from user input.
- Enable DB2 logging for audit trails and monitor for anomalous queries accessing system catalogs like SYSTABLES or TABLES.
- Deploy web application firewalls (WAFs) tuned to detect SQL injection patterns, including DB2-specific syntax.

## Objectives

1. Identify and exploit an SQL injection point in a DB2-backed application.
2. Enumerate table names using system catalog queries.
3. Verify the output to confirm successful schema discovery without triggering alerts.

## Instructions

### Step 1: Identify Injection Point and Test Vulnerability

**Context**: Locate an input field vulnerable to SQL injection and confirm DB2 as the backend by observing error messages or using fingerprinting payloads. This step ensures the target uses DB2 before attempting table enumeration.

**Command** (Use a generic SQL injection tester like sqlmap or manual Burp requests):

To test, append a single quote to input and check for errors indicating DB2 (e.g., SQLCODE -104).

> If errors reveal DB2 syntax, proceed. Otherwise, try blind injection techniques.

### Step 2: Inject Query to List Tables from Current Schema

**Context**: Use the TABLES view to retrieve table names from the current schema, which is often faster and less noisy for initial enumeration. This targets applications where the injection point allows UNION selection.

**Command** ([[commands/db2-select-table-names-from-tables]]):

```sql
select table_name from sysibm.tables
```

> Inject this via UNION, e.g., ' UNION SELECT table_name FROM sysibm.tables --. Expect a list of table names in the response. If no output, adjust for blind extraction using conditional statements.

### Step 3: Inject Query to List All Database Tables

**Context**: If the previous query yields limited results, use the SYSTABLES view to enumerate all tables across the database, providing a comprehensive schema map. This may require higher privileges or broader injection scope.

**Command** ([[commands/db2-select-table-names-from-systables]]):

```sql
select name from sysibm.systables
```

> Append to the vulnerable query similarly. The output will include table names; filter for user-created tables by excluding system ones (e.g., where type='T').

### Step 4: Verify and Document Results

**Context**: Cross-reference outputs from both queries to build a complete table inventory. Save results for further procedures like column enumeration.

Use the combined code snippet for efficiency:

**Code** ([[codes/DB2-Table-Enumeration-Queries]]):

```sql
select table_name from sysibm.tables
select name from sysibm.systables
```

> Success is indicated by retrieved table names without application crashes or log alerts. Document any sensitive tables (e.g., users, credentials) for next steps.
