---
id: d295f636-6f56-4d71-b9ae-409f3588d43e
name: Active Directory User Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.189185+00:00'
updated_at: '2023-04-10T20:36:03.675988+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[Data Encrypted for Impact|T1486 - Data Encrypted for Impact]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[User Hunting]]'
commands:
- '[[Enumerate SMB Sessions]]'
- '[[Find computers with Domain Admin or specified user session]]'
- '[[Find computers with Domain Admin or specified user session in specific group]]'
- '[[Find computers with Domain Admin or specified user session stealthily]]'
- '[[List Connected Users]]'
---

# Active Directory User Enumeration

## Summary

Active Directory User Enumeration is a technique used to gather information about users in a target Active Directory environment. This technique can be used to identify potential targets for further attacks, such as password spraying or phishing. 

To perform user enumeration, an attacker can use t

## Description

# Description

Active Directory User Enumeration is a technique used to gather information about users in a target Active Directory environment. This technique can be used to identify potential targets for further attacks, such as password spraying or phishing. 

To perform user enumeration, an attacker can use tools like Enumerate SMB Sessions, List Active Users, or User Hunter. These tools can be used to gather information about users, such as their usernames, email addresses, and group memberships. 

The business value of this technique is that it allows an attacker to gain a better understanding of the target environment, which can help them plan more effective attacks.

 

## Requirements

1. Access to the target Active Directory environment

1. Credentials with sufficient permissions to perform user enumeration

1. Tools like Enumerate SMB Sessions, List Active Users, or User Hunter

 

## Defense

1. Implement account lockout policies to prevent password spraying attacks

1. Monitor and analyze network traffic for signs of user enumeration

1. Limit user access to sensitive information and systems

 

## Objectives

1. Identify potential targets for further attacks

1. Gather intelligence about the target Active Directory environment

 

# Instructions

1. Use the CrackMapExec tool to enumerate SMB sessions on the target network.

 



**Code**: [[cme smb 10.10.10.0/24 -u Administrator -p 'P@ssw0r]]



> This command uses the CrackMapExec tool to enumerate SMB sessions on the target network. The '-u' flag specifies the username to use for authentication, while the '-p' flag specifies the password. The '--sessions' flag tells the tool to enumerate the sessions. The output shows the IP addresses, ports, and names of the target machines, as well as the user associated with each session. This information can be useful for further network analysis and exploitation.



**Command** ([[Enumerate SMB Sessions]]):

```bash
cme smb 10.10.10.0/24 -u Administrator -p 'P@ssw0rd' --sessions
SMB         10.10.10.10    445    WIN-8OJFTLMU1IG  [+] Enumerated sessions
SMB         10.10.10.10    445    WIN-8OJFTLMU1IG  \\10.10.10.10            User:Administrator
```



2. To list all active users on the target system, run the following command:

impacket-smbclient [user]@[target_ip]
who

Replace [user] with a valid username and [target_ip] with the IP address of the target system.

 



**Code**: [[$ impacket-smbclient Administrator@10.10.10.10
# w]]



> The 'impacket-smbclient' command is used to interact with SMB/CIFS servers. The 'who' command is used to display information about all active users on the target system. By running this command, you can identify who is currently logged in to the system and potentially gain information that can be used to further exploit the system.



**Command** ([[List Connected Users]]):

```bash
$ impacket-smbclient Administrator@10.10.10.10
# who
host:  \\10.10.10.10, user: Administrator, active:     1, idle:     0
```



3. This command helps to find computers where a Domain Admin or a specified user has an active session. It can also be used to find computers where a particular group has an active session. There are three ways to use this command. The first one is to simply run the command without any arguments. This will show all the computers where a Domain Admin or a specified user has an active session. The second way is to use the -GroupName argument followed by the name of the group. This will show all the computers where the specified group has an active session. The third way is to use the -Stealth argument. This will make the command run in stealth mode where it will not generate any network traffic.

 



**Code**: [[# Find computers were a Domain Admin OR a specifie]]



> The Invoke-UserHunter command is part of the PowerView module in PowerShell. It is used to find computers where a Domain Admin or a specified user has an active session. This command can be used in various scenarios such as finding compromised accounts or identifying machines that are being used by a specific user or group. The command can be run in three different ways as explained in the instruction field.



**Command** ([[Find computers with Domain Admin or specified user session]]):

```bash
Invoke-UserHunter
```





**Command** ([[Find computers with Domain Admin or specified user session in specific group]]):

```bash
Invoke-UserHunter -GroupName "RDPUsers"
```





**Command** ([[Find computers with Domain Admin or specified user session stealthily]]):

```bash
Invoke-UserHunter -Stealth
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Impact|TA0040 - Impact]]

### Techniques

- [[Data Encrypted for Impact|T1486 - Data Encrypted for Impact]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]

## Commands Used

- [[Enumerate SMB Sessions]]
- [[Find computers with Domain Admin or specified user session]]
- [[Find computers with Domain Admin or specified user session in specific group]]
- [[Find computers with Domain Admin or specified user session stealthily]]
- [[List Connected Users]]

## Tags

- [[Active Directory Attacks]]
- [[User Hunting]]


