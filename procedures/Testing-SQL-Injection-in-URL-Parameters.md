---
id: proc-sqli-test-url-001
tags:
  - sqli
  - testing
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.509Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Testing-SQL-Injection-in-URL-Parameters

## Summary

This procedure tests the customerId parameter in a URL path for SQL injection by injecting a single quote, confirming vulnerability through error messages.

## Description

Targeting paths like /path/customerId/value on admyntec.co.za, append ' to the value to break SQL queries. Lack of sanitization causes errors revealing the vuln. Used after recon; leads to exploitation if errors show SQL syntax issues.

## Requirements

1. Vulnerable URL from recon
2. Browser or curl for manual testing
3. Basic SQL knowledge

## Defense

Defensive measures and detection strategies:

- Parameterize queries with prepared statements
- Input validation and sanitization for URL paths
- Error handling to suppress SQL details

## Objectives

1. Confirm injectable parameter
2. Identify error-based confirmation
3. Assess injection type (e.g., error-based)

## Instructions

### Step 1: Inject Single Quote

**Context**: Modify the URL to include ' in customerId to trigger syntax error.

**Command** (Manual URL Test):
```bash
# Example: curl "http://admyntec.co.za/path/customerId=1'"
```

> Response shows SQL error like 'You have an error in your SQL syntax', confirming unsanitized input.

### Step 2: Analyze Response

**Context**: Check for database-specific errors.

**Command** (Manual):
```bash
# Inspect HTTP response body
```

> Expected: Leaked query fragments or table names.

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
- testing
