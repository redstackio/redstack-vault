---
tags:
  - sqli
  - mysql
  - database-setup
type: procedure
tools:
  - '[[tools/MySQL]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-user-table-mysql]]'
  - '[[commands/insert-test-data-user-table]]'
platforms:
  - Linux
  - macOS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 26fb715f-56be-41f9-8e6b-25db5922480f
created_at: '2025-12-14T03:46:15.039Z'
updated_at: '2025-12-14T03:46:15.039Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Test-MySQL-Database

## Summary

This procedure configures a MySQL test database with a 'user' table and sample data, providing a controlled environment to demonstrate SQL injection effects in the untitled-model module.

## Description

A MySQL instance is set up on localhost with an empty 'test' database. The procedure creates a simple table and inserts records that can be queried normally or via injection. This mirrors a typical application database, highlighting how unsanitized inputs lead to data leakage. Run via MySQL client like mysql command-line tool.

## Requirements

1. MySQL server running on localhost (version 5.7+)
2. Root user access with empty password for testing
3. 'test' database created (CREATE DATABASE test; if needed)

## Defense

Defensive measures and detection strategies:

- Enable MySQL query logging to detect anomalous patterns
- Use least-privilege accounts for application connections
- Implement web application firewalls (WAF) to block SQLi payloads

## Objectives

1. Establish baseline data for comparison
2. Ensure database readiness for module interaction
3. Validate setup without affecting production data

## Instructions

### Step 1: Create User Table

**Context**: Defines the schema for the user table with id, firstName, lastName, and age columns using InnoDB engine.

**Command** ([[commands/create-user-table-mysql]]):
```sql
CREATE TABLE `user` ( `id` int(11) NOT NULL, `firstName` varchar(255) NOT NULL, `lastName` varchar(255) NOT NULL, `age` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```

> Executes in MySQL shell (mysql -u root -p test). Expected output: Query OK, 0 rows affected.

### Step 2: Insert Test Data

**Context**: Populates the table with two records to test filter queries.

**Command** ([[commands/insert-test-data-user-table]]):
```sql
INSERT INTO `user` (`id`, `firstName`, `lastName`, `age`) VALUES (1, 'Timber', 'Saw', 25), (2, 'Timber 0', 'Saw', 25);
```

> Inserts sample users. Expected output: Query OK, 2 rows affected.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/create-user-table-mysql]]
- [[commands/insert-test-data-user-table]]

## Tools Used

- [[tools/MySQL]]

## Tags

- sqli
- mysql
