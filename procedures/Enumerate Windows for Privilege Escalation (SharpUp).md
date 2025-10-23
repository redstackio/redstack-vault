---
id: d998030b-fdcb-400c-9ea8-929cf9474587
name: Enumerate Windows for Privilege Escalation (SharpUp)
type: procedure
verified: false
submitted: false
created_at: '2020-03-13T18:30:55.970445+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[File System Permissions Weakness|T1044 - File System Permissions Weakness]]'
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
- '[[System Service Discovery|T1007 - System Service Discovery]]'
platforms:
- Windows
tags:
- '[[Enumeration]]'
commands:
- '[[PowerUp Enumerate for Privilege Escalation]]'
---

# Enumerate Windows for Privilege Escalation (SharpUp)

## Summary

Enumerate Windows systems for potential privilege escalations using SharpUp, a C# implementation of PowerUp. Scan for common privilege escalation paths, vulnerable servi ces, DLL hijacking opportunities, and vulnerable registry settings. 

## Description

# Description

Enumerate Windows systems for potential privilege escalations using SharpUp, a C# implementation of PowerUp. Scan for common privilege escalation paths, vulnerable servi ces, DLL hijacking opportunities, and vulnerable registry settings.



# Instructions





**Command** ([[PowerUp Enumerate for Privilege Escalation]]):

```bash
SharpUp.exe audit
```



Note: SharpUp also comes as a .ps1 script, which can be run from a PowerShell prompt with the same arguments.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[File System Permissions Weakness|T1044 - File System Permissions Weakness]]
- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]
- [[System Information Discovery|T1082 - System Information Discovery]]
- [[System Service Discovery|T1007 - System Service Discovery]]

## Commands Used

- [[PowerUp Enumerate for Privilege Escalation]]

## Tags

- [[Enumeration]]


