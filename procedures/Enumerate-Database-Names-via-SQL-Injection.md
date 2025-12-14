---
id: proc-enum-dbs-sqli-001
tags:
  - sqli
  - database-enumeration
  - data-exfiltration
type: procedure
tools:
  - '[[tools/SQLMap]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-enum-dbs]]'
verified: false
platforms:
  - Web
  - Database
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T03:46:20.153Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
---
# Enumerate-Database-Names-via-SQL-Injection

## Summary

This procedure exploits a confirmed SQL injection vulnerability to enumerate database names from the target DBMS, enabling further reconnaissance for data extraction.

## Description

Building on detected SQLi, this step uses SQLMap to query the database schema. In the Sony scenario, error-based injection in the login form allowed dumping database names, potentially exposing sensitive data stores. Targets relational DBMS like MySQL or PostgreSQL in web backends.

## Requirements

1. Confirmed SQLi vulnerability from prior detection
2. SQLMap installed and request file available
3. Stable connection to avoid rate-limiting

## Defense

Defensive measures and detection strategies:

- Use least-privilege database accounts for web apps
- Enable query logging and alert on schema queries (e.g., SHOW DATABASES)
- Implement database activity monitoring (DAM) tools

## Objectives

1. Extract list of database names via injected queries
2. Identify potentially sensitive databases for targeting
3. Assess scope for deeper exploitation like table enumeration

## Instructions

### Step 1: Confirm Injection Point

**Context**: Re-run detection to ensure the vuln is still exploitable.

Use a quick SQLMap test on the request file.

### Step 2: Enumerate Databases

**Context**: Trigger SQLMap to dump database names.

Execute [[commands/sqlmap-enum-dbs]]:

```bash
sqlmap -r request.txt --dbs --batch
```

> The --dbs flag instructs SQLMap to enumerate databases using blind or error-based techniques based on prior detection.

**Expected Output**: "Available databases [3]: [*] sony_main, [*] users_db, [*] admin_config".

### Step 3: Validate and Log

**Context**: Save results and check for further options.

SQLMap will suggest next commands like --tables for selected DBs. Log the output for reporting.

**Expected Output**: Text file or console list of DB names, confirming successful enumeration.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Local System]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-enum-dbs]]

## Tools Used

- [[tools/SQLMap]]

## Tags

- [[sqli]]
- [[database-enumeration]]
