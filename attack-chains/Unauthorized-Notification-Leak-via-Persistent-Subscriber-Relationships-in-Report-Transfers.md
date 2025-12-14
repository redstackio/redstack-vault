---
id: ac-001-persistent-subscriber-leak
tags:
  - access-control
  - info-leak
  - notifications
  - hackerone
  - rails
type: attack_chain
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2024-10-05T00:00:00Z'
procedures:
  - '[[procedures/Join-Program-and-Subscribe-to-Reports]]'
  - '[[procedures/Remove-User-from-Program]]'
  - '[[procedures/Transfer-Report-to-Another-Program]]'
  - '[[procedures/Receive-Unauthorized-Notification]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.269Z'
description: >-
  A multi-stage vulnerability in HackerOne's report system where removed users
  retain subscriber status, leading to unauthorized notifications containing
  sensitive report metadata during transfers.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Notification Leak via Persistent Subscriber Relationships in Report Transfers

Multi-stage attack chain demonstrating a logic flaw in subscriber management that allows former program members to receive sensitive notifications about report transfers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Join and Subscribe] --> B[Remove from Program]
    B --> C[Transfer Report]
    C --> D[Receive Notification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on platform UI interactions)

### Target Environment

- HackerOne platform (Ruby on Rails web application)
- Required services/ports: HTTPS on port 443
- Network access requirements: Internet access to HackerOne

### Initial Access Requirements

- Valid HackerOne account with program membership
- Network position: External user
- Prior access needed: Authorized program participation

## Detailed Attack Procedures

### Step 1: Join Program and Subscribe to Reports
procedure: [[procedures/Join-Program-and-Subscribe-to-Reports]]

**Objective**: Establish subscriber relationship to reports in the target program.

**Instructions**: Log in to HackerOne as a user, navigate to a program dashboard, and join the program. Once joined, subscribe to report notifications via the program's settings or report interface.

**Expected Output**: Confirmation of program membership and active subscription to report updates.

**Success Indicators**:
- User appears in program members list
- Subscription status shows active for reports

### Step 2: Remove User from Program
procedure: [[procedures/Remove-User-from-Program]]

**Objective**: Simulate user departure while leaving subscriber relationship intact due to the vulnerability.

**Instructions**: As a program admin or via self-removal, leave or remove the user from the program through the HackerOne admin interface. Verify removal from program members but note no unsubscribe from reports.

**Expected Output**: User no longer listed in program members, but subscriber link persists in backend.

**Success Indicators**:
- User removed from program access
- No explicit unsubscribe prompt for reports

### Step 3: Transfer Report to Another Program
procedure: [[procedures/Transfer-Report-to-Another-Program]]

**Objective**: Trigger notification system during report transfer, notifying all persisted subscribers.

**Instructions**: As an authorized user in the source program, select a report and initiate transfer to another program using the 'Transfer report' functionality in the HackerOne interface.

**Expected Output**: Report successfully transferred, with notifications queued to all subscribers including removed ones.

**Success Indicators**:
- Report status updated to transferred
- Notification logs show dispatch to subscribers

### Step 4: Receive Unauthorized Notification
procedure: [[procedures/Receive-Unauthorized-Notification]]

**Objective**: Capture leaked metadata from the notification sent to the former subscriber.

**Instructions**: Monitor the removed user's HackerOne notifications inbox for the transfer alert, which includes report title and other metadata.

**Expected Output**: In-app notification detailing the report transfer, visible despite lack of program access.

**Success Indicators**:
- Notification received with sensitive details
- Confirmation of leak without full report access

## Attack Chain Summary

### Key Achievements

1. Persistent subscriber relationships post-removal
2. Leaked report metadata via notifications (2110 instances across 21 programs)
3. Erosion of access control without granting full unauthorized access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Collection]]

---
*Last updated: 2024-10-05T00:00:00Z*
