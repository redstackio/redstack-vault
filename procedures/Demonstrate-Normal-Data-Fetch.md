---
id: proc-004
tags:
  - sqli
  - node.js
  - normal-execution
type: procedure
tools:
  - '[[tools/Node.js-Runtime]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/node-normal-fetch]]'
  - '[[commands/node-run-app]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:15.091Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-Normal-Data-Fetch

## Summary

This procedure creates and runs a Node.js script using query-mysql to fetch a single user record normally, validating the setup before injection exploitation.

## Description

Configure the module with MySQL connection details and call fetchById('users', 'noob', 'username'), which generates a safe query for one record. This contrasts with the exploited version, highlighting the vulnerability's impact.

## Requirements

1. query-mysql installed
2. MySQL running with populated 'test' database
3. app.js file in project root

## Defense

Defensive measures and detection strategies:

- Input validation on all parameters (table, id, name_id)
- Use parameterized queries or libraries like mysql2 with placeholders
- Log query executions for anomalies

## Objectives

1. Test module connectivity and normal query
2. Confirm single-record retrieval
3. Baseline for comparing injection results

## Instructions

### Step 1: Write Script

**Context**: Create app.js with normal fetch.

**Command** ([[commands/node-normal-fetch]]):
```javascript
const query = require('query-mysql'); query.configure({ 'host':'127.0.0.1', 'user':'root', 'password':'root', 'database':'test' }); query.base.fetchById('users','noob','username',(msg, res)=>{ console.log(msg, res) });
```

> Save to app.js; no output yet.

### Step 2: Execute Script

**Context**: Run to fetch data.

**Command** ([[commands/node-run-app]]):
```bash
node app.js
```

> Expected output: fetchById success [ { username: 'noob', password: 'noob' } ].

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/node-normal-fetch]]
- [[commands/node-run-app]]

## Tools Used

- [[tools/Node.js-Runtime]]

## Tags

- sqli
- node.js
- normal-execution
