---
tags:
  - sqli
  - detection
  - error-based
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqli-detection-single-quote]]'
  - '[[commands/sqli-detection-double-quote]]'
verified: false
platforms:
  - Web
  - Oracle Database
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:25.763Z'
sub_techniques: []
id: 069004cb-190a-4f5c-913c-a5990c681f39
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL-Injection-Detection-via-Error-Based-Testing

## Summary

This procedure detects SQL injection vulnerabilities in web applications by sending malformed inputs like single quotes to query parameters and observing differential error responses, such as HTTP 500 vs 404, to confirm injectable points without prior knowledge of the backend.

## Description

In the context of the Oracle APEX application at ipm.informatica.com, error-based testing involves crafting requests to the /pls/apex/f endpoint. Insufficient input validation allows SQL syntax errors to propagate, resulting in distinct server responses. This is a low-risk initial reconnaissance step that confirms the presence of SQLi before exploitation, applicable to Oracle-backed web apps using PL/SQL.

## Requirements

1. Network access to the target web application (http://ipm.informatica.com/pls/apex/f)
2. Proxy tool like Burp Suite for request interception and modification
3. Basic understanding of HTTP requests and SQL syntax

## Defense

Defensive measures and detection strategies:

- Implement parameterized queries and input sanitization to prevent SQL errors
- Use web application firewalls (WAF) to block anomalous requests with quotes
- Monitor server logs for 500 errors correlated with user inputs

## Objectives

1. Confirm SQL injection vulnerability through error differentiation
2. Identify injectable parameters for further exploitation
3. Establish baseline for payload crafting

## Instructions

### Step 1: Send Single Quote Test

**Context**: Inject a single quote to cause a SQL syntax error and trigger an internal server error.

**Command** ([[commands/sqli-detection-single-quote]]):
```bash
curl "http://ipm.informatica.com/pls/apex/f?1'=1" -v
```

> This request appends '=1' after a single quote in the parameter, leading to unbalanced quotes in the SQL query. Expected output includes HTTP 500 Internal Server Error with potential database error details.

### Step 2: Send Double Quote Follow-Up

**Context**: Use double single quotes to bypass or alter the error condition, expecting a different response like 404.

**Command** ([[commands/sqli-detection-double-quote]]):
```bash
curl "http://ipm.informatica.com/pls/apex/f?1''=1" -v
```

> This escapes the quote differently, resulting in HTTP 404 Not Found, confirming the parameter is injectable based on response variance.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqli-detection-single-quote]]
- [[commands/sqli-detection-double-quote]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- sqli
- oracle-apex
- error-based
