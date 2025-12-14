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
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.213Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manual-SQL-Injection-Testing

## Summary

This procedure involves manually testing a web application's input parameters for SQL Injection vulnerabilities by observing error responses to malformed inputs like single quotes, providing initial indicators of injection flaws without automation.

## Description

In the context of Mozilla's social platform registration, this targets the invite_code parameter in a POST request to an OIDC proxy endpoint. By appending quotes and observing HTTP status codes (e.g., 500 errors), attackers can identify unsanitized inputs leading to SQL errors. This is a foundational step before advanced exploitation, requiring only a proxy tool for request modification in a public-facing web environment.

## Requirements

1. Access to the target registration endpoint (public internet)
2. Proxy tool like Burp Suite to intercept and modify HTTP requests
3. Basic understanding of HTTP POST requests and SQL syntax

## Defense

Defensive measures and detection strategies:

- Implement input validation and prepared statements in backend queries
- Use Web Application Firewalls (WAF) to detect quote injections and anomalous requests
- Log and monitor for 500 errors correlated with suspicious payloads

## Objectives

1. Identify potential SQL Injection points in form parameters
2. Confirm error-based indicators without data leakage
3. Prepare for advanced blind SQLi testing

## Instructions

### Step 1: Intercept Registration Request

**Context**: Start the registration flow on the target site to capture the legitimate POST request.

No command; use browser to navigate to mozilla.social registration, enter dummy details, and intercept with proxy.

> Expected: POST to /interaction/KTTbkN8LaJgYIb7fIwPYX/signup with invite_code parameter.

### Step 2: Test Single Quote Injection

**Context**: Modify the invite_code to include a single quote to trigger SQL parsing errors.

Send modified request:

```bash
# Via proxy or curl equivalent:
POST /interaction/KTTbkN8LaJgYIb7fIwPYX/signup HTTP/1.1
Host: prod.oidc-proxy.prod.webservices.mozgcp.net
Content-Type: application/x-www-form-urlencoded

invite_code=xxx'
```

> Explanation: A 500 error indicates the quote disrupted the SQL query, suggesting lack of sanitization.

### Step 3: Test Escaped Input

**Context**: Use double quotes to check if the input is processed without error after basic escaping.

```bash
invite_code=xxx''
```

> Expected: 200 OK response, confirming the parameter influences SQL but basic escaping might be partial.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[sqli]]
- [[manual-testing]]
