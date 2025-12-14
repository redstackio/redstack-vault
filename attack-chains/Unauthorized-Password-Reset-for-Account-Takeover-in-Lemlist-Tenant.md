---
tags:
  - broken-access-control
  - account-takeover
  - password-reset
  - authorization-bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Discover-Tenant-Admin-Authorization-Flaw-in-User-Management]]'
  - '[[procedures/Perform-Unauthorized-Password-Reset-on-Target-User]]'
  - '[[procedures/Attempt-Account-Takeover-with-Reset-Password]]'
step_count: 3
techniques:
  - '[[Account Manipulation]]'
  - '[[Account Discovery]]'
description: >-
  An authorization vulnerability allowing tenant admins to reset passwords of
  other users in the same tenant, enabling account takeover after invitation
  acceptance.
skill_level: intermediate
impact_level: high
id: 887b14ae-a697-481b-97b8-bb2e27c5b9d9
created_at: '2025-12-14T17:33:06.696Z'
updated_at: '2025-12-14T17:33:06.696Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Account Discovery]]'
---
# Unauthorized Password Reset for Account Takeover in Lemlist Tenant

## Overview

This attack chain exploits a broken access control vulnerability in the Lemlist web application (app.lemlist.com), where tenant administrators can unauthorizedly reset passwords for other users within the same tenant, including invited agency accounts. The attack requires the victim to have accepted an invitation to the tenant. Once exploited, it enables potential account takeover, though multi-factor authentication (MFA) can mitigate actual login if enabled. The vulnerability stems from insufficient authorization checks in the user management and password reset features, allowing unintended access in shared tenant environments. Remediation involved implementing stricter access controls.

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
    A[Discover Authorization Flaw] --> B[Exploit Password Reset]
    B --> C[Attempt Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools for inspection)

### Target Environment

- Web platform: app.lemlist.com
- Required services/ports: HTTPS (443)
- Network access requirements: Direct internet access to the application

### Initial Access Requirements

- Valid tenant admin credentials
- Target user must have accepted an invitation to the tenant
- No prior access to victim's account needed, but shared tenant environment

## Detailed Attack Procedures

### Step 1: Discover Authorization Flaw
procedure: [[procedures/Discover-Tenant-Admin-Authorization-Flaw-in-User-Management]]

**Objective**: Identify the authorization issue allowing tenant admins to access and modify other users' credentials without proper checks.

**Instructions**: Log in to app.lemlist.com as a tenant admin. Navigate to the user management section and attempt to view or edit details of other users, including invited accounts. Test if password reset options are accessible for non-admin users by inspecting the UI or API responses in browser developer tools to confirm lack of authorization enforcement.

**Expected Output**: Ability to access user profiles and password reset interfaces for unauthorized users.

**Success Indicators**:
- Tenant admin can view/edit other users' credentials
- No permission errors when accessing password reset for invited users

### Step 2: Exploit Password Reset
procedure: [[procedures/Perform-Unauthorized-Password-Reset-on-Target-User]]

**Objective**: Reset the password of a target user within the same tenant to gain control over their account.

**Instructions**: From the user management dashboard, select the target user's account (ensuring they have accepted the invitation). Locate the password reset feature and execute the reset action, setting a new password known to the attacker. Confirm the change via application feedback or API calls intercepted in developer tools.

**Expected Output**: Confirmation message or updated user status indicating password reset success.

**Success Indicators**:
- Password reset completes without authorization denial
- Target user's password is updated to attacker's choice

### Step 3: Attempt Account Takeover
procedure: [[procedures/Attempt-Account-Takeover-with-Reset-Password]]

**Objective**: Use the newly set password to access the victim's account and perform unauthorized actions.

**Instructions**: Log out of the admin account and attempt to log in to the target user's account using their email and the newly reset password. If MFA is disabled, proceed to access tenant resources; if enabled, the login will fail at the MFA prompt.

**Expected Output**: Successful login to the victim's account or MFA challenge blocking access.

**Success Indicators**:
- Access granted to victim's dashboard
- Ability to view or modify tenant data as the victim (if no MFA)

## Attack Chain Summary

### Key Achievements

1. Exposed broken access control in tenant user management
2. Enabled unauthorized password resets across invited accounts
3. Demonstrated potential for account takeover in shared environments

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Manipulation]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
