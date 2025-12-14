---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - recon
  - api
  - idor
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-inspect-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:22.998Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Vulnerable-Uber-API-Endpoint

## Summary

This procedure involves inspecting Uber's Bonjour web API to identify the getConsentScreenDetails RPC endpoint and its 'userUuid' POST parameter, which lacks proper authorization checks, setting the stage for IDOR exploitation.

## Description

In the context of testing Uber's marketplace API, attackers examine network traffic or API documentation to locate endpoints handling user-specific data. The target endpoint https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails uses a JSON POST body with 'userUuid' to fetch consent details. Without server-side validation tying the UUID to the requester's session, this enables arbitrary user data access. Prerequisites include basic web access and familiarity with API requests; expected outcomes are endpoint confirmation and parameter details for manipulation.

## Requirements

1. Internet access to Uber's public API
2. Tools for inspecting HTTP requests (e.g., browser dev tools or curl)
3. Basic knowledge of JSON payloads and API testing

## Defense

Defensive measures and detection strategies:

- Implement proper access controls on API endpoints to validate user ownership of referenced objects
- Log and monitor API requests for anomalous UUID patterns or high-volume parameter changes
- Use rate limiting and anomaly detection on user-specific endpoints

## Objectives

1. Locate and document the vulnerable API endpoint and parameters
2. Verify the endpoint's response structure for user data
3. Prepare for parameter manipulation in subsequent steps

## Instructions

### Step 1: Inspect Network Requests

**Context**: Use developer tools or curl to capture legitimate requests to the endpoint and identify the 'userUuid' parameter.

**Command** ([[commands/curl-inspect-endpoint]]):
```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' \
  -H 'Content-Type: application/json' \
  -d '{"userUuid": "your-own-uuid"}' \
  -v
```

> This command sends a request with your own UUID and verbose output (-v) to inspect headers, payload, and response. Expected output includes a 200 OK response with consent details JSON, confirming the parameter's role.

### Step 2: Document Parameter Structure

**Context**: Analyze the request payload to note the exact format of 'userUuid' for later substitution.

No specific command; manually review the JSON body from the curl output or dev tools.

> Expected output: Confirmation that 'userUuid' is a string UUID in the POST data.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-inspect-endpoint]]

## Tools Used

- [[tools/curl]]

## Tags

- [[recon]]
- [[api]]
- [[idor]]
