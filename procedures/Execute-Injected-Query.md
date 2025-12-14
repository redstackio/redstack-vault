---
tags:
  - execution
  - exploitation
  - data-exfil
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/node-index-ts]]'
verified: false
platforms:
  - Node.js
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:15.127Z'
sub_techniques: []
id: 4f5d81a8-88dc-474e-9bc1-d20100f40a59
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Injected-Query

## Summary

This procedure runs the modified TypeORM script to execute the SQL injection, confirming the vulnerability by retrieving unintended database records.

## Description

Execution triggers the connection, data insertion, and injected query, where the function callback in the parameter leads to raw SQL injection via MysqlDriver.ts. This demonstrates potential for attackers to read sensitive data in misconfigured applications. Outcomes include console output of the exploited result.

## Requirements

1. Modified index.ts with injection
2. Valid DB configuration
3. Node.js runtime

## Defense

Defensive measures and detection strategies:

- Log and monitor database queries for anomalies (e.g., unexpected OR conditions)
- Use web application firewalls (WAF) for backend APIs
- Regularly audit ORM usage and update to patched versions

## Objectives

1. Trigger the injection payload
2. Observe data bypass and retrieval
3. Validate vulnerability impact

## Instructions

### Step 1: Run the Script

**Context**: Execute the Node.js script to perform operations.

**Command** ([[commands/node-index-ts]]):
```bash
node index.ts
```

> Connects to DB, inserts users, runs query. Expected output: Insertion logs followed by injected user object, e.g., 'User { id: 5, firstName: "Timber 3", lastName: "Saw", age: 28 }'. If errors, check DB connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/node-index-ts]]

## Tools Used

- [[tools/Node.js]]

## Tags

- execution
- exploitation
