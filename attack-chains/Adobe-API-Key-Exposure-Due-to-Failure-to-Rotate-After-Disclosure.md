---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - api-key-exposure
  - credential-reuse
  - adobe
  - cleartext-storage
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Check-Exposed-API-Key-Validity]]'
step_count: 1
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:10.349Z'
description: >-
  Attack chain demonstrating the discovery and exploitation of an unrotated API
  key exposed in a prior vulnerability report, allowing unauthorized access to
  Adobe's API services.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Adobe API Key Exposure Due to Failure to Rotate After Disclosure

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Exposed Key] --> B[Validation and Unauthorized Access]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform
- Adobe API services
- Network access to Adobe endpoints

### Initial Access Requirements

- Knowledge of the exposed API key from prior report
- No prior credentials needed beyond the exposed key

## Detailed Attack Procedures

### Step 1: Validate Exposed API Key
procedure: [[procedures/Check-Exposed-API-Key-Validity]]

**Objective**: Confirm if the previously exposed API key remains valid and can be used for unauthorized access to Adobe services.

**Instructions**: Obtain the API key from the prior vulnerability report (e.g., #1465145). Use [[commands/curl-test-api-key]] to send a test request to an Adobe API endpoint that requires authentication with the key.

```bash
curl -H "Authorization: Bearer EXPOSED_API_KEY" https://api.adobe.com/v1/test-endpoint
```

Replace `EXPOSED_API_KEY` with the actual key value and adjust the endpoint URL based on the key's permissions (e.g., a simple status or user info endpoint).

**Expected Output**: A successful HTTP 200 response with API data, indicating the key is valid and grants access.

**Success Indicators**:
- HTTP 200 or authorized response received
- API data returned without authentication errors

## Attack Chain Summary

### Key Achievements

1. Confirmed persistence of exposed credential vulnerability
2. Demonstrated ongoing unauthorized access risk to Adobe API services
3. Highlighted failure in key rotation post-disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
