---
tags:
  - ssrf
  - information-disclosure
  - credentials-exposure
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-SSRF-in-Lark-Messenger-Endpoint]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.440Z'
description: >-
  A Server-Side Request Forgery attack exploiting the Lark Suite messenger
  endpoint to force the server to access internal resources, resulting in the
  exposure of internal credentials.
skill_level: intermediate
impact_level: high
id: 3a674390-2a72-4462-b23e-eb2fa8a91b9a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF in Lark Suite Messenger Endpoint for Internal Credentials Disclosure

Multi-stage attack chain demonstrating exploitation of a Server-Side Request Forgery (SSRF) vulnerability in the Lark Suite messenger endpoint to disclose internal server credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoint] --> B[Exploit SSRF for Credential Disclosure]
    B --> C[Extract and Analyze Exposed Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- Web platform
- Lark Suite messenger service
- Requires authenticated access to the messenger endpoint

### Initial Access Requirements

- Valid user credentials for Lark Suite
- Network access to the public-facing messenger API
- No prior internal access needed

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoint

procedure: [[procedures/Identify-Lark-Messenger-SSRF-Endpoint]]

**Objective**: Locate and confirm the messenger endpoint susceptible to SSRF by testing for improper input validation on URL parameters.

**Instructions**: Review the Lark Suite API documentation or use API exploration tools to identify the messenger endpoint (typically something like `/api/messenger/send`). Test basic requests to confirm accessibility.

**Expected Output**: Successful response from the endpoint confirming it processes external URLs.

**Success Indicators**:
- Endpoint responds to standard requests
- No immediate input sanitization errors

### Step 2: Exploit SSRF for Credential Disclosure

procedure: [[procedures/Exploit-SSRF-in-Lark-Messenger-Endpoint]]

**Objective**: Craft a malicious request to the messenger endpoint that forces the server to fetch internal resources, such as metadata endpoints, leading to credential exposure.

**Instructions**: Use [[commands/curl-ssrf-payload]] to send a forged request targeting an internal service like a metadata endpoint (e.g., `http://169.254.169.254/latest/meta-data/`). Monitor the response for leaked internal data.

```bash
curl -X POST 'https://api.larksuite.com/api/messenger/send' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"url": "http://169.254.169.254/latest/meta-data/iam/security-credentials/"}'
```

**Expected Output**: Server response containing internal AWS IAM credentials or similar sensitive data.

**Success Indicators**:
- Response includes internal server data
- Credentials or metadata extracted successfully

## Attack Chain Summary

### Key Achievements

1. Confirmed SSRF vulnerability in Lark Suite messenger endpoint
2. Forced server-side request to internal metadata service
3. Disclosed internal credentials for potential further exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
