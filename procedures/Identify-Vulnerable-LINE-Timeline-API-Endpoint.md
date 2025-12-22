---
id: proc-uuid-1
tags:
  - api-recon
  - endpoint-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-api-probe]]'
verified: false
platforms:
  - Web
  - Mobile API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:20.935Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Vulnerable-LINE-Timeline-API-Endpoint

## Summary

This procedure involves reconnaissance to identify the LINE Timeline API endpoint that handles hidden friends lists, which suffers from insufficient access control checks, allowing unauthenticated probing.

## Description

In the LINE messaging app's ecosystem, the Timeline API manages social features including hidden contacts. Attackers can discover the vulnerable endpoint by inspecting network traffic during app usage or reviewing unofficial API documentation. The endpoint lacks verification for the requesting user's permissions, enabling global access. This step sets up exploitation by confirming the endpoint's behavior and response format, typically returning JSON without auth tokens.

## Requirements

1. Access to LINE app or web client for traffic inspection
2. HTTP client like curl for probing
3. Basic knowledge of LINE's internal user IDs

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on API endpoints
- Enforce strict authentication and authorization checks (e.g., JWT validation)
- Monitor for anomalous API calls from non-authenticated sources

## Objectives

1. Locate the exact API path for hidden friends retrieval
2. Verify lack of access controls
3. Prepare for targeted exploitation

## Instructions

### Step 1: Probe LINE API Endpoints

**Context**: Use an HTTP client to test potential Timeline API paths for hidden friends functionality.

**Command** ([[commands/curl-api-probe]]):
```bash
curl -X GET "https://api.line.me/v2/timeline/hidden_friends" -H "Accept: application/json" -v
```

> This command sends a verbose GET request to the suspected endpoint. Expected output includes HTTP 200 response with JSON structure, even without auth headers, confirming vulnerability.

### Step 2: Inspect Response Structure

**Context**: Analyze the response to understand data format for subsequent exploitation.

**Command** ([[commands/curl-api-probe]]):
```bash
curl -X GET "https://api.line.me/v2/timeline/hidden_friends?user_id=SELF_ID" -H "Accept: application/json"
```

> Replace SELF_ID with your own ID for testing. Success shows array of friends objects, indicating no access restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-probe]]

## Tools Used


## Tags

- [[api-recon]]
- [[endpoint-discovery]]
