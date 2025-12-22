---
tags:
  - sqli
  - django
  - execution
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Python
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.061Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 7bc63430-4b49-4aea-ae70-a998c978a117
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Injected-Query-in-Django-ORM

## Summary

This procedure triggers the query execution to run the injected SQL, realizing the SQLi for data manipulation or exfiltration.

## Description

Calling _fetch_all() or iterating the queryset executes the SQL against the database. With the injection, arbitrary SQL runs, e.g., UNION for exfil or COPY TO PROGRAM for RCE on PostgreSQL. Impacts authenticated users controlling aliases in Django apps.

## Requirements

1. Chained queryset with injection
2. Database connection (SQLite/PostgreSQL)
3. Permissions for SQL execution

## Defense

Defensive measures and detection strategies:

- Enable SQL query logging and WAF for injection detection
- Use parameterized queries strictly; avoid dynamic SQL
- Least privilege on DB users to limit RCE impact

## Objectives

1. Execute arbitrary SQL via injection
2. Achieve data exfil or modification
3. Escalate to RCE if PostgreSQL

## Instructions

### Step 1: Fetch Query Results

**Context**: Invoke the fetch to run SQL.

**Command** (Python code):
```python
list(qs)  # or qs._fetch_all()
```

> This executes the query. Expected output: Results with injected effects, e.g., extra data or errors revealing injection success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sqli
- django
- execution
