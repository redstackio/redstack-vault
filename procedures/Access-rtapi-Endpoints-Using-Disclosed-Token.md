---
id: ba574f2e-c690-4324-b008-355f2d341f93
name: Access-rtapi-Endpoints-Using-Disclosed-Token
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.406Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - unauthorized-access
  - api-abuse
  - token-impersonation
commands:
  - '[[commands/curl-access-rtapi-with-token]]'
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Access-rtapi-Endpoints-Using-Disclosed-Token

## Summary

This procedure uses a disclosed rtapi token to bypass authorization and access protected endpoints in Uber's rtapi system, simulating unauthorized user impersonation.

## Description

After obtaining an rtapi token from the vulnerable endpoint, substitute it into the x-uber-token header for requests to rtapi endpoints. This allows access to user data or services without legitimate credentials, highlighting the critical impact of the initial disclosure. The procedure assumes the token is valid in the staging environment and targets web API interactions.

## Requirements

1. Valid rtapi token from prior disclosure step
2. Knowledge of target rtapi endpoint URLs (e.g., via documentation or reconnaissance)
3. HTTP client for header manipulation

## Defense

Defensive measures and detection strategies:

- Enforce token validation and expiration on all rtapi endpoints
- Implement IP whitelisting or origin checks for token usage
- Log and alert on token usage from unexpected sources
- Rotate tokens frequently and monitor for anomalous patterns

## Objectives

1. Gain access to protected rtapi resources using the leaked token
2. Retrieve sensitive data or perform actions as an impersonated user
3. Validate the full attack chain impact

## Instructions

### Step 1: Substitute Token in API Request

**Context**: Inject the token into the authorization header to access restricted endpoints.

**Command** ([[commands/curl-access-rtapi-with-token]]):
```bash
curl -H "x-uber-token: YOUR_RETRIEVED_TOKEN" https://rtapi.uber.com/some-protected-endpoint
```

> Replace YOUR_RETRIEVED_TOKEN with the actual token and specify a valid rtapi endpoint. Expected output is a successful response (e.g., JSON data). If access is denied, verify token validity or endpoint path.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-access-rtapi-with-token]]

## Tools Used

- None

## Tags

- [[unauthorized-access]]
- [[api-abuse]]
- [[token-impersonation]]
