---
tags:
  - sso
  - saml
  - entityid
  - dos
  - account-takeover
  - auth-bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
verified: false
platforms:
  - Web
  - SAML SSO
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Legitimate-SSO-for-Victim-Organization]]'
  - >-
    [[procedures/Create-Malicious-Business-Account-with-Trailing-Space-EntityId]]
  - '[[procedures/Wait-for-Propagation-and-Test-Victim-Login]]'
  - '[[procedures/Verify-DOS-and-Test-User-Provisioning-via-Re-Authentication]]'
  - '[[procedures/Perform-Account-Takeover-Using-Provisioned-User]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.321Z'
description: >-
  Multi-stage attack exploiting inconsistent trimming of SAML entityId in
  Grammarly Business SSO, enabling DOS on victim logins, unauthorized user
  provisioning to attacker's organization, and subsequent account takeover.
skill_level: intermediate
impact_level: high
id: 4e43f105-5bec-40e3-9368-b631ebaa4f43
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# SSO EntityId Collision for Denial-of-Service and Account Takeover in Grammarly Business

Multi-stage attack chain demonstrating exploitation of a SAML SSO configuration flaw in Grammarly Business accounts, where inconsistent trimming of the entityId (Identity Provider Issuer) allows an attacker to create a colliding organization identifier with a trailing space, leading to prioritization of the attacker's setup during authentication and provisioning.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Legitimate SSO] --> B[Create Malicious Account with Colliding EntityId]
    B --> C[Wait for Propagation and Test Login]
    C --> D[Verify DOS and Provision User to Attacker Org]
    D --> E[Change EntityId and Take Over Account]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual configuration via web interface)

### Target Environment

- Grammarly Business web application
- SAML-based SSO services
- No specific ports required (HTTPS web access)

### Initial Access Requirements

- Ability to register new Grammarly Business accounts
- Access to a legitimate SSO provider for configuration
- Victim's entityId (obtainable via reconnaissance or prior knowledge)

## Detailed Attack Procedures

### Step 1: Setup Legitimate SSO for Victim Organization
procedure: [[procedures/Setup-Legitimate-SSO-for-Victim-Organization]]

**Objective**: Establish a baseline SAML SSO configuration for the victim's Grammarly Business account to verify normal functionality and capture the exact entityId.

**Instructions**: Configure SAML SSO in the victim's Grammarly Business settings using your IdP, noting the entityId (e.g., 'myentity'). Test authentication to ensure users can log in successfully.

**Expected Output**: Successful SSO login redirecting to the victim's organization dashboard.

**Success Indicators**:
- User authenticates and accesses victim organization resources
- EntityId confirmed without trailing spaces

### Step 2: Create Malicious Business Account with Trailing Space EntityId
procedure: [[procedures/Create-Malicious-Business-Account-with-Trailing-Space-EntityId]]

**Objective**: Register a new attacker-controlled Grammarly Business account and configure its SSO with an entityId matching the victim's but appended with a trailing space to create a collision.

**Instructions**: Sign up for a new Grammarly Business account, then in SSO settings, set the entityId to the victim's value plus a trailing space (e.g., 'myentity '). Use a distinct keypair for signing SAML assertions.

**Expected Output**: Attacker's organization created with the modified entityId; no immediate errors.

**Success Indicators**:
- New account registration succeeds
- SSO configuration saves without validation errors

### Step 3: Wait for Propagation and Test Victim Login
procedure: [[procedures/Wait-for-Propagation-and-Test-Victim-Login]]

**Objective**: Allow system propagation of the colliding entityId and attempt login to the victim's account to trigger the prioritization flaw.

**Instructions**: Wait approximately 2 minutes for backend propagation, then attempt SSO login to the victim's Grammarly Business account using legitimate credentials.

**Expected Output**: Authentication fails with an error message, as the system prioritizes the attacker's untrimmed entityId over the victim's trimmed one from the SAML response.

**Success Indicators**:
- Login error occurs (e.g., organization not found or invalid SSO)
- No access to victim's organization

### Step 4: Verify DOS and Test User Provisioning via Re-Authentication
procedure: [[procedures/Verify-DOS-and-Test-User-Provisioning-via-Re-Authentication]]

**Objective**: Confirm denial-of-service on the victim's SSO and demonstrate unauthorized provisioning by deleting and re-adding the user.

**Instructions**: Verify persistent login errors for the victim organization. As an admin, delete the affected user from the victim org, then re-attempt SSO login. The authentication succeeds against the trimmed issuer but provisions the user into the attacker's organization due to entityId matching.

**Expected Output**: User is redirected to and provisioned in the attacker's organization dashboard.

**Success Indicators**:
- Victim SSO remains inaccessible (DOS confirmed)
- User appears in attacker's org with access to its resources

### Step 5: Perform Account Takeover Using Provisioned User
procedure: [[procedures/Perform-Account-Takeover-Using-Provisioned-User]]

**Objective**: Leverage the provisioned user access to takeover the victim's account by modifying the attacker's entityId and using the keypair for impersonation.

**Instructions**: In the attacker's org settings, change the entityId to a new value. Then, use the attacker's keypair to sign a SAML assertion for the provisioned user's credentials, logging in to access the victim's original account and documents.

**Expected Output**: Access to victim's personal or business documents and settings.

**Success Indicators**:
- Successful login using attacker's keypair
- Visibility and control over victim's provisioned account data

## Attack Chain Summary

### Key Achievements

1. Achieved denial-of-service on victim's SSO login functionality
2. Unauthorized provisioning of victim users into attacker's organization
3. Full account takeover, including access to sensitive documents

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement

---
*Last updated: 2023-10-01T00:00:00Z*
