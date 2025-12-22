---
id: proc-uuid-3
tags:
  - sqli
  - injection
  - backtick
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
updated_at: '2025-12-14T03:46:15.019Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-SQL-Payload-in-Database-Name

## Summary

This procedure injects a SQL payload into the 'Database name' field of the ImpressCMS installation form, exploiting the failure of PHP's addslashes to escape backticks, allowing query termination and arbitrary SQL execution.

## Description

The vulnerability stems from addslashes escaping only single quotes, double quotes, backslashes, and NUL bytes, but not backticks used in MySQL for identifiers. The payload closes the original CREATE DATABASE statement with a backtick and semicolon, then appends a new command like CREATE DATABASE. This occurs during the installation's database setup on a web-based form.

## Requirements

1. Active ImpressCMS installation wizard at database configuration
2. Valid MySQL connection details for other fields
3. Knowledge of MySQL syntax for injection

## Defense

Defensive measures and detection strategies:

- Use prepared statements or PDO with proper escaping for all inputs
- Validate and sanitize database names to reject special characters like backticks and semicolons
- Log and audit installation attempts for injection patterns

## Objectives

1. Bypass input sanitization with backtick-based payload
2. Terminate original query and inject new SQL
3. Prepare for execution without form rejection

## Instructions

### Step 1: Enter Payload

**Context**: Fill the Database name field with the injection payload to manipulate the SQL query.

No command; form input:

Database name: `impresscms`; create database `vuln`

> This payload uses a closing backtick to end the original database name, a semicolon to terminate the statement, and injects a new CREATE DATABASE command. Expected: Field accepts input without errors.

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
- injection
- backtick
