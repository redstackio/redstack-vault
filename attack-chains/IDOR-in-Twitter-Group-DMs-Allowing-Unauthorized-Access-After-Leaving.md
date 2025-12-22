---
id: ac-uuid-001
name: IDOR in Twitter Group DMs Allowing Unauthorized Access After Leaving
type: attack_chain
description: >-
  Exploits an Insecure Direct Object Reference (IDOR) vulnerability in Twitter's
  direct messaging system to access group DM contents after leaving the group.
verified: false
submitted: true
step_count: 6
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:28.848Z'
procedures:
  - '[[procedures/Setup-Twitter-Accounts-and-Group-DM]]'
  - '[[procedures/Leave-Group-and-Send-Message]]'
  - '[[procedures/Exploit-IDOR-for-Unauthorized-DM-Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
tags:
  - idor
  - twitter
  - dm
  - access-control
  - unauthorized-access
platforms:
  - Web
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---

# IDOR in Twitter Group DMs Allowing Unauthorized Access After Leaving

Multi-stage attack chain demonstrating a complete attack workflow exploiting IDOR in Twitter's group direct messages.

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
    A[Setup Accounts and Group] --> B[Leave Group]
    B --> C[Send Message and Capture ID]
    C --> D[Exploit IDOR via Endpoint]
    D --> E[Access Private DM Contents]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Twitter web platform
- Access to multiple Twitter accounts
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid Twitter credentials for at least three accounts
- Network access to twitter.com
- No prior access to the target group needed beyond initial setup

## Detailed Attack Procedures

### Step 1: Setup Accounts and Group DM

procedure: [[procedures/Setup-Twitter-Accounts-and-Group-DM]]

**Objective**: Create the necessary user accounts and initiate a group direct message to establish the vulnerable conversation.

**Instructions**: Register three separate Twitter accounts (A, B, C) via the Twitter signup process. From account A, navigate to the direct messages section and create a new group DM including accounts A, B, and C.

**Expected Output**: A group DM conversation is active with all three participants.

**Success Indicators**:
- Three accounts successfully created and verified.
- Group DM initiated and visible to all participants.

### Step 2: Leave Group and Send Message

procedure: [[procedures/Leave-Group-and-Send-Message]]

**Objective**: Simulate departure from the group and introduce new content to test access controls.

**Instructions**: From account C, leave the group DM by selecting the option to exit the conversation. Then, from account A or B, send a test message in the group DM and inspect the URL or message details to identify the unique DM ID.

**Expected Output**: Account C is removed from the group; a new message is sent, and the DM ID is captured (e.g., from the conversation URL).

**Success Indicators**:
- Confirmation that account C has left the group.
- DM ID noted for later use.
- Message visible to remaining participants.

### Step 3: Exploit IDOR for Unauthorized DM Access

procedure: [[procedures/Exploit-IDOR-for-Unauthorized-DM-Access]]

**Objective**: Bypass access controls using the DM ID to view private messages from a former participant.

**Instructions**: From account C, directly navigate to the mobile web endpoint `https://mobile.twitter.com/a/messages/[DM_ID]/delete`, replacing `[DM_ID]` with the captured ID. This loads the conversation contents despite having left the group.

**Expected Output**: Full access to the group DM, including messages sent after leaving.

**Success Indicators**:
- Unauthorized messages are viewable.
- No authentication or membership errors occur.

## Attack Chain Summary

### Key Achievements

1. Successful setup of a vulnerable group DM scenario.
2. Demonstration of IDOR allowing post-departure access.
3. Exposure of sensitive private communications via direct endpoint manipulation.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
