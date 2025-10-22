---
id: bc4e5b82-e7fa-4963-9886-5b21da1c3246
name: Windows - WMIExec with Impacket
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.964543+00:00'
updated_at: '2023-04-10T20:38:06.926822+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Valid Accounts|T1078 - Valid Accounts]]'
- '[[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]'
tags:
- '[[Impacket]]'
- '[[Windows - Using credentials]]'
- '[[WMIExec]]'
commands:
- '[[Share Command]]'
---

# Windows - WMIExec with Impacket

## Summary

WMIExec is a tool that allows for the execution of commands on a remote Windows machine using Windows Management Instrumentation (WMI). This can be particularly useful for lateral movement within a network, as it allows an attacker to execute commands on a remote machine without needing to authenti

## Description

# Description

WMIExec is a tool that allows for the execution of commands on a remote Windows machine using Windows Management Instrumentation (WMI). This can be particularly useful for lateral movement within a network, as it allows an attacker to execute commands on a remote machine without needing to authenticate to that machine. Impacket is a collection of Python classes for working with network protocols, which includes a version of WMIExec.

Technical Explanation: An attacker can use Impacket's WMIExec to execute commands on a remote Windows machine using WMI. This can be done without needing to authenticate to the remote machine, as long as the attacker has valid credentials for a user on the remote machine. The attacker can specify a share to redirect the output of the executed command to, allowing them to retrieve the output from the remote machine.

Business Value: An attacker can use WMIExec with Impacket to move laterally within a network and execute commands on remote machines, potentially allowing them to gain access to sensitive data or systems.

## Requirements

1. Valid credentials for a user on the remote machine

1. Access to a share on the remote machine to redirect output to

1. Impacket installed on the attacker's machine

## Defense

1. Limit user privileges to prevent attackers from obtaining valid credentials

1. Use network segmentation to limit lateral movement within a network

1. Monitor network traffic for signs of WMIExec or Impacket usage

## Objectives

1. Execute commands on a remote Windows machine

1. Lateral movement within a network

# Instructions

1. This command allows the user to specify a non-default share to be used in the operation.

**Code**: [[-share SHARE]]

> The '-share' argument is followed by the name of the share that the user wants to use. This is useful when the user wants to perform an operation on a specific share rather than the default share. For example, if the default share is 'public', but the user wants to perform an operation on a share called 'private', they can use this command with the argument '-share private'. This will ensure that the operation is performed on the 'private' share instead of the default 'public' share. 

**Command** ([[Share Command]]):

```bash
-share SHARE
```

2. This command allows the user to execute a command and redirect the output to the administrative share. The administrative share is a hidden network share that is created automatically by Windows on all computers. The share is used to allow administrators to remotely manage a computer. The command can be modified to redirect the output to a different location.

**Code**: [[cmd.exe /Q /c cd 1&gt; \\127.0.0.1\ADMIN$\__RANDOM]]

> The 'cd' command is used to change the current directory of the command prompt to the administrative share. The '1>' and '2>&1' are used to redirect the standard output and standard error of the command to the administrative share. The '\\127.0.0.1\ADMIN$\__RANDOM' is the path to the administrative share and '__RANDOM' is a randomly generated folder name that is created to prevent conflicts with other commands that may be using the administrative share at the same time.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Valid Accounts|T1078 - Valid Accounts]]
- [[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]

## Commands Used

- [[Share Command]]

## Tags

- [[Impacket]]
- [[Windows - Using credentials]]
- [[WMIExec]]
