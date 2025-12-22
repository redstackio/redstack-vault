---
id: proc-list-tables-001
tags:
  - sqli
  - sqlmap
  - table-enumeration
type: procedure
tools:
  - '[[tools/SQLMap]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/sqlmap-list-tables]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.336Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# List Tables in Acronis Site Database

## Summary

This procedure employs SQLMap to dump table names from the 'acronis_site' database, revealing sensitive structures like 'users' and 'password_resets' for potential credential theft.

## Description

Targeting the identified database, SQLMap uses the established injection point to query INFORMATION_SCHEMA.TABLES, listing 24 tables in the Acronis Laravel application. This exposes data schemas without real user data in the dev environment but highlights compromise risks.

## Requirements

1. Confirmed SQLi and database name from prior enumeration
2. SQLMap session or request file
3. Stable connection to the endpoint

## Defense

Defensive measures and detection strategies:

- Restrict database user privileges to least necessary
- Audit schema access logs for unauthorized queries
- Implement anomaly detection on query volumes and types

## Objectives

1. Map database schema
2. Identify high-value tables
3. Enable targeted data extraction

## Instructions

### Step 1: Target Specific Database

**Context**: Specify 'acronis_site' for table listing.

Execute [[commands/sqlmap-list-tables]]:

```bash
sqlmap -D acronis_site --tables
```

> Outputs 24 tables including sensitive ones.

### Step 2: Analyze Table List

**Context**: Review for exploitable structures.

Look for tables like 'users', 'password_resets'; note potential for --dump in follow-ups.

> Success if full list retrieved, highlighting 'users' etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-list-tables]]

## Tools Used

- [[tools/SQLMap]]

## Tags

- sqli
- sqlmap
