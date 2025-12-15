---
tags:
  - auth-bypass
  - 2fa-bypass
  - hackerone
  - vulnerability-report
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Create-2FA-Enabled-Program-and-Submit-Report]]'
  - '[[procedures/Invite-Non-2FA-Account-as-Collaborator]]'
  - '[[procedures/Accept-Invitation-to-Gain-Unauthorized-Access]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
description: >-
  Multi-stage attack chain exploiting a vulnerability in HackerOne that allows
  inviting non-2FA accounts as collaborators to reports in 2FA-required
  programs, bypassing multi-factor authentication controls.
skill_level: intermediate
impact_level: high
id: 54fa8a38-4546-4a3a-90e3-e4ab07879df2
created_at: '2025-12-14T17:24:45.537Z'
updated_at: '2025-12-14T17:24:45.537Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass 2FA Requirement via Collaborator Invitation in HackerOne Programs

Multi-stage attack chain demonstrating a complete attack workflow to bypass 2FA enforcement in HackerOne bug bounty programs by inviting collaborators without multi-factor authentication.

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
    A[Create Program and Submit Report] --> B[Invite Non-2FA Collaborator]
    B --> C[Accept Invite and Access Report]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)
- HackerOne account with program creation privileges (typically for researchers or testers)

### Target Environment

- HackerOne platform (web application)
- Access to program management features
- No specific ports or services beyond standard HTTPS (port 443)

### Initial Access Requirements

- Valid HackerOne credentials with ability to create programs
- Network access to hackerone.com
- No prior access to target reports needed, but assumes tester role

## Detailed Attack Procedures

### Step 1: Create Program and Submit Report
procedure: [[procedures/Create-2FA-Enabled-Program-and-Submit-Report]]

**Objective**: Set up a 2FA-required program and submit a sample report to enable collaborator invitations.

**Instructions**: Log in to HackerOne, navigate to program creation, enable 2FA enforcement, and submit a vulnerability report.

**Expected Output**: A new program with 2FA enabled and a pending report accessible via the dashboard.

**Success Indicators**:
- Program created with 2FA policy active
- Report submitted and visible in the program interface

### Step 2: Invite Non-2FA Account as Collaborator
procedure: [[procedures/Invite-Non-2FA-Account-as-Collaborator]]

**Objective**: Register a secondary account without 2FA and send a collaborator invitation to it from the report.

**Instructions**: Create a new HackerOne account without enabling 2FA, then from the original report, use the invite feature to add the new account as a collaborator.

**Expected Output**: Invitation email or notification sent to the non-2FA account.

**Success Indicators**:
- New account registered successfully without 2FA
- Invitation sent without 2FA validation errors

### Step 3: Accept Invitation to Gain Unauthorized Access
procedure: [[procedures/Accept-Invitation-to-Gain-Unauthorized-Access]]

**Objective**: Have the non-2FA account accept the invite, granting access to the sensitive report.

**Instructions**: Log in to the non-2FA account, view the invitation, and accept it to join the report.

**Expected Output**: Non-2FA account gains full read access to the report content without prompting for 2FA.

**Success Indicators**:
- Invitation accepted successfully
- Report details visible to non-2FA account, confirming bypass

## Attack Chain Summary

### Key Achievements

1. Successfully created a 2FA-enforced program and report.
2. Invited and added a non-2FA account as collaborator without enforcement.
3. Gained unauthorized access to sensitive report data, undermining 2FA policy.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
