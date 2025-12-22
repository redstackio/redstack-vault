---
type: procedure
description: >-
  Enumerate local user accounts on a Windows system using built-in commands for
  discovery of potential escalation targets.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Owner-User Discovery]]'
sub_techniques: []
tags:
  - enumeration
  - windows
platforms:
  - Windows
commands:
  - '[[commands/Net-User-List-Local-Accounts]]'
tools: []
validated: true
---

# List-Local-Users-on-Windows

## Summary

This procedure lists all local user accounts on a Windows machine using net user, identifying admins or weak accounts for privilege escalation.

## Description

Local users provide pivots in AD environments; enumerating them reveals non-domain accounts with potential weak passwords or elevated rights, useful post-WinRM access.

## Requirements

1. Shell access (local or remote via WinRM)
2. No elevated privileges needed for basic list
3. Net.exe available (built-in)
4. Target Windows 7+

## Defense

- Use domain accounts only; disable unused locals
- Rename default Administrator
- Enable LAPS for local admin password management
- Monitor net user executions (Process Creation logs)

## Objectives

1. Catalog local accounts
2. Spot potential targets
3. Check for admin group membership

## Instructions

### Step 1: Run Basic User List

**Context**: Net user displays all locals.

**Command** ([[commands/Net-User-List-Local-Accounts]]):
```command_prompt
net user
```

> Lists accounts. Expected: Administrator, Guest, etc.

### Step 2: Query Specific User Details

**Context**: For each, get more info like last logon.

**Command**:
```command_prompt
net user $_USERNAME
```

> Shows privileges, password age.

### Step 3: List Local Groups and Members

**Context**: Identify admins.

**Command**:
```command_prompt
net localgroup administrators
```

> Reveals members. Expected: Local admins listed.

### Step 4: Export for Analysis

**Context**: Save output.

**Command**:
```command_prompt
net user > users.txt
```

> Success: Accounts enumerated for targeting.
