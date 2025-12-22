---
tags:
  - privilege-escalation
  - access-control
  - yelp
  - business-account
  - user-invite
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-as-Non-Owner-Business-User]]'
  - '[[procedures/Invite-New-Users-as-Non-Owner]]'
  - '[[procedures/Verify-Invisible-Users-from-Owner-Perspective]]'
step_count: 3
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:35.269Z'
description: >-
  A multi-stage privilege escalation attack in Yelp's business account system
  where non-owner users can invite additional users without permissions, and
  these additions remain invisible to the account owner, enabling unauthorized
  access and potential account compromise.
skill_level: intermediate
impact_level: high
id: 86b0aceb-6331-4eef-9408-d35eb1b1f647
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
---
# Yelp Business Account Privilege Escalation via Unauthorized Non-Owner User Invites

Multi-stage attack chain demonstrating a complete privilege escalation workflow in Yelp's business account system, exploiting improper access controls to add invisible users and potentially compromise the account.

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
    A[Login as Non-Owner User] --> B[Invite Unauthorized Users]
    B --> C[Verify Invisibility to Owner]
    C --> D[Account Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox with developer tools for inspection)

### Target Environment

- Yelp Business account interface (web-based)
- Access to a non-owner business user account
- Owner account credentials for verification

### Initial Access Requirements

- Valid credentials for a restricted (non-owner) business user role
- No special network access beyond standard internet connectivity
- Prior legitimate access to the business account as a standard user

## Detailed Attack Procedures

### Step 1: Login as Non-Owner Business User
procedure: [[procedures/Login-as-Non-Owner-Business-User]]

**Objective**: Gain access to the Yelp Business account interface using a restricted user role that lacks user management permissions but retains access to other features.

**Instructions**: Open a web browser and navigate to the Yelp Business login page. Enter credentials for a non-owner business user account. Once logged in, confirm that the user management section is inaccessible, but other account functionalities (e.g., profile editing) are available.

**Expected Output**: Successful login to the business dashboard as a standard user, with restricted permissions visible (e.g., no 'User Management' option).

**Success Indicators**:
- Dashboard loads without errors
- User management features are hidden or disabled

### Step 2: Invite New Users as Non-Owner
procedure: [[procedures/Invite-New-Users-as-Non-Owner]]

**Objective**: Exploit the invite functionality to add new users to the business account without required permissions, bypassing access controls.

**Instructions**: From the business account dashboard, navigate to the settings or team management section. Locate the 'Invite' or 'Add User' option, which should not be available to non-owners but is accessible due to the vulnerability. Enter email addresses for new users and submit the invitations. Monitor for confirmation messages indicating successful invites.

**Expected Output**: Invitation emails sent or confirmation of added users within the inviter's view, despite lacking permissions.

**Success Indicators**:
- Invite form is accessible and submittable
- No error messages blocking the action
- New users receive invite links

### Step 3: Verify Invisibility to Owner
procedure: [[procedures/Verify-Invisible-Users-from-Owner-Perspective]]

**Objective**: Confirm that the newly invited users are not visible in the account owner's user management interface, allowing persistent unauthorized access.

**Instructions**: Log out from the non-owner account and log in using the account owner's credentials. Navigate to the user management or team members page. Search for or list all users; the newly invited ones should not appear in the list.

**Expected Output**: User management page shows only existing authorized users, with no trace of the invited ones.

**Success Indicators**:
- Invited users absent from owner’s view
- No alerts or notifications to the owner about new additions

## Attack Chain Summary

### Key Achievements

1. Bypassed access controls to invite users as a non-owner
2. Added unauthorized users invisibly to the owner
3. Enabled potential account takeover through hidden access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
