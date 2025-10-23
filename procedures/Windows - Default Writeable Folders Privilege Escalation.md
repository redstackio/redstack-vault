---
id: fc41d0a3-fbf2-48b8-bea1-8df83b4d27ec
name: Windows - Default Writeable Folders Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.779353+00:00'
updated_at: '2023-04-10T20:37:32.626348+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[File Permissions Modification|T1222 - File Permissions Modification]]'
tags:
- '[[Default Writeable Folders]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[List of Directories]]'
---

# Windows - Default Writeable Folders Privilege Escalation

## Summary

Windows systems have a number of default folders that are writeable by users with limited privileges. Attackers can take advantage of this by modifying the permissions of these folders to grant themselves elevated privileges. By doing so, they can gain access to sensitive data, install malware, or 

## Description

# Description

Windows systems have a number of default folders that are writeable by users with limited privileges. Attackers can take advantage of this by modifying the permissions of these folders to grant themselves elevated privileges. By doing so, they can gain access to sensitive data, install malware, or perform other malicious actions. To escalate privileges, attackers may use techniques such as access token manipulation or modification of file and directory permissions.

From a technical perspective, this procedure involves identifying the default writeable folders on the target system and modifying their permissions to grant the attacker elevated privileges. This can be done using tools such as icacls or PowerShell commands.

The business value of this procedure is that it allows attackers to gain access to sensitive data, install malware, or perform other malicious actions that can have a significant impact on the target organization.

 

## Requirements

1. Access to a Windows system with default writeable folders

1. User account with limited privileges

1. Tools such as icacls or PowerShell commands

 

## Defense

1. Ensure that default writeable folders are properly secured and permissions are set to prevent unauthorized modification

1. Implement the principle of least privilege to limit the access of users and applications to sensitive data and systems

1. Monitor file and directory permissions for suspicious changes, and investigate any unauthorized modifications

 

## Objectives

1. Escalate privileges on the target system

1. Gain access to sensitive data or install malware

1. Perform other malicious actions on the target system

 

# Instructions

1. To list all the system directories, run the following command:

 



**Code**: [[C:\Windows\System32\Microsoft\Crypto\RSA\MachineKe]]



> This command lists all the system directories that are present in the Windows operating system. These directories contain important system files and configurations required for the smooth functioning of the operating system. The directories listed include directories for system tasks, temporary files, printer drivers, and much more.



**Command** ([[List of Directories]]):

```bash
C:\\Windows\\System32\\Microsoft\\Crypto\\RSA\\MachineKeys\nC:\\Windows\\System32\\spool\\drivers\\color\nC:\\Windows\\System32\\spool\\printers\nC:\\Windows\\System32\\spool\\servers\nC:\\Windows\\tracing\nC:\\Windows\\Temp\nC:\\Users\\Public\nC:\\Windows\\Tasks\nC:\\Windows\\System32\\tasks\nC:\\Windows\\SysWOW64\\tasks\nC:\\Windows\\System32\\tasks_migrated\\microsoft\\windows\\pls\\system\nC:\\Windows\\SysWOW64\\tasks\\microsoft\\windows\\pls\\system\nC:\\Windows\\debug\\wia\nC:\\Windows\\registration\\crmlog\nC:\\Windows\\System32\\com\\dmp\nC:\\Windows\\SysWOW64\\com\\dmp\nC:\\Windows\\System32\\fxstmp\nC:\\Windows\\SysWOW64\\fxstmp
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[File Permissions Modification|T1222 - File Permissions Modification]]

## Commands Used

- [[List of Directories]]

## Tags

- [[Default Writeable Folders]]
- [[Windows - Privilege Escalation]]


