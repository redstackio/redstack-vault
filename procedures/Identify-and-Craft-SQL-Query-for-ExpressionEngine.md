---
id: proc-expressionengine-sqli-craft
tags:
  - sqli
  - expressionengine
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/base64-encode-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:47.213Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-and-Craft-SQL-Query-for-ExpressionEngine

## Summary

This procedure identifies the vulnerable SQL Query Form endpoint in ExpressionEngine and crafts Base64-encoded SQL queries for arbitrary execution, enabling data extraction from database tables like exp_members when accessed by an authenticated admin.

## Description

The ExpressionEngine SQL Query Form module at `/admin.php?/cp/utilities/query/run-query` accepts GET parameter `thequery` as Base64-encoded SQL without validation, allowing read-only operations (SELECT, SHOW). This targets PHP-based web apps with MySQL, requiring admin session for execution. Outcomes include disclosing user data, which can chain to broader compromises.

## Requirements

1. Access to target ExpressionEngine instance admin interface
2. Knowledge of database schema (e.g., exp_members table)
3. Tool for Base64 encoding (built-in bash)
4. Valid admin session on target (exploited via social engineering)

## Defense

Defensive measures and detection strategies:

- Disable or restrict SQL Query Form module to trusted admins only
- Implement input validation and sanitization on `thequery` parameter
- Monitor admin access logs for unusual GET requests to utilities/query
- Use WAF rules to block Base64-decoded SQL patterns in URLs

## Objectives

1. Locate and confirm vulnerable endpoint
2. Encode malicious SQL for injection
3. Prepare payload for delivery to admin

## Instructions

### Step 1: Locate the Endpoint

**Context**: Navigate to the admin utilities to identify the query form path.

**Command** ([[No specific command]]):

Inspect the admin interface or source code for `/admin.php?/cp/utilities/query/run-query`.

> This endpoint handles GET requests; test with a benign query to confirm.

### Step 2: Craft and Encode SQL Query

**Context**: Create a SQL statement targeting sensitive data and encode it in Base64.

**Command** ([[commands/base64-encode-query]]):
```bash
echo -n 'SELECT * FROM exp_members' | base64 -w 0
```

> Outputs Base64 string like `c2VsZWN0ICogZnJvbSBleHBfbWVtYmVycw==`. Append to URL for execution. Expected: Encoded payload ready for phishing link.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/base64-encode-query]]

## Tools Used


## Tags

- sqli
- expressionengine
- database-extraction
