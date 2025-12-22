---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - idor
  - information-disclosure
  - account-takeover
  - api
  - uber
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Vulnerable-Uber-API-Endpoint]]'
  - '[[procedures/Manipulate-userUuid-for-IDOR]]'
  - '[[procedures/Retrieve-Sensitive-User-Data-and-Token]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.004Z'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in Uber's web API to access any user's sensitive data, including
  mobile authentication tokens, enabling full account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# IDOR in Uber API Leading to Sensitive User Data Disclosure and Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in Uber's Bonjour API to disclose sensitive user information and authentication tokens, ultimately enabling account impersonation and takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoint] --> B[Manipulate Parameter]
    B --> C[Retrieve Data and Token]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- Browser developer tools or API testing tool like Burp Suite (optional for inspection)

### Target Environment

- Web platform with access to Uber's Bonjour API (https://bonjour.uber.com)
- Required services: Web API (RPC endpoint)
- Network access: Internet connectivity to reach the public API

### Initial Access Requirements

- No prior credentials needed; the endpoint is publicly accessible but requires a valid session or basic authentication for testing
- Attacker must have a victim's UUID (obtainable via social engineering or prior recon)
- Network position: External attacker with internet access

## Detailed Attack Procedures

### Step 1: Identify the Vulnerable API Endpoint
procedure: [[procedures/Identify-Vulnerable-Uber-API-Endpoint]]

**Objective**: Examine the Uber Bonjour API endpoint to identify the 'userUuid' parameter susceptible to IDOR manipulation.

**Instructions**: Use browser developer tools or an API client to inspect network requests to https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails. Look for POST requests containing the 'userUuid' parameter in the payload.

**Expected Output**: Confirmation of the endpoint and parameter structure in the request.

**Success Indicators**:
- Endpoint URL and parameters identified
- Request format documented for manipulation

### Step 2: Manipulate the userUuid Parameter
procedure: [[procedures/Manipulate-userUuid-for-IDOR]]

**Objective**: Substitute the attacker's own UUID with the victim's UUID in the POST request to bypass authorization checks.

**Instructions**: Craft a POST request using [[commands/curl-post-uber-idor]] to the endpoint, replacing 'userUuid' with the victim's UUID.

```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' \
  -H 'Content-Type: application/json' \
  -d '{"userUuid": "victim-uuid-here"}'
```

**Expected Output**: Server response without authorization errors, indicating successful parameter manipulation.

**Success Indicators**:
- No 403/401 errors returned
- Response contains user data structure

### Step 3: Retrieve Sensitive Data and Mobile Auth Token
procedure: [[procedures/Retrieve-Sensitive-User-Data-and-Token]]

**Objective**: Parse the API response to extract personal information and the mobile authentication token for further exploitation.

**Instructions**: Send the manipulated request and analyze the JSON response for fields like personal details and auth tokens. Use the token in subsequent mobile API requests for impersonation.

**Expected Output**: JSON object with sensitive data, including mobile token.

**Success Indicators**:
- Personal user information disclosed
- Valid mobile auth token obtained
- Ability to make authenticated requests as the victim confirmed

## Attack Chain Summary

### Key Achievements

1. Identification of IDOR-vulnerable endpoint in Uber's API
2. Successful manipulation leading to unauthorized data access
3. Extraction of auth tokens enabling full account takeover via mobile APIs

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

---
*Last updated: 2024-01-01T00:00:00Z*
