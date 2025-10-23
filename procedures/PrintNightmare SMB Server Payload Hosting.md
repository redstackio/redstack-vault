---
id: 8dcb432a-ff23-4efd-8319-b199a11dd62b
name: PrintNightmare SMB Server Payload Hosting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:02.875983+00:00'
updated_at: '2023-04-10T20:25:52.007173+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Active Directory Attacks]]'
- '[[From CVE to SYSTEM shell on DC]]'
- '[[PrintNightmare]]'
commands:
- '[[Start SMB Server]]'
---

# PrintNightmare SMB Server Payload Hosting

## Summary

The PrintNightmare vulnerability allows an attacker to remotely execute code with SYSTEM level privileges on a Domain Controller (DC). This procedure involves hosting a malicious SMB server payload that can be used to exploit the PrintNightmare vulnerability. By exploiting this vulnerability, an at

## Description

# Description

The PrintNightmare vulnerability allows an attacker to remotely execute code with SYSTEM level privileges on a Domain Controller (DC). This procedure involves hosting a malicious SMB server payload that can be used to exploit the PrintNightmare vulnerability. By exploiting this vulnerability, an attacker can gain access to sensitive information stored within the Active Directory environment, including user credentials, and potentially move laterally to other systems. This attack can be devastating to an organization as it can lead to complete compromise of their Active Directory environment.

 

## Requirements

1. Access to a vulnerable system

1. Knowledge of the PrintNightmare vulnerability

1. Ability to host a malicious SMB server payload

 

## Defense

1. Ensure all systems are patched and up-to-date

1. Restrict access to sensitive systems and information to only authorized personnel

1. Monitor network traffic for any suspicious activity

 

## Objectives

1. Gain SYSTEM level access on a Domain Controller

1. Compromise Active Directory environment

1. Steal sensitive information

 

# Instructions

1. This command starts an SMB server that can be used to host payloads on a specified share directory (/tmp/smb/ in this case).

 



**Code**: [[python3 ./smbserver.py share /tmp/smb/]]



> The 'python3' command is used to execute the 'smbserver.py' script. The 'share' parameter specifies the name of the share that will be created on the SMB server. The '/tmp/smb/' parameter specifies the directory on the local file system that will be shared on the SMB server. This can be replaced with any other directory on the system. The SMB server can be used to host payloads that can be executed on a target system by exploiting vulnerabilities in the SMB protocol.



**Command** ([[Start SMB Server]]):

```bash
python3 ./smbserver.py share /tmp/smb/
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Start SMB Server]]

## Tags

- [[Active Directory Attacks]]
- [[From CVE to SYSTEM shell on DC]]
- [[PrintNightmare]]


