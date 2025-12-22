---
tags:
  - information-disclosure
  - graphql
  - hackerone
  - privacy-breach
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
commands:
  - '[[commands/ruby-redact-pii]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Create-Dummy-Report-on-HackerOne]]'
  - '[[procedures/Add-Collaborator-to-HackerOne-Report]]'
  - '[[procedures/Send-Collaboration-Invitation-on-HackerOne]]'
  - '[[procedures/Capture-GraphQL-Traffic-for-Email-Disclosure]]'
step_count: 4
techniques:
  - '[[Data from Information Repositories]]'
  - '[[Gather Victim Host Information]]'
description: >-
  Exploiting an information disclosure vulnerability in HackerOne's
  collaboration feature to reveal private user emails via GraphQL requests.
skill_level: beginner
impact_level: high
id: c4b6beea-5d92-4af0-b4db-b9a848f2bc90
created_at: '2025-12-11T06:10:15.688Z'
updated_at: '2025-12-11T06:10:15.688Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1213]]'
  - '[[T1592]]'
---
# HackerOne Email Disclosure via Collaboration Invitation

Multi-stage attack chain demonstrating how to exploit an information disclosure vulnerability in HackerOne's collaboration feature to view private user emails by capturing GraphQL request traffic during collaborator invitations.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Dummy Report] --> B[Add Collaborator]
    B --> C[Send Invite]
    C --> D[Capture GraphQL Traffic]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform: HackerOne
- Required services/ports: HTTPS access to hackerone.com
- Network access requirements: Standard internet access

### Initial Access Requirements

- Credential requirements: Valid HackerOne account
- Network position: External access to HackerOne platform
- Prior access needed: Ability to submit reports on HackerOne

## Detailed Attack Procedures

### Step 1: Create Dummy Report - [[procedures/Create-Dummy-Report-on-HackerOne]]

**Procedure**: [[procedures/Create-Dummy-Report-on-HackerOne]]

**Objective**: Establish a report context to invite collaborators and trigger the vulnerable GraphQL mutation.

**Expected Output**: A new dummy report created and submitted on the HackerOne platform.

First, log into your HackerOne account and navigate to the report submission page. Submit a new report with placeholder details.

**Success Indicators**:
- Report is successfully created and visible in your dashboard.
- No errors during submission.

### Step 2: Add Collaborator - [[procedures/Add-Collaborator-to-HackerOne-Report]]

**Procedure**: [[procedures/Add-Collaborator-to-HackerOne-Report]]

**Objective**: Select and add the target hacker's username to the report as a collaborator to prepare for email disclosure.

**Expected Output**: Target hacker added to the collaborator list in pending status.

In the report dashboard, click to add collaborators and enter the username of the hacker whose email you want to disclose. You can add up to 2 invites per report.

**Success Indicators**:
- Collaborator appears in the list.
- Invitation is ready to send.

### Step 3: Send Invite - [[procedures/Send-Collaboration-Invitation-on-HackerOne]]

**Procedure**: [[procedures/Send-Collaboration-Invitation-on-HackerOne]]

**Objective**: Send the invitation to place the collaborator in pending status, setting up for the GraphQL request capture.

**Expected Output**: Invitation sent, collaborator status updated to pending.

Click the send button to dispatch the invitation. The hacker remains in pending status until acceptance.

**Success Indicators**:
- Invitation confirmation received.
- Status updates to pending.

### Step 4: Capture GraphQL Traffic - [[procedures/Capture-GraphQL-Traffic-for-Email-Disclosure]]

**Procedure**: [[procedures/Capture-GraphQL-Traffic-for-Email-Disclosure]]

**Objective**: Intercept the GraphQL request to expose the private email in the payload.

**Expected Output**: Captured request payload containing the target's email address.

Use [[tools/Burp-Suite]] to proxy your browser traffic. Click the pen icon to edit collaborators, then capture the POST request to /graphql with the SaveCollaboratorsMutation operation. Inspect the payload for the email details.

**Success Indicators**:
- GraphQL request captured successfully.
- Email address visible in the request payload, even before invitation acceptance.

## Attack Chain Summary

### Key Achievements

1. Successful creation of a dummy report to facilitate invitations.
2. Addition and invitation of target collaborators without their acceptance.
3. Disclosure of private emails via intercepted GraphQL traffic, enabling privacy breaches.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Data from Information Repositories]]
- [[Gather Victim Host Information]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]
- [[Discovery]]

*Last updated: 2024-01-01T00:00:00Z*
