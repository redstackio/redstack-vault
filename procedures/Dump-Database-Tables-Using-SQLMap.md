---
type: procedure
description: >-
  This procedure automates the extraction of table names from a vulnerable SQL
  database using SQLMap, assuming a confirmed SQL injection point.
verified: true
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - owasp
  - owasp-top-10
  - sqli
  - sql-injection
  - web-applications
commands:
  - '[[commands/sqlmap-enumerate-databases]]'
  - '[[commands/sqlmap-dump-tables-from-specified-database]]'
tools:
  - '[[tools/sqlmap]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Dump-Database-Tables-Using-SQLMap

## Summary

This procedure utilizes SQLMap, an automated tool for exploiting SQL injection vulnerabilities, to enumerate available databases and then dump the table names from a specific database. It is particularly useful in web application penetration testing where a SQL injection (SQLi) vulnerability has been identified in a GET or POST parameter, allowing attackers to extract schema information for further data exfiltration or privilege escalation.

## Description

SQL injection vulnerabilities occur when user input is not properly sanitized, enabling attackers to inject malicious SQL code into queries. SQLMap automates the detection and exploitation of these flaws, including blind, time-based, and error-based injections. In this procedure, we first enumerate all accessible databases using the --dbs option to identify targets, then specify a database with -D and use --tables to retrieve its table names. This technique maps to MITRE ATT&CK as exploiting public-facing applications for execution and collection. It requires a confirmed injection point and works against common DBMS like MySQL, PostgreSQL, and Oracle. Success reveals the database structure, aiding in targeted data dumping or identifying sensitive tables like user credentials.

## Requirements

1. SQLMap installed and accessible in the PATH (see [[tools/sqlmap]] for installation).
2. A confirmed SQL injection vulnerable endpoint (e.g., a web URL with an injectable parameter like a search field).
3. Network access to the target web application.
4. Basic knowledge of the target DBMS (e.g., MySQL); if unknown, the enumeration step will identify it.
5. Optional: Prior session file from initial SQLi testing to resume exploitation faster.

## Defense

Defensive measures include input validation and parameterization of SQL queries using prepared statements. Implement web application firewalls (WAFs) to detect anomalous payloads. Enable database logging for failed queries and monitor for unusual delays indicative of time-based blind SQLi. Regularly audit application code for OWASP Top 10 vulnerabilities like A03:2021 - Injection.

## Objectives

1. Identify accessible databases on the vulnerable endpoint.
2. Extract table names from a targeted database to map the schema.
3. Validate the output for sensitive tables that may contain valuable data.

## Instructions

### Step 1: Enumerate Available Databases

**Context**: If the target database name is unknown, start by using SQLMap to list all databases accessible via the injection point. This step confirms the DBMS type and provides options for the next step. It uses time-based or boolean blind techniques if no direct output is available.

**Command** ([[commands/sqlmap-enumerate-databases]]):
```bash
sqlmap -u "$_URL" --dbs
```

Run this command against the vulnerable URL. SQLMap will test the injection, identify the DBMS, and retrieve database names. If resuming from a previous session, SQLMap will load it automatically. Expected output includes a list of databases; select one relevant to the application (e.g., 'vulcart' for an e-commerce site).

### Step 2: Dump Tables from the Specified Database

**Context**: With the database name identified, use the -D flag to target it specifically and --tables to extract table names. This narrows the scope, reducing noise and execution time compared to dumping everything. Monitor for warnings about empty parameters or redirects, and follow prompts to optimize delays for blind injections.

**Command** ([[commands/sqlmap-dump-tables-from-specified-database]]):
```bash
sqlmap -u "$_URL" -D "$_DB_NAME" --tables
```

Substitute the URL and database name from Step 1. SQLMap will fetch and display the tables. If the injection is time-based, it may take several minutes per table due to sleep-based queries.

### Step 3: Verify and Log Results

**Context**: Review the output for completeness and log the results for further analysis. Check for tables like 'users', 'admin', or 'products' that indicate sensitive data. If no tables appear, verify the injection point or try alternative techniques like --schema.

No specific command is needed here, but pipe output to a file for persistence:
```bash
tables.txt > $(sqlmap -u "$_URL" -D "$_DB_NAME" --tables)
```

Expected: A table listing all schema elements. Success is confirmed if multiple tables are retrieved without errors.
