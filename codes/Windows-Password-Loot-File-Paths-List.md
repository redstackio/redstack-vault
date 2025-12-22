---
id: 6c4cae2d-7a71-4860-8c7c-8c607e3a5f27
name: Windows-Password-Loot-File-Paths-List
type: code
language: bat
verified: true
created_at: '2023-04-06T03:56:29.150229+00:00'
updated_at: '2023-04-10T20:37:33.011332+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - looting
  - file-list
validated: true
---

# Windows-Password-Loot-File-Paths-List

## Code

```bat
%SYSTEMDRIVE%\pagefile.sys
%WINDIR%\debug\NetSetup.log
%WINDIR%\repair\sam
%WINDIR%\repair\system
%WINDIR%\repair\software, %WINDIR%\repair\security
%WINDIR%\iis6.log
%WINDIR%\system32\config\AppEvent.Evt
%WINDIR%\system32\config\SecEvent.Evt
%WINDIR%\system32\config\default.sav
%WINDIR%\system32\config\security.sav
%WINDIR%\system32\config\software.sav
%WINDIR%\system32\config\system.sav
%WINDIR%\system32\CCM\logs\*.log
%USERPROFILE%\ntuser.dat
%USERPROFILE%\LocalS~1\Tempor~1\Content.IE5\index.dat
%WINDIR%\System32\drivers\etc\hosts
C:\ProgramData\Configs\*
C:\Program Files\Windows PowerShell\*
dir c:*vnc.ini /s /b
dir c:*ultravnc.ini /s /b
```

## Description

This batch code snippet provides a comprehensive list of file paths on a Windows system where unsecured credentials may be stored in logs, backups, and configurations. It includes paths to memory dumps, registry hives, event logs, and specific searches for VNC configs. Save as a .bat file and run with admin privileges to output or copy these files for analysis.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static list; no variables to substitute. Paths use environment variables like %WINDIR% for portability. | N/A |

## Usage

Execute in an elevated CMD prompt to list or redirect output to a file, e.g., `script.bat > loot_paths.txt`. Then manually copy files from the listed paths to a staging area for exfiltration. Useful in red team engagements after initial foothold for credential gathering.

## Detection

- Monitor for elevated CMD executions accessing system directories (Event ID 4688 with cmd.exe parent).
- File access audits on protected paths like %WINDIR%\repair\ or %WINDIR%\system32\config\ (Event ID 4663).
- Anomalous searches for .ini files or bulk file copies in user timelines.

## Related

- [[procedures/Windows-Password-Looting-via-System-and-Application-Logs]]
