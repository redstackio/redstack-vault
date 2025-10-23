---
id: 03b7977e-d7b6-4a64-a41b-61e90a648edb
name: DCOM ShellExecute Calculator Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.167035+00:00'
updated_at: '2023-04-10T20:25:47.007212+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Active Directory Attacks]]'
- '[[DCOM Exploitation]]'
- '[[DCOM via ShellExecute]]'
commands:
- '[[Execute Calculator]]'
---

# DCOM ShellExecute Calculator Execution

## Summary

DCOM ShellExecute Calculator Execution is a technique used to execute a remote process on a target machine via DCOM. This technique involves using the ShellExecute function to execute a command on a remote machine. By using this technique, an attacker can execute any command on the remote machine w

## Description

# Description

DCOM ShellExecute Calculator Execution is a technique used to execute a remote process on a target machine via DCOM. This technique involves using the ShellExecute function to execute a command on a remote machine. By using this technique, an attacker can execute any command on the remote machine with the same privileges as the user running the DCOM service. This technique can be used for lateral movement within a network or to execute commands on a compromised machine.

Technical Explanation: The attacker uses the DCOM protocol to remotely execute the ShellExecute function on the target machine. The ShellExecute function is used to execute a command on the remote machine. The attacker can use this technique to execute any command on the remote machine with the same privileges as the user running the DCOM service.

Business Value: This technique can be used to move laterally within a network and gain access to sensitive information. It can also be used to execute commands on a compromised machine, allowing the attacker to maintain access to the network.

 

## Requirements

1. Authenticated access to the target machine

1. DCOM service running on the target machine

1. ShellExecute function available on the target machine

 

## Defense

1. Disable DCOM if it is not required for business purposes

1. Limit the privileges of the user running the DCOM service

1. Use network segmentation to limit the impact of lateral movement

 

## Objectives

1. Execute a remote process on a target machine via DCOM

1. Lateral movement within a network

1. Execute commands on a compromised machine

 

# Instructions

1. This command opens the Windows Calculator. 

 



**Code**: [[$com = [Type]::GetTypeFromCLSID('9BA05972-F6A8-11C]]



> The command uses PowerShell to create an instance of the Windows Script Host Shell Object and then uses the ShellExecute method to run the 'cmd.exe' command with the '/c' switch followed by 'calc.exe' which opens the Calculator application. The fourth argument is set to $null and the last argument is set to 0 to indicate that the command should run hidden and not show any windows.



**Command** ([[Execute Calculator]]):

```bash
$com = [Type]::GetTypeFromCLSID('9BA05972-F6A8-11CF-A442-00A0C90A8F39',"10.10.10.1")
$obj = [System.Activator]::CreateInstance($com)
$item = $obj.Item()
$item.Document.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Commands Used

- [[Execute Calculator]]

## Tags

- [[Active Directory Attacks]]
- [[DCOM Exploitation]]
- [[DCOM via ShellExecute]]


