---
type: procedure
tactics:
  - '[[tactics/Credential-Access|TA0006 - Credential Access]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Unsecured-Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[sub-techniques/Credentials-In-Files|T1552.001 - Credentials In Files]]'
tags:
  - '[[tags/EoP-Looting-for-passwords]]'
  - '[[tags/Powershell-History]]'
  - '[[tags/Windows-Privilege-Escalation]]'
commands:
  - '[[commands/set-psreadlineoption-disable-history-saving]]'
tools: []
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Windows-Privilege-Escalation-via-Powershell-History-Looting

## Summary

This procedure involves searching the PowerShell command history file for unsecured credentials, such as passwords passed as parameters in previous commands, to facilitate privilege escalation on a Windows system. By accessing the PSReadLine history log stored in the user's AppData directory, attackers can extract sensitive information that users may have inadvertently exposed through command-line usage.

## Description

PowerShell maintains a command history via the PSReadLine module, which logs executed commands to a plaintext file (typically ConsoleHost_history.txt) in the user's profile directory. This history can contain passwords or other credentials if users type them directly into commands like Connect-VPN or Set-Credential. With low-privilege access, an attacker can read this file, search for patterns indicating credentials (e.g., words like 'passw' or '-Password'), and use them for lateral movement or escalation. This technique targets environments where PowerShell is commonly used for administration, and history logging is enabled by default. Success depends on the target user having recently executed credential-exposed commands.

## Requirements

1. Low-privilege shell access on a Windows system (e.g., standard user account).
2. Ability to execute PowerShell commands without restrictions.
3. PowerShell version 5.0 or later with PSReadLine module installed (default on modern Windows).

## Defense

- Disable or limit PowerShell history logging via Group Policy or by setting HistorySaveStyle to SaveNothing.
- Implement PowerShell logging and monitoring (e.g., Module Logging, Script Block Logging) to detect history file access.
- Educate users on secure credential handling, such as using secure strings or credential managers instead of plaintext parameters.
- Regularly clear history files or use tools like PowerShell's Clear-History cmdlet.

## Objectives

1. Prevent future command history from being saved to avoid logging attacker actions.
2. Locate and extract the existing PowerShell command history file.
3. Search the history for credential patterns to obtain passwords for privilege escalation.

## Instructions

### Step 1: Disable Future History Saving

**Context**: Optionally disable the saving of command history to prevent your own reconnaissance commands from being logged in the history file, maintaining operational security during the escalation attempt.

**Command** ([[commands/set-psreadlineoption-disable-history-saving]]):
```powershell
Set-PSReadlineOption -HistorySaveStyle SaveNothing
```

> This PowerShell cmdlet configures the PSReadLine module to stop saving command history to disk. It takes effect immediately for the current session and future ones if persisted. No output is produced on success, but you can verify by running Get-PSReadlineOption and checking HistorySaveStyle.

### Step 2: Locate and Search PowerShell History File

**Context**: Retrieve the path to the history file using PSReadLine options, then display its contents and search for potential credentials. This step uses multiple paths to account for variations in user profiles or environment setups, ensuring the file is found even in non-standard configurations.

**Code** ([[codes/powershell-history-locator-and-searcher]]):
```powershell
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
type C:\Users\swissky\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
type $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
cat (Get-PSReadlineOption).HistorySavePath
cat (Get-PSReadlineOption).HistorySavePath | sls passw
```

> This multi-line snippet first attempts to display the history file using Windows-style (type with %userprofile%), a hardcoded example path, and environment variable-based paths to cover common locations. It then retrieves the exact history save path via Get-PSReadlineOption and pipes the contents to Select-String (sls) to grep for 'passw', highlighting potential password entries. Expected output includes the full command history log (a list of executed commands) and filtered lines containing credential-like patterns. If the file doesn't exist or is empty, no output will appear—indicating no history or logging disabled.
