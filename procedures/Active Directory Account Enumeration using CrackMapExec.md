---
id: 2779c9fb-0f35-4003-865c-b035fa8a008c
name: Active Directory Account Enumeration using CrackMapExec
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.040390+00:00'
updated_at: '2023-04-10T20:26:23.328637+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[Data Encrypted for Impact|T1486 - Data Encrypted for Impact]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[From CVE to SYSTEM shell on DC]]'
- '[[samAccountName spoofing]]'
commands:
- '[[Enumerate machine account quota]]'
- '[[Execute StandIn.exe with ms-DS-MachineAccountQuota]]'
---

# Active Directory Account Enumeration using CrackMapExec

## Summary

Active Directory (AD) is a central component of most enterprise networks, and is therefore a prime target for attackers looking to gain access to sensitive information or systems. One of the first steps in an AD attack is to enumerate user and machine accounts, which can provide valuable informatio

## Description

# Description

Active Directory (AD) is a central component of most enterprise networks, and is therefore a prime target for attackers looking to gain access to sensitive information or systems. One of the first steps in an AD attack is to enumerate user and machine accounts, which can provide valuable information for further exploitation. CrackMapExec is a tool that can be used to enumerate machine accounts in an AD environment. This procedure outlines the steps for using CrackMapExec to perform machine account enumeration.

Technical Explanation: By using the CrackMapExec tool, an attacker can query Active Directory for a list of machine accounts. This information can then be used to identify potential targets for further exploitation. The tool works by using the LDAP protocol to query the AD database for a list of machine accounts. Once the list is obtained, the tool can be used to perform additional actions against the identified machines.

Business Value: By identifying machine accounts in an AD environment, an attacker can gain valuable information about the network architecture and potential targets for further exploitation. This can lead to the compromise of sensitive information or systems, which can have significant financial and reputational impacts on the victim organization.

 

## Requirements

1. Access to an AD environment

1. CrackMapExec tool installed

 

## Defense

1. Implement strong password policies for all AD accounts

1. Use multi-factor authentication to protect against unauthorized access

1. Monitor AD logs for suspicious activity, such as failed login attempts or unusual queries

 

## Objectives

1. Identify machine accounts in an AD environment

1. Gain information about the network architecture

1. Identify potential targets for further exploitation

 

# Instructions

1. This command uses CrackMapExec to perform LDAP queries against a domain controller to enumerate machine accounts. The '-u' flag specifies the username to use for authentication, '-p' specifies the password, '-d' specifies the domain to query, and '--kdcHost' specifies the IP address of the Kerberos Distribution Center. The '-M MAQ' flag specifies to use the 'ms-DS-MachineAccountQuota' object class for querying machine accounts. The 'StandIn.exe --object ms-DS-MachineAccountQuota=*' command is used to retrieve the results of the LDAP query.

 



**Code**: [[crackmapexec ldap 10.10.10.10 -u username -p 'Pass]]



> This command can be used by security professionals to discover all the machine accounts in a domain. This information can be useful for identifying potential targets for lateral movement or privilege escalation attacks.



**Command** ([[Enumerate machine account quota]]):

```bash
ldap 10.10.10.10 -u username -p 'Password123' -d 'domain.local' --kdcHost 10.10.10.10
```





**Command** ([[Execute StandIn.exe with ms-DS-MachineAccountQuota]]):

```bash
MAQ
StandIn.exe --object ms-DS-MachineAccountQuota=*
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Impact|TA0040 - Impact]]

### Techniques

- [[Data Encrypted for Impact|T1486 - Data Encrypted for Impact]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]

## Commands Used

- [[Enumerate machine account quota]]
- [[Execute StandIn.exe with ms-DS-MachineAccountQuota]]

## Tags

- [[Active Directory Attacks]]
- [[From CVE to SYSTEM shell on DC]]
- [[samAccountName spoofing]]


