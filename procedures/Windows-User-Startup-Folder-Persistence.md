---
id: c543cd82-3434-4376-a354-ef65467f5e6d
name: Windows-User-Startup-Folder-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.815561+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Boot or Logon Autostart Execution|T1547 - Boot or Logon
    Autostart Execution]]
sub_techniques:
  - >-
    [[sub-techniques/Registry Run Keys / Startup Folder|T1547.001 - Registry Run
    Keys / Startup Folder]]
tags:
  - '[[tags/Simple User]]'
  - '[[tags/Startup]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/powershell-create-startup-batch-file]]'
  - '[[commands/cmd-start-backdoor-executable]]'
  - '[[commands/sharpersist-add-startup-folder-persistence]]'
platforms:
  - Windows
tools:
  - '[[tools/SharPersist]]'
validated: true
---

# Windows-User-Startup-Folder-Persistence

## Summary

This procedure demonstrates how to achieve user-level persistence on a Windows system by placing a batch script in the user's Startup folder. The script executes a backdoor executable each time the user logs in, allowing attackers to maintain access without administrative privileges. It includes both a manual method using PowerShell and an automated method using the SharPersist tool.

## Description

The Startup folder in Windows is a user-specific location (%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup) where files are automatically executed upon user logon. Attackers with simple user access can create a batch file here containing commands to launch malicious payloads, such as a backdoor executable hidden in a temporary directory. This technique ensures persistence across reboots and logons for the affected user account. It is low-privilege, stealthy if the payload is obfuscated, and commonly used in post-exploitation scenarios to maintain a foothold. The procedure assumes the backdoor executable already exists on the system (e.g., dropped via prior execution). For automation, SharPersist can be used to manage persistence entries without manual file manipulation.

## Requirements

1. Local access to the target Windows system as the target user (no admin privileges needed).
2. A backdoor executable already present on the system (e.g., in %TEMP%).
3. PowerShell or Command Prompt access.
4. For the SharPersist method: The SharPersist executable downloaded and available in the current directory.

## Defense

- Monitor the Startup folder (%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup) for unauthorized batch or executable files using tools like Sysinternals Autoruns.
- Implement application whitelisting (e.g., AppLocker or WDAC) to block execution of unsigned scripts or executables from temp directories.
- Enable PowerShell logging and script block logging to detect creation of suspicious files.
- Use endpoint detection tools to alert on modifications to startup locations and anomalous process spawning at logon.

## Objectives

1. Establish persistence by automating backdoor execution on user logon.
2. Maintain access to the system for data exfiltration or further lateral movement.
3. Ensure the persistence mechanism is simple and evades basic detection.

## Instructions

### Step 1: Create Batch Script for Startup Persistence

**Context**: Manually create a batch file in the user's Startup folder that launches the backdoor executable in the background. This uses PowerShell to write the file atomically, ensuring it runs on every logon.

**Command** ([[commands/powershell-create-startup-batch-file]]):
```powershell
New-Item -Path "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\backdoor.bat" -ItemType File -Force -Value "start /b C:\Users\$env:USERNAME\AppData\Local\Temp\backdoor.exe"
```

> This command creates or overwrites backdoor.bat in the Startup folder with content that starts the backdoor.exe silently. The /b flag runs it without opening a new window. Verify by checking the file contents with Get-Content backdoor.bat or by logging off and on to test execution. Expected: File created successfully, no errors; the backdoor process spawns on logon.

### Step 2: Verify and Execute Backdoor Launch

**Context**: The batch script's core command launches the backdoor. Reference this for understanding the payload execution; it runs automatically but can be tested manually.

**Command** ([[commands/cmd-start-backdoor-executable]]):
```cmd
start /b C:\Users\%USERNAME%\AppData\Local\Temp\backdoor.exe
```

> This is the exact command embedded in the batch file. Run it manually to test the backdoor without relying on logon. Expected: Backdoor process starts in the background (check Task Manager for backdoor.exe); no visible window or errors.

**Code** ([[codes/windows-batch-startup-backdoor-script]]):

> The batch script content is preserved as a standalone code snippet for reuse in similar persistence scenarios.

### Step 3: Alternative - Add Persistence Using SharPersist Tool

**Context**: If SharPersist is available, use it to add a startup folder entry without manual file creation. This automates the process and supports removal (-m remove).

First, ensure [[tools/SharPersist]] is in your path or current directory.

**Command** ([[commands/sharpersist-add-startup-folder-persistence]]):
```powershell
SharPersist.exe -t startupfolder -c "C:\Windows\System32\cmd.exe" -a "/c C:\Users\%USERNAME%\AppData\Local\Temp\backdoor.exe" -f "backdoor-launcher" -m add
```

> This adds an entry to the Startup folder via SharPersist, executing the backdoor through cmd.exe to mimic legitimate behavior. Replace the -a argument with your payload path. Expected: Confirmation message like "Persistence added successfully"; verify in Startup folder for the created file or use Autoruns to list entries. To remove: Change -m to remove.
