---
id: ac-yelp-priv-esc-owner-removal
tags:
  - privilege-escalation
  - access-control
  - yelp
  - business-account
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Invite-Low-Privilege-User-to-Yelp-Business-Account]]'
  - '[[procedures/Remove-Yelp-Business-Account-Owner-as-Low-Privilege-User]]'
step_count: 2
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:27.033Z'
description: >-
  A privilege escalation attack in Yelp's business account system allowing a
  low-privilege invited user to remove the account owner due to improper access
  controls.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Yelp Business Account Privilege Escalation via Unauthorized Owner Removal

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper access controls in Yelp's business account user management.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Invite Low-Privilege User] --> B[Remove Account Owner]
    B --> C[Gain Control Disruption]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)

### Target Environment

- Yelp Business web platform
- Active business account with owner privileges
- No special services or ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Valid Yelp business account owner credentials
- Ability to invite users via the business dashboard
- Low-privilege user account (can be a test account)

## Detailed Attack Procedures

### Step 1: Invite Low-Privilege User
procedure: [[procedures/Invite-Low-Privilege-User-to-Yelp-Business-Account]]

**Objective**: Add a low-privilege user to the business account without granting access to user management features, setting up for escalation.

**Instructions**: Log in as the account owner and navigate to the user invitation section in the Yelp Business dashboard. Enter the email of a low-privilege user and send the invitation. The user accepts the invite, gaining standard view-only or limited edit access but explicitly no user management permissions.

**Expected Output**: Confirmation email sent and user added to the account with restricted role.

**Success Indicators**:
- Invitation email received and accepted by low-privilege user
- User appears in the account members list with limited permissions

### Step 2: Unauthorized Owner Removal
procedure: [[procedures/Remove-Yelp-Business-Account-Owner-as-Low-Privilege-User]]

**Objective**: Exploit missing authorization checks to remove the account owner as the low-privilege user, disrupting ownership.

**Instructions**: Log in as the low-privilege user and attempt to access the user removal functionality in the business dashboard. Select the owner account and execute the removal action. Due to improper controls, the removal succeeds without requiring user management access.

**Expected Output**: Owner account removed from the business, potentially transferring or disrupting control.

**Success Indicators**:
- Owner removal confirmation displayed
- Owner no longer listed in account members
- Account control impacted (e.g., owner locked out)

## Attack Chain Summary

### Key Achievements

1. Successful invitation of a low-privilege user to a Yelp business account.
2. Unauthorized removal of the account owner by the low-privilege user.
3. Demonstration of privilege escalation leading to potential account control loss.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
