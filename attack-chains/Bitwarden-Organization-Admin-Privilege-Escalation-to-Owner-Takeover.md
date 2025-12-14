---
id: ac-bitwarden-owner-escalation
tags:
  - bitwarden
  - privilege-escalation
  - business-logic
  - account-takeover
  - saas
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Bitwarden-Test-Accounts]]'
  - '[[procedures/Invite-and-Confirm-Admin-to-Organization]]'
  - '[[procedures/Escalate-Admin-Role-to-Owner]]'
  - '[[procedures/Eject-Original-Organization-Owner]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:29:36.680Z'
description: >-
  A business logic vulnerability in Bitwarden's organization role management
  allows an admin to escalate privileges to owner, enabling full control and
  ejection of the legitimate owner.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Bitwarden Organization Admin Privilege Escalation to Owner Takeover

Multi-stage attack chain exploiting a business logic error in Bitwarden's organization role management. An attacker creates two accounts, invites the second as an admin to the first's organization, escalates the admin's role to owner via self-editing without authorization checks, and then removes the original owner, achieving full organization takeover. This compromises all organization data, including shared passwords and secrets.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Accounts] --> B[Invite Admin]
    B --> C[Escalate to Owner]
    C --> D[Takeover Organization]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)
- Bitwarden account credentials (attacker-controlled)

### Target Environment

- Bitwarden web platform (app.bitwarden.com)
- Organization feature enabled
- No additional services or ports required

### Initial Access Requirements

- Ability to register new Bitwarden accounts
- No prior organization access needed; starts from scratch
- Network access to Bitwarden's web interface

## Detailed Attack Procedures

### Step 1: Create Test Accounts
procedure: [[procedures/Create-Bitwarden-Test-Accounts]]

**Objective**: Establish two attacker-controlled accounts to simulate owner and admin roles.

**Instructions**: Register two new user accounts on the Bitwarden platform. Label the first as accountA (future owner) and the second as accountB (future admin/escalator).

**Expected Output**: Two active Bitwarden accounts with login credentials.

**Success Indicators**:
- Successful registration and login for both accounts
- Email verification completed if required

### Step 2: Invite and Confirm Admin to Organization
procedure: [[procedures/Invite-and-Confirm-Admin-to-Organization]]

**Objective**: Set up the organization under accountA and grant admin access to accountB.

**Instructions**: Using accountA, create a new organization and invite accountB as an admin. Accept the invitation with accountB, then confirm it from accountA.

**Expected Output**: accountB listed as a confirmed admin in the organization.

**Success Indicators**:
- Invitation accepted and confirmed
- accountB appears in organization members as admin

### Step 3: Escalate Admin Role to Owner
procedure: [[procedures/Escalate-Admin-Role-to-Owner]]

**Objective**: Exploit the lack of self-editing restrictions to promote accountB from admin to owner.

**Instructions**: Log in with accountB, navigate to organization settings, and edit its own role to owner via the invite users section.

**Expected Output**: accountB's role updated to owner in the organization settings.

**Success Indicators**:
- Role change persists without errors
- accountB now has owner privileges (e.g., can manage all members)

### Step 4: Eject Original Organization Owner
procedure: [[procedures/Eject-Original-Organization-Owner]]

**Objective**: Use new owner privileges to remove accountA, completing the takeover.

**Instructions**: From accountB (now owner), remove accountA from the organization members list. Verify by logging in/out with accountA.

**Expected Output**: accountA ejected; no longer has organization access.

**Success Indicators**:
- accountA removed from members
- accountA login shows no organization affiliation

## Attack Chain Summary

### Key Achievements

1. Privilege escalation from admin to owner without authorization
2. Full organization control takeover
3. Ejection of legitimate owner, compromising shared secrets

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Persistence]] Persistence

---
*Last updated: 2023-10-01T00:00:00Z*
