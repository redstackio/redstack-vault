---
id: e1ea6186-0294-41bd-8074-3e01ed53e5f8
name: Enumerate Windows for Privilege Escalation (PowerUp)
type: procedure
verified: false
submitted: false
created_at: '2019-11-26T21:22:56.206129+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]'
- '[[File System Permissions Weakness|T1044 - File System Permissions Weakness]]'
- '[[Modify Existing Service|T1031 - Modify Existing Service]]'
- '[[Path Interception|T1034 - Path Interception]]'
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
- '[[Query Registry|T1012 - Query Registry]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
platforms:
- Windows
tags:
- '[[Misconfiguration]]'
- '[[Service Attacks]]'
commands:
- '[[PowerUp Enumerate for Privilege Escalation]]'
---

# Enumerate Windows for Privilege Escalation (PowerUp)

## Summary

Use the PowerUp PowerShell script to enumerate a Windows system for common vulnerabilities, including misconfigurations, vulnerable services, DLL hijacking opportunities, and vulnerable registry settings. 

## Description

# Description

Use the PowerUp PowerShell script to enumerate a Windows system for common vulnerabilities, including misconfigurations, vulnerable services, DLL hijacking opportunities, and vulnerable registry settings.

# Instructions

1. Download PowerUp from PowerSploit's dev branch: [Download from GitHub](https://github.com/PowerShellMafia/PowerSploit/blob/dev/Privesc/PowerUp.ps1)

2. Copy PowerUp.ps1 to the target

3. Import PowerUp.ps1 and run "Invoke-AllChecks"

**Command** ([[PowerUp Enumerate for Privilege Escalation]]):

```bash
Import-Module .\PowerUp.ps1;
Invoke-AllChecks
```

Parse results for instructions on exploiting the vulnerabilities.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]
- [[File System Permissions Weakness|T1044 - File System Permissions Weakness]]
- [[Modify Existing Service|T1031 - Modify Existing Service]]
- [[Path Interception|T1034 - Path Interception]]
- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]
- [[Query Registry|T1012 - Query Registry]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[PowerUp Enumerate for Privilege Escalation]]

## Tags

- [[Misconfiguration]]
- [[Service Attacks]]
