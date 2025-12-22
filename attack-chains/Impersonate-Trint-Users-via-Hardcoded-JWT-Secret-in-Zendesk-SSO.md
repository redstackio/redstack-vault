---
tags:
  - jwt
  - sso
  - zendesk
  - hardcoded-secret
  - impersonation
type: attack_chain
tools:
  - '[[tools/jwt-io]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Access-Application-and-Trigger-SSO-Flow]]'
  - '[[procedures/Intercept-Traffic-to-Capture-JWT]]'
  - '[[procedures/Logout-from-Zendesk]]'
  - '[[procedures/Decode-Captured-JWT]]'
  - '[[procedures/Tamper-and-Sign-JWT-Payload]]'
  - '[[procedures/Access-Zendesk-with-Tampered-JWT]]'
step_count: 6
techniques:
  - '[[Valid Accounts]]'
  - '[[Credentials In Files]]'
description: >-
  Exploitation of hardcoded JWT secret in client-side JavaScript to generate
  arbitrary tokens and impersonate users in Zendesk support system
skill_level: intermediate
impact_level: high
id: db27b79d-400b-45bd-a389-a82ee4c12e7a
created_at: '2025-12-13T09:01:26.703Z'
updated_at: '2025-12-13T09:01:26.703Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Credentials In Files]]'
---
# Impersonate Trint Users via Hardcoded JWT Secret in Zendesk SSO

Multi-stage attack chain demonstrating how to exploit a hardcoded JWT secret in client-side JavaScript to generate arbitrary tokens and impersonate any Trint customer in Zendesk, gaining access to their support tickets and history.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Application] --> B[Capture JWT]
    B --> C[Logout Zendesk]
    C --> D[Decode JWT]
    D --> E[Tamper Payload]
    E --> F[Access with Tampered JWT]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#e74c3c
    style F fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[tools/jwt-io]]

### Target Environment

- Web platform
- Services: Zendesk
- Tech stack: JavaScript, React

### Initial Access Requirements

- Access to Trint application as a logged-in user
- Network access to app.trint.com and trintsupport.zendesk.com
- No prior Zendesk credentials needed beyond the exploit

## Detailed Attack Procedures

### Step 1: Access Application and Trigger SSO Flow
procedure: [[procedures/Access-Application-and-Trigger-SSO-Flow]]

**Objective**: Initiate the SSO process to observe the JWT generation in the browser.

**Instructions**: Navigate to the Trint application and click on the 'Support' section to trigger the SSO flow.

Press 'Support' on https://app.trint.com.

**Expected Output**: SSO flow initiates, loading the Zendesk integration.

**Success Indicators**:
- SSO request observed in browser traffic
- Application redirects to Zendesk endpoint

### Step 2: Intercept Traffic to Capture JWT
procedure: [[procedures/Intercept-Traffic-to-Capture-JWT]]

**Objective**: Capture the JWT token sent during the SSO process.

**Instructions**: Use browser developer tools or a proxy to intercept the request to the Zendesk JWT endpoint.

Capture the request to https://trintsupport.zendesk.com/access/jwt?jwt=[JWT_TOKEN].

**Expected Output**: Raw JWT token string captured.

**Success Indicators**:
- JWT token successfully intercepted
- Token payload visible upon initial inspection

### Step 3: Logout from Zendesk
procedure: [[procedures/Logout-from-Zendesk]]

**Objective**: Ensure no active session interferes with the impersonation attempt.

**Instructions**: Log out of any existing Zendesk session to start fresh.

Ensure no active session in Zendesk.

**Expected Output**: Session cleared, no active login in Zendesk.

**Success Indicators**:
- User is logged out
- No cookies or sessions persist

### Step 4: Decode Captured JWT
procedure: [[procedures/Decode-Captured-JWT]]

**Objective**: Analyze the structure and contents of the captured JWT.

**Instructions**: Use [[tools/jwt-io]] to decode the JWT token.

Paste the JWT into jwt.io to decode and view payload.

**Expected Output**: Decoded JWT payload showing claims like email, iat, jti.

**Success Indicators**:
- Payload decoded successfully
- Secret or signing method identified (HMAC)

### Step 5: Tamper and Sign JWT Payload
procedure: [[procedures/Tamper-and-Sign-JWT-Payload]]

**Objective**: Modify the JWT to impersonate a target user and sign it with the extracted secret.

**Instructions**: Use [[tools/jwt-io]] to tamper with the payload.

Modify iat to current Unix timestamp, jti to random UUID v4, email to victim's email, and sign using the extracted HMAC secret oq1HJ4jXo99Wt41bwvLh9BXBVdgpi52CjkXbThow7UhWQGtJ.

**Expected Output**: New tampered and signed JWT token generated.

**Success Indicators**:
- Token signs successfully with the secret
- Modified claims reflect target user's details

### Step 6: Access Zendesk with Tampered JWT
procedure: [[procedures/Access-Zendesk-with-Tampered-JWT]]

**Objective**: Use the forged JWT to log in as the impersonated user.

**Instructions**: Navigate to the Zendesk endpoint with the tampered JWT.

Navigate to https://trintsupport.zendesk.com/access/jwt?jwt=[TAMPERED_JWT_TOKEN] to log in as the victim.

**Expected Output**: Successful login to Zendesk as the target user, with access to their tickets.

**Success Indicators**:
- Authentication succeeds
- Victim's support tickets and history accessible

## Attack Chain Summary

### Key Achievements

1. Extraction of hardcoded JWT secret from client-side code
2. Generation of arbitrary JWTs for user impersonation
3. Unauthorized access to Zendesk support data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Credentials In Files]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

*Last updated: 2023-10-01*
