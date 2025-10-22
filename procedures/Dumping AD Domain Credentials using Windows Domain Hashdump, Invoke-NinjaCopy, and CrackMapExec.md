---
id: 019d9286-1588-469f-8b94-15fd7f3b43e9
name: Dumping AD Domain Credentials using Windows Domain Hashdump, Invoke-NinjaCopy,
  and CrackMapExec
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.998564+00:00'
updated_at: '2023-04-10T20:25:43.666133+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques:
- '[[LSA Secrets|T1003.004 - LSA Secrets]]'
- '[[NTDS|T1003.003 - NTDS]]'
- '[[Security Account Manager|T1003.002 - Security Account Manager]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Alternatives - modules]]'
- '[[Dumping AD Domain Credentials]]'
commands:
- '[[Copy NTDS.dit file using NinjaCopy tool]]'
- '[[Extract NTDS.dit using DRSUAPI]]'
- '[[Extract NTDS.dit using VSS]]'
---

# Dumping AD Domain Credentials using Windows Domain Hashdump, Invoke-NinjaCopy, and CrackMapExec

## Summary

Dumping AD Domain Credentials is a common technique used by attackers to obtain sensitive information such as usernames and passwords. This procedure involves using three different commands - Windows Domain Hashdump, Invoke-NinjaCopy, and CrackMapExec. Windows Domain Hashdump is used to dump the ha

## Description

# Description

Dumping AD Domain Credentials is a common technique used by attackers to obtain sensitive information such as usernames and passwords. This procedure involves using three different commands - Windows Domain Hashdump, Invoke-NinjaCopy, and CrackMapExec. Windows Domain Hashdump is used to dump the hashes from the local SAM database, while Invoke-NinjaCopy is used to copy the NTDS.dit file from the domain controller. CrackMapExec is used to enumerate the NTDS file and extract the password hashes. This technique can be used to gain access to other systems within the network and escalate privileges.

From a technical perspective, this procedure involves exploiting vulnerabilities within the Windows operating system to obtain sensitive information. The business value of this procedure is that it allows attackers to gain access to sensitive information and escalate privileges within the network.

## Requirements

1. Access to a domain controller

1. Authentication with valid credentials

1. PowerShell

1. CrackMapExec

## Defense

1. Implement strong password policies and enforce regular password changes

1. Implement multi-factor authentication

1. Monitor for suspicious activity such as unusual logins or failed login attempts

## Objectives

1. Gain access to sensitive information such as usernames and passwords

1. Escalate privileges within the network

# Instructions

1. This command allows you to gather the password hashes of all users in the domain controller. It uses the Windows Management Instrumentation (WMI) protocol to access the domain controller and extract the hashes.

**Code**: [[windows/gather/credentials/domain_hashdump]]

> The 'windows/gather/credentials/domain_hashdump' module is used to dump the password hashes of all users in the domain controller. This module requires administrative privileges on the target machine. The hashes can be used for offline cracking or for pass-the-hash attacks. The module can be configured to use different authentication methods and can also perform the hash dumping across multiple domain controllers. The output of this module is a list of username and hash pairs.

2. Use this command to copy the NTDS.dit file from the domain controller to a local destination.

**Code**: [[Invoke-NinjaCopy --path c:\windows\NTDS\ntds.dit -]]

> The 'Invoke-NinjaCopy' command is a part of the PowerSploit module that allows you to copy files from remote machines to a local destination. In this case, we are using it to copy the NTDS.dit file from the domain controller to a local destination. The '--path' argument specifies the path of the file that needs to be copied. The '--verbose' argument is used to provide detailed information about the copy process. The '--localdestination' argument specifies the local destination where the file needs to be copied. This command can be useful for forensic analysis or for extracting password hashes from the NTDS.dit file.

**Command** ([[Copy NTDS.dit file using NinjaCopy tool]]):

```bash
Invoke-NinjaCopy --path c:\windows\NTDS\ntds.dit --verbose --localdestination c:\ntds.dit
```

3. This command is used to enumerate the NTDS file from a remote SMB server using CrackMapExec. The command takes the IP address of the remote SMB server, the username and password of a valid user account on the server as arguments, and then uses either the vss or drsuapi method to extract the NTDS file.

**Code**: [[cme smb 10.10.0.202 -u username -p password --ntds]]

> - smb: Specifies that the target is a remote SMB server.
- 10.10.0.202: The IP address of the remote SMB server.
- -u: Specifies the username of a valid user account on the remote SMB server.
- username: The username of the valid user account.
- -p: Specifies the password of the valid user account on the remote SMB server.
- password: The password of the valid user account.
- --ntds vss: Extracts the NTDS file using the VSS method.
- --ntds drsuapi: Extracts the NTDS file using the DRSUAPI method.
- #default: Specifies the default method to extract the NTDS file if no method is specified.

**Command** ([[Extract NTDS.dit using VSS]]):

```bash
cme smb 10.10.0.202 -u username -p password --ntds vss
```

**Command** ([[Extract NTDS.dit using DRSUAPI]]):

```bash
cme smb 10.10.0.202 -u username -p password --ntds drsuapi #default
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

### Sub-Techniques

- [[LSA Secrets|T1003.004 - LSA Secrets]]
- [[NTDS|T1003.003 - NTDS]]
- [[Security Account Manager|T1003.002 - Security Account Manager]]

## Commands Used

- [[Copy NTDS.dit file using NinjaCopy tool]]
- [[Extract NTDS.dit using DRSUAPI]]
- [[Extract NTDS.dit using VSS]]

## Tags

- [[Active Directory Attacks]]
- [[Alternatives - modules]]
- [[Dumping AD Domain Credentials]]
