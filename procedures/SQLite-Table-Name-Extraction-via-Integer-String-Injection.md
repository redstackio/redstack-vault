---
type: procedure
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Sharepoint]]'
sub_techniques: []
tags:
  - sqlite-injection
  - sql-injection
  - table-extraction
  - database-enumeration
commands: []
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/cURL]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# SQLite-Table-Name-Extraction-via-Integer-String-Injection

## Summary

This procedure demonstrates how to extract table names from an SQLite database using SQL injection attacks that exploit integer or string-based input parameters in a vulnerable web application. By injecting a crafted SQL payload, an attacker can query the sqlite_master table to enumerate user-created tables, excluding system tables, providing insight into the database schema for further exploitation such as data extraction or privilege escalation.

## Description

SQLite databases are lightweight and commonly embedded in web and mobile applications, making them frequent targets for SQL injection (SQLi) vulnerabilities. Integer-based injections occur when numeric parameters lack proper type enforcement, allowing SQL keywords to be appended without quotes. String-based injections exploit unescaped quotes in text inputs, enabling termination of the original query and injection of additional statements. This procedure focuses on using a UNION-based injection to append a SELECT query against sqlite_master, which metadata table stores information about all database objects. The attack reveals table names, helping identify sensitive data stores like user credentials or application configurations. It maps to MITRE ATT&CK techniques for exploiting public-facing applications and collecting data from information repositories. Success depends on the application's query structure, but it typically requires no authentication if the endpoint is public-facing.

## Requirements

1. Access to a web application using SQLite as its backend database with a confirmed SQL injection vulnerability in an integer or string parameter (e.g., via error messages or time-based blind SQLi confirmation).
2. Tools for intercepting and modifying HTTP requests, such as Burp Suite or curl, to craft and send injection payloads.
3. Basic knowledge of SQL syntax and HTTP request manipulation to observe responses for leaked data.
4. Network access to the target application, potentially behind a proxy for traffic interception.

## Defense

Defensive measures and detection strategies:

- Use parameterized queries or prepared statements in application code to separate SQL logic from user input, preventing injection entirely.
- Implement web application firewalls (WAFs) with SQLi rules to detect and block anomalous payloads like UNION SELECT or references to sqlite_master.
- Enable database logging to monitor for unexpected queries accessing metadata tables; use tools like SQLite's PRAGMA statements for query tracing.
- Conduct regular input validation, type enforcement for integers, and output encoding to mitigate blind injections.
- Perform security testing with tools like sqlmap to identify and patch SQLi vulnerabilities before deployment.

## Objectives

1. Confirm SQL injection vulnerability in integer or string parameters to bypass input validation.
2. Extract a list of user table names from the SQLite database schema.
3. Identify potential sensitive tables for targeted follow-on attacks, such as column enumeration or data dumping.
4. Achieve database schema reconnaissance without direct database access.

## Instructions

### Step 1: Identify Vulnerable Parameter and Confirm SQLi

**Context**: Locate an endpoint accepting integer or string inputs (e.g., user ID in a GET/POST parameter) and test for SQLi by appending SQL syntax to observe errors or behavior changes. This step verifies the injection point before attempting table extraction.

Use Burp Suite or curl to send test payloads. For integer parameters, try appending ' OR 1=1 --; for strings, try ' OR '1'='1. If the query returns more data or errors mentioning SQL syntax, injection is possible.

**Expected Output**: Application response alters (e.g., all records returned or SQL error like "no such table"), confirming vulnerability.

### Step 2: Craft UNION-Based Payload for Table Extraction

**Context**: Once SQLi is confirmed, construct a UNION SELECT payload to append the table extraction query. Match the number of columns in the original query (probe with ORDER BY to determine count, e.g., ORDER BY 1--, ORDER BY 2-- until error). Use the provided code snippet to query sqlite_master, excluding system tables starting with 'sqlite_'.

Reference the extraction query from [[codes/SQLite-Table-Names-Extraction-Query]] and inject it via UNION. For string-based injection in a parameter like 'id': id=1' UNION SELECT tbl_name FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%' --. For integer-based: id=1 UNION SELECT tbl_name FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%' -- (no quotes needed if type enforcement is weak).

Send the payload using curl:

```bash
curl -X POST "http://target.com/vulnerable-endpoint" -d "id=1 UNION SELECT tbl_name FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%' --" -v
```

Or intercept and modify in Burp Suite's Repeater.

**Expected Output**: Application response includes table names in the data field, such as 'users', 'credentials', or 'config', blended with legitimate results.

### Step 3: Enumerate and Verify Extracted Tables

**Context**: Parse the response to list unique table names, then probe further (e.g., inject to count rows in each table with SELECT COUNT(*) FROM [table_name]). This validates the extraction and prioritizes high-value targets.

Manually review output or use response processing tools. If blind SQLi (no direct output), use conditional payloads like IF((SELECT COUNT(*) FROM sqlite_master WHERE type='table')>0, SLEEP(5), 0) to infer via timing.

**Expected Output**: Confirmed list of tables; follow-up queries reveal row counts, e.g., "5 rows in 'users' table".

### Step 4: Mitigate Detection and Clean Up

**Context**: Avoid alerting defenders by limiting payload size and using encoding if WAF is present (e.g., URL encode quotes). Test in a controlled environment first.

Rotate payloads or use case variations (e.g., Sqlite_master instead of sqlite_master) if blocked.

**Expected Output**: Successful extraction without triggering errors or logs indicating attack.
