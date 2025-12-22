---
id: bef04dd5-50dc-4b20-b39b-b325e1ca9341
name: Create-Windows-SMB-Share-with-PowerShell
type: procedure
verified: true
submitted: false
created_at: '2020-03-27T22:21:14.939690+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Exfiltration]]'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
sub_techniques: []
tags:
  - file-transfer
  - Network
commands:
  - '[[commands/new-smbshare-create-share]]'
platforms:
  - Windows
tools: []
validated: true
---

# Create-Windows-SMB-Share-with-PowerShell

## Summary

This procedure outlines how to create a new SMB (Server Message Block) share on a Windows system using PowerShell. SMB shares enable file and printer sharing over a network, which can be leveraged in red team operations for data exfiltration by allowing remote access to specific directories with controlled permissions.

## Description

In offensive security scenarios, creating an SMB share allows attackers with local access to expose directories for remote file transfer without relying on external tools. This technique maps to MITRE ATT&CK's Exfiltration tactic (TA0010) and the Exfiltration Over Alternative Protocol technique (T1048), as it facilitates moving data out of a compromised environment via SMB protocol. The procedure requires administrative privileges on the target Windows machine and is typically used post-compromise to stage files for extraction. It assumes the attacker has already gained shell access via methods like credential dumping or lateral movement.

## Requirements

1. Administrative privileges on the Windows target (local or domain admin).
2. PowerShell execution policy allowing script execution (bypass if needed with Set-ExecutionPolicy).
3. A target directory or folder to share (local path on the system).
4. Network connectivity to the target for remote access testing post-creation.

## Defense

- Enable PowerShell logging and monitor for New-SmbShare cmdlet usage via Event ID 4104 in Windows Event Logs.
- Implement AppLocker or WDAC to restrict PowerShell execution to signed scripts.
- Use Group Policy to limit share creation to authorized users and audit SMB traffic with tools like Sysmon (filter for SMB-related events).
- Regularly review existing shares with Get-SmbShare and remove unauthorized ones.

## Objectives

1. Establish a network-accessible share for file exfiltration.
2. Grant full access to a specified user account for controlled remote access.
3. Verify share creation and accessibility without alerting defenders.

## Instructions

### Step 1: Identify or Create the Folder to Share

**Context**: Before creating the share, select or create a directory that contains the files to be exfiltrated or staged. This ensures the share points to relevant data without exposing the entire filesystem. Use PowerShell to navigate and create if needed.

**Command** (use built-in PowerShell cmdlets like New-Item):
```powershell
New-Item -Path "C:\Temp\SharedFolder" -ItemType Directory -Force
```

> This command creates a new directory at the specified path if it doesn't exist. Replace the path with your target location. Expected output: Confirmation message like "Directory 'C:\Temp\SharedFolder' created successfully" or no output if it already exists. Verify with Get-Item "C:\Temp\SharedFolder" to confirm the folder is present.

### Step 2: Create the SMB Share with Full Access

**Context**: Use the New-SmbShare cmdlet to define the share name, associate it with the folder path, and assign full permissions to a specific user. This step makes the folder accessible over SMB (ports 445/TCP) from remote systems. The share name is what remote clients will use to mount it (e.g., \\target\sharename).

**Command** ([[commands/new-smbshare-create-share]]):
```powershell
New-SmbShare -Name "$_NAME" -Path "$_PATH" -FullAccess "$_USERNAME"
```

> Substitute $_NAME with the desired share name (e.g., "ExfilShare"), $_PATH with the full folder path (e.g., "C:\Temp\SharedFolder"), and $_USERNAME with the target user (e.g., "attackeruser"). This grants read/write/delete permissions to the specified user. Expected output: A table displaying the new share details, including Name, ScopeName, Path, and Description. If the share already exists, it will error with "Share name is already in use"; delete it first with Remove-SmbShare if needed.

### Step 3: Verify Share Creation and Access

**Context**: Test the share locally and remotely to ensure it functions as intended. This confirms success and allows immediate use for exfiltration without further configuration.

**Command** (use Get-SmbShare and Test-Path):
```powershell
Get-SmbShare -Name "$_NAME"; Test-Path "\\localhost\$_NAME"
```

> Run Get-SmbShare to list the share and confirm its path and permissions. Then, test local access with Test-Path using the UNC path. Expected output for Get-SmbShare: Table showing the share with ScopeName "*", correct Path, and no Description (unless specified). Test-Path should return "True". For remote testing, from another machine: net use \\target-ip\$_NAME /user:$_USERNAME password, then dir \\target-ip\$_NAME to list files.
