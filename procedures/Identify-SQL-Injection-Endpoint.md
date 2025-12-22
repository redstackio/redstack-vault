---
id: proc-sqli-identify-001
name: Identify-SQL-Injection-Endpoint
tags:
  - sqli
  - web
  - recon
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/burp-intercept-request]]'
  - '[[commands/sqlmap-basic-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.122Z'
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
# Identify-SQL-Injection-Endpoint

## Summary

This procedure involves probing web application endpoints, such as those on www.zomato.com, to identify parameters vulnerable to SQL injection by injecting test payloads and observing responses.

## Description

In a typical scenario, attackers target user inputs in web forms or URL parameters that are directly concatenated into SQL queries without sanitization. For the Zomato vulnerability, testing revealed a boolean-based SQLi in one of the applications. This procedure uses manual and automated methods to detect such flaws, focusing on error-based or boolean response differences to confirm exploitability. Prerequisites include access to a proxy tool like Burp Suite for traffic interception.

## Requirements

1. Network access to the target web application (e.g., www.zomato.com)
2. Installed Burp Suite or sqlmap for testing
3. Basic knowledge of SQL syntax and HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and parameterized queries to prevent injection
- Use web application firewalls (WAFs) to block suspicious payloads
- Monitor application logs for anomalous SQL errors or repeated failed queries

## Objectives

1. Locate injectable input fields in the target application
2. Confirm SQL injection vulnerability type (e.g., boolean-based)
3. Gather initial insights into the backend database

## Instructions

### Step 1: Intercept and Test Requests

**Context**: Capture legitimate requests to the application and modify parameters to inject SQL fragments, looking for database errors.

**Command** ([[commands/burp-intercept-request]]):
```bash
# In Burp Suite: Enable Intercept in Proxy tab, submit a form or navigate to URL, then edit parameter to ' OR 1=1 --
```

> This command simulates manual testing; forward the request and check for changes like full data dumps (true condition) or empty results (false).

### Step 2: Automate Vulnerability Scanning

**Context**: Use sqlmap to systematically test the endpoint for SQLi, specifying the URL and parameter.

**Command** ([[commands/sqlmap-basic-test]]):
```bash
sqlmap -u "https://www.zomato.com/app?param=value" --batch --level=1 --risk=1
```

> Expected output includes vulnerability confirmation, such as "Parameter: param (GET) is vulnerable" and details on exploitation method (boolean).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/burp-intercept-request]]
- [[commands/sqlmap-basic-test]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/sqlmap]]

## Tags

- [[sqli]]
- [[web]]
- [[recon]]
