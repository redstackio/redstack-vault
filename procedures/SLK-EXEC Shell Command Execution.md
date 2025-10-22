---
id: 7a9bce08-c2a1-4972-86e4-f40f8157cacc
name: SLK-EXEC Shell Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.348526+00:00'
updated_at: '2023-04-10T20:36:58.711880+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Office - Attacks]]'
- '[[SLK - EXEC]]'
---

# SLK-EXEC Shell Command Execution

## Summary

SLK-EXEC Shell Command Execution is a technique used to execute arbitrary shell commands on a target system. This technique can be used to achieve various objectives such as gaining access to sensitive information, establishing persistence or executing further stages of an attack. By exploiting the

## Description

# Description

SLK-EXEC Shell Command Execution is a technique used to execute arbitrary shell commands on a target system. This technique can be used to achieve various objectives such as gaining access to sensitive information, establishing persistence or executing further stages of an attack. By exploiting the 'Execute Shell Command' command in SLK-EXEC, an attacker can execute arbitrary shell commands on a target system.

Technical Description: SLK-EXEC is a Microsoft Office add-in that allows users to execute custom code on a system. The 'Execute Shell Command' command can be used to execute arbitrary shell commands on a target system. This command can be used to achieve various objectives such as gaining access to sensitive information, establishing persistence or executing further stages of an attack.

Business Value: An attacker can use SLK-EXEC Shell Command Execution to gain access to sensitive information, establish persistence or execute further stages of an attack on a target system.

## Requirements

1. Access to a system with SLK-EXEC installed

1. Authentication on the target system

## Defense

1. Disable or restrict the use of SLK-EXEC in the enterprise environment

1. Monitor for the use of SLK-EXEC and other Office add-ins

1. Implement least privilege access control to limit the ability of users to execute arbitrary shell commands

## Objectives

1. Execute arbitrary shell commands on a target system

1. Gain access to sensitive information

1. Establish persistence

1. Execute further stages of an attack

# Instructions

1. To execute a shell command using this script, follow these steps:
1. Open the command prompt.
2. Navigate to the folder where the script is saved.
3. Type the name of the script file followed by the command you want to execute.
For example, if the script file is named 'shell.ps1' and you want to execute the 'dir' command, type the following command: 'shell.ps1 dir'.

**Code**: [[ID;P
O;E
NN;NAuto_open;ER101C1;KOut Flank;F
C;X1;Y]]

> This script allows you to execute shell commands from within PowerShell. The 'EEXEC' command is used to execute the shell command specified in the argument. The 'EHALT' command is used to stop the script from executing further. You can modify the 'c:\shell.cmd' argument to specify the path of the shell command you want to execute.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Tags

- [[Office - Attacks]]
- [[SLK - EXEC]]
