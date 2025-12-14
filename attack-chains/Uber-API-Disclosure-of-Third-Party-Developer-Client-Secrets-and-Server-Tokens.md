---
tags:
  - information-disclosure
  - api-vulnerability
  - token-exposure
  - uber
type: attack_chain
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-api-query-with-auth]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Query-Uber-API-for-Exposed-Developer-Tokens]]'
step_count: 2
techniques:
  - '[[Unsecured Credentials]]'
description: >-
  An information disclosure vulnerability in Uber's internal API endpoint that
  exposes sensitive client secrets and server tokens for authorized third-party
  developer applications, enabling potential misuse of user account access.
skill_level: basic
impact_level: high
id: 009da5b2-d13e-4019-8200-8653e632b83c
created_at: '2025-12-14T17:32:48.435Z'
updated_at: '2025-12-14T17:32:48.435Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Uber API Disclosure of Third-Party Developer Client Secrets and Server Tokens

Multi-stage attack chain demonstrating a complete attack workflow for exploiting an information disclosure vulnerability in Uber's riders API.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Basic |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[User Authentication] --> B[API Query for Tokens]
    B --> C[Token Exfiltration and Misuse]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-api-query-with-auth]]

### Target Environment

- Web platform
- Access to Uber riders.uber.com API
- Valid user authentication (e.g., Uber account login)

### Initial Access Requirements

- Uber user credentials for authentication
- Network access to https://riders.uber.com/
- No prior elevated access needed; standard user session suffices

## Detailed Attack Procedures

### Step 1: User Authentication

**Objective**: Establish a valid authenticated session to access the internal API endpoint.

**Instructions**: Log in to the Uber riders portal using valid user credentials to obtain an authentication token (e.g., Bearer token). This token is required for subsequent API requests.

**Expected Output**: Authentication token in response headers or session cookies.

**Success Indicators**:
- Successful login redirect to riders.uber.com dashboard
- Presence of auth token in developer tools (e.g., via browser inspection)

### Step 2: Query API Endpoint for Exposed Tokens

procedure: [[procedures/Query-Uber-API-for-Exposed-Developer-Tokens]]

**Objective**: Send a request to the vulnerable internal API endpoint to retrieve sensitive client secrets and server tokens for third-party developer applications linked to the user's account.

**Instructions**: Use [[commands/curl-api-query-with-auth]] to query the endpoint with the authentication token. The endpoint lacks proper data filtering, returning unredacted secrets.

```bash
curl -H "Authorization: Bearer YOUR_AUTH_TOKEN" https://riders.uber.com/api/v1/developer-apps -X GET
```

**Expected Output**: JSON response containing client_secret and server_token fields for authorized apps.

**Success Indicators**:
- Response includes sensitive token data
- Tokens can be extracted for potential misuse (e.g., impersonating apps)

## Attack Chain Summary

### Key Achievements

1. Authenticated access to Uber's internal API
2. Disclosure of third-party app client secrets and server tokens
3. Potential for attackers to misuse tokens for unauthorized account access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]]

### MITRE ATT&CK Tactics

- [[Credential Access]]

*Last updated: 2023-10-01*
