---
id: 6d912fe3-7ec1-4dbd-b62b-d35757268034
name: Windows - PowerShell Remoting Protocol with PSSESSION
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.151347+00:00'
updated_at: '2023-04-10T20:37:59.117240+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Remote Services|T1021 - Remote Services]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
- '[[Windows Remote Management|T1021.006 - Windows Remote Management]]'
tags:
- '[[Powershell PSSESSION]]'
- '[[Powershell Remoting Protocol]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Create new PSSession]]'
- '[[Enable PowerShell Remoting and Add Host to Trusted Hosts]]'
- '[[Execute scriptBlock on remote session]]'
- '[[Execute scriptBlock on remote session]]'
---

# Windows - PowerShell Remoting Protocol with PSSESSION

## Summary

PowerShell Remoting Protocol with PSSESSION allows an attacker to remotely execute PowerShell commands on a target machine. This technique requires valid credentials to authenticate to the target machine. An attacker can use this technique to perform various actions such as reconnaissance, lateral 

## Description

# Description

PowerShell Remoting Protocol with PSSESSION allows an attacker to remotely execute PowerShell commands on a target machine. This technique requires valid credentials to authenticate to the target machine. An attacker can use this technique to perform various actions such as reconnaissance, lateral movement, and data exfiltration. The PSSESSION command allows an attacker to establish a persistent connection to the target machine, which can be used for multiple commands. This technique is commonly used by attackers to evade detection by security controls as it leverages legitimate protocols and tools. Business value of this technique includes the ability to perform remote administration tasks and automate repetitive tasks across multiple machines.

 

## Requirements

1. Valid credentials to authenticate to the target machine

1. Remote PowerShell enabled on the target machine

1. Firewall rules allowing inbound traffic on port 5985 (HTTP) or 5986 (HTTPS)

 

## Defense

1. Ensure that all remote PowerShell sessions are authenticated and encrypted

1. Implement network segmentation to limit the scope of remote PowerShell sessions

1. Monitor for anomalous PowerShell activity such as suspicious commands, large data transfers, and unusual process spawning

 

## Objectives

1. Remotely execute PowerShell commands on a target machine

1. Establish a persistent connection to the target machine

1. Perform reconnaissance, lateral movement, and data exfiltration

 

# Instructions

1. This command enables PowerShell Remoting on the host machine. It starts the Windows Remote Management (WinRM) service and sets the trusted hosts list to allow remote connections. This command must be run with administrative privileges.

 



**Code**: [[Enable-PSRemoting -Force
net start winrm

# Add th]]



> The 'Enable-PSRemoting' cmdlet configures the computer to receive PowerShell remote commands. The '-Force' parameter suppresses the confirmation prompt. The 'net start winrm' command starts the WinRM service. The 'Set-Item' cmdlets add the machine to the trusted hosts list. The 'wsman:\localhost\client\trustedhosts *' command adds all hosts to the trusted hosts list. The 'WSMan:\localhost\Client\TrustedHosts -Value "10.10.10.10"' command adds a specific IP address to the trusted hosts list. This allows remote connections from that IP address.



**Command** ([[Enable PowerShell Remoting and Add Host to Trusted Hosts]]):

```bash
Enable-PSRemoting -Force
net start winrm

Set-Item wsman:\localhost\client\trustedhosts *
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "10.10.10.10"
```



2. To execute a single PowerShell command on a remote computer, use the Invoke-Command cmdlet. To execute multiple commands on multiple computers, separate the computer names with commas.

 



**Code**: [[PS> Invoke-Command -ComputerName DC -Credential $c]]



> The -ComputerName parameter specifies the name of the remote computer(s) on which to execute the command. The -Credential parameter specifies the user account to use for the connection. The -ScriptBlock parameter specifies the PowerShell script to execute on the remote computer(s). The -FilePath parameter specifies the path to a PowerShell script file to execute on the remote computer(s).

3. To interact with a remote computer via PowerShell session, follow the steps below:
1. Open PowerShell and run the command 'Enter-PSSession -computerName <computer_name>'
2. You will now be connected to the remote computer and can execute commands on it.
3. To execute a command on the remote computer, use the 'Invoke-Command' cmdlet with the '-Session' parameter and the script block containing the command(s) you want to run.
4. To disconnect from the remote computer, use the 'Exit-PSSession' cmdlet.

 



**Code**: [[PS> Enter-PSSession -computerName DC01
[DC01]: PS>]]



> This command allows you to establish a remote PowerShell session with a computer and execute commands on it. The 'Enter-PSSession' cmdlet is used to connect to the remote computer, and the 'Invoke-Command' cmdlet is used to execute commands on it. The '-Session' parameter of the 'Invoke-Command' cmdlet specifies the session to use for the command execution. The script block following the '-scriptBlock' parameter contains the commands to be executed on the remote computer. The 'Exit-PSSession' cmdlet is used to disconnect from the remote computer.



**Command** ([[Create new PSSession]]):

```bash
$Session = New-PSSession -ComputerName CLIENT1
```





**Command** ([[Execute scriptBlock on remote session]]):

```bash
Invoke-Command -Session $Session -scriptBlock { $test = 1 }
```





**Command** ([[Execute scriptBlock on remote session]]):

```bash
Invoke-Command -Session $Session -scriptBlock { $test }
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Remote Services|T1021 - Remote Services]]
- [[Valid Accounts|T1078 - Valid Accounts]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]
- [[Windows Remote Management|T1021.006 - Windows Remote Management]]

## Commands Used

- [[Create new PSSession]]
- [[Enable PowerShell Remoting and Add Host to Trusted Hosts]]
- [[Execute scriptBlock on remote session]]
- [[Execute scriptBlock on remote session]]

## Tags

- [[Powershell PSSESSION]]
- [[Powershell Remoting Protocol]]
- [[Windows - Using credentials]]


