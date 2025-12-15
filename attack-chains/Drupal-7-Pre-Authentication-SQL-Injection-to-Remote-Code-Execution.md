---
tags:
  - sqli
  - drupal
  - rce
  - php
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-Drupal-expandArguments-Function]]'
  - '[[procedures/Craft-Malicious-Array-for-SQL-Injection]]'
  - '[[procedures/Exploit-SQL-Injection-for-Database-Operations]]'
  - '[[procedures/Manipulate-Sessions-via-SQL-Injection]]'
  - '[[procedures/Achieve-RCE-via-Admin-Session]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:31:30.681Z'
description: >-
  A multi-stage attack exploiting a SQL injection vulnerability in Drupal 7's
  database abstraction layer to achieve arbitrary SQL execution, session
  manipulation, and remote code execution without authentication.
skill_level: intermediate
impact_level: high
id: a06ea1d9-fbf6-4676-acd2-19bc5b56e581
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Drupal 7 Pre-Authentication SQL Injection to Remote Code Execution

Multi-stage attack chain demonstrating exploitation of a SQL injection vulnerability in Drupal 7 versions prior to 7.32, leading to arbitrary SQL execution, admin session hijacking, and remote code execution.

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
    A[Analyze Vulnerability] --> B[Craft Injection Payload]
    B --> C[Execute SQL Operations]
    C --> D[Manipulate Sessions]
    D --> E[Achieve RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or curl for HTTP requests
- Knowledge of Drupal 7 structure

### Target Environment

- Drupal 7 < 7.32
- Web platform with PHP and MySQL/PostgreSQL
- Exposed Drupal site without authentication

### Initial Access Requirements

- Network access to the Drupal site
- No credentials needed (pre-auth)
- Ability to send crafted HTTP requests

## Detailed Attack Procedures

### Step 1: Analyze Vulnerability
procedure: [[procedures/Analyze-Drupal-expandArguments-Function]]

**Objective**: Identify the SQL injection flaw in Drupal's database abstraction layer by reviewing the expandArguments function.

**Instructions**: Examine the source code of Drupal 7's includes/database/database.inc, focusing on the expandArguments function. Look for the foreach loop that iterates over array keys to generate placeholders for IN clauses, noting the assumption of integer keys.

**Expected Output**: Understanding that non-integer keys (e.g., strings with SQL payloads) can inject code by altering the SQL structure.

**Success Indicators**:
- Confirmed vulnerability in expandArguments handling of array keys
- Identified potential injection points in db_query calls with IN clauses

### Step 2: Craft Malicious Array
procedure: [[procedures/Craft-Malicious-Array-for-SQL-Injection]]

**Objective**: Create a malicious array structure to exploit the non-integer key handling in prepared statements.

**Instructions**: Construct an array like array(':name' => array('test) -- ' => 'user1', 'test' => 'user2')) to be passed to a db_query IN clause. This results in malformed SQL such as 'SELECT * FROM users WHERE name IN (:name_test) -- , :name_test )', injecting a comment to bypass the query.

**Expected Output**: Payload that alters the generated SQL, allowing injection without authentication via a crafted HTTP request to a vulnerable endpoint (e.g., user search or filter form).

**Success Indicators**:
- Payload generates invalid placeholders leading to SQL injection
- Test request returns unexpected database results or errors indicating injection success

### Step 3: Exploit for Database Operations
procedure: [[procedures/Exploit-SQL-Injection-for-Database-Operations]]

**Objective**: Use the SQL injection to perform arbitrary database actions like insert, update, delete, dump, or drop pre-authentication.

**Instructions**: Send the crafted payload via HTTP POST/GET to a Drupal endpoint using db_query with IN (e.g., a search form). Leverage PDO's multi-query support to chain operations, such as dumping user tables or inserting records.

**Expected Output**: Successful execution of arbitrary SQL, e.g., SELECT * FROM users revealing data, or INSERT statements modifying the database.

**Success Indicators**:
- Database data retrieved or modified without auth
- No authentication errors; query executes as intended

### Step 4: Manipulate Sessions
procedure: [[procedures/Manipulate-Sessions-via-SQL-Injection]]

**Objective**: Inject SQL to create or modify a session record granting admin privileges (User ID 1).

**Instructions**: Using the injection, execute an INSERT into the sessions table: INSERT INTO sessions (sid, ssid, uid, hostname, timestamp, session) VALUES ('fake_sid', '', 1, 'attacker_ip', UNIX_TIMESTAMP(), 'admin_session_data'). Follow with a session cookie set to the fake_sid to impersonate admin.

**Expected Output**: Valid admin session established, allowing access to privileged Drupal areas.

**Success Indicators**:
- Session cookie accepted as admin user
- Access to /admin pages without login

### Step 5: Achieve Remote Code Execution
procedure: [[procedures/Achieve-RCE-via-Admin-Session]]

**Objective**: Leverage the admin session and Drupal's PHP callback features to execute arbitrary code.

**Instructions**: With admin access, upload or trigger a module/callback that executes PHP code, e.g., via a form with file upload or serialized object deserialization. Use a second request to run code like system('id') and clean up the session.

**Expected Output**: Arbitrary PHP code execution on the server, e.g., command output or file creation.

**Success Indicators**:
- Server commands executed successfully
- Session cleanup prevents detection

## Attack Chain Summary

### Key Achievements

1. Pre-auth SQL injection via array key manipulation
2. Arbitrary database control leading to session hijacking
3. Full RCE through Drupal's admin features and PHP callbacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
