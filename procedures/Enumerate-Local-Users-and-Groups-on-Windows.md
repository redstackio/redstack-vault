---
id: d50f9ec5-ab44-4b8f-9dd0-c928c5362097
name: Enumerate-Local-Users-and-Groups-on-Windows
type: procedure
verified: true
submitted: true
created_at: '2020-03-20T20:55:41.162948+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Owner/User Discovery|T1033 - System Owner/User Discovery]]'
sub_techniques:
  - '[[.001]] Local Account'
platforms:
  - Windows
tags:
  - enumeration
  - operating-systems
  - security
commands:
  - '[[commands/net-user-list-local]]'
  - '[[commands/net-user-info-and-groups]]'
tools: []
validated: true
---

# Enumerate-Local-Users-and-Groups-on-Windows

## Summary

This procedure queries a Windows system via command line to list local users and retrieve account details including group memberships, aiding in privilege assessment.

## Description

Net user commands are built-in for user management and enumeration. From a remote shell (e.g., WinRM), they reveal local accounts, last logon, and groups like Administrators. Useful post-access to identify escalation paths. Works on domain members but focuses on local SIDs.

## Requirements

- Local or remote shell access (e.g., via WinRM)
- No elevated privileges needed for basic queries
- Command Prompt or PowerShell

## Defense

- Restrict net.exe usage via AppLocker
- Audit process creation for net.exe (Event ID 4688)
- Use LAPS for local admin passwords
- Monitor for enumeration patterns in logs

## Objectives

- List all local users
- Get user details and groups
- Identify privileged accounts

## Instructions

### Step 1: List All Local Users

**Context**: Retrieve a complete list of local accounts to scope targets.

**Command** ([[commands/net-user-list-local]]):
```command_prompt
net user
```

> Expected: Bullet list of users (e.g., Administrator, Guest). Why: Quick overview; pipe to file for offline analysis.

### Step 2: Query Specific User Details and Groups

**Context**: For interesting users (e.g., admins), get full info including memberships.

**Command** ([[commands/net-user-info-and-groups]]):
```command_prompt
net user $_TARGET_USER
```

> Replace $_TARGET_USER (e.g., Administrator). Expected: Account status, groups (*Administrators). Decision: If in privileged group, target for escalation.
