---
tags:
  - access
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:46:25.936Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 82fedb6f-5b71-4a3d-bbd4-b59a62adc7e0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-SQL-Query-Analyzer-Interface

## Summary

This procedure outlines accessing the internal SQL Query Analyzer interface in HackerOne's application, requiring authenticated engineer privileges, to set up for subsequent SQL injection exploitation.

## Description

The SQL Query Analyzer is an internal feature allowing engineers to run EXPLAIN ANALYZE queries on the database. It wraps user input in a transaction for safety, but this can be bypassed. Access is via a web interface on localhost:8080, assuming internal network or local setup. Successful access positions the attacker to input raw SQL without immediate execution risks.

## Requirements

1. Authenticated session as an internal engineer
2. Access to http://localhost:8080 or equivalent internal URL
3. Web browser

## Defense

Defensive measures and detection strategies:

- Restrict access to SQL tools to minimal privileged users
- Monitor access logs for SQL Query Analyzer usage
- Implement IP whitelisting for internal tools

## Objectives

1. Gain interface access for query submission
2. Verify 'public' database connection availability
3. Prepare for payload injection without alerting

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to the HackerOne internal dashboard to reach the support tools section.

No specific command; use browser to visit http://localhost:8080/support/sql_query_analyzer.

> Ensure session is active; page should load with query input fields and database selector.

### Step 2: Select Connection

**Context**: Choose the target database to ensure the injection targets the correct schema.

Select 'public' from the database connection dropdown.

> Interface ready for raw_sql input; no output yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access
- web
