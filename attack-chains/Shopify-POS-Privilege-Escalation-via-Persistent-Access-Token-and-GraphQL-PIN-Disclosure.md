---
id: ac-shopify-pos-escalation-001
tags:
  - shopify
  - pos
  - graphql
  - privilege-escalation
  - information-disclosure
  - broken-access-control
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Low-Privilege-User-with-POS-Access]]'
  - '[[procedures/Obtain-Persistent-POS-Access-Token]]'
  - '[[procedures/Disclose-Staff-PINs-via-GraphQL]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:17.925Z'
description: >-
  A multi-stage attack exploiting insufficient access controls in Shopify POS to
  allow a low-privilege user to obtain a persistent access token and query
  sensitive staff PINs via GraphQL, enabling privilege escalation on physical
  POS devices.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# Shopify POS Privilege Escalation via Persistent Access Token and GraphQL PIN Disclosure

Multi-stage attack chain demonstrating a complete attack workflow in Shopify Plus, where a low-privilege user exploits persistent POS access to obtain an authentication token and disclose sensitive staff PINs via GraphQL, leading to privilege escalation on physical POS devices.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Low-Privilege User] --> B[Obtain POS Token]
    B --> C[Query GraphQL for PINs]
    C --> D[Privilege Escalation on POS Device]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or API client (e.g., curl, Postman)

### Target Environment

- Shopify Plus admin panel
- Shopify POS app installed
- Access to physical POS device for escalation validation

### Initial Access Requirements

- Valid Shopify Plus org owner credentials for setup
- Low-privilege user credentials (email and password)
- Network access to Shopify admin APIs (e.g., https://*.myshopify.com/admin)

## Detailed Attack Procedures

### Step 1: Setup Low-Privilege User

procedure: [[procedures/Setup-Low-Privilege-User-with-POS-Access]]

**Objective**: Create a minimal-privilege staff user and enable POS access while revoking all admin permissions to simulate a low-privilege scenario.

**Instructions**: Log in as Shopify Plus org owner, create the user, enable POS Associate role, and revoke permissions. Note the warning that POS access persists.

**Expected Output**: User created with ID (e.g., 61357948984), POS enabled, all admin perms revoked.

**Success Indicators**:
- User profile shows no admin permissions but POS access active
- Warning message confirms POS persistence

### Step 2: Obtain Persistent POS Access Token

procedure: [[procedures/Obtain-Persistent-POS-Access-Token]]

**Objective**: Authenticate as the low-privilege user to request a POS access token, demonstrating that access persists despite revoked permissions.

**Instructions**: Use the low-privilege credentials to POST to the xauth endpoint with the POS app's API key. Include the header X-Shopify-Access-Token if needed for follow-up.

**Expected Output**: JSON response with access_token (e.g., "shpat_...") and scopes like write_pos_channel.access.

**Success Indicators**:
- Token issued successfully
- Scopes include POS-related permissions

### Step 3: Disclose Staff PINs via GraphQL

procedure: [[procedures/Disclose-Staff-PINs-via-GraphQL]]

**Objective**: Use the obtained token to query the GraphQL API for all staff members' sensitive data, including PINs, enabling escalation.

**Instructions**: POST the GraphQL query to the unversioned endpoint with the access_token in the header. Use variables to fetch up to 100 staff updated since epoch.

**Expected Output**: JSON with staff list including PINs (e.g., "3333" for a manager).

**Success Indicators**:
- Response includes unauthorized sensitive fields like pin, email, permissions
- PINs for higher-privilege staff visible

## Attack Chain Summary

### Key Achievements

1. Persistent POS access for low-privilege users post-revocation
2. Disclosure of sensitive staff PINs via GraphQL without proper authorization
3. Potential for physical POS privilege escalation using disclosed PINs

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
