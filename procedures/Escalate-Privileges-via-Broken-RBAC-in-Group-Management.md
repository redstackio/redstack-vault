---
id: proc-hackerone-rbac-escalation-001
tags:
  - rbac
  - privilege-escalation
  - hackerone
  - web
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:58.445Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Escalate Privileges via Broken RBAC in Group Management

## Summary

This procedure exploits inadequate access controls in HackerOne's team management system, allowing users with only 'Program' permission to access the group management page and self-escalate to 'Admin' by modifying group permissions, thereby gaining full administrative capabilities including report management, reward granting, and user invitations.

## Description

In HackerOne's Ruby on Rails-based platform, the group management functionality at /TEAM/groups lacks proper backend authorization checks, despite UI menus being hidden for non-admin users. An attacker with 'Program' permission can directly navigate to this endpoint, select their group, and assign elevated roles like 'Admin'. This leads to complete compromise of the team/program, as the escalated user can perform any administrative action. The vulnerability stems from frontend-backend desynchronization in RBAC enforcement.

## Requirements

1. Valid HackerOne account with 'Program' permission in the target team
2. Web browser access to the HackerOne dashboard
3. Knowledge of the team slug (e.g., 'TEAM') for URL construction
4. No additional tools required; uses native browser navigation

## Defense

Defensive measures and detection strategies:

- Implement consistent RBAC checks on backend endpoints, not just UI visibility
- Log and monitor unauthorized access attempts to admin endpoints like /groups
- Use role-based URL guards and audit permission changes in group management
- Enable anomaly detection for sudden permission escalations in user sessions

## Objectives

1. Gain unauthorized access to group management interface
2. Modify group permissions to escalate user role to Admin
3. Achieve full control over team functions like reports and rewards
4. Validate escalation by performing admin-only actions

## Instructions

### Step 1: Navigate to Group Management Page

**Context**: Directly access the hidden endpoint to bypass UI restrictions.

No command required; use browser URL bar:

```plaintext
https://hackerone.com/TEAM/groups
```

> The page loads, revealing group list despite lacking menu access. Expected output: Editable group interface.

### Step 2: Select User's Group

**Context**: Target the group containing the low-privilege user for editing.

Use the page's dropdown to select the current user's group.

> Group details load. Expected output: Permissions form visible.

### Step 3: Assign Admin Permissions

**Context**: Exploit editable permissions to escalate role.

In the permissions section, check 'Admin' and save changes.

> Permissions update. Expected output: Dashboard refresh shows new Admin menus.

### Step 4: Verify Escalation

**Context**: Confirm elevated access by testing admin features.

Navigate to reports or rewards sections.

> Successful access to previously restricted areas.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rbac
- privilege-escalation
- web
