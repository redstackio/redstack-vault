---
id: ac-idor-exness-1159367
tags:
  - idor
  - access-control
  - privilege-escalation
  - web
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-for-Horizontal-Privilege-Escalation]]'
step_count: 2
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:36.367Z'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability on the EXNESS platform to achieve horizontal privilege
  escalation, enabling read-only access to other users' sensitive information by
  manipulating object references in API requests.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR Horizontal Privilege Escalation for Unauthorized User Data Access on EXNESS

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability on the EXNESS trading platform.

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
    A[Initial Access] --> B[Exploit IDOR]
    B --> C[Data Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for request manipulation

### Target Environment

- Web platform (EXNESS trading application)
- Required services/ports: HTTPS on standard web ports (443)
- Network access requirements: Valid user session/cookie for authenticated access

### Initial Access Requirements

- Valid authenticated session as a low-privilege user
- Knowledge of API endpoints handling user-specific data
- No prior elevated access needed, but horizontal escalation targets peer users

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoint
procedure: [[procedures/Exploit-IDOR-for-Horizontal-Privilege-Escalation]]

**Objective**: Locate an API endpoint that uses direct object references (e.g., user IDs) without proper access controls, allowing manipulation for unauthorized access.

**Instructions**: Log in to the EXNESS platform as an authenticated user. Use browser developer tools or a proxy to inspect network requests. Identify endpoints like `/api/user/{user_id}/profile` or similar that expose user data via URL parameters or request bodies containing predictable identifiers (e.g., numeric user IDs).

For example, capture your own profile request using [[commands/curl-get-user-data]]:

```bash
curl -H "Cookie: session=your_session_cookie" "https://exness.com/api/user/123/profile"
```

Analyze the response to confirm it returns your data, noting the user ID (e.g., 123).

**Expected Output**: JSON response with your user profile data, confirming the endpoint structure.

**Success Indicators**:
- Endpoint identified with direct reference to user ID
- Successful retrieval of own data without errors

### Step 2: Exploit IDOR for Unauthorized Access
procedure: [[procedures/Exploit-IDOR-for-Horizontal-Privilege-Escalation]]

**Objective**: Manipulate the object reference to access another user's data, achieving horizontal privilege escalation for read-only information disclosure.

**Instructions**: Replace the user ID in the request with another known or guessed ID (e.g., increment to 124). Replay the modified request using [[commands/curl-get-user-data]]:

```bash
curl -H "Cookie: session=your_session_cookie" "https://exness.com/api/user/124/profile"
```

If successful, the response will contain the target user's sensitive information (e.g., account details, trading history) without authentication checks.

**Expected Output**: JSON response with unauthorized user's data, such as profile details or transaction history.

**Success Indicators**:
- Access to data not belonging to the authenticated user
- No 403/401 errors; data loads as if authorized
- Confirmation of read-only nature (no modification possible)

## Attack Chain Summary

### Key Achievements

1. Identification of IDOR-vulnerable endpoint on EXNESS platform
2. Horizontal escalation to read sensitive user data
3. Disclosure of unauthorized information without modification capabilities

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
