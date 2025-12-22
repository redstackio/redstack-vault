---
type: procedure
description: >-
  This procedure demonstrates how to use UNC path injection to bypass access
  controls and read restricted files on a Windows system by leveraging
  administrative shares.
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - unc-bypass
  - directory-traversal
  - file-access
  - windows-exploitation
commands:
  - '[[commands/powershell-invoke-unc-file-read]]'
tools: []
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Bypass-Access-Controls-Using-UNC-Path-Injection

## Summary

This procedure exploits UNC path injection to access files on a Windows target that would otherwise be restricted, such as system files in protected directories. By injecting a UNC share pointing to localhost administrative shares (e.g., C$), attackers can bypass local access controls, read sensitive configuration files like win.ini, and potentially escalate reconnaissance or data exfiltration efforts.

## Description

UNC (Universal Naming Convention) path injection involves crafting file paths that reference Windows administrative shares via SMB, such as \\localhost\c$\path\to\file. This technique tricks applications or scripts into resolving the path through the SMB protocol, which may not enforce the same access controls as direct local file system access. It is particularly effective against software that processes user-supplied paths without proper validation, allowing directory traversal-like behavior to reach arbitrary files. In a typical scenario, an attacker with initial code execution on a Windows host (e.g., via a webshell or compromised application) can use PowerShell to invoke commands that read files through this method. Success depends on administrative shares being enabled (default on many systems) and the attacker having sufficient privileges to access the shares. This can lead to discovery of credentials, configurations, or other sensitive data, enabling further attacks like privilege escalation or lateral movement.

## Requirements

1. Code execution access on the target Windows system (e.g., via PowerShell or command prompt).
2. Administrative shares enabled on the target (e.g., C$, ADMIN$ shares accessible via SMB).
3. Network connectivity to localhost (loopback) or the target itself.
4. PowerShell execution policy allowing script execution (bypass if needed).

## Defense

Defensive measures and detection strategies:

- Disable unnecessary administrative shares using Group Policy or registry edits (e.g., set AutoShareServer to 0 in HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters).
- Implement application-level path validation to sanitize user inputs and block UNC paths (e.g., using whitelisting or regex to reject \\ patterns).
- Enable PowerShell logging (Module, ScriptBlock, and Transcription) to monitor suspicious Invoke-Expression calls and UNC resolutions.
- Use endpoint detection tools to alert on SMB connections to localhost or anomalous file reads from system directories.
- Regularly audit file access logs and restrict SMB share permissions to authenticated users only.

## Objectives

1. Gain unauthorized read access to restricted files on the target system.
2. Bypass local file system access controls using SMB redirection.
3. Evade detection by avoiding direct file system APIs that trigger security controls.
4. Collect sensitive data such as configuration files for further exploitation.

## Instructions

### Step 1: Verify Administrative Share Access

**Context**: Before attempting file reads, confirm that the target allows access to administrative shares like C$. This step ensures the UNC bypass technique is viable without triggering immediate failures.

**Command** ([[commands/powershell-invoke-unc-file-read]]):
```powershell
Invoke-Expression "cmd.exe /C dir \\\localhost\c$\windows"
```

> This command lists the contents of the Windows directory via the UNC path. If successful, it indicates shares are accessible. If it fails with access denied, administrative shares may be disabled or privileges insufficient—consider escalating privileges first.

**Expected Output**: A directory listing similar to:
```
 Volume in drive C is Windows
 Directory of \\localhost\c$\windows

04/06/2023  03:55 PM    <DIR>          addins
04/06/2023  03:55 PM    <DIR>          AppPatch
...
```

### Step 2: Read a Restricted File Using UNC Injection

**Context**: Once share access is confirmed, inject the UNC path to read a specific file, such as win.ini, which may contain legacy configuration data. This demonstrates the bypass for arbitrary file access.

**Command** ([[commands/powershell-invoke-unc-file-read]]):
```powershell
Invoke-Expression "cmd.exe /C type \\localhost\c$\windows\win.ini"
```

> The Invoke-Expression cmdlet executes the cmd.exe type command on the UNC path, redirecting file access through SMB to bypass direct local restrictions. Replace win.ini with the target file path (e.g., \\localhost\c$\windows\system32\config\SAM for credential data, if accessible).

**Expected Output**: The contents of the file, for example:
```
; for 16-bit app support
[fonts]
[extensions]
[files]
[Mail]
MAPI=1
```

**Success Indicators**:
- File contents are displayed without access denied errors.
- No SMB authentication prompts or failures occur.
