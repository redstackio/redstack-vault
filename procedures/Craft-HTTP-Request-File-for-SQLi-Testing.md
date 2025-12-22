---
tags:
  - sql-injection
  - http
  - testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:52.753Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9d1ecba9-051e-4504-8e7d-13a6c8c8645f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-HTTP-Request-File-for-SQLi-Testing

## Summary

This procedure captures and saves an HTTP POST request to the vulnerable search endpoint in a file format compatible with sqlmap, including headers and form data for reproducible injection testing.

## Description

For the U.S. Department of State search vulnerability, this involves intercepting a POST request to /search with the 'query' parameter in form-urlencoded format. The file includes essential headers like User-Agent, Content-Type (application/x-www-form-urlencoded), Referer, and Cookie to mimic legitimate traffic. This setup allows sqlmap to automate injection without manual replay, targeting the MySQL backend for time-based blind SQLi.

## Requirements

1. Proxy tool like Burp Suite or browser developer tools to intercept requests
2. Access to the search form and ability to submit a test query
3. Text editor to format the request file

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and validate all headers to prevent request tampering
- Rate-limit search requests to detect automated crafting attempts
- Log all POST requests to /search for anomaly review

## Objectives

1. Create a portable HTTP request file for sqlmap
2. Ensure the file accurately represents the vulnerable interaction
3. Prepare for automated exploitation without alerting defenses

## Instructions

### Step 1: Intercept the Request

**Context**: Use a proxy to capture the POST request during a normal search submission.

No command; configure Burp Suite proxy, submit a search query (e.g., "test"), and copy the raw request.

> Expected output: Raw HTTP POST with body like "query=test&submit=Search".

### Step 2: Format and Save the File

**Context**: Edit the intercepted request into a sqlmap-compatible .txt file, adding necessary headers.

No command; create request.txt with content:

```http
POST /search HTTP/1.1
Host: www.state.gov
User-Agent: Mozilla/5.0 (compatible; sqlmap/1.7)
Content-Type: application/x-www-form-urlencoded
Referer: https://www.state.gov/
Cookie: session=abc123
Content-Length: 20

query=test&submit=Search
```

> Expected output: Valid file that sqlmap can load with -r flag.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- http
- crafting
