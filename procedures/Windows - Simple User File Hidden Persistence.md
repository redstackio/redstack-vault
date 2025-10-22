---
id: 2747fb30-1416-46d5-b4d2-3b8e96a44137
name: Windows - Simple User File Hidden Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.749292+00:00'
updated_at: '2023-04-10T20:37:22.022270+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Hide Artifacts|T1564 - Hide Artifacts]]'
sub_techniques:
- '[[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]'
tags:
- '[[Simple User]]'
- '[[Windows - Persistence]]'
commands:
- '[[Hide autoexec.bat file]]'
---

# Windows - Simple User File Hidden Persistence

## Summary

This procedure involves setting a file as hidden in order to establish persistence on a Windows system. By setting the file as hidden, it can evade detection from basic file searches and provide a simple means of persistence for an attacker. This technique can be used to maintain access to a compro

## Description

# Description

This procedure involves setting a file as hidden in order to establish persistence on a Windows system. By setting the file as hidden, it can evade detection from basic file searches and provide a simple means of persistence for an attacker. This technique can be used to maintain access to a compromised system even after a reboot or other system changes. 

To execute this procedure, the attacker must first gain access to the system and identify a file that can be used for persistence. Once the file has been chosen, the attacker can use the 'Set File as Hidden' command to hide the file from view. This can be done either manually or through a script or tool. Once the file is hidden, it will remain on the system and can be executed at a later time to maintain access.

This technique can be valuable for an attacker looking to maintain a foothold on a compromised system, even after the initial point of entry has been secured. By establishing persistence, the attacker can continue to gather data, escalate privileges, and execute further attacks.

## Requirements

1. Access to the target Windows system

1. Ability to identify a file for persistence

## Defense

1. Regularly monitor for hidden files and directories on Windows systems

1. Implement file integrity monitoring to detect changes to critical files

1. Use endpoint detection and response (EDR) tools to detect and respond to suspicious activity on Windows systems

## Objectives

1. Establish persistence on a compromised Windows system

# Instructions

1. To set a file as hidden using the 'attrib' command, follow these steps:
1. Open PowerShell or Command Prompt.
2. Type 'attrib +h' followed by the file path and name.
3. Press Enter.

For example, to set the file 'autoexec.bat' as hidden in the 'C:' drive, you would type 'attrib +h c:\autoexec.bat' and press Enter.

**Code**: [[attrib +h c:\autoexec.bat]]

> The 'attrib' command is used to change the attributes of a file or folder. The '+h' argument sets the 'hidden' attribute of the file, making it invisible in file explorer unless the 'show hidden files' option is enabled. The file path and name should be specified after the '+h' argument.

**Command** ([[Hide autoexec.bat file]]):

```bash
attrib +h c:\autoexec.bat
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Hide Artifacts|T1564 - Hide Artifacts]]

### Sub-Techniques

- [[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]

## Commands Used

- [[Hide autoexec.bat file]]

## Tags

- [[Simple User]]
- [[Windows - Persistence]]
