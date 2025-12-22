---
id: ac-nextcloud-priv-esc-storage-mask
tags:
  - nextcloud
  - privilege-escalation
  - external-storage
  - masking
  - sftp
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
  - Nextcloud
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Conflicting-External-Storage-Mount]]'
  - '[[procedures/Share-Conflicting-Storage-with-Group]]'
  - '[[procedures/Verify-Masking-on-Victim]]'
step_count: 4
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:29:19.894Z'
description: >-
  A non-privileged user escalates privileges in Nextcloud 10.0 by creating and
  sharing an external storage mount with the same name as an admin-shared one,
  masking the admin's resources for group members.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[External Remote Services]]'
---
# Nextcloud 10.0 Privilege Escalation via Conflicting External Storage Mounts

Multi-stage attack chain demonstrating a complete attack workflow in Nextcloud 10.0, where a non-privileged user masks admin-shared external storage to override group resources.

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
    A[Admin Shares Storage] --> B[Attacker Creates Conflicting Mount]
    B --> C[Attacker Shares Conflicting Mount]
    C --> D[Victim Accesses Masked Storage]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Nextcloud web interface access

### Target Environment

- Nextcloud 10.0 instance
- External storage support enabled (Local and SFTP)
- Group with admin, attacker, and victim users

### Initial Access Requirements

- Valid non-privileged user account in the target group
- Admin has shared an external storage with the group
- Network access to Nextcloud UI

## Detailed Attack Procedures

### Step 1: Admin Creates and Shares External Storage

**Objective**: Establish the baseline admin-shared resource that will be masked.

**Instructions**: As admin, log into Nextcloud UI, navigate to Settings > External Storages, create a new local storage named 'localstrg' mounted at '/', with no authentication, enable sharing, and share it with the group 'samplegroup'.

**Expected Output**: Storage 'localstrg' visible and shared to group members.

**Success Indicators**:
- Group members can access admin's 'localstrg' files
- No conflicts yet

### Step 2: Create Conflicting External Storage Mount

procedure: [[procedures/Create-Conflicting-External-Storage-Mount]]

**Objective**: Attacker sets up a conflicting SFTP storage with the same name to override the admin's mount.

**Instructions**: Log in as attacker via Nextcloud UI, go to Settings > External Storages, add new SFTP storage named 'localstrg', configure host, root, username, and password for an attacker-controlled SFTP server, enable sharing.

**Expected Output**: New 'localstrg' SFTP mount created without errors.

**Success Indicators**:
- Attacker's SFTP storage is mounted successfully
- Name matches admin's exactly

### Step 3: Share Conflicting Storage with Group

procedure: [[procedures/Share-Conflicting-Storage-with-Group]]

**Objective**: Propagate the masked storage to group members, overriding the admin's share.

**Instructions**: In Nextcloud UI, select the new 'localstrg' SFTP storage and share it with the group 'samplegroup' containing admin, attacker, and victim.

**Expected Output**: Share confirmation; group members now see the shared SFTP storage.

**Success Indicators**:
- Share link or notification sent to group
- No permission errors

### Step 4: Verify Masking on Victim

procedure: [[procedures/Verify-Masking-on-Victim]]

**Objective**: Confirm the privilege escalation by checking that victim sees only attacker's files.

**Instructions**: Log in as victim, navigate to Files > 'localstrg'; observe that only files from attacker's SFTP are visible, masking admin's original content.

**Expected Output**: Victim's view shows attacker-controlled files exclusively.

**Success Indicators**:
- Admin's files hidden
- Attacker's SFTP content displayed to victim

## Attack Chain Summary

### Key Achievements

1. Non-privileged user overrides admin-shared resources
2. Group members exposed to attacker-controlled content
3. Potential for hiding legitimate files or injecting malicious ones

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[External Remote Services]] External Remote Services

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
