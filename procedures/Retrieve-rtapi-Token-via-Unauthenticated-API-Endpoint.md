---
id: 27795532-0760-48ea-92f1-4050e4640134
name: Retrieve-rtapi-Token-via-Unauthenticated-API-Endpoint
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.418Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques: []
tags:
  - information-disclosure
  - api-vulnerability
  - token-leak
commands:
  - '[[commands/curl-retrieve-rtapi-token]]'
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---

# Retrieve-rtapi-Token-via-Unauthenticated-API-Endpoint

## Summary

This procedure exploits a lack of authentication in Uber's staging API endpoint to retrieve a sensitive rtapi token associated with any user, enabling further unauthorized access.

## Description

The vulnerability exists in the endpoint https://video-support-staging.uber.com/video/api/getPopulousUser, which returns user-specific rtapi tokens without verifying the requester's identity. This information disclosure allows attackers to obtain valid tokens for staging environment access, potentially leading to data exfiltration or service abuse in Uber's rtapi system. The procedure targets web-based API interactions and requires no prior credentials.

## Requirements

1. Internet access to reach the staging API
2. HTTP client (e.g., curl or browser developer tools)
3. Basic understanding of JSON responses

## Defense

Defensive measures and detection strategies:

- Implement proper authentication (e.g., API keys or JWT) on all endpoints
- Rate-limit unauthenticated requests to prevent abuse
- Monitor API logs for anomalous access patterns from unknown IPs
- Use web application firewalls (WAF) to block unauthorized endpoint calls

## Objectives

1. Obtain a valid rtapi token without authentication
2. Validate token usability for subsequent API access
3. Demonstrate critical impact of the disclosure

## Instructions

### Step 1: Call the Vulnerable Endpoint

**Context**: Directly query the unauthenticated API to retrieve the token in the response.

**Command** ([[commands/curl-retrieve-rtapi-token]]):
```bash
curl https://video-support-staging.uber.com/video/api/getPopulousUser
```

> This command sends a GET request to the endpoint. Expected output is a JSON object containing the rtapi token field. Extract the token value for use in further steps. If the endpoint returns an error, verify network connectivity or endpoint availability.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-retrieve-rtapi-token]]

## Tools Used

- None

## Tags

- [[information-disclosure]]
- [[api-vulnerability]]
- [[token-leak]]
