---
id: 64ee48bd-9b55-47a9-b00d-5b2b2830e211
name: DCOM ShellBrowserWindow Calculator Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.190088+00:00'
updated_at: '2023-04-10T20:25:47.349814+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Active Directory Attacks]]'
- '[[DCOM Exploitation]]'
- '[[DCOM via ShellBrowserWindow]]'
commands:
- '[[Open Calculator]]'
---

# DCOM ShellBrowserWindow Calculator Execution

## Summary

DCOM via ShellBrowserWindow is a technique used to execute arbitrary code on a remote Windows system by abusing the ShellWindows object. An attacker can exploit this vulnerability by sending a specially crafted message to the ShellWindows object that will execute the desired code on the target syst

## Description

# Description

DCOM via ShellBrowserWindow is a technique used to execute arbitrary code on a remote Windows system by abusing the ShellWindows object. An attacker can exploit this vulnerability by sending a specially crafted message to the ShellWindows object that will execute the desired code on the target system. This technique can be used to execute various payloads such as a calculator, a backdoor, or a ransomware. 

This technique is commonly used in Active Directory environments where the attacker has already gained access to a domain user account. The attacker can use this technique to move laterally across the network and gain access to other systems. 

The business value of this technique is that it allows the attacker to gain access to sensitive data, disrupt business operations, or cause financial losses.

 

## Requirements

1. Authenticated access to a domain user account

1. Ability to send a specially crafted message to the ShellWindows object

 

## Defense

1. Disable DCOM if it is not needed

1. Implement network segmentation to limit lateral movement

1. Monitor network traffic for signs of DCOM exploitation

 

## Objectives

1. Execute arbitrary code on a remote Windows system

1. Move laterally across the network

1. Gain access to sensitive data

 

# Instructions

1. This command executes the calculator on a Windows 10 machine. It uses a COM object to create an instance of the calculator and then executes it using the ShellExecute method.

 



**Code**: [[$com = [Type]::GetTypeFromCLSID('C08AFD90-F2A1-11D]]



> The command consists of the following steps:
1. Get the type of the COM object using the GetTypeFromCLSID method.
2. Create an instance of the COM object using the CreateInstance method.
3. Use the ShellExecute method of the Application property to execute the calculator. The first argument is the name of the executable, the second argument is the command line arguments, the third argument is the working directory, the fourth argument is the window style, and the fifth argument is the show command.

Note that this command only works on Windows 10 machines, and the COM object used doesn't exist in Windows 7.



**Command** ([[Open Calculator]]):

```bash
$com = [Type]::GetTypeFromCLSID('C08AFD90-F2A1-11D1-8455-00A0C91F3880',"10.10.10.1")
$obj = [System.Activator]::CreateInstance($com)
$obj.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Commands Used

- [[Open Calculator]]

## Tags

- [[Active Directory Attacks]]
- [[DCOM Exploitation]]
- [[DCOM via ShellBrowserWindow]]


