---
id: ab26cc02-4da5-44c7-83e2-eedbc5e86a70
name: Dumping Active Directory Credentials via NTDS.dit File
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.782103+00:00'
updated_at: '2023-04-10T20:36:03.346161+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Credentials in Files|T1081 - Credentials in Files]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
---

# Dumping Active Directory Credentials via NTDS.dit File

## Summary

Dumping Active Directory (AD) credentials via the NTDS.dit file is a common technique used by attackers to obtain domain credentials. The NTDS.dit file is the main database file for AD and contains all domain objects and their attributes, including password hashes. By dumping this file, an attacker

## Description

# Description

Dumping Active Directory (AD) credentials via the NTDS.dit file is a common technique used by attackers to obtain domain credentials. The NTDS.dit file is the main database file for AD and contains all domain objects and their attributes, including password hashes. By dumping this file, an attacker can obtain the password hashes for all domain accounts, which can then be cracked offline. This technique is often used in combination with other techniques, such as Pass the Hash, to gain access to domain resources.

To dump the NTDS.dit file, an attacker must have administrative access to a domain controller or have compromised a domain admin account. Once access is obtained, the attacker can use tools such as ntdsutil or PowerSploit's Invoke-NinjaCopy to copy the NTDS.dit file. The file can then be extracted and the password hashes can be cracked using tools such as Hashcat or John the Ripper.

Dumping AD credentials via the NTDS.dit file can have serious business impact, as it can allow an attacker to gain access to sensitive information and resources within the domain.

 

## Requirements

1. Administrative access to a domain controller or a compromised domain admin account

1. Tools such as ntdsutil or PowerSploit's Invoke-NinjaCopy to copy the NTDS.dit file

1. Tools such as Hashcat or John the Ripper to crack password hashes

 

## Defense

1. Limit administrative access to domain controllers and domain admin accounts

1. Implement strong password policies and multi-factor authentication

1. Monitor for suspicious activity, such as unusual file access or use of ntdsutil or PowerSploit's Invoke-NinjaCopy

 

## Objectives

1. Obtain domain credentials via dumping the NTDS.dit file

1. Use obtained credentials to gain access to domain resources

 

# Instructions

1. To locate the NTDS database, open the Command Prompt and type 'ntdsutil.exe'. From there, type 'Activate instance NTDS' and then 'Files'. Finally, type 'Info' to display the NTDS database location.

 



**Code**: [[systemroot\NTDS\ntds.dit]]



> The NTDS database is a crucial component of Active Directory and contains information about all objects in the directory. It is important to know the location of this file for backup and disaster recovery purposes.

2. To locate the NTDS.dit file, open File Explorer and navigate to the following path: systemroot\System32\ntds.dit

 



**Code**: [[systemroot\System32\ntds.dit]]



> The NTDS.dit file is a critical component of the Active Directory database. It contains the data for all objects in the directory, including users, groups, and computers. It is important to know the location of this file for troubleshooting and disaster recovery purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Credentials in Files|T1081 - Credentials in Files]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]


