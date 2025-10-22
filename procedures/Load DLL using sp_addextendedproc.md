---
id: 9d926e7c-fe07-4fd8-8bb8-be1e0e6a6acb
name: Load DLL using sp_addextendedproc
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.339528+00:00'
updated_at: '2023-04-10T20:36:36.092476+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Add the extended stored procedure and list extended stored procedures]]'
- '[[Extended Stored Procedure]]'
- '[[MSSQL Server]]'
commands:
- '[[Drop xp_calc]]'
- '[[Execute xp_calc]]'
- '[[Load xp_calc.dll using sp_addextendedproc]]'
---

# Load DLL using sp_addextendedproc

## Summary

The 'Load DLL using sp_addextendedproc' procedure allows an attacker to load a custom DLL into memory and execute it within the context of the SQL Server process. This can be used to achieve persistence, privilege escalation, or to execute arbitrary code on the target system. To execute this proced

## Description

# Description

The 'Load DLL using sp_addextendedproc' procedure allows an attacker to load a custom DLL into memory and execute it within the context of the SQL Server process. This can be used to achieve persistence, privilege escalation, or to execute arbitrary code on the target system. To execute this procedure, an attacker must have administrative privileges on the SQL Server instance.

Technical Description: This procedure adds an extended stored procedure to the SQL Server instance, which loads a specified DLL into memory and executes it. The DLL must be located on the target system or accessible over the network. The DLL can be obfuscated to avoid detection by security software.

Business Value: An attacker can use this procedure to gain persistent access to the target system, escalate privileges, and execute arbitrary code. This can lead to data theft, system compromise, and disruption of business operations.

## Requirements

1. Administrative privileges on the SQL Server instance

1. Access to the DLL on the target system or network

## Defense

1. Restrict administrative privileges to trusted users only

1. Monitor for suspicious activity related to extended stored procedures

1. Use network segmentation to limit access to the SQL Server instance

## Objectives

1. Load a custom DLL into memory

1. Execute arbitrary code within the context of the SQL Server process

1. Achieve persistence or privilege escalation

# Instructions

1. Use the sp_addextendedproc command to load a DLL into SQL Server. The DLL can be located on the local file system or on a network share. Once the DLL is loaded, you can execute it using the xp_ prefix followed by the name of the DLL function. Finally, use sp_dropextendedproc to remove the DLL from SQL Server.

**Code**: [[-- can also be loaded from UNC path or Webdav
sp_a]]

> {'EXEC xp_calc': {'arguments': {}, 'description': 'Executes the xp_calc extended stored procedure.'}, 'sp_addextendedproc': {'arguments': {'name': 'The name of the extended stored procedure.', 'dll_path': 'The path to the DLL that contains the extended stored procedure.'}, 'description': 'Adds an extended stored procedure to SQL Server.'}, 'sp_dropextendedproc': {'arguments': {'name': 'The name of the extended stored procedure to remove.'}, 'description': 'Removes an extended stored procedure from SQL Server.'}}

**Command** ([[Load xp_calc.dll using sp_addextendedproc]]):

```bash
sp_addextendedproc 'xp_calc', 'C:\mydll\xp_calc.dll'
```

**Command** ([[Execute xp_calc]]):

```bash
EXEC xp_calc
```

**Command** ([[Drop xp_calc]]):

```bash
sp_dropextendedproc 'xp_calc'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Commands Used

- [[Drop xp_calc]]
- [[Execute xp_calc]]
- [[Load xp_calc.dll using sp_addextendedproc]]

## Tags

- [[Add the extended stored procedure and list extended stored procedures]]
- [[Extended Stored Procedure]]
- [[MSSQL Server]]
