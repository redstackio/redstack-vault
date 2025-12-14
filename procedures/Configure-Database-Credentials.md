---
tags:
  - configuration
  - mysql
  - database
type: procedure
tools:
  - '[[tools/typeorm]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.600Z'
sub_techniques: []
id: f461b682-bf87-4b84-9bcf-b4e71e42be8b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Database-Credentials

## Summary

This procedure updates the TypeORM configuration to connect to a local MySQL database, enabling database operations for vulnerability reproduction.

## Description

Editing ormconfig.json establishes the connection parameters needed for the MySQL driver. This is a manual step post-initialization, targeting local credentials to simulate a development database. Prerequisites include a running MySQL instance with a test database created.

## Requirements

1. Initialized TypeORM project
2. Running MySQL server (localhost:3306)
3. Root or user credentials with database creation privileges

## Defense

Defensive measures and detection strategies:

- Store credentials in environment variables or secret managers, not config files
- Use least-privilege database accounts
- Scan for hardcoded secrets in version control

## Objectives

1. Establish valid database connection
2. Prepare for data insertion and querying
3. Avoid connection errors in execution

## Instructions

### Step 1: Edit Configuration File

**Context**: Manually update the JSON file to include connection details.

**Command** (Manual Edit):
No command; use a text editor to modify ormconfig.json:
```json
{
  "type": "mysql",
  "host": "localhost",
  "port": 3306,
  "username": "root",
  "password": "yourpassword",
  "database": "testdb",
  "synchronize": true,
  "logging": false,
  "entities": [
    "src/entity/**/*.ts"
  ],
  "cli": {
    "entitiesDir": "src/entity",
    "migrationsDir": "src/migration",
    "targets": [
      "src"
    ]
  }
}
```

> Save the file and test connectivity by running a simple connection script if needed. Expected outcome: No syntax errors in JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/typeorm]]

## Tags

- configuration
- mysql
