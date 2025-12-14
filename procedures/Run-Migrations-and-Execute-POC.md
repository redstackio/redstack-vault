---
id: p6f7g8h9-i0j1-2345-fghi-678901234567
name: Run-Migrations-and-Execute-POC
tags:
  - sqli
  - migrations
  - poc
  - exploit
type: procedure
tools:
  - '[[tools/manage-py]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/python-manage-py-makemigrations]]'
  - '[[commands/python-manage-py-migrate]]'
  - '[[commands/python-manage-py-poc]]'
verified: false
platforms:
  - Python
  - Database
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.955Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Run-Migrations-and-Execute-POC

## Summary

Applies database schema changes and runs the POC to trigger the SQL injection, demonstrating filter bypass and data exfiltration.

## Description

Migrations create the User table, then the POC command executes the vulnerable Q filter, injecting the connector to alter the SQL and return all records. This shows how attackers can exfiltrate sensitive data or cause DoS.

## Requirements

1. Defined model and POC code
2. Database configured (default SQLite)
3. Project ready for commands

## Defense

Defensive measures and detection strategies:

- Parameterize all ORM queries
- Log and alert on unexpected SQL patterns
- Upgrade Django to patched version

## Objectives

1. Persist model to database
2. Execute injection payload
3. Verify bypass and exfiltration

## Instructions

### Step 1: Generate Migrations

**Context**: Detects model changes and creates scripts.

**Command** ([[commands/python-manage-py-makemigrations]]):
```bash
python manage.py makemigrations
```

> Creates migration file for User model. Expected output: 'Migrations for 'webapp': webapp/migrations/0001_initial.py - Create model User'.

### Step 2: Apply Migrations

**Context**: Builds the database tables.

**Command** ([[commands/python-manage-py-migrate]]):
```bash
python manage.py migrate
```

> Applies all migrations. Expected output: 'Applying webapp.0001_initial... OK' and table creation.

### Step 3: Run POC Command

**Context**: Triggers the exploit.

**Command** ([[commands/python-manage-py-poc]]):
```bash
python manage.py poc
```

> Executes the vulnerable code. Expected output: Injected SQL printed, all users listed, 'SUCCESS: The filter was bypassed'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/python-manage-py-makemigrations]]
- [[commands/python-manage-py-migrate]]
- [[commands/python-manage-py-poc]]

## Tools Used

- [[tools/manage-py]]

## Tags

- sqli
- migrations
- poc
- exploit
