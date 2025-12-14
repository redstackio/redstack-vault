---
tags:
  - reconnaissance
  - api-discovery
type: procedure
tools:
  - '[[tools/Swagger]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-swagger-docs]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:01.600Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 64dde5e3-9936-43d7-af09-026119d38b24
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-Exposed-API-Documentation-via-Manual-Reconnaissance

## Summary

This procedure involves manual reconnaissance to locate and review publicly exposed Swagger API documentation revealing unauthenticated endpoints for document and email management in a sensitive system like the Seaport Bid proposal.

## Description

In the attack scenario a tester manually explores the target domain for common API documentation paths such as /swagger or /api-docs. Upon discovery the Swagger UI provides interactive details on endpoints allowing attackers to understand and exploit routes without authentication. This targets web-based RESTful APIs in test/integration environments exposing DoD-related sensitive data. Prerequisites include public access to the target URL; expected outcomes are full API mapping enabling further unauthorized access.

## Requirements

1. Public internet access to the target domain
2. Web browser or curl for probing paths
3. Basic knowledge of REST APIs and Swagger format

## Defense

Defensive measures and detection strategies:

- Implement authentication on all API documentation endpoints (e.g. IP whitelisting or API keys)
- Monitor access logs for anomalous requests to /swagger or /api-docs paths
- Use web application firewalls (WAF) to block unauthenticated doc access

## Objectives

1. Identify exposed API structure and endpoints
2. Map sensitive operations like document retrieval and email access
3. Enable subsequent exploitation without credentials

## Instructions

### Step 1: Probe for Swagger Documentation

**Context**: Manually check common paths for exposed API docs to reveal endpoint details.

**Command** ([[commands/curl-get-swagger-docs]]):
```bash
curl -X GET "https://target/swagger" -H "Accept: text/html"
```

> This command fetches the Swagger UI HTML if exposed. Expected output is HTML content with interactive API specs or a 200 OK response. If successful review the docs for endpoints like /api/1_0/Documents.

### Step 2: Review and Interact with Documentation

**Context**: Use the browser to interact with Swagger UI for testing endpoints without auth.

No command needed; navigate to https://target/swagger in a browser and explore routes.

> Expected output: List of API methods (GET/POST) parameters and schemas for documents emails and PDFs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-swagger-docs]]

## Tools Used

- [[tools/Swagger]]

## Tags

- [[Reconnaissance]]
- [[api-discovery]]
