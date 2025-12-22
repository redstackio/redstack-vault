---
tags:
  - idor
  - paypal
  - api
  - authorization-bypass
  - account-takeover
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands:
  - '[[commands/curl-api-request]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Identify-PayPal-Business-User-Management-API-Endpoint]]'
  - '[[procedures/Exploit-IDOR-to-Add-Secondary-User-from-Unrelated-Account]]'
  - '[[procedures/Access-Target-Account-via-Added-Secondary-User]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Create Account]]'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in PayPal's business user management API to add secondary users
  from unrelated accounts, granting unauthorized access to business functions.
skill_level: intermediate
impact_level: high
id: dd8427d2-15b8-4e60-9b1d-3ac41a0ae9d6
created_at: '2025-12-14T17:25:52.953Z'
updated_at: '2025-12-14T17:25:52.953Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Create Account]]'
---
# IDOR in PayPal Business User Management to Add Unauthorized Secondary Users

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR in PayPal's API to unauthorizedly add secondary users and gain access to business accounts.

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
    A[Identify API Endpoint] --> B[Exploit IDOR to Add User]
    B --> C[Gain Unauthorized Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or API testing tool like Postman
- Valid PayPal business account credentials for initial access

### Target Environment

- Web platform
- PayPal business management portal
- API endpoint: www.paypal.com/businessmanage/users/api/v1/users

### Initial Access Requirements

- Authenticated session as a PayPal business account owner
- Knowledge of target user IDs from other accounts
- Network access to PayPal's web services

## Detailed Attack Procedures

### Step 1: Identify API Endpoint
procedure: [[procedures/Identify-PayPal-Business-User-Management-API-Endpoint]]

**Objective**: Locate and understand the API endpoint responsible for managing secondary users in PayPal business accounts.

**Instructions**: Use browser developer tools to inspect network traffic while navigating the PayPal business management interface. Look for API calls related to user addition under the users management section.

**Expected Output**: Identification of the endpoint www.paypal.com/businessmanage/users/api/v1/users and its request format for adding users.

**Success Indicators**:
- API endpoint documented with parameters for user addition
- Request structure captured, including authentication headers

### Step 2: Exploit IDOR
procedure: [[procedures/Exploit-IDOR-to-Add-Secondary-User-from-Unrelated-Account]]

**Objective**: Manipulate user identifiers in the API request to add a secondary user from an unrelated account, bypassing authorization checks.

**Instructions**: Prepare an API request using [[commands/curl-api-request]] to POST to the identified endpoint, replacing the user ID with one from a target unrelated account. Include necessary authentication tokens from your session.

```bash
curl -X POST 'https://www.paypal.com/businessmanage/users/api/v1/users' \
  -H 'Authorization: Bearer YOUR_SESSION_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"user_id": "TARGET_UNRELATED_USER_ID", "privileges": ["view", "edit"]}'
```

**Expected Output**: HTTP 200 or 201 response confirming the secondary user addition without errors.

**Success Indicators**:
- Secondary user successfully added to the target business account
- No authorization denial in response

### Step 3: Gain Access
procedure: [[procedures/Access-Target-Account-via-Added-Secondary-User]]

**Objective**: Log in using the added secondary user's credentials to access the target business account's functions and privileges.

**Instructions**: Use the login credentials of the added secondary user to authenticate into the PayPal portal. Verify access to business management features assigned during addition, such as viewing or editing account details.

**Expected Output**: Successful login and access to the target account's dashboard with elevated privileges.

**Success Indicators**:
- Unauthorized access to target account functions confirmed
- Ability to perform actions like user management or transaction views

## Attack Chain Summary

### Key Achievements

1. Discovered vulnerable API endpoint for secondary user management
2. Exploited IDOR to add unauthorized secondary users
3. Achieved unauthorized access to business account privileges

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Create Account]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

---
*Last updated: 2023-10-01T00:00:00Z*
