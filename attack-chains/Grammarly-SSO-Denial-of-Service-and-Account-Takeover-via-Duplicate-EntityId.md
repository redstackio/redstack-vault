---
tags:
  - sso
  - saml
  - authentication-bypass
  - dos
  - account-takeover
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Setup-SSO-for-Legitimate-Organization]]'
  - '[[procedures/Create-Modified-EntityId-Account]]'
  - '[[procedures/Induce-DoS-on-SSO-Login]]'
  - '[[procedures/Provision-User-to-Attacker-Organization]]'
  - '[[procedures/Modify-EntityId-for-Account-Takeover]]'
step_count: 5
techniques:
  - '[[Modify Authentication Process]]'
  - '[[Network Denial of Service]]'
description: >-
  Exploits improper handling of entityIds in Grammarly's SSO to create
  duplicates with trailing spaces, enabling DoS on legitimate SSO and potential
  account takeovers.
skill_level: intermediate
impact_level: high
id: d871d481-495f-467c-9624-7744695cb31a
created_at: '2025-12-13T09:01:26.875Z'
updated_at: '2025-12-13T09:01:26.875Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
  - '[[Network Denial of Service]]'
---
# Grammarly SSO Denial of Service and Account Takeover via Duplicate EntityId

Multi-stage attack chain demonstrating exploitation of improper entityId handling in Grammarly's SSO integration, leading to DoS on legitimate organizations and potential account takeovers.

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
    A[Setup Legit SSO] --> B[Create Duplicate EntityId] --> C[Induce DoS] --> D[Provision User] --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specified; requires access to Grammarly Business account creation and SSO configuration interfaces.

### Target Environment

- Web-based Grammarly Business SSO
- SAML-based authentication
- Network access to Grammarly services

### Initial Access Requirements

- Ability to create Grammarly Business accounts
- Control over an SSO provider for entityId configuration
- No prior credentials needed for the target organization

## Detailed Attack Procedures

### Step 1: Setup SSO for Legitimate Organization
procedure: [[procedures/Setup-SSO-for-Legitimate-Organization]]

**Objective**: Establish and verify a functional SSO setup for the target legitimate organization to baseline normal behavior.

**Instructions**: Configure SSO with a specific entityId (Identity Provider Issuer) through the Grammarly Business interface. Verify successful authentication by logging in with legitimate credentials.

**Expected Output**: Successful login confirmation without errors.

**Success Indicators**:
- SSO configuration accepted
- Authentication works as expected

### Step 2: Create Modified EntityId Account
procedure: [[procedures/Create-Modified-EntityId-Account]]

**Objective**: Create an attacker-controlled Grammarly Business account with a duplicate entityId modified by a trailing space.

**Instructions**: Sign up for a new Grammarly Business account using the same entityId as the legitimate one but append a space at the end. Use a different keypair for this organization.

**Expected Output**: New account created with the modified entityId.

**Success Indicators**:
- Account creation successful
- Modified entityId accepted by Grammarly

### Step 3: Induce DoS on SSO Login
procedure: [[procedures/Induce-DoS-on-SSO-Login]]

**Objective**: Trigger a denial of service on the legitimate organization's SSO by exploiting the duplicate entityId.

**Instructions**: Wait approximately 2 minutes for propagation. Attempt to log in to the legitimate account, which should result in an error due to the conflicting spaced entityId.

**Expected Output**: Login error message indicating failure.

**Success Indicators**:
- Login attempts fail for legitimate users
- DoS condition confirmed

### Step 4: Provision User to Attacker Organization
procedure: [[procedures/Provision-User-to-Attacker-Organization]]

**Objective**: Redirect user provisioning to the attacker's organization after deleting the user from the victim organization.

**Instructions**: Delete the target user from the legitimate organization. Attempt login again; the user should authenticate against the original but get provisioned into the attacker's organization due to prioritization of the spaced entityId.

**Expected Output**: User provisioned into attacker's organization.

**Success Indicators**:
- User appears in attacker's organization
- Authentication succeeds but under attacker control

### Step 5: Modify EntityId for Account Takeover
procedure: [[procedures/Modify-EntityId-for-Account-Takeover]]

**Objective**: Complete account takeover by modifying the attacker's entityId and logging in with the attacker's keypair.

**Instructions**: Change the attacker's entityId to a new value. Log in to the victim's account using the attacker's keypair, gaining access to personal documents if applicable.

**Expected Output**: Successful login to victim's account with attacker's credentials.

**Success Indicators**:
- Full access to victim's account
- Potential access to sensitive documents

## Attack Chain Summary

### Key Achievements

1. Denial of service on legitimate SSO logins
2. User provisioning into attacker-controlled organization
3. Complete account takeover with access to victim data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Modify Authentication Process]]
- [[Network Denial of Service]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

*Last updated: 2023-10-01*
