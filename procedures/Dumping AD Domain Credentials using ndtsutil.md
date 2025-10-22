---
id: 07b176c5-3bb1-49c7-9c9f-f78b64fb04e8
name: Dumping AD Domain Credentials using ndtsutil
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.827981+00:00'
updated_at: '2023-04-10T20:25:43.312540+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques:
- '[[LSASS Memory|T1003.001 - LSASS Memory]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
- '[[Using ndtsutil]]'
commands:
- '[[Create full IFM backup of ntds instance]]'
---

# Dumping AD Domain Credentials using ndtsutil

## Summary

Dumping Active Directory domain credentials is a common technique used by attackers to obtain sensitive information. By using ndtsutil, an attacker can create an IFM (Install From Media) backup of the Active Directory database, which contains hashed passwords for all domain users. The attacker can 

## Description

# Description

Dumping Active Directory domain credentials is a common technique used by attackers to obtain sensitive information. By using ndtsutil, an attacker can create an IFM (Install From Media) backup of the Active Directory database, which contains hashed passwords for all domain users. The attacker can then use various tools to extract these hashes and attempt to crack them to obtain cleartext passwords.

Technical Explanation: ndtsutil is a command-line tool that is installed as part of the Active Directory Domain Services role. It can be used to perform various administrative tasks, including creating IFM backups. An IFM backup is a snapshot of the Active Directory database that can be used to install domain controllers or restore domain data. By creating an IFM backup, an attacker can obtain a copy of the Active Directory database and extract sensitive information such as hashed passwords.

Business Value: Dumping AD domain credentials using ndtsutil can allow an attacker to gain access to sensitive information and potentially compromise an entire network. This can lead to data theft, unauthorized access, and financial loss for the affected organization.

## Requirements

1. Access to a domain controller

1. Authentication credentials with administrative privileges

1. Access to ndtsutil

## Defense

1. Limit access to domain controllers to authorized personnel only

1. Implement strong password policies and multi-factor authentication

1. Regularly monitor and audit Active Directory for suspicious activity

## Objectives

1. Obtain hashed passwords for all domain users

1. Attempt to crack hashed passwords to obtain cleartext passwords

# Instructions

1. To create an IFM backup of Active Directory, follow these steps:
1. Open Command Prompt as an administrator.
2. Type 'ntdsutil' and press Enter.
3. Type 'activate instance ntds' and press Enter.
4. Type 'ifm' and press Enter.
5. Type 'create full c:\pentest' and press Enter. Replace 'c:\pentest' with the path where you want to save the backup.
6. Type 'quit' and press Enter.
7. Type 'quit' again and press Enter to exit ntdsutil.

**Code**: [[C:\>ntdsutil
ntdsutil: activate instance ntds
ntds]]

> The 'ntdsutil' command is used to manage Active Directory databases. The 'activate instance ntds' command selects the domain controller whose database you want to manage. The 'ifm' command opens the Install from Media (IFM) tool, which is used to create a backup of Active Directory that can be used to install Active Directory on another server. The 'create full' command creates a full backup of Active Directory. Replace 'c:\pentest' with the path where you want to save the backup. Finally, the 'quit' command exits the IFM tool and ntdsutil.

**Command** ([[Create full IFM backup of ntds instance]]):

```bash
ntdsutil
activate instance ntds
ifm
create full c:\pentest
quit
quit
```

2. To create a backup of the Active Directory database, use the ntdsutil command with the ifm parameter and specify the location where you want to store the backup. The create full option will create a full backup of the database.

**Code**: [[ntdsutil "ac i ntds" "ifm" "create full c:\temp" q]]

> The ntdsutil command is used to manage Active Directory databases. The ac i ntds parameter specifies that we want to work with the active instance of the NTDS database. The ifm parameter specifies that we want to create an Install From Media (IFM) backup. The create full option specifies that we want to create a full backup of the database. Finally, we specify the location where we want to store the backup, in this case, c:\temp. The q q option is used to exit the ntdsutil command after the backup is created.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

### Sub-Techniques

- [[LSASS Memory|T1003.001 - LSASS Memory]]

## Commands Used

- [[Create full IFM backup of ntds instance]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]
- [[Using ndtsutil]]
