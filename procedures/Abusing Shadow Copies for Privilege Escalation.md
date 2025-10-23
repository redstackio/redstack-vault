---
id: 798ed535-73a6-4e7d-b1b3-04c41c2a56d4
name: Abusing Shadow Copies for Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.017370+00:00'
updated_at: '2023-04-10T20:37:37.792409+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
- '[[Inhibit System Recovery|T1490 - Inhibit System Recovery]]'
sub_techniques:
- '[[PowerShell Profile|T1546.013 - PowerShell Profile]]'
tags:
- '[[EoP - Abusing Shadow Copies]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[List shadow copies using diskshadow]]'
- '[[List shadow copies using vssadmin]]'
- '[[Make a symlink to the shadow copy and access it]]'
---

# Abusing Shadow Copies for Privilege Escalation

## Summary

Abusing Shadow Copies for Privilege Escalation is a technique used to escalate privileges on a Windows system by abusing the Shadow Copies feature. Shadow Copies are backups of files and folders created by the Volume Shadow Copy Service (VSS) and can be used to restore previous versions of files. T

## Description

# Description

Abusing Shadow Copies for Privilege Escalation is a technique used to escalate privileges on a Windows system by abusing the Shadow Copies feature. Shadow Copies are backups of files and folders created by the Volume Shadow Copy Service (VSS) and can be used to restore previous versions of files. This technique abuses the ability to restore previous versions of files to gain SYSTEM-level privileges. An attacker can use this technique to restore a previous version of a system file that is writable and then use it to execute arbitrary code with SYSTEM-level privileges.

This technique requires an attacker to have administrative privileges on the system. The attacker must also have access to the Shadow Copies and be able to restore a previous version of a system file.

 

## Requirements

1. Administrative privileges on the target system

1. Access to the Shadow Copies feature

 

## Defense

1. Enabling and enforcing the use of security tools such as antivirus and intrusion detection systems can help detect and prevent this type of attack.

1. Limiting the privileges of user accounts can help prevent attackers from being able to abuse the Shadow Copies feature.

1. Disabling the Shadow Copies feature can prevent attackers from being able to use this technique.

 

## Objectives

1. Escalate privileges on a Windows system

 

# Instructions

1. To list shadow copies using vssadmin, run the command 'vssadmin list shadows' in a PowerShell prompt with administrator access. To list shadow copies using diskshadow, run the command 'diskshadow list shadows all' in a PowerShell prompt with administrator access. To make a symlink to the shadow copy and access it, run the command 'mklink /d c:\shadowcopy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\' in a PowerShell prompt with administrator access.

 



**Code**: [[# List shadow copies using vssadmin (Needs Admnist]]



> Shadow copies are snapshots of the system state and can be used to restore data in case of an issue. However, they can also be used for privilege escalation by accessing sensitive data that may have been deleted or modified. The commands provided here can be used to list the available shadow copies and create a symlink to access them.



**Command** ([[List shadow copies using vssadmin]]):

```bash
vssadmin list shadows
```





**Command** ([[List shadow copies using diskshadow]]):

```bash
diskshadow list shadows all
```





**Command** ([[Make a symlink to the shadow copy and access it]]):

```bash
mklink /d c:\shadowcopy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\
```



## MITRE ATT&CK Mapping

### Tactics

- [[Impact|TA0040 - Impact]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Event Triggered Execution|T1546 - Event Triggered Execution]]
- [[Inhibit System Recovery|T1490 - Inhibit System Recovery]]

### Sub-Techniques

- [[PowerShell Profile|T1546.013 - PowerShell Profile]]

## Commands Used

- [[List shadow copies using diskshadow]]
- [[List shadow copies using vssadmin]]
- [[Make a symlink to the shadow copy and access it]]

## Tags

- [[EoP - Abusing Shadow Copies]]
- [[Windows - Privilege Escalation]]


