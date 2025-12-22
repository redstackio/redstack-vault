---
id: 770de051-9fcd-4885-ac01-2afbe6aa2212
type: procedure
verified: true
submitted: true
created_at: '2019-11-14T00:19:34.820853+00:00'
updated_at: '2023-05-25T19:55:55.881162+00:00'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Create Account]]'
sub_techniques: []
tags:
  - administrator
  - setup
commands:
  - '[[commands/windows-add-new-user]]'
  - '[[commands/windows-add-user-to-local-administrators-group]]'
platforms:
  - Windows
tools: []
validated: true
---

# Add-Local-Administrator-to-Windows

## Summary

This procedure creates a new local user account on a Windows system and adds it to the local Administrators group, providing persistent administrative access without relying on the built-in Administrator account. It is typically used after initial privilege escalation to establish backdoor access for future operations.

## Description

In post-exploitation scenarios, after gaining local administrator privileges through escalation techniques, creating a secondary administrator account enhances operational security by avoiding detection associated with the default Administrator account, which may be monitored or renamed. This procedure uses native Windows net commands executed in Command Prompt to add the user and grant administrative rights. It assumes the attacker has already achieved code execution as an administrator on the target Windows machine. The technique aligns with persistence strategies by embedding a new privileged account into the system's local user base.

## Requirements

1. Local administrator privileges on the target Windows system (achieved via prior privilege escalation).
2. Access to Command Prompt (cmd.exe) on the target.
3. No additional tools required; uses built-in Windows utilities.
4. Target must be a Windows operating system (e.g., Windows 10, Server 2019).

## Defense

Defensive measures include enabling advanced auditing for account management events (Event ID 4720 for user creation, 4732 for group additions), restricting net.exe usage via AppLocker or WDAC policies, and monitoring for anomalous local account creations through SIEM tools. User Account Control (UAC) and just-in-time administration can limit the impact of such accounts.

## Objectives

1. Create a new local user account with a known password.
2. Elevate the new user to the local Administrators group for full system control.
3. Establish persistence without alerting common monitoring for the default admin account.

## Instructions

### Step 1: Create New Local User

**Context**: This step adds a new user account to the local system using the net user command. Choose a username and password that blend with the environment to avoid detection; the password should meet complexity requirements if enforced.

**Command** ([[commands/windows-add-new-user]]):
```cmd
net user $_USERNAME $_PASSWORD /add
```

> This command creates the user with the specified password. Replace $_USERNAME with the desired account name (e.g., 'backupadmin') and $_PASSWORD with a secure password (e.g., 'P@ssw0rd123'). Success is indicated by the command completing without errors.

### Step 2: Add User to Local Administrators Group

**Context**: After user creation, this step grants the new account membership in the local Administrators group, providing elevated privileges. Verify the addition afterward using 'net localgroup Administrators' to confirm.

**Command** ([[commands/windows-add-user-to-local-administrators-group]]):
```cmd
net localgroup Administrators $_USERNAME /add
```

> This command appends the user to the Administrators group. Use the same $_USERNAME as in Step 1. Upon success, the user can log in with administrative rights, enabling remote access via tools like RDP or PsExec.
