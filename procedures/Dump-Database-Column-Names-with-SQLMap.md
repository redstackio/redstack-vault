---
id: f372ff1c-ee98-4593-814c-ad9e87d2889b
name: Dump-Database-Column-Names-with-SQLMap
type: procedure
verified: true
submitted: true
created_at: '2020-08-19T18:56:34.641445+00:00'
updated_at: '2023-05-26T01:27:56.870610+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - owasp
  - owasp top 10
  - sqli
  - SQL Injection
  - SQLMap
  - Web Applications
commands:
  - '[[commands/sqlmap-dump-columns]]'
platforms:
  - Web
tools:
  - '[[tools/sqlmap]]'
validated: true
---

# Dump-Database-Column-Names-with-SQLMap

## Summary

This procedure uses SQLMap to exploit a SQL injection vulnerability in a web application to enumerate and dump the column names from a specific table in a targeted database. It automates the injection process to retrieve schema information, which can reveal sensitive data structures like user credentials or session details, aiding in further database enumeration and exploitation.

## Description

SQL injection (SQLi) vulnerabilities allow attackers to manipulate database queries through unsanitized user inputs in web applications. SQLMap is an open-source tool that automates the detection and exploitation of SQLi flaws, including blind and time-based injections. In this procedure, we target a known vulnerable endpoint (e.g., a search parameter) to specify a database (--D) and table (--T), then use the --columns flag to list all columns and their data types. This is particularly useful in reconnaissance phases to map the database schema without direct access. The procedure assumes a MySQL backend but can adapt to others like PostgreSQL. It maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) for initial access via web vulnerabilities and TA0007 (Discovery) for information gathering.

## Requirements

1. SQLMap installed and accessible in the PATH (see [[tools/sqlmap]] for installation).
2. Network access to the target web application URL with a confirmed SQLi vulnerability (e.g., via manual testing or prior scanning).
3. Knowledge of the target database name (e.g., from previous enumeration) and table name (e.g., 'admindetails').
4. Optional: Prior session file from SQLMap if resuming a previous scan to avoid re-detection.

## Defense

- Implement prepared statements and parameterized queries in application code to prevent SQLi.
- Use web application firewalls (WAFs) like ModSecurity to detect and block SQLMap payloads.
- Enable database logging for anomalous queries and monitor for time-based delays indicative of blind SQLi.
- Regularly audit database schemas and restrict unnecessary column exposure.

## Objectives

1. Exploit SQLi to retrieve column names and types from a specified table.
2. Verify the schema to identify potential sensitive data fields (e.g., passwords, sessions).
3. Log results for further exploitation, such as dumping actual data.

## Instructions

### Step 1: Verify SQL Injection Point

**Context**: Before dumping columns, confirm the injection point is exploitable. Use SQLMap's basic testing mode to resume or detect the vulnerability, ensuring the parameter (e.g., 'term') supports time-based blind SQLi. This step identifies the DBMS and injection type without dumping data yet.

**Command** ([[commands/sqlmap-test-injection]]):
```bash
sqlmap -u "$_TARGET_URL" --batch --level=1 --risk=1
```

> This command tests the URL for SQLi without interactive prompts (--batch). Replace $_TARGET_URL with the vulnerable endpoint (e.g., 'http://example.com/search.php?term='). Expected output includes confirmation of the DBMS (e.g., MySQL) and injection type (e.g., time-based blind). If a session file exists, SQLMap will resume automatically.

### Step 2: Enumerate Database and Table Details

**Context**: If not already known, enumerate databases and tables to select the target. This ensures accurate specification of --D and --T flags, avoiding errors in the dump command. Use SQLMap's enumeration flags to list available databases and tables.

**Command** ([[commands/sqlmap-enumerate-dbs-tables]]):
```bash
sqlmap -u "$_TARGET_URL" --dbs --tables -D $_DB_NAME --batch
```

> Run this to list databases (--dbs) and then tables (--tables) for the specified database (-D $_DB_NAME, e.g., 'vulcart'). Expected output: A list of databases and tables, such as 'admindetails' under 'vulcart'. Use this to confirm targets before proceeding.

### Step 3: Dump Column Names

**Context**: Execute the core dump operation to retrieve column names and types from the specified table. This exploits the SQLi to query the database schema (e.g., INFORMATION_SCHEMA.COLUMNS in MySQL). The --columns flag automates the retrieval, handling blind injection delays.

**Command** ([[commands/sqlmap-dump-columns]]):
```bash
sqlmap -u "$_TARGET_URL" -D $_DB_NAME -T $_TABLE_NAME --columns --batch
```

> Specify the URL, database (-D, e.g., 'vulcart'), and table (-T, e.g., 'admindetails'). The --batch flag avoids prompts. Expected output: A table listing columns like 'username varchar(50)', 'password varchar(50)', confirming successful schema dump. Results are also logged to ~/.sqlmap/output/.

### Step 4: Validate and Log Results

**Context**: Review the output for accuracy and check log files for full details. This step verifies success and prepares for next actions like data dumping (--dump).

**Instructions**: Inspect the console output for the column table. If issues arise (e.g., time delays), adjust --time-sec or --threads. Manually query logs with `cat ~/.sqlmap/output/$_TARGET/dump/$_DB_NAME/$_TABLE_NAME/*`.

> No specific command here; use built-in OS tools. Expected output: Confirmation of column details in logs, with no errors like 'parameter empty'.
