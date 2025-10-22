---
id: 57582d72-35c3-461e-bac1-bd57f1a21e78
name: Windows Remote Management
type: sub-technique
mitre_id: T1021.006
mitre_url: null
created_at: '2023-04-06T00:31:26.213619+00:00'
updated_at: '2023-04-06T00:31:26.213619+00:00'
parent_technique: '[[Remote Services|T1021 - Remote Services]]'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[AWS SSM Command Execution - EC2 Shell Script]]'
- '[[Copying EC2 Instances using AMI Image in AWS]]'
- '[[Network Pivoting with sshuttle]]'
- '[[Ruby Bind Shell]]'
- '[[Windows - PowerShell Remoting Protocol with PSSESSION]]'
- '[[Windows - SMBExec with Impacket for Command Execution]]'
---

# Windows Remote Management

**MITRE ID**: T1021.006

**Parent Technique**: [[Remote Services|T1021 - Remote Services]]

This is a sub-technique of T1021 - Remote Services.

## Summary

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to interact with remote systems using Windows Remote Management (WinRM). The adversary may then perform actions as the logged-on user.

WinRM is the name of both a Windows service and a protocol that allows a user to int

## Description

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to interact with remote systems using Windows Remote Management (WinRM). The adversary may then perform actions as the logged-on user.

WinRM is the name of both a Windows service and a protocol that allows a user to interact with a remote system (e.g., run an executable, modify the Registry, modify services).(Citation: Microsoft WinRM) It may be called with the `winrm` command or by any number of programs such as PowerShell.(Citation: Jacobsen 2014) WinRM  can be used as a method of remotely interacting with [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047).(Citation: MSDN WMI)

## Tactics

This sub-technique is used in the following tactics:

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures

There are 6 procedures using this sub-technique:

- [[AWS SSM Command Execution - EC2 Shell Script]]
- [[Copying EC2 Instances using AMI Image in AWS]]
- [[Network Pivoting with sshuttle]]
- [[Ruby Bind Shell]]
- [[Windows - PowerShell Remoting Protocol with PSSESSION]]
- [[Windows - SMBExec with Impacket for Command Execution]]
