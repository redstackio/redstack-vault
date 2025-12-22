---
id: proc-uuid-4
tags:
  - sqli
  - execution
  - mysql
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:15.008Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Database-Configuration-Form

## Summary

This procedure submits the ImpressCMS database configuration form with the injected payload, triggering the execution of arbitrary SQL to create an unauthorized database alongside the intended one.

## Description

Upon submission, the PHP backend constructs and executes the SQL query using the unsanitized input, resulting in two databases: the original 'impresscms' and the injected 'vuln'. This demonstrates the impact of the SQL injection, allowing database manipulation during installation.

## Requirements

1. Payload entered in Database name field
2. Valid MySQL host, user, and password
3. Form submission capability via browser

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls to block SQL injection patterns
- Review database logs for unexpected CREATE statements during installs
- Enforce least-privilege MySQL users for installation processes

## Objectives

1. Execute the injected SQL command
2. Verify unauthorized database creation
3. Complete installation with evidence of exploitation

## Instructions

### Step 1: Submit Form

**Context**: Finalize and send the database configuration to trigger SQL execution.

No command; click Submit button in the form.

> The backend runs the query, creating both databases. Expected output: Installation proceeds, and MySQL shows new 'vuln' database via `SHOW DATABASES;`.

### Step 2: Verify Impact

**Context**: Confirm arbitrary SQL execution.

Connect to MySQL and run:

```sql
SHOW DATABASES;
```

> Look for 'impresscms' and 'vuln' in the list to validate success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sqli
- execution
- mysql
