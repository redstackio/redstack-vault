---
id: proc-003
tags:
  - sqli
  - mysql
  - data-population
type: procedure
tools:
  - '[[tools/MySQL-Command-Line-Client]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/mysql-insert-sample-users]]'
  - '[[commands/mysql-select-all-users]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Server Software Component]]'
updated_at: '2025-12-14T03:46:15.092Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Server Software Component]]'
---
# Populate-Database-with-Sample-Data

## Summary

This procedure inserts sample user records into the 'users' table, providing data to exfiltrate via SQL injection, simulating sensitive credentials in a real application.

## Description

Insert three records: admin/admin, user/user, noob/noob. This targets the fetchById vulnerability where injecting into the 'id' parameter (e.g., 'noob\' or 1=1-- ') alters the WHERE clause to return all rows, enabling collection of all credentials.

## Requirements

1. 'users' table already created in 'test' database
2. Active MySQL session as root
3. No existing data conflicts

## Defense

Defensive measures and detection strategies:

- Hash passwords with bcrypt; avoid plaintext storage
- Log INSERT operations and alert on bulk inserts
- Use row-level security in database

## Objectives

1. Add realistic sample data
2. Verify insertion for test integrity
3. Prepare for injection-based exfiltration

## Instructions

### Step 1: Insert Records

**Context**: Add user data to table.

**Command** ([[commands/mysql-insert-sample-users]]):
```sql
INSERT INTO users (username, password) VALUES ('admin', 'admin'), ('user', 'user'), ('noob', 'noob');
```

> Expected output: Query OK, 3 rows affected.

### Step 2: Verify Data

**Context**: Confirm population.

**Command** ([[commands/mysql-select-all-users]]):
```sql
SELECT * FROM users;
```

> Expected output: Table with 3 rows: admin, user, noob.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Server Software Component]] Server Software Component: Database Services

### Sub-Techniques


## Commands Used

- [[commands/mysql-insert-sample-users]]
- [[commands/mysql-select-all-users]]

## Tools Used

- [[tools/MySQL-Command-Line-Client]]

## Tags

- sqli
- mysql
- data-population
