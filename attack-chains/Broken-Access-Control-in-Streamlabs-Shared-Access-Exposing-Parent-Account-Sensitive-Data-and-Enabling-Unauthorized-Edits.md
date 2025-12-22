---
id: ac-streamlabs-broken-access-001
tags:
  - broken-access-control
  - information-disclosure
  - api-vulnerability
  - jwt-leak
  - billing-exposure
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Invite-Moderator-to-Shared-Access]]'
  - '[[procedures/Accept-Invitation-as-Moderator]]'
  - '[[procedures/Switch-to-Parent-Account-as-Moderator]]'
  - '[[procedures/Test-Restricted-API-Access]]'
  - '[[procedures/Exploit-Platform-API-for-Data-Disclosure]]'
  - '[[procedures/Access-Profile-for-Unauthorized-Edits]]'
step_count: 6
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:20.842Z'
description: >-
  Multi-stage attack exploiting improper access controls in Streamlabs shared
  access feature, allowing moderators to disclose parent account emails, JWT
  tokens, billing info, and perform unauthorized edits.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
---
# Broken Access Control in Streamlabs Shared Access Exposing Parent Account Sensitive Data and Enabling Unauthorized Edits

Multi-stage attack chain demonstrating exploitation of improper permission checks in the Streamlabs platform API shared access feature, allowing a moderator to bypass restrictions and access parent account sensitive information like emails, JWT tokens, and billing details, while also enabling unauthorized modifications to subscriptions and profile settings.

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
    A[Invite Moderator] --> B[Accept Invitation]
    B --> C[Switch to Parent Account]
    C --> D[Test Restricted Access]
    D --> E[Exploit API for Disclosure]
    E --> F[Access Profile for Edits]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)
- Access to two Streamlabs accounts: parent (User A) and moderator (User B)

### Target Environment

- Streamlabs web platform (https://streamlabs.com)
- No specific ports required; web-based over HTTPS
- Requires internet access and valid Streamlabs credentials

### Initial Access Requirements

- Valid credentials for User A (parent account, optionally Prime subscriber for full impact)
- Valid credentials for User B (to act as moderator)
- No prior network position needed; all actions via web interface

## Detailed Attack Procedures

### Step 1: Invite Moderator to Shared Access
procedure: [[procedures/Invite-Moderator-to-Shared-Access]]

**Objective**: Create a shared access invitation for a moderator role to gain limited access to the parent account.

**Instructions**: Log in to User A's Streamlabs account, navigate to the shared access settings, and generate an invitation link with Moderator permissions.

**Expected Output**: A unique invitation link is generated and copied.

**Success Indicators**:
- Invitation link created successfully
- Moderator role selected in settings

### Step 2: Accept Invitation as Moderator
procedure: [[procedures/Accept-Invitation-as-Moderator]]

**Objective**: Join the parent account as a moderator using the invitation link.

**Instructions**: Log out of User A, log in to User B's account, and use the invitation link to accept the moderator role.

**Expected Output**: User B is now listed as a moderator for User A's account.

**Success Indicators**:
- Invitation accepted without errors
- Moderator status confirmed in User B's dashboard

### Step 3: Switch to Parent Account as Moderator
procedure: [[procedures/Switch-to-Parent-Account-as-Moderator]]

**Objective**: Switch context from moderator account to parent account via the dashboard.

**Instructions**: In User B's dashboard, go to shared access settings and select to act as User A.

**Expected Output**: Dashboard updates to show "You are currently acting as [User A]".

**Success Indicators**:
- Context switch successful
- Parent account interface loads for User B

### Step 4: Test Restricted API Access
procedure: [[procedures/Test-Restricted-API-Access]]

**Objective**: Verify that standard endpoints enforce access controls for moderators.

**Instructions**: While acting as User A, attempt to access the v5 user endpoint in the browser.

**Expected Output**: "Request Unauthorized" error response.

**Success Indicators**:
- Access denied on restricted endpoint
- Confirms partial restrictions are in place

### Step 5: Exploit Platform API for Data Disclosure
procedure: [[procedures/Exploit-Platform-API-for-Data-Disclosure]]

**Objective**: Bypass controls to retrieve sensitive parent account data via the vulnerable endpoint.

**Instructions**: Directly access the platform API endpoint in the browser while in the parent context.

**Expected Output**: JSON response containing User A's ID, username, email, JWT token, and other details.

**Success Indicators**:
- Sensitive data like email and JWT returned
- No authorization prompt or error

### Step 6: Access Profile for Unauthorized Edits
procedure: [[procedures/Access-Profile-for-Unauthorized-Edits]]

**Objective**: View and modify billing, subscriptions, and app settings for Prime accounts.

**Instructions**: Navigate to the app-store profile page and interact with sensitive sections.

**Expected Output**: Access to credit card details, CVV, subscriptions, and edit capabilities.

**Success Indicators**:
- Billing info visible and editable
- Apps and subscriptions modifiable without restrictions

## Attack Chain Summary

### Key Achievements

1. Successful invitation and acceptance of moderator role
2. Context switch to parent account without full privilege checks
3. Disclosure of sensitive data including JWT tokens and emails
4. Unauthorized access to billing and profile management for Prime users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unsecured Credentials]] Unsecured Credentials

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
