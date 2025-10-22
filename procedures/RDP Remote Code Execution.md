---
id: ac52ca09-69db-4ac0-8329-3c465634f359
name: RDP Remote Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.079282+00:00'
updated_at: '2023-04-10T20:38:03.059185+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]'
- '[[Remote File Copy|T1105 - Remote File Copy]]'
tags:
- '[[RDP Remote Desktop Protocol]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Execute file.exe on target computer using SharpRDP]]'
- '[[Remote desktop connection to 10.10.10.10 with DOMAIN credentials and shared folder]]'
- '[[Remote desktop connection to 10.10.10.10 with local credentials and shared folder]]'
---

# RDP Remote Code Execution

## Summary

RDP Remote Code Execution is a technique used by attackers to gain access to a target machine by exploiting the Remote Desktop Protocol. Attackers can use stolen or brute-forced credentials to remotely connect to a machine via RDP and execute code on it. This technique can also be used to move late

## Description

# Description

RDP Remote Code Execution is a technique used by attackers to gain access to a target machine by exploiting the Remote Desktop Protocol. Attackers can use stolen or brute-forced credentials to remotely connect to a machine via RDP and execute code on it. This technique can also be used to move laterally within a network. The business value of this technique is that it allows attackers to gain access to a target machine without physically being present, and can be used to gain access to sensitive data or systems.

Technical Explanation: Attackers can use stolen or brute-forced credentials to remotely connect to a machine via RDP and execute code on it. This can be done by using the Remote Desktop Connection or FreeRDP tools. Once the attacker has access to the machine, they can use the Remote File Copy technique to move laterally within the network and access other machines.

## Requirements

1. Valid credentials for the target machine

1. Access to the network where the target machine is located

1. Remote Desktop Connection or FreeRDP tool

## Defense

1. Use strong, unique passwords and enable two-factor authentication for RDP access

1. Monitor for failed login attempts and anomalous RDP connections

1. Restrict RDP access to only necessary users and IP addresses

## Objectives

1. Gain access to a target machine

1. Execute code on a target machine

1. Move laterally within a network

# Instructions

1. The `rdesktop` command is used to remotely access a desktop environment of a remote system. The command can be used with the following arguments:
-d: Specifies the domain to use for authentication.
-u: Specifies the username to use for authentication.
-p: Specifies the password to use for authentication.
-g: Specifies the size of the remote desktop screen.
-r disk:share: Shares a local folder during the remote desktop session.

**Code**: [[root@payload$ rdesktop -d DOMAIN -u username -p pa]]

> To use the `rdesktop` command, specify the IP address of the remote system and the required arguments. The `-g` flag can be used to specify the size of the remote desktop screen, and the `-r disk:share` flag can be used to share a local folder during the remote desktop session. The `-d` flag can be used to specify the domain to use for authentication, and the `-u` and `-p` flags can be used to specify the username and password to use for authentication.

**Command** ([[Remote desktop connection to 10.10.10.10 with DOMAIN credentials and shared folder]]):

```bash
rdesktop -d DOMAIN -u username -p password 10.10.10.10 -g 70 -r disk:share=/home/user/myshare
```

**Command** ([[Remote desktop connection to 10.10.10.10 with local credentials and shared folder]]):

```bash
rdesktop -u username -p password -g 70% -r disk:share=/tmp/myshare 10.10.10.10
```

2. The `freerdp` command is used to remotely connect to a Windows machine using Remote Desktop Protocol (RDP).

**Code**: [[root@payload$ xfreerdp /v:10.0.0.1 /u:'Username' /]]

> This command can be used to connect to a remote Windows machine using RDP. The `/v` option specifies the IP address or hostname of the remote machine. The `/u` option specifies the username to use for authentication. The `/p` option specifies the password to use for authentication. The `+clipboard` option enables clipboard redirection. The `/cert-ignore` option ignores certificate errors. The `/size` option specifies the screen resolution of the remote desktop. The `/smart-sizing` option enables smart sizing. The `/d` option specifies the domain to use for authentication. The `/pth` option can be used to pass the hash for authentication using Restricted Admin mode. Note that this option requires an admin account that is not in the "Remote Desktop Users" group. This option works for Server 2012 R2 / Win 8.1+ and requires the freerdp2-x11 and freerdp2-shadow-x11 packages instead of freerdp-x11.

3. To execute a file remotely on a Windows machine using RDP, use SharpRDP.exe with the following parameters:

**Code**: [[PS C:\> SharpRDP.exe computername=target.domain co]]

> - `computername`: The target machine's hostname or IP address.
- `command`: The path to the file you want to execute remotely.
- `username`: The username of an account that has permission to log in to the target machine.
- `password`: The password for the specified user account.

**Command** ([[Execute file.exe on target computer using SharpRDP]]):

```bash
SharpRDP.exe computername=target.domain command="C:\Temp\file.exe" username=domain\user password=password
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]
- [[Remote File Copy|T1105 - Remote File Copy]]

## Commands Used

- [[Execute file.exe on target computer using SharpRDP]]
- [[Remote desktop connection to 10.10.10.10 with DOMAIN credentials and shared folder]]
- [[Remote desktop connection to 10.10.10.10 with local credentials and shared folder]]

## Tags

- [[RDP Remote Desktop Protocol]]
- [[Windows - Using credentials]]
