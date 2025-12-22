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
  - '[[Defense Evasion]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Configure-and-Verify-Grammarly-SSO]]'
  - >-
    [[procedures/Register-Malicious-Grammarly-Business-Account-with-Spaced-EntityId]]
  - '[[procedures/Induce-SSO-Denial-of-Service]]'
  - '[[procedures/Provision-Victim-User-to-Attacker-Organization]]'
  - '[[procedures/Complete-Account-Takeover-via-EntityId-Update]]'
step_count: 5
techniques:
  - '[[Use Alternate Authentication Material]]'
  - '[[Valid Accounts]]'
description: >-
  Exploits improper handling of entityIds in Grammarly's SSO by creating
  duplicates with trailing spaces, leading to SSO denial of service and account
  takeovers.
skill_level: intermediate
impact_level: high
id: 76040e41-b35a-4d76-ae40-ac49ade4c8d0
created_at: '2025-12-11T03:47:39.575Z'
updated_at: '2025-12-11T03:47:39.575Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0005]]'
mitre_techniques:
  - '[[T1550]]'
  - '[[T1078]]'
---
# Grammarly SSO EntityId Conflict for Denial of Service and Account Takeover

Multi-stage attack chain demonstrating exploitation of improper entityId handling in Grammarly's SSO integration, allowing denial of service on organizational SSO and account takeovers by provisioning users to an attacker's organization.

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
    A[Setup Legitimate SSO] --> B[Register Malicious Account] --> C[Induce DoS] --> D[Provision Victim] --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (web-based interactions)

### Target Environment

- Web platform
- Grammarly SSO and Business Accounts services
- SAML tech stack

### Initial Access Requirements

- Ability to create Grammarly business accounts
- Access to SSO configuration interfaces
- No prior credentials needed beyond account creation

## Detailed Attack Procedures

## Step 1: Setup Legitimate SSO - [[procedures/Configure-and-Verify-Grammarly-SSO]]

**Procedure**: [[procedures/Configure-and-Verify-Grammarly-SSO]]

**Objective**: Establish a baseline legitimate SSO configuration for a Grammarly business account to verify normal functionality before exploitation.

**Instructions**:
Configure SSO for a Grammarly business account and verify successful authentication. This involves setting up the entityId (Identity Provider Issuer) and confirming login works as expected.

**Expected Output**: Successful SSO login to the legitimate organization.

**Success Indicators**:
- User can authenticate and access the account.
- No errors during login.

## Step 2: Register Malicious Account - [[procedures/Register-Malicious-Grammarly-Business-Account-with-Spaced-EntityId]]

**Procedure**: [[procedures/Register-Malicious-Grammarly-Business-Account-with-Spaced-EntityId]]

**Objective**: Create a conflicting entityId by appending a space, setting up the attacker's organization for later provisioning.

**Instructions**:
Register a new Grammarly business account using the same entityId from Step 1 but with a trailing space appended. Assign a different cryptographic keypair to this organization.

**Expected Output**: New attacker-controlled organization created with modified entityId.

**Success Indicators**:
- Account registration succeeds without entityId conflict detection.
- Different keypair is configured.

## Step 3: Induce Denial of Service - [[procedures/Induce-SSO-Denial-of-Service]]

**Procedure**: [[procedures/Induce-SSO-Denial-of-Service]]

**Objective**: Trigger authentication conflicts leading to denial of service on the legitimate SSO.

**Instructions**:
Wait approximately 2 minutes for changes to propagate, then attempt to log in to the original account from Step 1. Observe the authentication error due to the entityId conflict.

**Expected Output**: Login failure with an error message.

**Success Indicators**:
- SSO login to legitimate organization fails.
- Error indicates authentication conflict.

## Step 4: Provision Victim User - [[procedures/Provision-Victim-User-to-Attacker-Organization]]

**Procedure**: [[procedures/Provision-Victim-User-to-Attacker-Organization]]

**Objective**: Reprovision the victim user into the attacker's organization by exploiting the entityId prioritization.

**Instructions**:
Delete the user from the victim organization, then retry the SSO login. The user will be provisioned to the attacker's organization despite using the legitimate keypair, due to the trimmed issuer validation but non-trimmed prioritization.

**Expected Output**: User added to attacker's organization.

**Success Indicators**:
- User appears in attacker's organization dashboard.
- Authentication succeeds but routes to attacker org.

## Step 5: Complete Takeover - [[procedures/Complete-Account-Takeover-via-EntityId-Update]]

**Procedure**: [[procedures/Complete-Account-Takeover-via-EntityId-Update]]

**Objective**: Finalize account takeover by updating the entityId and accessing the victim's account with the attacker's keypair.

**Instructions**:
Update the attacker's entityId to a unique value, then log in using the attacker's keypair to access the provisioned victim's account, including any personal documents.

**Expected Output**: Full access to victim's account and data.

**Success Indicators**:
- Attacker can log in as the victim.
- Access to documents and account features confirmed.

## Attack Chain Summary

### Key Achievements

1. Denial of service on any organization's SSO.
2. Provisioning of victim users into attacker's organization.
3. Full account takeover with access to personal documents.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Use Alternate Authentication Material]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Defense Evasion]]

*Last updated: 2023-10-01*
