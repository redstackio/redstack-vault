---
id: proc-uuid-3
tags:
  - sqli
  - database-enumeration
  - sqlmap
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-enumerate-databases]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.023Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Database-Enumeration-with-sqlmap

## Summary

This procedure leverages a confirmed SQL injection to enumerate all accessible databases using sqlmap, revealing the database schema and highlighting risks of unauthorized access to sensitive information like user data.

## Description

Once injection is confirmed, sqlmap's --dbs option queries the MySQL information_schema to list databases. Applied to the vulnerable login endpoint, this exposes 13 databases, including system ones (mysql, information_schema) and custom (testusers, LEAM), demonstrating potential for further extraction of schemas or data from user-related tables.

## Requirements

1. Prior confirmation of SQLi vulnerability
2. sqlmap installed and configured
3. Same network access as confirmation step

## Defense

Defensive measures and detection strategies:

- Restrict database privileges to least necessary for the application
- Log and alert on queries accessing information_schema
- Use database activity monitoring (DAM) tools to detect enumeration attempts

## Objectives

1. List all databases accessible via the injection
2. Identify sensitive or custom databases for targeted exfiltration
3. Quantify the scope of unauthorized access

## Instructions

### Step 1: Run sqlmap for Database Listing

**Context**: Build on the injection point to enumerate databases, reusing evasion settings.

**Command** ([[commands/sqlmap-enumerate-databases]]):
```bash
python3 sqlmap.py --level=5 --risk=3 --tamper=space2comment --random-agent -u https://target.com/olc/setlogin.php --data="username=admin&password=pass" -p username --dbms=mysql --dbs
```

> This executes blind queries to fetch database names. Expected output: Available databases [13]: information_schema, mysql, testusers, LEAM, etc.

### Step 2: Analyze Enumerated Databases

**Context**: Review the list for high-value targets like user databases.

**Command** (No new; output parsing):

> Note custom databases indicating potential sensitive data. Success if user-related DBs like testusers are listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-enumerate-databases]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- sqli
- enumeration
