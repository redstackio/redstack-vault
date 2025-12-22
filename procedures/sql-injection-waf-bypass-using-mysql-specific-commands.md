---
id: cdc95f23-a64f-4764-80a4-9f9dead3c53c
name: SQL Injection WAF Bypass using MySQL Specific Commands
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.843368+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/SQL Injection]]'
  - '[[tags/WAF Bypass]]'
  - '[[tags/MySQL]]'
commands:
  - '[[commands/mysql-select-innodb-version]]'
  - '[[commands/mysql-select-mysql-version]]'
  - '[[commands/mysql-select-information-schema-tables]]'
  - '[[commands/mysql-select-innodb-table-stats]]'
  - '[[commands/mysql-show-tables-in-database]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# SQL Injection WAF Bypass using MySQL Specific Commands

## Summary

This procedure demonstrates how to bypass Web Application Firewalls (WAFs) during SQL Injection (SQLi) attacks on MySQL-backed web applications by using MySQL-specific queries that may not be blocked by standard WAF rules. These queries target database metadata like table lists, statistics, and version information, allowing attackers to enumerate the database structure without triggering common SQLi signatures.

## Description

SQL Injection vulnerabilities occur when user input is not properly sanitized, allowing attackers to inject malicious SQL code into queries. WAFs often block obvious payloads like 'UNION SELECT' or '1=1', but MySQL-specific commands such as querying the information_schema, innodb_table_stats, or version variables can evade detection if the WAF is not tuned for them. This technique is useful in reconnaissance phases to map the database schema (e.g., in applications like DVWA) and prepare for data extraction or privilege escalation. It assumes a reflected or blind SQLi vulnerability in a parameter like a search field or login form. Success enables discovery of sensitive tables like 'users' without alerting defenses.

## Requirements

1. Access to a vulnerable web application with a confirmed SQLi entry point (e.g., via Burp Suite or manual testing).
2. Knowledge of basic SQL Injection techniques, including payload construction and error-based/blind exploitation.
3. Familiarity with MySQL syntax and database administration commands.
4. Tools like a proxy (e.g., Burp Suite) to intercept and modify HTTP requests containing the injected payloads.
5. Target application using MySQL as the backend database.

## Defense

- Implement parameterized queries and prepared statements in application code to prevent SQLi entirely.
- Configure WAF rules to detect and block MySQL-specific queries, including references to information_schema, innodb_table_stats, and version functions.
- Enable database logging (e.g., MySQL general query log) and monitor for anomalous queries from web app IPs.
- Use web application firewalls with machine learning-based anomaly detection and regularly update rule sets for MySQL evasions.
- Conduct regular vulnerability scans and input validation audits.

## Objectives

1. Bypass WAF filters using non-malicious-looking MySQL metadata queries.
2. Enumerate database tables, schemas, and structure to identify sensitive data locations.
3. Gather version and engine information to tailor further exploits.
4. Extract initial reconnaissance data without causing errors that alert defenders.
5. Prepare for advanced SQLi actions like data exfiltration or command execution.

## Instructions

### Step 1: Identify Vulnerable Injection Point and Test Basic Connectivity

**Context**: Confirm the SQLi vulnerability exists and the backend is MySQL. Inject a simple payload to cause a database error revealing MySQL specifics, then prepare to use metadata queries for bypass.

Navigate to the vulnerable input field (e.g., search box in DVWA SQLi module). Append a single quote (') to trigger an error. If successful, proceed to inject MySQL version checks to confirm the DBMS without aggressive payloads.

**Command** ([[commands/mysql-select-mysql-version]]):
```sql
' UNION SELECT @@version--
```

> This injects a UNION-based query to retrieve the MySQL version. The @@version variable returns the server version string. If the WAF blocks UNION, try blind techniques like conditional errors. Expected: Response includes version like '5.7.XX' or error confirming MySQL.

### Step 2: Enumerate Tables Using Information Schema

**Context**: Use the standard information_schema to list tables, which is less likely to be blocked than direct SHOW commands. This step maps the database structure for targeting sensitive tables like 'users' or 'guestbook'.

Inject the payload into the vulnerable parameter, adjusting for the query context (e.g., after WHERE clause).

**Command** ([[commands/mysql-select-information-schema-tables]]):
```sql
' UNION SELECT table_name FROM information_schema.tables WHERE table_schema=DATABASE()--
```

> This queries the current database's tables. In MySQL, replace 'public' with DATABASE() for dynamic schema. Expected: List of table names in the response, such as 'users', 'guestbook'. If blocked, encode or use comments to obfuscate.

### Step 3: Query InnoDB Table Statistics for Additional Details

**Context**: Access MySQL's internal innodb_table_stats for row counts and update times, providing insights into data volume without full schema dumps that might trigger WAFs.

Inject into the SQLi point, ensuring the payload fits the original query (e.g., as a subquery or UNION).

**Command** ([[commands/mysql-select-innodb-table-stats]]):
```sql
' UNION SELECT CONCAT(table_name, ':', n_rows) FROM mysql.innodb_table_stats WHERE database_name=DATABASE()--
```

> This retrieves table names and row counts from InnoDB stats. Expected: Output like 'users:5', 'guestbook:0', indicating populated tables for prioritization.

### Step 4: List Tables in Specific Database with SHOW Command

**Context**: Use the SHOW TABLES command targeted at the application database (e.g., 'dvwa') to verify and list tables directly, often evading WAFs tuned for schema queries.

Tailor the injection to reference the known database name from prior steps or app context.

**Command** ([[commands/mysql-show-tables-in-database]]):
```sql
' UNION SELECT table_name FROM (SHOW TABLES IN dvwa) AS t--
```

> Wrap in a subquery if needed for compatibility. Expected: Table list like 'guestbook', 'users' in the response body or error message.

### Step 5: Check InnoDB Engine Version for Compatibility

**Context**: Retrieve the InnoDB version to assess storage engine capabilities, which can inform if advanced features like file privileges are available for escalation.

Inject as a final reconnaissance payload.

**Command** ([[commands/mysql-select-innodb-version]]):
```sql
' UNION SELECT @@innodb_version--
```

> This pulls the InnoDB storage engine version. Expected: Version string like '5.7.XX', confirming MySQL variant and potential exploits.
