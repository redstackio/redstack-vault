---
tags:
  - unauthenticated-access
  - information-disclosure
  - api
  - pii
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-retrieve-api-data]]'
verified: false
platforms:
  - Web
  - API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.429Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: e3089134-49a2-49e2-a746-bc17bbf892a9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover-and-Access-Unauthenticated-API-Endpoint

## Summary

This procedure outlines the discovery and exploitation of an unauthenticated API endpoint to retrieve sensitive employee PII, such as work scheduling and leave dates, as identified in the Starbucks China system. It leverages endpoint exploration to bypass authentication and expose critical data.

## Description

In this attack scenario, an attacker explores public-facing API endpoints of a web application, such as a corporate scheduling system, to identify paths that handle sensitive data without requiring authentication. The target environment is a web API, typically over HTTPS, where the root cause is the absence of proper access controls on data retrieval endpoints. Expected outcomes include unauthorized access to PII, enabling further risks like identity theft or social engineering. Prerequisites include basic knowledge of HTTP requests and access to an HTTP client; no special privileges are needed due to the unauthenticated nature.

## Requirements

1. Network access to the target API domain (public internet)
2. HTTP client tool like curl or browser developer console
3. Basic understanding of API structures and common paths (e.g., /scheduling, /employee)

## Defense

Defensive measures and detection strategies:

- Implement authentication (e.g., API keys, JWT tokens) on all endpoints handling PII
- Use rate limiting and IP whitelisting to monitor anomalous access patterns
- Log all API requests and alert on unauthenticated data retrieval attempts
- Conduct regular API audits with tools like OWASP ZAP to identify exposed endpoints

## Objectives

1. Identify unprotected API endpoints through manual exploration
2. Retrieve and validate exposure of employee PII
3. Demonstrate the potential for data exfiltration without credentials

## Instructions

### Step 1: Explore API Endpoints

**Context**: Use browser developer tools or an HTTP client to probe common API paths related to scheduling or employee data, looking for responses that return sensitive information without login.

**Command** ([[commands/curl-retrieve-api-data]]):
```bash
curl -X GET "https://api.target-domain.com/scheduling/leave?employee_id=123" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> This command sends a GET request to a suspected endpoint, mimicking a browser to avoid basic detection. Expected output is a JSON payload with PII if vulnerable; otherwise, an error or empty response.

### Step 2: Validate and Extract Data

**Context**: If the initial request succeeds, iterate over parameters like employee IDs to gather more data, confirming the scope of exposure.

**Command** ([[commands/curl-retrieve-api-data]]):
```bash
curl -X GET "https://api.target-domain.com/scheduling/leave?employee_id=456" -H "Accept: application/json"
```

> This follow-up request tests additional parameters. Successful execution yields more PII entries, such as leave dates and employee details, highlighting the breadth of the disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-retrieve-api-data]]

## Tools Used


## Tags

- unauthenticated-access
- information-disclosure
- api
- pii
