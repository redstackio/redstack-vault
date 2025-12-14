---
id: uuid-identify-endpoint
tags:
  - sqli
  - recon
  - web
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-api-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:09.920Z'
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
# Identify-and-Test-SQL-Injection-Endpoint

## Summary

This procedure involves examining a web API endpoint to identify parameters vulnerable to SQL injection, specifically the search parameter in the Atavist docs API.

## Description

In a web application using a MySQL backend, unsanitized user input in search queries can lead to SQL injection. This step focuses on the /reader_api/stories.php endpoint, testing GET parameters to establish baseline behavior before injection attempts. The target environment is a public-facing web app on Apache 2.2.34 with MySQL services.

## Requirements

1. Network access to the target URL (docs.atavist.com)
2. Tools like curl for sending HTTP requests
3. Basic understanding of HTTP GET parameters

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and parameterized queries in backend code
- Use web application firewalls (WAF) to detect anomalous query patterns
- Monitor response times for delays indicative of time-based attacks

## Objectives

1. Confirm the endpoint accepts and processes the search parameter
2. Establish normal response time and format
3. Identify potential injection points without triggering alerts

## Instructions

### Step 1: Send Baseline Request

**Context**: Craft a standard GET request to observe normal API behavior.

**Command** ([[commands/curl-api-test]]):
```bash
curl "https://docs.atavist.com/reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0&sort="
```

> This command sends a request with typical parameters, expecting a JSON response with story data. Normal execution time should be under 1 second.

### Step 2: Analyze Response

**Context**: Review the output to confirm the search parameter influences the query.

**Command** (No specific command; manual inspection):

> Look for JSON array of stories; ensure no errors occur with search=0.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-test]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- sqli
- recon
