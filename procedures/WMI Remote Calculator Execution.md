---
id: a6df01bd-c86e-4af6-96c4-1e060beef4fe
name: WMI Remote Calculator Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.258203+00:00'
updated_at: '2023-04-10T20:38:05.824805+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]'
tags:
- '[[Windows - Using credentials]]'
- '[[WMI Protocol]]'
commands:
- '[[Create process on remote machine]]'
---

# WMI Remote Calculator Execution

## Summary

WMI Remote Calculator Execution is a technique used by attackers to execute commands on a remote Windows machine. This technique utilizes the Windows Management Instrumentation (WMI) protocol to remotely execute commands on a target machine. Attackers can use this technique to execute various comma

## Description

# Description

WMI Remote Calculator Execution is a technique used by attackers to execute commands on a remote Windows machine. This technique utilizes the Windows Management Instrumentation (WMI) protocol to remotely execute commands on a target machine. Attackers can use this technique to execute various commands on a remote machine, such as launching a remote calculator. This technique can be used for lateral movement, privilege escalation, and data exfiltration. To execute this technique, an attacker needs to have valid credentials for the target machine.

Technical Explanation: WMI is a Windows management protocol that provides a standardized way for administrators to manage Windows systems. It allows administrators to remotely manage Windows systems by providing a set of APIs to interact with the operating system. The WMI protocol can be used to execute commands on a remote machine, such as launching a remote calculator. The 'wmic' command-line tool can be used to execute commands on a remote machine using the WMI protocol.

Business Value: This technique can be used by attackers to gain unauthorized access to sensitive data or systems. By using WMI to remotely execute commands, an attacker can move laterally within a network, escalate privileges, and exfiltrate data. Organizations should be aware of this technique and take appropriate measures to protect against it.

 

## Requirements

1. Valid credentials for the target machine

1. Access to the WMI protocol on the target machine

 

## Defense

1. Limit access to the WMI protocol to only authorized users

1. Monitor for suspicious WMI activity

1. Implement network segmentation to limit lateral movement

 

## Objectives

1. Execute commands on a remote Windows machine

1. Lateral movement within a network

1. Privilege escalation

1. Data exfiltration

 

# Instructions

1. To open Calculator remotely using WMIC, use the following command:

 



**Code**: [[PS C:\> wmic /node:target.domain /user:domain\user]]



> This command uses the Windows Management Instrumentation Command-line (WMIC) tool to remotely execute the Calculator application on a target computer. The /node parameter specifies the target computer, and the /user and /password parameters specify the credentials to use for authentication. The process call create command is used to create a new process on the remote computer, and the path to the Calculator executable is provided as an argument.



**Command** ([[Create process on remote machine]]):

```bash
wmic /node:target.domain /user:domain\user /password:password process call create "C:\Windows\System32\calc.exe”
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]

## Commands Used

- [[Create process on remote machine]]

## Tags

- [[Windows - Using credentials]]
- [[WMI Protocol]]


