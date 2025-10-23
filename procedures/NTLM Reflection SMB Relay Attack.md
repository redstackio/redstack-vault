---
id: 7e54e698-72b1-4682-8b3f-799caf3ba23e
name: NTLM Reflection SMB Relay Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.338754+00:00'
updated_at: '2023-04-10T20:26:13.118953+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[Domain Controller Authentication|T1556.001 - Domain Controller Authentication]]'
- '[[Golden Ticket|T1558.001 - Golden Ticket]]'
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Man-in-the-Middle attacks & relaying]]'
- '[[MS08-068 NTLM reflection]]'
commands:
- '[[Show Targets for SMB Relay Exploit]]'
---

# NTLM Reflection SMB Relay Attack

## Summary

The NTLM Reflection SMB Relay attack is a type of man-in-the-middle attack that allows an attacker to relay authentication attempts made using NTLM to another system. This attack exploits a vulnerability in the Microsoft Windows operating system (MS08-068) that allows an attacker to execute arbitra

## Description

# Description

The NTLM Reflection SMB Relay attack is a type of man-in-the-middle attack that allows an attacker to relay authentication attempts made using NTLM to another system. This attack exploits a vulnerability in the Microsoft Windows operating system (MS08-068) that allows an attacker to execute arbitrary code with SYSTEM privileges. The attacker can then use this access to compromise the target system and gain access to sensitive data.

To perform this attack, the attacker needs to intercept an authentication attempt made using NTLM and relay it to another system. The attacker can then use the compromised system to access sensitive data or execute commands on behalf of the user.

This attack can be used to gain access to sensitive information such as usernames and passwords, and can also be used to execute commands on behalf of the user. It is a powerful attack that can be used to compromise entire networks.

 

## Requirements

1. Access to the target network

1. Ability to intercept NTLM authentication attempts

1. SMB Relay Exploit tool

 

## Defense

1. Use Kerberos instead of NTLM for authentication

1. Disable NTLM authentication if possible

1. Use SMB signing to prevent SMB Relay attacks

 

## Objectives

1. Compromise user credentials

1. Gain access to sensitive data

1. Execute commands on behalf of the user

 

# Instructions

1. This command is used to exploit a vulnerability in the SMB protocol, allowing an attacker to relay authentication requests to another machine. This can result in gaining access to the targeted system or stealing sensitive information. To use this exploit, first load it in Metasploit using the 'use' command, followed by specifying the target using the 'set' command. Finally, run the exploit using the 'exploit' command.

 



**Code**: [[msf > use exploit/windows/smb/smb_relay
msf exploi]]



> The 'use' command is used to load a specific exploit module in Metasploit. The 'show targets' command is used to display the available targets for the loaded exploit. The vulnerability being exploited is a reflection vulnerability in the NTLM authentication protocol used by the SMB protocol. The exploit only works on Windows 2000 to Windows Server 2008 systems. The 'set' command is used to specify the target system and other required parameters for the exploit. The 'exploit' command is used to run the exploit and attempt to gain access to the targeted system.



**Command** ([[Show Targets for SMB Relay Exploit]]):

```bash
use exploit/windows/smb/smb_relay
show targets
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Modify Authentication Process|T1556 - Modify Authentication Process]]
- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[Domain Controller Authentication|T1556.001 - Domain Controller Authentication]]
- [[Golden Ticket|T1558.001 - Golden Ticket]]
- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[Show Targets for SMB Relay Exploit]]

## Tags

- [[Active Directory Attacks]]
- [[Man-in-the-Middle attacks & relaying]]
- [[MS08-068 NTLM reflection]]


