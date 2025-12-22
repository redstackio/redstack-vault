---
tags:
  - sqli
  - blind-sqli
  - stacked-queries
  - impresscms
  - php
  - mysql
type: attack_chain
tools:
  - '[[tools/sqli-php]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
  - PHP
  - MySQL
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Retrieve-Security-Token-via-Auth-Bypass]]'
  - '[[procedures/Exploit-SQL-Injection-in-findusers-php]]'
  - '[[procedures/Extract-Data-or-Modify-Database-via-SQLi]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.614Z'
description: >-
  Multi-stage attack exploiting an authentication bypass and SQL injection in
  ImpressCMS to gain unauthenticated access, extract sensitive user data like
  emails and password hashes, and perform database modifications such as
  inserting new users.
skill_level: intermediate
impact_level: high
id: 02e64c74-e5cc-4466-82d8-2f18d3bb69b1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthenticated SQL Injection in ImpressCMS to Extract User Data and Create Accounts

Multi-stage attack chain demonstrating exploitation of an authentication bypass combined with SQL injection in ImpressCMS 1.4.2 to enable unauthenticated attackers to extract sensitive user information and modify the database.

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
    A[Retrieve Security Token] --> B[Exploit SQL Injection]
    B --> C[Extract Data or Modify DB]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/sqli-php]]

### Target Environment

- ImpressCMS 1.4.2 on PHP with MySQL backend
- Web server accessible (e.g., Apache/Nginx)
- No authentication required due to chained bypass

### Initial Access Requirements

- Network access to the ImpressCMS installation
- Knowledge of related auth bypass (report #1081137)
- Guessed table prefix for advanced exploitation (e.g., 'i36fd6f18_')

## Detailed Attack Procedures

### Step 1: Retrieve Security Token
procedure: [[procedures/Retrieve-Security-Token-via-Auth-Bypass]]

**Objective**: Obtain a security token without authentication to enable access to protected endpoints like /include/findusers.php.

**Instructions**: Use the custom PoC script to exploit the related authentication bypass vulnerability.

**Expected Output**: Security token retrieved and displayed in script output.

**Success Indicators**:
- Token value obtained (e.g., a session-like string)
- No authentication errors in subsequent requests

### Step 2: Exploit SQL Injection
procedure: [[procedures/Exploit-SQL-Injection-in-findusers-php]]

**Objective**: Send manipulated POST requests to /include/findusers.php with unsanitized 'groups' parameter to inject SQL payloads.

**Instructions**: Execute the PoC script with the target URL, providing 'groups' as an array containing the SQL injection payload.

**Expected Output**: Successful injection, with responses indicating boolean conditions or stacked query execution.

**Success Indicators**:
- Server responds without errors to injected payloads
- Boolean-based extraction yields data bits

### Step 3: Extract Data or Modify Database
procedure: [[procedures/Extract-Data-or-Modify-Database-via-SQLi]]

**Objective**: Use blind SQLi for data extraction or stacked queries for database writes like inserting users.

**Instructions**: Leverage boolean conditions to extract fields from users table or append INSERT statements.

**Expected Output**: Extracted data (e.g., admin email) or confirmation of new user creation.

**Success Indicators**:
- Sensitive data like emails or hashes retrieved
- New user appears in database (verify via admin panel if accessible)

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access via token retrieval
2. SQL injection to read user emails and password hashes, enabling potential account takeovers
3. Database modification to insert arbitrary users, achieving persistence

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]
- [[Persistence]]

---
*Last updated: 2023-10-01T00:00:00Z*
