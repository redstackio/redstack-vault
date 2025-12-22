---
id: 00be1a21-2bfe-470c-81cc-615e53550c25
name: Dump-Database-Contents-Using-SQLMap
type: procedure
verified: true
submitted: true
created_at: '2020-08-19T19:04:18.134284+00:00'
updated_at: '2023-05-26T18:21:28.615058+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
sub_techniques: []
tags:
  - owasp
  - owasp-top-10
  - sql
  - sqli
  - sql-injection
  - sqlmap
  - web-applications
commands:
  - '[[commands/sqlmap-dump-specific-table]]'
platforms:
  - Web
tools:
  - '[[tools/sqlmap]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Dump-Database-Contents-Using-SQLMap

## Summary

This procedure uses SQLMap, an automated tool for exploiting SQL injection vulnerabilities, to dump the contents of a specific table from a vulnerable web application's database. It targets confirmed SQL injection points in GET parameters, specifying the database and table to extract sensitive data such as credentials or user information, enabling data exfiltration in penetration testing or red team scenarios.

## Description

SQL injection (SQLi) vulnerabilities in web applications allow attackers to manipulate database queries by injecting malicious SQL code through input fields like search parameters. Once a vulnerability is identified (e.g., via time-based blind SQLi), SQLMap automates the exploitation process to enumerate and dump database structures and contents. This procedure assumes a confirmed injectable endpoint and focuses on dumping a targeted table, such as an admin details table containing usernames and passwords. It is commonly used in web application assessments to demonstrate the impact of A1: Injection from the OWASP Top 10. The technique aligns with exploiting public-facing applications to collect data from information repositories, potentially leading to further compromise like credential theft.

## Requirements

1. Confirmed SQL injection vulnerability in a web application parameter (e.g., time-based blind SQLi in a GET parameter).
2. Network access to the target web application (e.g., HTTP/HTTPS endpoint).
3. SQLMap tool installed on the attacker's machine (Kali Linux recommended).
4. Knowledge of the target database name and table (from prior enumeration, e.g., via sqlmap --dbs and --tables).
5. Optional: Prior session file from initial SQLi detection to resume exploitation.

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and parameterized queries in application code to prevent SQLi.
- Use web application firewalls (WAFs) like ModSecurity to detect and block SQLi payloads.
- Enable database logging to monitor anomalous queries (e.g., SLEEP functions in MySQL).
- Regularly scan for vulnerabilities using tools like OWASP ZAP or Burp Suite.
- Monitor network traffic for sqlmap user-agent strings or unusual query patterns.

## Objectives

1. Extract all records from a specified database table via SQL injection.
2. Identify sensitive data such as credentials or session tokens.
3. Save dumped data to files for further analysis or reporting.
4. Validate successful exfiltration without alerting the target.

## Instructions

### Step 1: Confirm SQL Injection Vulnerability and Gather Database Info

**Context**: Before dumping, ensure the endpoint is vulnerable and enumerate databases/tables if not already known. This step uses SQLMap to test and list available databases and tables, providing the necessary details for targeted dumping.

**Command** ([[commands/sqlmap-enumerate-databases-and-tables]]):
```bash
sqlmap -u '$_TARGET_URL' --dbs --tables
```

> This command tests the URL for SQLi and lists databases (--dbs) followed by tables in the target database (--tables). Replace $_TARGET_URL with the vulnerable endpoint (e.g., http://example.com/search.php?term=). Expected output includes a list of databases like 'vulcart' and tables like 'admindetails'. If a session file exists from prior scans, SQLMap will resume automatically. Success is indicated by retrieved database and table names without connection errors.

### Step 2: Dump Contents from Specific Table

**Context**: With database and table identified, execute the dump to extract all records. This leverages the confirmed injection point to retrieve column data row-by-row, handling blind SQLi via time-based delays.

**Command** ([[commands/sqlmap-dump-specific-table]]):
```bash
sqlmap -u '$_TARGET_URL' -D $_DB_NAME -T $_TABLE_NAME --dump
```

> Run this on the vulnerable URL, specifying the database (-D) and table (-T). For example, with a MySQL backend, it will fetch columns like 'username' and 'password', then dump entries. SQLMap optimizes delays for time-based payloads and saves output to CSV files in ~/.sqlmap/output/. Expected output shows progress like "retrieved: username" and a final table dump (e.g., | sessionid | username | password |). If prompted, follow redirects (e.g., to login.php) with 'y'. Verify by checking the generated CSV file for complete data.

### Step 3: Review and Analyze Dumped Data

**Context**: Post-exploitation, inspect the extracted data for sensitive information and log it securely. This step ensures the dump's integrity and prepares data for reporting or further use.

**Instructions**: Locate the output files in ~/.sqlmap/output/$_TARGET_HOST/dump/$_DB_NAME/$_TABLE_NAME.csv. Open with a text editor or spreadsheet tool to review records. Cross-reference with known admin credentials to assess impact.

> No specific command needed, but use tools like cat or grep for quick searches:
```bash
grep "admin" ~/.sqlmap/output/*/*.csv
```
Expected output: Matching lines with sensitive data. Success indicators include complete records without truncation and no errors in SQLMap logs.
