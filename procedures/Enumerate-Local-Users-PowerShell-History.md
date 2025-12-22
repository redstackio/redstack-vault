---
id: d028a34c-3ab4-4e50-b9c2-5fd51ae5a7d0
name: Enumerate-Local-Users-PowerShell-History
type: procedure
verified: true
submitted: true
created_at: '2020-06-24T23:40:58.220763+00:00'
updated_at: '2023-05-25T19:59:39.474418+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
sub_techniques: []
tags:
  - '[[tags/data exposure]]'
  - '[[tags/Enumeration]]'
commands:
  - '[[commands/get-local-powershell-history-files]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enumerate-Local-Users-PowerShell-History

## Summary

This procedure retrieves and displays the PowerShell command history from all local user profiles on a Windows system. PowerShell history files, stored in user-specific directories, can reveal sensitive information such as executed commands, credentials, or administrative actions performed by other users, aiding in data collection during post-exploitation or discovery phases.

## Description

PowerShell maintains a history of executed commands in the ConsoleHost_history.txt file within each user's AppData directory, specifically under Roaming\Microsoft\Windows\PowerShell\PSReadLine. This procedure uses PowerShell cmdlets to recursively search for these files across all user profiles (C:\Users\*) and outputs their contents. It is particularly useful in scenarios where an attacker has gained initial access to a system and seeks to harvest artifacts left by other users, such as domain admin commands or installation scripts. The technique aligns with collecting data from the local system without requiring elevated privileges beyond read access to user directories, though administrative rights may be needed for protected profiles. Potential findings include password changes, file manipulations, or tool installations that inform further attack paths.

## Requirements

1. Execution on a Windows system with PowerShell available (version 5.0 or later recommended).
2. Read access to user profile directories (C:\Users\); local administrator privileges may be required for some protected profiles.
3. PowerShell execution policy allowing script execution (e.g., Unrestricted or Bypass).

## Defense

Defensive measures and detection strategies:

- Enable PowerShell logging (Module, Script Block, and Transcription) via Group Policy to capture command executions.
- Implement file integrity monitoring on user AppData directories to detect unauthorized reads.
- Use endpoint detection tools to alert on processes accessing multiple user history files, such as unusual Get-ChildItem patterns.
- Regularly clear or disable PowerShell history via PSReadLine module configuration (Set-PSReadLineOption -HistorySaveStyle SaveNothing).

## Objectives

1. Identify and extract command history from all local user accounts to uncover sensitive operations or credentials.
2. Analyze history for indicators of prior administrative actions or tool usage.
3. Collect data non-destructively for further reconnaissance without alerting the user.

## Instructions

### Step 1: Locate and Retrieve PowerShell History Files

**Context**: This step scans the default location for PowerShell history files across all user profiles and pipes the contents to the console for review. The wildcard (*) expands to all subdirectories under C:\Users, targeting the PSReadLine history file. This reveals commands run by other users, which could include credential manipulations or network operations.

**Command** ([[commands/get-local-powershell-history-files]]):
```powershell
Get-ChildItem -Path "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" | Get-Content
```

> This command first uses Get-ChildItem to find all matching history files and then Get-Content to display their contents. Run it from an elevated PowerShell prompt to ensure access to all profiles. Review the output for patterns like 'net user', 'choco install', or path navigations that indicate user activities. If no files are found, users may have disabled history or used different shells.
