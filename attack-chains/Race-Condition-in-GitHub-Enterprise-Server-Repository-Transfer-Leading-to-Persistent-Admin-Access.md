---
id: ac-github-race-transfer-persist-admin
tags:
  - race-condition
  - github-enterprise
  - access-bypass
  - privilege-escalation
  - persistence
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Persistence]]'
verified: false
platforms:
  - GitHub Enterprise Server
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-GitHub-Repository-Transfer-Race-Condition]]'
step_count: 2
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:30:18.756Z'
description: >-
  An attack chain exploiting a race condition in GitHub Enterprise Server's
  repository transfer process to add an outside collaborator and retain
  unauthorized admin access after transfer.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[T1078.004]]'
---
# Race Condition in GitHub Enterprise Server Repository Transfer Leading to Persistent Admin Access

Multi-stage attack chain demonstrating exploitation of a race condition during repository transfer in GitHub Enterprise Server, allowing an outside collaborator to gain and retain admin privileges post-transfer.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Repository Transfer] --> B[Exploit Race Condition]
    B --> C[Verify Persistent Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- GitHub account with collaborator access
- Access to repository settings

### Target Environment

- GitHub Enterprise Server (versions 3.8 and later)
- Repository with transfer capabilities enabled
- Admin privileges on source organization

### Initial Access Requirements

- Valid outside collaborator invitation or access
- Network access to GitHub Enterprise Server instance
- No prior transfer in progress

## Detailed Attack Procedures

### Step 1: Initiate Repository Transfer

**Objective**: Start the repository transfer process to create a window for the race condition.

**Instructions**: As an admin in the source organization, navigate to the repository settings and begin the transfer to a new owner organization. This action triggers the transfer workflow but does not complete it immediately, opening a timing window.

**Expected Output**: Transfer initiation confirmation, with the repository in a pending transfer state.

**Success Indicators**:
- Repository shows as transferring in the UI
- No immediate completion of transfer

### Step 2: Exploit Race Condition and Verify Access
procedure: [[procedures/Exploit-GitHub-Repository-Transfer-Race-Condition]]

**Objective**: Add an outside collaborator during the transfer window to bypass access controls and retain admin privileges after transfer completes.

**Instructions**: While the transfer is in progress, quickly add the target outside collaborator to the repository with admin permissions. Complete the transfer process. Post-transfer, confirm the collaborator retains admin access on the new owner's repository.

**Expected Output**: Collaborator listed with admin role in the transferred repository, able to perform admin actions like deleting branches or managing settings.

**Success Indicators**:
- Collaborator addition succeeds during transfer
- Persistent admin access confirmed after transfer completion
- Unauthorized control over repository settings

## Attack Chain Summary

### Key Achievements

1. Bypassed repository transfer restrictions via timing manipulation
2. Achieved persistent unauthorized admin access
3. Enabled ongoing control over transferred repository assets

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[T1078.004]] Cloud Accounts

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Persistence]] Persistence

---
*Last updated: 2023-10-01T00:00:00Z*
