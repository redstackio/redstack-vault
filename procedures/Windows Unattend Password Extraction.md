---
id: 3151fe9c-208d-47bd-b244-9594fb802fb4
name: Windows Unattend Password Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.087769+00:00'
updated_at: '2023-04-10T20:37:39.314637+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Credentials in Files|T1081 - Credentials in Files]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Passwords in unattend.xml]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Decode base64 encoded password]]'
- '[[List of Unattend files]]'
- '[[Unattend File Enumeration]]'
---

# Windows Unattend Password Extraction

## Summary

Windows Unattend Password Extraction is a technique used to extract passwords from unattend.xml files. These files contain sensitive information such as usernames and passwords that are used during the Windows installation process. Attackers can use this technique to gain access to privileged accou

## Description

# Description

Windows Unattend Password Extraction is a technique used to extract passwords from unattend.xml files. These files contain sensitive information such as usernames and passwords that are used during the Windows installation process. Attackers can use this technique to gain access to privileged accounts and escalate their privileges. The technical process involves locating the unattend.xml files, decoding the credentials, and then using the extracted passwords to gain access to systems. The business value of this technique is that attackers can gain access to sensitive information and systems, which can lead to data theft and loss of intellectual property.

## Requirements

1. Access to the target system

1. Knowledge of the location of unattend.xml files

1. Ability to decode credentials

## Defense

1. Encrypt sensitive information in unattend.xml files

1. Restrict access to unattend.xml files

1. Use strong and unique passwords for all accounts

## Objectives

1. Extract passwords from unattend.xml files

1. Gain access to privileged accounts

1. Escalate privileges

# Instructions

1. Use this command to get the location of the unattend.xml files.

**Code**: [[C:\unattend.xml
C:\Windows\Panther\Unattend.xml
C:]]

> This command returns the file path of the unattend.xml files that are used during Windows installation. These files contain configuration settings that are applied during the installation process. The files can be located in different directories depending on the version of Windows and the installation method used. The returned file paths can be used to modify the configuration settings in the unattend.xml files.

**Command** ([[List of Unattend files]]):

```bash
C:\unattend.xml
C:\Windows\Panther\Unattend.xml
C:\Windows\Panther\Unattend\Unattend.xml
C:\Windows\system32\sysprep.inf
C:\Windows\system32\sysprep\sysprep.xml
```

2. This command lists all files with the names ending in sysprep.inf, sysprep.xml, unattended.xml, unattend.xml, and unattend.txt in the current directory and all subdirectories. The output is sent to the console, and any error messages are suppressed.

**Code**: [[dir /s *sysprep.inf *sysprep.xml *unattended.xml *]]

> This command is useful for finding system preparation files that may be used to automate the installation of Windows on multiple machines. These files contain configuration settings that are applied during the installation process, such as product keys, network settings, and user account information.

3. To configure Windows Autologon and create a new local user account, follow the instructions below:

1. Open Windows PowerShell as an administrator.
2. Copy and paste the code above into the PowerShell console.
3. Replace the values for 'Password' and 'Name' fields with your desired values.
4. Run the script by pressing Enter.
5. After the script has run, restart your computer to apply the changes.

**Code**: [[<component name="Microsoft-Windows-Shell-Setup" pu]]

> This command configures Windows Autologon and creates a new local user account. The 'AutoLogon' section specifies the username and password to use for automatic logon. The 'UserAccounts' section creates a new local user account with the specified name and password. The 'Group' field specifies which groups the new user account should be added to. This command can be useful for setting up a new computer or for automating the creation of user accounts on multiple computers.

4. To decode the unattend credentials, run the following command:

**Code**: [[$ echo "U2VjcmV0U2VjdXJlUGFzc3dvcmQxMjM0Kgo="  | b]]

> The "echo" command is used to print the base64 encoded string to the console. The "|" character is used to pipe the output of the "echo" command to the "base64" command, which decodes the base64 string. The decoded password is then printed to the console.

**Command** ([[Decode base64 encoded password]]):

```bash
$ echo "U2VjcmV0U2VjdXJlUGFzc3dvcmQxMjM0Kgo="  | base64 -d
```

5. To use this module, you need to have a Meterpreter session open on a Windows host. Once you have a session, simply load the module and execute it.

**Code**: [[post/windows/gather/enum_unattend]]

> This module is used to enumerate unattend.xml files on a Windows host. Unattend.xml files are used during the Windows installation process to automate the installation and configuration of the operating system. By enumerating these files, an attacker can potentially find sensitive information such as usernames, passwords, and other configuration details. The module takes several arguments, including the target IP address, the username and password to use for authentication, and the path to the directory where the unattend.xml files are located.

**Command** ([[Unattend File Enumeration]]):

```bash
Enumerating Unattend files...
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Credentials in Files|T1081 - Credentials in Files]]

## Commands Used

- [[Decode base64 encoded password]]
- [[List of Unattend files]]
- [[Unattend File Enumeration]]

## Tags

- [[EoP - Looting for passwords]]
- [[Passwords in unattend.xml]]
- [[Windows - Privilege Escalation]]
