---
id: proc-uuid-1
tags:
  - sqli
  - manual-testing
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/manual-sqli-test-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.145Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manual-SQL-Injection-Testing-in-Login-Form

## Summary

This procedure involves manually testing a web application's login form for SQL injection vulnerabilities by injecting special characters like single quotes into input fields to disrupt SQL query syntax.

## Description

In the context of the MTN Bissau admin panel, the login form at /webadmin/index.php processes POST parameters 'login' and 'pass' without proper sanitization, allowing attackers to inject SQL code. This test sends a payload with a trailing single quote in the 'login' field to attempt breaking out of the expected string in the backend query, potentially causing errors or delays that reveal the vulnerability. Successful injection enables further exploitation for unauthorized data access in the MySQL database.

## Requirements

1. Access to the target web application over HTTP/HTTPS
2. Tool like curl or a browser with developer tools for sending POST requests
3. Basic understanding of HTTP requests and SQL syntax

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries in PHP code
- Use input validation and sanitization libraries like PDO with bindParam
- Monitor application logs for SQL error patterns or anomalous request payloads

## Objectives

1. Identify if the login parameter is vulnerable to SQL injection
2. Confirm injection point without automated tools
3. Gather evidence of vulnerability for reporting or escalation

## Instructions

### Step 1: Prepare and Send Test Payload

**Context**: Craft a POST request mimicking a login attempt but injecting a single quote in the 'login' field to test for SQL breakout.

**Command** ([[commands/manual-sqli-test-post]]):
```bash
curl -X POST https://mtngbissau.com/webadmin/index.php \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" \
  -d "login=user'&pass=uesse"
```

> This command sends the payload 'login=user'' to cause a syntax error in the SQL query like SELECT * FROM users WHERE login='user'' AND pass='uesse'. Expected output includes an SQL error message or unexpected response code indicating vulnerability.

### Step 2: Analyze Response

**Context**: Review the HTTP response for signs of injection success, such as database error messages or altered form behavior.

**Command** (No specific command; use response inspection):

> Manually inspect the response body for strings like "SQL syntax error" or observe if the page loads differently. Success is indicated by error exposure confirming lack of sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/manual-sqli-test-post]]

## Tools Used


## Tags

- sqli
- manual-testing
- web
