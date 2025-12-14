---
id: ac-persistent-notifications-disclosure
tags:
  - logic-error
  - information-disclosure
  - access-control-bypass
  - notifications
  - hackerone
type: attack_chain
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Join-Team-and-Interact-with-Reports]]'
  - '[[procedures/Remove-User-from-Team]]'
  - '[[procedures/Observe-Unauthorized-Notifications]]'
  - '[[procedures/Verify-User-Removal-from-Team]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:20.656Z'
description: >-
  Demonstrates a logic error in HackerOne's notification system allowing former
  team members to receive emails disclosing private report details like ID,
  team, and title after removal.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Persistent Team Notifications After Removal Leading to Private Report Disclosure

Multi-stage attack chain demonstrating a logic error in HackerOne's team notification system, where removed users continue receiving sensitive report updates.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Join Team] --> B[Interact with Report]
    B --> C[Remove from Team]
    C --> D[Receive Notification]
    D --> E[Verify Removal]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual account management via web interface)

### Target Environment

- HackerOne platform (web application)
- Access to multiple user accounts
- Team creation privileges

### Initial Access Requirements

- Valid HackerOne accounts
- Ability to create or join teams
- No special network access beyond standard web

## Detailed Attack Procedures

### Step 1: Join Team and Interact with Reports
procedure: [[procedures/Join-Team-and-Interact-with-Reports]]

**Objective**: Establish baseline access to team reports to set up notification triggers.

**Instructions**: Log in to HackerOne with the test account (e.g., @lccunha) and join the target team (e.g., 'Test' team). Create or interact with a private report (e.g., #45958) to ensure notifications are subscribed.

**Expected Output**: Confirmation of team membership and report visibility.

**Success Indicators**:
- User listed as team member
- Report details accessible

### Step 2: Remove User from Team
procedure: [[procedures/Remove-User-from-Team]]

**Objective**: Simulate user departure to test access revocation.

**Instructions**: Using admin privileges or self-removal, remove the test account (@lccunha) from the 'Test' team via the team management interface.

**Expected Output**: User no longer appears in team member list.

**Success Indicators**:
- Removal confirmation
- No access to team dashboard sections

### Step 3: Observe Unauthorized Notifications
procedure: [[procedures/Observe-Unauthorized-Notifications]]

**Objective**: Trigger and capture persistent notifications revealing private data.

**Instructions**: From a remaining team member account, update the report (e.g., schedule #45958 to become public). Monitor the removed account's email and dashboard for incoming notifications.

**Expected Output**: Email notification with report ID (#45958), team name ('Test'), and title, despite removal.

**Success Indicators**:
- Receipt of email with sensitive details
- Lingering dashboard elements related to the team

### Step 4: Verify User Removal from Team
procedure: [[procedures/Verify-User-Removal-from-Team]]

**Objective**: Confirm the removal was successful to isolate the notification flaw.

**Instructions**: Log in to a current team member account (e.g., @brdoors2) and check the team members list to ensure @lccunha is no longer visible.

**Expected Output**: Removed user absent from member roster.

**Success Indicators**:
- No trace of removed user in team view
- Contrast with received notifications

## Attack Chain Summary

### Key Achievements

1. Demonstrated failure in revoking notification subscriptions upon team removal.
2. Exposed partial private report details (ID, team, title) to unauthorized former members.
3. Highlighted dashboard cleanup issues persisting team associations.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
