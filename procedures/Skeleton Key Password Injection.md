---
id: 27b6a129-08b1-4a08-b180-2872824c6c17
name: Skeleton Key Password Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.308841+00:00'
updated_at: '2023-04-10T20:37:18.411594+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
tags:
- '[[Skeleton key]]'
- '[[Windows - Mimikatz]]'
commands:
- '[[Login to remote desktop]]'
- '[[Map share]]'
---

# Skeleton Key Password Injection

## Summary

Skeleton Key Password Injection is a technique used by attackers to inject a password into the memory of a Windows domain controller. This allows the attacker to bypass authentication and gain access to any account in the domain. The technique is often used in combination with Mimikatz, a post-expl

## Description

# Description

Skeleton Key Password Injection is a technique used by attackers to inject a password into the memory of a Windows domain controller. This allows the attacker to bypass authentication and gain access to any account in the domain. The technique is often used in combination with Mimikatz, a post-exploitation tool used for dumping credentials from Windows machines. By using Mimikatz to dump the domain controller's NTLM hash, the attacker can then use the Skeleton Key Password Injection technique to inject a new password into the domain controller's memory. This effectively gives the attacker unrestricted access to the domain and any resources within it.

From a technical perspective, Skeleton Key Password Injection works by exploiting a vulnerability in the domain controller's implementation of the Kerberos authentication protocol. The attacker sends a specially crafted authentication request to the domain controller, which causes it to load the attacker's password into memory. The attacker can then use this password to authenticate as any user in the domain. The business value of this attack is that it allows attackers to gain persistent access to a network and steal sensitive data over a longer period of time.

 

## Requirements

1. Access to a Windows domain controller

1. Mimikatz or similar post-exploitation tool

 

## Defense

1. Implement strong password policies to reduce the effectiveness of password-based attacks

1. Monitor network traffic for signs of Kerberos authentication abuse

1. Implement multi-factor authentication to make it more difficult for attackers to gain access to user accounts

 

## Objectives

1. Gain access to a Windows domain controller

1. Bypass authentication and gain access to any account in the domain

1. Steal sensitive data from the domain

 

# Instructions

1. To escalate privileges using Mimikatz, follow these steps:
1. Open PowerShell on the target machine.
2. Copy and paste the provided Mimikatz command in PowerShell.
3. Press Enter to execute the command.
4. Once the command is executed, a new drive letter P: will be mapped to the target machine's admin share.
5. Use the provided RDP command to login as a user with elevated privileges.

 



**Code**: [[privilege::debug
misc::skeleton
# map the share
ne]]



> The provided command uses Mimikatz to escalate privileges on the target machine. The 'privilege::debug' command is used to enable debug privileges for the current user. The 'misc::skeleton' command is used to load the Mimikatz Skeleton module which adds additional functionality to Mimikatz. The 'net use' command is used to map the target machine's admin share to a new drive letter P:. The '/user:john' parameter is used to specify the username 'john' which has administrative privileges on the target machine. The 'mimikatz' parameter is used to specify the password for the 'john' user. Finally, the 'rdesktop' command is used to connect to the target machine using RDP with the provided credentials.



**Command** ([[Map share]]):

```bash
net use p: \\WIN-PTELU2U07KG\admin$ /user:john mimikatz
```





**Command** ([[Login to remote desktop]]):

```bash
rdesktop 10.0.0.2:3389 -u test -p mimikatz -d pentestlab
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Pass the Hash|T1075 - Pass the Hash]]

## Commands Used

- [[Login to remote desktop]]
- [[Map share]]

## Tags

- [[Skeleton key]]
- [[Windows - Mimikatz]]


