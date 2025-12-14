---
tags:
  - information-disclosure
  - api-exposure
  - pii-leak
  - unauthenticated-access
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-get-sam-api-applications]]'
platforms:
  - Web
techniques:
  - '[[T1213.003]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: a0e38d9f-0191-407d-b9fb-513e3a5a2979
created_at: '2025-12-14T17:32:10.314Z'
updated_at: '2025-12-14T17:32:10.314Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# Retrieve-Sensitive-User-Data-via-Exposed-API-Endpoint

## Summary

This procedure exploits an unauthenticated API endpoint in SAM.gov to retrieve sensitive user data, including PII such as emails, names, IP addresses, physical locations, and Okta integration details, allowing attackers to gather intelligence for targeted attacks without any access controls.

## Description

The procedure targets the /api/prod/iam/cws/v1/applications/ endpoint on sam.gov, which returns a JSON list of application objects containing user and organization details. Discovered through direct URL navigation, this endpoint lacks authentication, exposing data to any internet user. In an attack scenario, a threat actor performs a simple GET request to collect this information, which can be used for reconnaissance, phishing target selection, or identifying integration points like Okta for further exploitation. Expected outcomes include obtaining raw PII for analysis, with no prerequisites beyond internet access.

## Requirements

1. Network access to https://sam.gov over HTTPS
2. An HTTP client such as curl or a web browser
3. No credentials or special permissions required

## Defense

Defensive measures and detection strategies:

- Implement authentication (e.g., API keys, OAuth) on all endpoints handling sensitive data
- Use web application firewalls (WAF) to block unauthorized access patterns to admin APIs
- Monitor API logs for anomalous GET requests to internal endpoints from public IPs
- Conduct regular API audits to identify exposed endpoints using tools like OWASP ZAP

## Objectives

1. Collect PII from unauthenticated users and system accounts
2. Identify organization details including IPs, locations, and integrations
3. Enable downstream attacks like targeted phishing or account enumeration

## Instructions

### Step 1: Send GET Request to Exposed Endpoint

**Context**: Initiate an unauthenticated request to fetch the JSON data containing user applications and associated PII.

**Command** ([[commands/curl-get-sam-api-applications]]):
```bash
curl -X GET "https://sam.gov/api/prod/iam/cws/v1/applications/"
```

> This command sends a GET request to the vulnerable endpoint and returns a JSON response with application objects. Each object includes fields like user emails, full names, organization IP addresses, physical locations, and flags indicating Okta integration. Successful execution yields raw data without errors, confirming the disclosure.

### Step 2: Parse and Analyze Response

**Context**: Review the JSON output to extract actionable intelligence such as target emails or integration details.

**Command** (Use jq for parsing if available):
```bash
curl -X GET "https://sam.gov/api/prod/iam/cws/v1/applications/" | jq '.[] | {email: .email, name: .name, ip: .ip, location: .location, okta: .okta_integration}'
```

> This filters the JSON for key PII fields. Expected output is a structured list of user details, highlighting potential targets. If jq is not installed, manually inspect the raw JSON in a tool like jqplay.org or a text editor.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]
- [[Collection]]

### Techniques

- [[T1213.003]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-sam-api-applications]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[api-exposure]]
- [[pii-leak]]
- [[unauthenticated-access]]
