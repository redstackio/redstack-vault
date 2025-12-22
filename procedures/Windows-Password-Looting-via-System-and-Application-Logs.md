---
id: 35a01dc5-6dd7-4196-a2f8-f2dfe2f6b2ea
name: Windows-Password-Looting-via-System-and-Application-Logs
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.151925+00:00'
updated_at: '2023-04-10T20:37:32.977104+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques: []
tags:
  - EoP - Looting for passwords
  - Other files
  - Windows - Privilege Escalation
commands:
  - '[[commands/cmd-search-vnc-and-ultravnc-inis]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-Password-Looting-via-System-and-Application-Logs

## Summary

This procedure outlines how to search for and extract potentially unsecured credentials from Windows system and application logs, including event logs, registry hives, configuration files, and other artifacts that may contain plaintext or weakly protected passwords. It is useful during post-exploitation for credential dumping in privilege escalation scenarios, targeting files like pagefile.sys, NetSetup.log, SAM backups, and VNC configurations.

## Description

Windows systems often store sensitive information in logs and backup files accessible after privilege escalation. Attackers with local administrator access can loot these for weak or reused passwords, enabling lateral movement or further escalation. This involves manually inspecting or copying files from system directories, repair folders, and user profiles. Key targets include binary files like pagefile.sys (which may contain memory dumps with credentials), event log files (.Evt), registry hives (.sav), and config files like vnc.ini. Analysis may require additional tools like strings or hex editors to extract readable data. This technique aligns with scenarios where logs are not properly secured, such as in legacy systems or misconfigured environments.

## Requirements

1. Local administrator privileges on the target Windows system to access protected logs and system files.
2. Command-line access (CMD or PowerShell) for file enumeration and copying.
3. Sufficient disk space on the attacker's system to exfiltrate large files like pagefile.sys or event logs.
4. Optional: Tools like strings.exe or a hex editor for parsing binary files post-extraction.

## Defense

- Restrict access to log files and system directories using least privilege principles and AppLocker policies.
- Implement strong password policies to avoid weak or reused credentials in logs.
- Enable advanced auditing and monitor for unauthorized access to sensitive files via Event ID 4663 (file access).
- Regularly clear or rotate logs and use secure deletion for backups like .sav files.

## Objectives

1. Identify and collect log files and configurations containing potential credentials.
2. Extract readable passwords or hashes for reuse in lateral movement.
3. Analyze looted files to uncover weak security practices for further exploitation.

## Instructions

### Step 1: Locate and Copy Core System Log Files

**Context**: Begin by targeting system-level logs and backups that may contain credential artifacts from repairs, setups, or memory dumps. These files often require admin access and can be copied to a user-writable directory for exfiltration.

Navigate to the relevant directories and copy the files using built-in commands. Key locations include:

- `%SYSTEMDRIVE%\pagefile.sys` (virtual memory file potentially containing passwords)
- `%WINDIR%\debug\NetSetup.log` (network setup logs with possible creds)
- `%WINDIR%\repair\sam`, `%WINDIR%\repair\system`, `%WINDIR%\repair\software`, `%WINDIR%\repair\security` (registry backups with hashes)
- `%WINDIR%\system32\config\AppEvent.Evt`, `%WINDIR%\system32\config\SecEvent.Evt` (event logs)
- `%WINDIR%\system32\config\default.sav`, `%WINDIR%\system32\config\security.sav`, `%WINDIR%\system32\config\software.sav`, `%WINDIR%\system32\config\system.sav` (registry hive backups)
- `%WINDIR%\system32\CCM\logs\*.log` (SCCM logs if present)
- `%USERPROFILE%\ntuser.dat` (user registry hive)
- `%USERPROFILE%\LocalS~1\Tempor~1\Content.IE5\index.dat` (IE history with potential URLs/creds)
- `%WINDIR%\System32\drivers\etc\hosts` (hosts file for config)
- `C:\ProgramData\Configs\*` (app configs)
- `C:\Program Files\Windows PowerShell\*` (PowerShell configs)

Use `copy` or `xcopy` to stage them, e.g., `copy %SYSTEMDRIVE%\pagefile.sys C:\temp\loot\`.

**Expected Output**: Files copied to staging directory without access denied errors.

### Step 2: Search for VNC Configuration Files

**Context**: VNC tools often store passwords in plaintext in .ini files. Search the entire C: drive for these to uncover remote access credentials.

**Command** ([[commands/cmd-search-vnc-and-ultravnc-inis]]):

Execute the command to find VNC config files.

**Expected Output**: List of full paths to vnc.ini and ultravnc.ini files, e.g., `C:\Program Files\UltraVNC\ultravnc.ini`.

### Step 3: Extract and Analyze Looted Files

**Context**: Once files are staged, inspect them for credentials. For binary files like pagefile.sys or .Evt logs, use tools like `strings` to dump readable text; for .ini files, use `type` or a text editor.

For example, run `strings C:\temp\loot\pagefile.sys | findstr /i pass` to search for password strings.

**Expected Output**: Extracted strings containing potential credentials, such as "password=secret123" from .ini files or log entries with user creds.

> Post-exploitation tip: Exfiltrate files via SMB or HTTP, then parse offline with tools like RegRipper for hives or EVT parsers for logs.
