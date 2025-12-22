---
id: 1d31852e-9372-4dd9-8b3b-324d56aa1ae0
name: >-
  Abusing Group Policy Objects with StandIn to Manage Local Administrators and
  User Rights
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.753525+00:00'
updated_at: '2023-04-10T20:25:53.868787+00:00'
tactics:
  - '[[Defense Evasion]]'
  - '[[Impact]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[Data Destruction]]'
  - '[[Group Policy Modification]]'
sub_techniques: []
tags:
  - abuse-gpo-standin
  - active-directory-attacks
  - exploit-gpo
commands:
  - '[[commands/add-local-administrator-with-standin]]'
  - '[[commands/execute-custom-command-with-standin]]'
  - '[[commands/set-custom-user-rights-with-standin]]'
platforms:
  - Windows
  - Active Directory
tools: []
validated: true
---

# Abusing Group Policy Objects with StandIn to Manage Local Administrators and User Rights

## Summary

Abusing Group Policy Objects (GPO) with StandIn is a technique used to escalate privileges and maintain persistence in an Active Directory environment. This procedure involves modifying existing GPOs or creating new ones to add malicious scripts or commands that give an attacker the ability to manage local administrators and user rights on targeted machines.

## Description

Abusing Group Policy Objects (GPO) with StandIn is a technique used to escalate privileges and maintain persistence in an Active Directory environment. This technique involves modifying existing GPOs or creating new ones to add malicious scripts or commands that give an attacker the ability to manage local administrators and user rights on targeted machines. This attack can be carried out by an attacker with access to the Active Directory environment and knowledge of GPOs. The business value of this technique is that it allows an attacker to gain and maintain access to sensitive data and systems within the target environment. StandIn simulates GPO modifications without directly altering them, allowing for testing and evasion of detection.

## Requirements

1. Access to the Active Directory environment with domain credentials.
2. Knowledge of existing GPOs and their filters.
3. Authentication credentials with sufficient privileges to execute StandIn (e.g., domain admin or equivalent).
4. StandIn.exe tool installed on the attacker's machine.

## Defense

Defensive measures and detection strategies:

- Regularly review and audit GPOs for any unauthorized modifications using tools like PowerShell's Get-GPOReport.
- Implement the principle of least privilege for user and computer accounts to limit who can modify GPOs.
- Use tools such as Microsoft's Local Administrator Password Solution (LAPS) to manage local administrator passwords and rotate them automatically.
- Monitor for anomalous scheduled tasks or user right assignments via Windows Event Logs (Event ID 4732, 4738).

## Objectives

1. Escalate privileges within the target environment by adding local administrators.
2. Maintain persistence in the target environment through custom user rights and scheduled tasks.
3. Gain access to sensitive data and systems by executing arbitrary commands via GPO abuse.

## Instructions

### Step 1: Add a Local Administrator via GPO

**Context**: This step uses StandIn to simulate adding a specified user as a local administrator on machines targeted by a GPO filter. This achieves privilege escalation by granting admin access without direct GPO edits, which helps evade detection.

**Command** ([[commands/add-local-administrator-with-standin]]):
```cmd
StandIn.exe --gpo --filter $_FILTER_NAME --localadmin $_USERNAME
```

> This command applies the local admin addition through the specified GPO filter. Replace $_FILTER_NAME with the GPO filter (e.g., 'Shards') and $_USERNAME with the target user (e.g., 'user002'). Expected output includes confirmation of the simulated modification and details on affected machines.

### Step 2: Set Custom User Rights

**Context**: Assign specific user rights (e.g., SeDebugPrivilege) to a user via GPO simulation. This step is useful for enabling advanced privileges needed for further exploitation, such as debugging or driver loading, while maintaining persistence.

**Command** ([[commands/set-custom-user-rights-with-standin]]):
```cmd
StandIn.exe --gpo --filter $_FILTER_NAME --setuserrights $_USERNAME --grant "$_RIGHTS"
```

> Execute this to grant the specified rights. Replace $_FILTER_NAME (e.g., 'Shards'), $_USERNAME (e.g., 'user002'), and $_RIGHTS (e.g., 'SeDebugPrivilege,SeLoadDriverPrivilege'). Success is indicated by output showing the rights applied to the user on filtered machines.

### Step 3: Execute a Custom Command

**Context**: Simulate the creation of a scheduled task via GPO to run arbitrary commands on target machines. This allows for remote code execution and persistence, such as deploying payloads or exfiltrating data.

**Command** ([[commands/execute-custom-command-with-standin]]):
```cmd
StandIn.exe --gpo --filter $_FILTER_NAME --tasktype $_TASK_TYPE --taskname $_TASK_NAME --author "$_AUTHOR" --command "$_COMMAND_PATH" --args "$_ARGUMENTS"
```

> This simulates a GPO-based scheduled task. Replace $_FILTER_NAME (e.g., 'Shards'), $_TASK_TYPE (e.g., 'computer'), $_TASK_NAME (e.g., 'Liber'), $_AUTHOR (e.g., 'REDHOOK\Administrator'), $_COMMAND_PATH (e.g., 'C:\I\do\the\thing.exe'), and $_ARGUMENTS (e.g., 'with args'). Expected output confirms task creation details and execution parameters.
