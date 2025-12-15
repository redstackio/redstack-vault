---
id: proc-002
tags:
  - sqli
  - testing
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
updated_at: '2025-12-14T17:26:27.849Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-SQL-Injection-with-Single-Quote

## Summary

This procedure tests for SQL injection vulnerability by appending a single quote to a URL path parameter, causing a backend query error that confirms the lack of sanitization.

## Description

Targeting the customerId parameter in the application's URL, this manual test introduces a single quote (') to terminate the SQL string prematurely, leading to a syntax error if the parameter is unsanitized. This is a classic first step in SQLi assessment, applicable to web apps where IDs are concatenated directly into queries. Success indicates potential for further exploitation to dump data.

## Requirements

1. Vulnerable URL from previous access step
2. Web browser for URL manipulation
3. Basic understanding of SQL syntax errors

## Defense

Defensive measures and detection strategies:

- Enforce input validation to reject special characters in path parameters
- Log and alert on SQL error messages exposed to users
- Use web application firewalls (WAF) to detect injection patterns

## Objectives

1. Confirm SQL injection point in customerId parameter
2. Observe error response for vulnerability validation
3. Identify the injection vector for exploitation

## Instructions

### Step 1: Modify URL Parameter

**Context**: Append a single quote to the customerId to break the query.

Manually edit the URL in the browser.

```bash
# No command; browser-based: Change customerId/732562 to customerId/732562'
```

> Full URL example: https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562'/contactPersonId/0. Expected output: SQL error page, e.g., "You have an error in your SQL syntax".

### Step 2: Analyze Error Response

**Context**: Verify the error indicates injection success.

Inspect the page source or error message for database-specific details.

> Look for phrases like "near '''" or stack traces revealing query structure.

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
