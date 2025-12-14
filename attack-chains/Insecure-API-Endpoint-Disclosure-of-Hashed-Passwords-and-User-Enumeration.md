---
tags:
  - api
  - information-disclosure
  - hashed-passwords
  - enumeration
  - credential-leak
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-api-user-request]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Exploit-Insecure-API-Endpoint-for-Credential-Disclosure]]'
step_count: 2
techniques:
  - '[[Account Discovery]]'
  - '[[Unsecured Credentials]]'
description: >-
  Attack chain exploiting an insecure API endpoint that leaks hashed passwords
  and enables user enumeration via sequential IDs without authorization checks.
skill_level: beginner
impact_level: high
id: 64716f65-ec6e-4df4-b91d-27ad6889d133
created_at: '2025-12-14T17:32:39.389Z'
updated_at: '2025-12-14T17:32:39.389Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Unsecured Credentials]]'
---
# Insecure API Endpoint Disclosure of Hashed Passwords and User Enumeration

Multi-stage attack chain demonstrating a complete attack workflow targeting an insecure web API that exposes sensitive user data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[API Endpoint Discovery] --> B[Unauthorized Data Request]
    B --> C[Credential Disclosure and Enumeration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-api-user-request]]

### Target Environment

- Web platform with exposed API endpoints
- No specific ports required (standard HTTPS/80,443)
- Publicly accessible API without authentication

### Initial Access Requirements

- Network access to the target web application
- No prior credentials needed due to lack of authorization

## Detailed Attack Procedures

### Step 1: API Endpoint Discovery

**Objective**: Identify the vulnerable API endpoint through testing or documentation review to confirm exposure of user data.

**Instructions**: Review the application's API documentation or use network scanning tools to identify endpoints handling user data. Focus on endpoints like /api/users that may lack authorization.

**Expected Output**: Confirmation of the endpoint URL, such as https://target.com/api/users/1.

**Success Indicators**:
- Endpoint responds without authentication prompt
- Response includes user-related fields

### Step 2: Unauthorized Data Request and Enumeration

procedure: [[procedures/Exploit-Insecure-API-Endpoint-for-Credential-Disclosure]]

**Objective**: Send unauthorized requests to the API to retrieve sensitive user information, including hashed passwords, and enumerate accounts using sequential IDs.

**Instructions**: Use [[commands/curl-api-user-request]] to query the endpoint with a specific user ID:

```bash
curl -X GET "https://target.com/api/users/1" -H "Accept: application/json"
```

Increment the ID (e.g., 2, 3) to enumerate multiple users. Parse responses for hashed passwords and other sensitive data.

**Expected Output**: JSON response containing user details like {"id":1, "username":"user1", "password_hash":"$2b$12$hashedvalue"}.

**Success Indicators**:
- Hashed passwords visible in response
- Successful enumeration of multiple users via sequential IDs
- No 401/403 errors indicating lack of auth checks

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to hashed user credentials
2. Enumeration of user accounts using predictable sequential IDs
3. Potential for offline cracking of weak hashes leading to account compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]
- [[Unsecured Credentials]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Credential Access]]

---
*Last updated: 2023-10-01*
