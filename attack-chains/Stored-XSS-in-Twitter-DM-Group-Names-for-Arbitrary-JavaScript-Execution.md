---
id: ac-twitter-dm-xss-001
tags:
  - xss
  - stored-xss
  - twitter
  - dm
  - javascript
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Twitter-DM-Group-with-XSS-Payload]]'
  - '[[procedures/Trigger-XSS-via-Tweet-Sharing-in-DM]]'
  - '[[procedures/Trigger-XSS-via-Recent-Conversations-Selection]]'
  - '[[procedures/Update-Existing-DM-Group-Name-with-XSS-Payload]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.339Z'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in Twitter's DM
  group name feature to execute arbitrary JavaScript in victims' browsers.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in Twitter DM Group Names for Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting insufficient input sanitization in Twitter's Direct Message (DM) group name feature, allowing stored XSS to execute arbitrary JavaScript against other group members.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create DM Group with XSS Payload] --> B[Trigger via Tweet Sharing]
    B --> C[Trigger via Recent Conversations]
    C --> D[Update Group Name for Ongoing Attacks]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools for payload testing)

### Target Environment

- Twitter web platform
- Access to Direct Messages feature
- No specific ports or services beyond standard HTTPS

### Initial Access Requirements

- Valid Twitter account with permission to create or join DM groups
- Ability to invite other users to a DM group (up to 150 members)
- No elevated privileges needed; standard user account suffices

## Detailed Attack Procedures

### Step 1: Create DM Group with XSS Payload
procedure: [[procedures/Create-Twitter-DM-Group-with-XSS-Payload]]

**Objective**: Establish a DM group with a malicious payload in the name to store the XSS for later execution.

**Instructions**: Log in to Twitter, navigate to Messages, create a new group DM, and set the name to an XSS payload such as `<script>alert(1);//`. Invite at least one other user to the group.

**Expected Output**: Group created successfully; payload stored in the group name without sanitization.

**Success Indicators**:
- Group appears in DM list with the payload name
- No errors during creation

### Step 2: Trigger XSS via Tweet Sharing in DM
procedure: [[procedures/Trigger-XSS-via-Tweet-Sharing-in-DM]]

**Objective**: Cause the payload to execute when a victim interacts with the group by sharing a tweet.

**Instructions**: Have a victim (or simulate as another account) select a tweet, choose the DM option to share it to the vulnerable group. The group name renders unsanitized, executing the script.

**Expected Output**: JavaScript alert (or custom payload) pops up in the victim's browser.

**Success Indicators**:
- Payload executes on victim's side during share action
- Arbitrary JS runs in victim's session context

### Step 3: Trigger XSS via Recent Conversations Selection
procedure: [[procedures/Trigger-XSS-via-Recent-Conversations-Selection]]

**Objective**: Execute the payload through navigation in the DM interface without sharing content.

**Instructions**: Victim opens the DM dialog, clicks 'New message', views recent conversations, and selects the vulnerable group. The name renders and triggers the XSS.

**Expected Output**: Script execution upon group selection.

**Success Indicators**:
- Alert or payload effect visible when selecting group
- Execution occurs in DM UI rendering

### Step 4: Update Existing DM Group Name with XSS Payload
procedure: [[procedures/Update-Existing-DM-Group-Name-with-XSS-Payload]]

**Objective**: Extend the attack to large, existing groups by editing the name post-creation.

**Instructions**: As a group member, edit the group settings and change the name to the XSS payload. This affects all members immediately upon next interaction.

**Expected Output**: Name updated; subsequent triggers execute the new payload.

**Success Indicators**:
- Name change saved without validation
- Victims in group (e.g., 150 users) become vulnerable

## Attack Chain Summary

### Key Achievements

1. Stored XSS payload persists in group metadata, evading basic filters.
2. Multiple low-friction triggers (sharing, navigation) maximize execution opportunities.
3. Scalable to large groups via name edits, impacting non-technical users.
4. Enables session hijacking, data theft, or phishing in victim browsers.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
