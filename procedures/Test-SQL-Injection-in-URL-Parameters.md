---
id: proc-test-sqli-001
tags:
  - sqli
  - testing
  - injection
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
updated_at: '2025-12-14T03:15:05.284Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-SQL-Injection-in-URL-Parameters

## Summary

This procedure tests for SQL injection vulnerabilities by appending a single quote to URL path parameters, observing backend errors that indicate lack of input sanitization.

## Description

Targeting applications like https://corporate.admyntec.co.za/, modify path parameters (e.g., customerId) with a single quote to inject malformed SQL. If the backend directly concatenates the parameter into queries without escaping, it causes syntax errors, confirming the vulnerability. This is a low-risk manual test before automated exploitation.

## Requirements

1. Valid base URL from application workflow
2. Web browser for URL manipulation
3. Basic understanding of SQL syntax errors

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries in backend code
- Deploy intrusion detection systems (IDS) to flag anomalous requests with quotes or SQL keywords

## Objectives

1. Detect unsanitized input in URL parameters
2. Confirm SQL injection point via error responses
3. Avoid triggering alerts with minimal payload

## Instructions

### Step 1: Modify URL and Test

**Context**: Append a single quote to the vulnerable parameter to break the SQL query.

No command required; modify and visit in browser: https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562'/contactPersonId/0

> Expect a server error like "SQL syntax error" or stack trace revealing database details. Successful test shows query breakage.

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
- injection
