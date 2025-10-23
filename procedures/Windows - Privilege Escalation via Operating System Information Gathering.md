---
id: b2bfa237-6d31-49b4-8261-e2969187c51c
name: Windows - Privilege Escalation via Operating System Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.595982+00:00'
updated_at: '2023-04-10T20:37:36.279741+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Execution through API|T1106 - Execution through API]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Windows - Privilege Escalation]]'
- '[[Windows Version and Configuration]]'
commands:
- '[[Display Environment Variables]]'
- '[[Retrieve OS Name and Version]]'
---

# Windows - Privilege Escalation via Operating System Information Gathering

## Summary

Operating system information gathering is a critical step in the process of privilege escalation. Attackers can leverage the information gathered to identify vulnerabilities in the system and exploit them to elevate their privileges. This technique involves gathering information about the Windows v

## Description

# Description

Operating system information gathering is a critical step in the process of privilege escalation. Attackers can leverage the information gathered to identify vulnerabilities in the system and exploit them to elevate their privileges. This technique involves gathering information about the Windows version and configuration, operating system architecture, environment variables, and all drives present on the system. This information can then be used to identify vulnerabilities and weaknesses in the system that can be exploited to escalate privileges.

From a technical standpoint, this technique involves running commands to gather information about the system. The commands used in this technique include Operating System Information, Windows Updates Information, Operating System Architecture, List Environment Variables, and List All Drives.

The business value of this technique is that it allows attackers to gain access to sensitive data and resources that are only accessible to privileged users. This can result in significant financial losses, reputational damage, and legal penalties for the targeted organization.

 

## Requirements

1. Access to the target system

1. Privileged access to execute commands

1. Knowledge of Windows operating system commands

 

## Defense

1. Regularly update and patch the operating system to address vulnerabilities

1. Implement the principle of least privilege to limit the impact of privilege escalation attacks

1. Monitor system logs and network traffic for signs of suspicious activity

 

## Objectives

1. Gather information about the Windows version and configuration

1. Identify vulnerabilities and weaknesses in the system

1. Exploit vulnerabilities to elevate privileges

 

# Instructions

1. To retrieve the Operating System Name and Version, run the following command in PowerShell:

 



**Code**: [[systeminfo | findstr /B /C:"OS Name" /C:"OS Versio]]



> This command retrieves information about the operating system installed on the computer. The 'systeminfo' command displays a lot of information about the system, but by piping it to 'findstr', we can filter the output to only show the 'OS Name' and 'OS Version' fields. The '/B' switch in 'findstr' specifies that the search should be performed at the beginning of each line, and the '/C' switch specifies the string to be searched for. This command can be useful when troubleshooting or verifying the operating system version on a remote computer.



**Command** ([[Retrieve OS Name and Version]]):

```bash
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```



2. This command extracts information about the installed Windows updates and patches.

 



**Code**: [[wmic qfe]]



> The 'wmic qfe' command is used to extract information about the installed Windows updates and patches. It provides details such as the update ID, installed on date, description, and the hotfix ID. This information can be useful in troubleshooting issues related to Windows updates and helps in keeping the system up-to-date with the latest patches and updates.

3. To retrieve the architecture of the operating system, run the following command:

 



**Code**: [[wmic os get osarchitecture || echo %PROCESSOR_ARCH]]



> The command uses the Windows Management Instrumentation Command-line (WMIC) utility to get the architecture of the operating system. If WMIC is not available, the command falls back to using the %PROCESSOR_ARCHITECTURE% environment variable to get the architecture. The architecture can be either 32-bit or 64-bit.

4. To list all environment variables, run the following commands in PowerShell:
1. set
2. Get-ChildItem Env: | ft Key,Value

 



**Code**: [[set
Get-ChildItem Env: | ft Key,Value]]



> The 'set' command is used to display all environment variables in the current session. The 'Get-ChildItem Env:' command is used to retrieve all environment variables and the 'ft Key,Value' argument formats the output in a table with the columns 'Key' and 'Value'.



**Command** ([[Display Environment Variables]]):

```bash
Get-ChildItem Env: | ft Key,Value
```



5. This command will list all the drives that are currently available on the system. It will display the drive letter, description, and provider name. The command can be executed in PowerShell or Command Prompt.

 



**Code**: [[wmic logicaldisk get caption || fsutil fsinfo driv]]



> This command uses multiple commands to achieve the desired result. The first command 'wmic logicaldisk get caption || fsutil fsinfo drives' will list all the available drives on the system. The second command 'wmic logicaldisk get caption,description,providername' will display the drive letter, description, and provider name. The last command 'Get-PSDrive | where {$_.Provider -like "Microsoft.PowerShell.Core\FileSystem"}| ft Name,Root' will display the name and root of all the drives that are currently available on the system. The command can be executed in PowerShell or Command Prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Execution through API|T1106 - Execution through API]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Display Environment Variables]]
- [[Retrieve OS Name and Version]]

## Tags

- [[Windows - Privilege Escalation]]
- [[Windows Version and Configuration]]


