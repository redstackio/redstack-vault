---
tags:
  - sqli
  - typeorm
  - mysql
  - node.js
  - database-exploitation
type: attack_chain
tools:
  - '[[tools/npx]]'
  - '[[tools/typeorm]]'
  - '[[tools/Node.js]]'
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Node.js
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initialize-TypeORM-Project]]'
  - '[[procedures/Configure-Database-Credentials]]'
  - '[[procedures/Modify-Script-for-Injection]]'
  - '[[procedures/Execute-Injected-Query]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.619Z'
description: >-
  Demonstrates SQL injection exploitation in TypeORM by using unescaped function
  callbacks in query parameters to bypass filters and extract sensitive database
  data.
id: d640d504-9d8b-46d6-8f31-88e624d59559
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL Injection via Function Callbacks in TypeORM Query Builder

Multi-stage attack chain demonstrating exploitation of a SQL injection vulnerability in TypeORM's MysqlDriver by using function callbacks in query parameters to inject raw SQL and retrieve unauthorized data from a MySQL database.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Configure DB] --> C[Inject Payload] --> D[Execute and Exfil]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npx]]
- [[tools/typeorm]]
- [[tools/Node.js]]
- [[tools/npm]]

### Target Environment

- Node.js runtime (v8.12.0 or later)
- MySQL database server running locally
- TypeORM version 0.2.14

### Initial Access Requirements

- Local development environment with Node.js and MySQL installed
- Administrative access to MySQL for credential setup
- No network access required; local reproduction

## Detailed Attack Procedures

### Step 1: Initialize TypeORM Project
procedure: [[procedures/Initialize-TypeORM-Project]]

**Objective**: Set up a basic TypeORM project to replicate the vulnerable environment.

**Instructions**: Use [[commands/npx-typeorm-init]] to create a new project:

```bash
npx typeorm init --name Test --database mysql
```

This generates project files including ormconfig.json, an entity folder, and index.ts. Verify the project structure is created without errors.

**Expected Output**: Project directory 'Test' with configuration files and sample scripts.

**Success Indicators**:
- Project files generated successfully
- No initialization errors

### Step 2: Configure Database Credentials
procedure: [[procedures/Configure-Database-Credentials]]

**Objective**: Connect the project to a local MySQL instance by updating configuration.

**Instructions**: Manually edit the ormconfig.json file to include your local MySQL host, port, username, password, and database name. For example, set "host": "localhost", "port": 3306, "username": "root", "password": "yourpassword", "database": "testdb".

**Expected Output**: Valid JSON configuration file with database details.

**Success Indicators**:
- Configuration file updated without syntax errors
- Database connection testable in subsequent steps

### Step 3: Modify Script for Injection
procedure: [[procedures/Modify-Script-for-Injection]]

**Objective**: Insert test data and craft a vulnerable query using a function callback to inject SQL.

**Instructions**: Edit index.ts to import reflect-metadata and createConnection from 'typeorm'. Define a User entity with fields like id, firstName, lastName, age. Create a connection, insert 10 test users (e.g., firstName: 'Timber ' + i), then use createQueryBuilder('user').where('user.firstName = :name', {name: () => "-1 or firstName=0x54696d6265722033"}).getOne() to inject and retrieve a specific user.

**Expected Output**: Modified index.ts ready for execution with injection payload.

**Success Indicators**:
- Script compiles without errors
- Test data insertion logic present
- Injection function callback integrated

### Step 4: Execute Injected Query
procedure: [[procedures/Execute-Injected-Query]]

**Objective**: Run the script to trigger the injection and observe unauthorized data retrieval.

**Instructions**: Execute the modified script using [[commands/node-index-ts]]:

```bash
node index.ts
```

Monitor console output for insertion confirmations and the injected query result.

**Expected Output**: Logs showing user insertions followed by the injected result, e.g., User { id: 5, firstName: 'Timber 3', lastName: 'Saw', age: 28 }.

**Success Indicators**:
- Script runs without crashes
- Unauthorized user data retrieved via injection
- Database query bypassed as intended

## Attack Chain Summary

### Key Achievements

1. Successful reproduction of SQL injection in TypeORM query builder
2. Bypassing parameter filters to read sensitive user data
3. Demonstration of impact on applications using function callbacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
