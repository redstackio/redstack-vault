---
id: proc-identify-wp-login-001
tags:
  - sqli
  - wordpress
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-basic-login-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:09.899Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify WordPress Login Endpoint for SQLi

## Summary

This procedure locates the WordPress login form endpoint and identifies injectable parameters like 'log' and 'pwd' for SQL injection testing, setting the stage for blind SQLi exploitation.

## Description

In a WordPress environment, the login form at /wp-login.php processes POST requests with username (log) and password (pwd) parameters. Insufficient sanitization allows SQL injection. This step involves inspecting the form to confirm the target without triggering alerts, applicable to any PHP/MySQL-based web app.

## Requirements

1. Network access to the target domain (e.g., www.acronis.cz)
2. Browser or curl for HTTP requests
3. Basic knowledge of HTTP POST methods

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and input validation in login queries
- Use Web Application Firewalls (WAF) to detect anomalous payloads
- Monitor response times for delays indicating time-based attacks

## Objectives

1. Confirm the presence of /wp-login.php
2. Identify 'log' and 'pwd' as potential injection points
3. Establish baseline response time without payloads

## Instructions

### Step 1: Access the Login Endpoint

**Context**: Send a basic POST to verify the endpoint responds as expected.

**Command** ([[commands/curl-basic-login-test]]):
```bash
curl -X POST https://www.acronis.cz/wp-login.php -d "log=admin&pwd=test&wp-submit=Log+In" -w "%{time_total}s"
```

> This tests normal login flow; expect quick response (~0.5-1s) and error for invalid creds.

### Step 2: Inspect Form Parameters

**Context**: Review the request body to note parameters like log, pwd, and any CAPTCHA fields.

**Command** ([[commands/curl-basic-login-test]] with verbose):
```bash
curl -v -X POST https://www.acronis.cz/wp-login.php -d "log=admin&pwd=test&wp-submit=Log+In"
```

> Look for 200/302 status and form confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-basic-login-test]]

## Tools Used


## Tags

- sqli
- wordpress
- recon

