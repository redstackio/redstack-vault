---
id: proc-uuid-1
tags:
  - sqli
  - error-based
  - modx
type: procedure
tools:
  - '[[tools/Burp-Repeater]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/Test-SQL-Injection-with-Single-Quote-in-URL]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:47.405Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SQL-Syntax-Error-in-404-Logging

## Summary

This procedure tests for SQL injection in MODx CMS by injecting a single quote into a non-existent URL, causing a syntax error in the 404 logging INSERT query and exposing the vulnerability through the error response.

## Description

In the attack scenario, the MODx CMS logs 404 errors to a MySQL database without sanitizing the user-controlled URL path. Crafting a URL like /Campin/jeatest' inserts the quote directly into the SQL VALUES clause, breaking the query and revealing the injection point. This is the initial reconnaissance step to confirm the presence of SQLi before attempting exploitation. Prerequisites include access to Burp Repeater or a similar proxy for request crafting, and the target must use MODx with unsanitized logging.

## Requirements

1. Network access to the target web application (e.g., smarthistory.khanacademy.org)
2. Burp Suite or equivalent HTTP interception tool
3. Basic knowledge of SQL syntax and HTTP requests

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries for all database inputs
- Implement web application firewalls (WAF) to detect and block SQL injection patterns like single quotes in URLs
- Sanitize and validate all user inputs before database insertion
- Monitor logs for SQL error exposures and rate-limit 404 requests

## Objectives

1. Confirm unsanitized URL insertion into SQL query
2. Expose the database table structure (e.g., error_404_logger)
3. Establish foundation for further SQLi exploitation

## Instructions

### Step 1: Craft and Send Injection Request

**Context**: Intercept and modify a GET request to a non-existent path, appending a single quote to trigger the syntax error.

**Command** ([[commands/Test-SQL-Injection-with-Single-Quote-in-URL]]):
```bash
curl -X GET "http://smarthistory.khanacademy.org/Campin/jeatest'" -H "Host: smarthistory.khanacademy.org" -H "Accept: */*" -H "Accept-Language: en" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)" --connect-timeout 10
```

> This command simulates the request in Burp Repeater. The single quote closes the string prematurely, causing a MySQL error like "You have an error in your SQL syntax" with the partial query visible, confirming the injection point in the VALUES clause.

### Step 2: Analyze Response

**Context**: Review the 404 page for SQL error details to validate the vulnerability.

**Command** (Manual inspection in tool):
```bash
# No command; inspect HTTP response body for error message
```

> Look for the echoed URL in the error, e.g., VALUES ('/Campin/jeatest'','IP', ...). Success is indicated by the syntax error exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/Test-SQL-Injection-with-Single-Quote-in-URL]]

## Tools Used

- [[tools/Burp-Repeater]]

## Tags

- [[sqli]]
- [[web]]
