---
id: proc-uuid-001
tags:
  - sql-injection
  - detection
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T03:46:14.861Z'
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
# Detect-SQL-Injection-in-From-Parameter

## Summary

This procedure identifies SQL injection vulnerabilities in the 'from' parameter of a web application's file upload endpoint by injecting a single quote to break SQL syntax and observe error responses.

## Description

In a typical attack scenario targeting public-facing web apps backed by MSSQL, testers intercept HTTP POST requests to upload endpoints and tamper with parameters. A single quote in the 'from' field causes unescaped input to disrupt the SQL query, revealing the injection point. This is a foundational step for blind SQLi exploitation, applicable to DoD or similar environments where input validation is lacking.

## Requirements

1. Proxy tool like Burp Suite for request interception
2. Access to the target web application endpoint
3. Basic knowledge of HTTP multipart/form-data

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries
- Use web application firewalls (WAF) to block quote injections
- Log and monitor SQL error responses

## Objectives

1. Confirm the 'from' parameter is vulnerable to SQLi
2. Establish baseline for payload crafting
3. Minimize false positives by observing syntax errors

## Instructions

### Step 1: Intercept and Modify Request

**Context**: Capture the legitimate POST request to /FileTransfer/Upload and alter the 'from' parameter to test for injection.

No specific command; use proxy interface to set 'from' to 'hello'' and submit.

> The response will show SQL errors if vulnerable, such as syntax issues from the unclosed quote.

### Step 2: Analyze Response

**Context**: Review server output for indicators of SQL interpretation.

No command; inspect HTTP response body for database errors.

> Successful detection: Response contains MSSQL error messages or behaves unexpectedly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[sql-injection]]
- [[detection]]
