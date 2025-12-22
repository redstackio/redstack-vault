---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Oracle-SQL-Injection]]'
  - '[[tags/Oracle-SQL-List-Columns]]'
commands:
  - '[[commands/oracle-sql-enumerate-columns-by-table]]'
  - '[[commands/oracle-sql-enumerate-columns-by-table-and-owner]]'
platforms:
  - Database
  - Oracle
tools: []
verified: true
validated: true
---

# Oracle-SQL-Column-Enumeration

## Summary

Oracle SQL Column Enumeration is a procedure to extract column names from Oracle database tables via SQL injection vulnerabilities. This allows attackers to map database schemas, identify sensitive data structures like user credentials or financial records, and support further exploitation such as data extraction or privilege escalation.

## Description

This procedure targets Oracle databases accessible through web applications vulnerable to SQL injection. By injecting UNION-based or error-based SQL payloads, attackers can query system views like ALL_TAB_COLUMNS to retrieve column metadata without direct database access. It is typically used in reconnaissance phases to understand data layout before attempting broader queries for actual content. The technique exploits insufficient input sanitization, enabling arbitrary SQL execution. In a real-world scenario, this might occur in legacy enterprise applications using Oracle backends, revealing columns in tables like USERS or ACCOUNTS for targeted attacks.

## Requirements

1. Valid SQL injection point in a web application connected to an Oracle database (e.g., via a login form or search field).
2. Basic knowledge of SQL injection payloads, including UNION SELECT statements to append queries.
3. Tools like a web proxy (e.g., Burp Suite) or SQLMap for crafting and sending injections.
4. Network access to the vulnerable application; no direct DB credentials needed.

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and parameterized queries to prevent SQL injection.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns in requests.
- Enable database auditing for queries accessing system views like ALL_TAB_COLUMNS.
- Regularly scan for vulnerabilities using tools like SQLMap or OWASP ZAP.

## Objectives

1. Extract column names from specified tables to map database schema.
2. Identify potential sensitive data locations for further reconnaissance or exfiltration.
3. Validate SQL injection exploitability and gather intelligence on database structure.

## Instructions

### Step 1: Identify Injection Point and Test Basic SQLi

**Context**: Confirm the presence of a SQL injection vulnerability by appending quotes or boolean conditions to inputs and observing database errors or behavior changes. This step ensures the endpoint is exploitable before attempting enumeration.

Use a tool like Burp Suite to intercept and modify requests. For example, in a search parameter, test with `' OR 1=1 --` to bypass authentication or return extra results.

> If errors reveal Oracle-specific messages (e.g., ORA-XXXX), proceed; otherwise, try different payloads.

### Step 2: Enumerate Columns for a Specific Table

**Context**: Inject a query to retrieve column names from ALL_TAB_COLUMNS for a known or guessed table name. This reveals the schema without needing owner details, useful when table ownership is ambiguous.

**Command** ([[commands/oracle-sql-enumerate-columns-by-table]]):
```sql
SELECT column_name FROM all_tab_columns WHERE table_name = '$_TABLE_NAME';
```

> Replace $_TABLE_NAME with the target table (e.g., 'USERS'). Inject this via UNION SELECT in the vulnerable parameter, e.g., `' UNION SELECT column_name FROM all_tab_columns WHERE table_name='USERS' --`. Expected output appears in the application response, listing columns like 'USERNAME', 'PASSWORD'.

### Step 3: Enumerate Columns for a Table Owned by a Specific User

**Context**: If multiple schemas exist, narrow the query by owner to avoid duplicates or irrelevant results. This is essential in multi-tenant Oracle environments.

**Command** ([[commands/oracle-sql-enumerate-columns-by-table-and-owner]]):
```sql
SELECT column_name FROM all_tab_columns WHERE table_name = '$_TABLE_NAME' AND owner = '$_OWNER_NAME';
```

> Replace $_TABLE_NAME with the table and $_OWNER_NAME with the schema owner (e.g., 'HR' for 'EMPLOYEES'). Inject similarly: `' UNION SELECT column_name FROM all_tab_columns WHERE table_name='EMPLOYEES' AND owner='HR' --`. Success yields owner-specific columns.

### Step 4: Verify and Document Results

**Context**: Analyze the returned column names to identify sensitive ones (e.g., those suggesting credentials or PII). Cross-reference with known Oracle table patterns.

> If no results, try uppercase table names (Oracle is case-sensitive) or enumerate tables first via similar queries on ALL_TABLES. Document findings for chaining to data extraction procedures.
