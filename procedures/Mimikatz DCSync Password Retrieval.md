---
id: aa1dc5d8-cf23-4898-bb36-8aaf2d8b90fb
name: Mimikatz DCSync Password Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.043420+00:00'
updated_at: '2023-04-10T20:26:28.898523+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
- '[[Using Mimikatz DCSync]]'
commands:
- '[[DCSync all users for htb.local domain]]'
- '[[DCSync only one user for htb.local domain]]'
---

# Mimikatz DCSync Password Retrieval

## Summary

Mimikatz DCSync is a tool that can be used to retrieve password hashes for user accounts in an Active Directory domain. This tool can be used to dump credentials from the domain controller without being detected by most anti-virus software. Attackers can use these password hashes to perform lateral

## Description

# Description

Mimikatz DCSync is a tool that can be used to retrieve password hashes for user accounts in an Active Directory domain. This tool can be used to dump credentials from the domain controller without being detected by most anti-virus software. Attackers can use these password hashes to perform lateral movement and privilege escalation within the network. Technical details include Mimikatz DCSync using the Directory Replication Service Remote Protocol (MS-DRSR) to request password data from the domain controller. The tool can be used to retrieve password hashes for all user accounts in the domain or for specific accounts if the attacker has the appropriate permissions. The business value of this procedure is that it allows attackers to gain access to sensitive data and systems within the network.

 

## Requirements

1. Access to the domain controller

1. Mimikatz DCSync tool

 

## Defense

1. Implement strong password policies and multi-factor authentication to prevent attackers from easily retrieving password hashes

1. Monitor for suspicious activity such as unusual logins and password changes

1. Restrict access to domain controllers to only authorized personnel

 

## Objectives

1. Retrieve password hashes for user accounts in an Active Directory domain

1. Perform lateral movement and privilege escalation within the network

 

# Instructions

1. To retrieve the password of a specific user, run the command 'lsadump::dcsync /domain:<domain_name> /user:<username>'. To retrieve the passwords of all users in the domain, run the command 'lsadump::dcsync /domain:<domain_name> /all /csv'.

 



**Code**: [[# DCSync only one user
mimikatz# lsadump::dcsync /]]



> The DCSync command is used to retrieve password data from the Active Directory domain controller. This command can be executed by any member of the Administrators, Domain Admins, or Enterprise Admins groups, as well as by Domain Controller computer accounts. The command syntax includes the domain name and the user account whose password is to be retrieved. The output can be in CSV format for easy parsing.



**Command** ([[DCSync only one user for htb.local domain]]):

```bash
mimikatz# lsadump::dcsync /domain:htb.local /user:krbtgt
```





**Command** ([[DCSync all users for htb.local domain]]):

```bash
mimikatz# lsadump::dcsync /domain:htb.local /all /csv
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[DCSync all users for htb.local domain]]
- [[DCSync only one user for htb.local domain]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]
- [[Using Mimikatz DCSync]]


