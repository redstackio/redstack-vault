---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - api-key
  - credential-validation
  - unauthorized-access
  - adobe
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-api-key]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:10.335Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Check-Exposed-API-Key-Validity

## Summary

This procedure verifies the validity of an exposed API key, such as one disclosed in a prior vulnerability report, by attempting an authenticated request to the target API service. It is primarily used to assess the ongoing risk of unrotated credentials in scenarios like the Adobe API key exposure in report #1465145, where failure to rotate leaves the key accessible for unauthorized use.

## Description

In this attack scenario, an attacker obtains an API key from a previous disclosure (e.g., cleartext in a public report or repository). Without rotation by the service provider, the key remains functional, enabling unauthorized access to API endpoints for data retrieval, modifications, or other actions based on the key's scope. The target environment is web-based API services like Adobe's, requiring only HTTP access. Prerequisites include the exposed key value and knowledge of a testable endpoint. Expected outcomes include confirmation of access, potentially leading to data exfiltration or service abuse.

## Requirements

1. Exposed API key value from prior disclosure
2. Network access to the target API endpoints (e.g., Adobe API)
3. HTTP client tool like curl for testing

## Defense

Defensive measures and detection strategies:

- Immediately rotate exposed API keys upon disclosure and monitor for anomalous usage
- Implement API key expiration and usage logging to detect unauthorized access
- Use rate limiting and IP whitelisting on API endpoints to mitigate abuse

## Objectives

1. Confirm if the API key grants active access to services
2. Identify the scope of permissions (e.g., read/write access to data)
3. Demonstrate risk of persistent exposure for reporting or exploitation

## Instructions

### Step 1: Obtain and Prepare the API Key

**Context**: Retrieve the exposed key from the source report and prepare it for use in authentication headers.

No command needed; manually copy the key (e.g., from HackerOne report #1465145).

### Step 2: Test Key Validity with API Request

**Context**: Send an authenticated request to a known API endpoint to check if the key is accepted, accomplishing validation of unauthorized access potential.

**Command** ([[commands/curl-test-api-key]]):
```bash
curl -H "Authorization: Bearer EXPOSED_API_KEY" https://api.adobe.com/v1/test-endpoint
```

> This command sends a GET request with the API key in the Authorization header. Replace `EXPOSED_API_KEY` with the actual key and `https://api.adobe.com/v1/test-endpoint` with a real endpoint (e.g., a user info or status API). Expected output is a JSON response with data if valid, or 401 Unauthorized if invalid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-api-key]]

## Tools Used


## Tags

- [[api-key]]
- [[credential-validation]]
- [[unauthorized-access]]
