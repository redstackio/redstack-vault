---
id: b273656d-d1f6-4f88-8364-38d6d14081e5
name: Windows - Run Programs with Different Permissions using Runas Command
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.377881+00:00'
updated_at: '2023-04-10T20:38:03.428908+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Process Injection|T1055 - Process Injection]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
sub_techniques:
- '[[Dynamic-link Library Injection|T1055.001 - Dynamic-link Library Injection]]'
- '[[Scheduled Task|T1053.005 - Scheduled Task]]'
tags:
- '[[Other methods]]'
- '[[Runas as another user]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Run cmd.exe as DOMAIN\username with netonly]]'
- '[[Run cmd.exe as DOMAIN\username with netonly and no profile]]'
---

# Windows - Run Programs with Different Permissions using Runas Command

## Summary

This procedure involves using the Runas command in Windows to run programs with different permissions. This can be useful for privilege escalation or for running programs as a different user without logging out. The Runas command allows you to specify a different user account and password, and can 

## Description

# Description

This procedure involves using the Runas command in Windows to run programs with different permissions. This can be useful for privilege escalation or for running programs as a different user without logging out. The Runas command allows you to specify a different user account and password, and can be run from the command prompt or through a script.

From a technical perspective, the Runas command creates a new process with the specified user's security context. This allows the user to run programs with elevated privileges or as a different user without logging out. The business value of this procedure is that it allows users to perform tasks that require elevated privileges or access to resources that they would not normally have access to.


 

## Requirements

1. Valid user credentials for the target system

 

## Defense

1. Limit user access to only the resources they need to perform their job

1. Implement least privilege access control to limit the impact of potential privilege escalation

1. Monitor for suspicious command line activity, especially the use of the Runas command

 

## Objectives

1. Run programs with different permissions

1. Perform tasks that require elevated privileges

1. Access resources that the user would not normally have access to

 

# Instructions

1. To use the Runas command, open a Command Prompt window and type 'runas' followed by the command you want to run. You can specify different options such as /user and /netonly to run the program with different permissions.

 



**Code**: [[PS C:\> runas /netonly /user:DOMAIN\username "cmd.]]



> The /user option is used to specify the user account that the command should be run as. The syntax for this option is '/user:DOMAIN\username'. The /netonly option is used to specify that the user's current credentials should not be used to authenticate the user on the network. Instead, the specified user's credentials will be used. The /noprofil option is used to specify that the user's profile should not be loaded when the command is run. This can be useful when running commands that do not require access to the user's profile, as it can speed up the execution time of the command.



**Command** ([[Run cmd.exe as DOMAIN\username with netonly]]):

```bash
runas /netonly /user:DOMAIN\username "cmd.exe"
```





**Command** ([[Run cmd.exe as DOMAIN\username with netonly and no profile]]):

```bash
runas /noprofil /netonly /user:DOMAIN\username cmd.exe
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Process Injection|T1055 - Process Injection]]
- [[Scheduled Task|T1053 - Scheduled Task]]

### Sub-Techniques

- [[Dynamic-link Library Injection|T1055.001 - Dynamic-link Library Injection]]
- [[Scheduled Task|T1053.005 - Scheduled Task]]

## Commands Used

- [[Run cmd.exe as DOMAIN\username with netonly]]
- [[Run cmd.exe as DOMAIN\username with netonly and no profile]]

## Tags

- [[Other methods]]
- [[Runas as another user]]
- [[Windows - Using credentials]]


