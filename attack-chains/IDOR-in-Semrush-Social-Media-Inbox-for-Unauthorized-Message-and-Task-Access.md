---
id: ac-uuid-123
name: IDOR in Semrush Social Media Inbox for Unauthorized Message and Task Access
tags:
  - idor
  - information-disclosure
  - semrush
  - web
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Task-Assignment-Feature-in-Social-Media-Inbox]]'
  - '[[procedures/Exploit-IDOR-by-Assigning-Messages-to-Arbitrary-User-IDs]]'
step_count: 2
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:34.617Z'
description: >-
  An Insecure Direct Object Reference vulnerability in Semrush's Social Media
  Inbox tool enables unauthorized assignment of messages to arbitrary user IDs,
  leading to information disclosure of other users' messages and tasks.
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in Semrush Social Media Inbox for Unauthorized Message and Task Access

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in Semrush's Social Media Inbox tool.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Feature] --> B[Exploit IDOR]
    B --> C[Access Disclosed Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual testing via web interface)

### Target Environment

- Web platform
- Semrush Social Media Inbox tool
- Active user account with access to the tool

### Initial Access Requirements

- Valid Semrush account credentials
- Network access to Semrush web application
- No prior elevated access needed, but legitimate user session required

## Detailed Attack Procedures

### Step 1: Identify Task Assignment Feature
procedure: [[procedures/Identify-Task-Assignment-Feature-in-Social-Media-Inbox]]

**Objective**: Locate and understand the task assignment functionality in the Social Media Inbox tool to identify potential access control weaknesses.

**Instructions**: Log in to the Semrush dashboard and navigate to the Social Media Inbox tool. Link social media accounts if not already done, then explore the task tracker section where messages can be delegated to colleagues.

**Expected Output**: Visibility into the task assignment interface, confirming the ability to link accounts and assign tasks.

**Success Indicators**:
- Task tracker feature accessible
- Option to assign messages to users visible

### Step 2: Exploit IDOR for Unauthorized Access
procedure: [[procedures/Exploit-IDOR-by-Assigning-Messages-to-Arbitrary-User-IDs]]

**Objective**: Test and exploit the lack of authorization checks by assigning messages to arbitrary user IDs, gaining unauthorized access to other users' data.

**Instructions**: In the task assignment interface, input an arbitrary user ID (e.g., obtained from other parts of the application or guessed) instead of a valid colleague ID. Submit the assignment and observe if the system accepts it without validation, allowing access to the assigned messages and tasks.

**Expected Output**: Successful assignment to the arbitrary user ID, with disclosure of messages and tasks belonging to that user.

**Success Indicators**:
- Assignment accepted without error
- Access granted to unauthorized messages and tasks

## Attack Chain Summary

### Key Achievements

1. Identification of vulnerable task assignment feature in Semrush Social Media Inbox.
2. Exploitation of IDOR to assign messages to arbitrary users.
3. Achievement of information disclosure without evidence of prior exploitation.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
