---
id: 031e2992-394d-4071-ad77-192ba9c7d1b1
name: Dumping AD Domain Credentials via NTDS Reversible Encryption
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.131567+00:00'
updated_at: '2023-04-10T20:35:59.222956+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
- '[[NTDS Reversible Encryption]]'
commands:
- '[[Check if password encryption is allowed]]'
---

# Dumping AD Domain Credentials via NTDS Reversible Encryption

## Summary

Dumping Active Directory (AD) domain credentials is a common technique used by attackers to gain access to sensitive information. One method for doing this is by exploiting the NTDS.dit file, which contains the AD database. The NTDS.dit file is encrypted by default, but can be configured to use rev

## Description

# Description

Dumping Active Directory (AD) domain credentials is a common technique used by attackers to gain access to sensitive information. One method for doing this is by exploiting the NTDS.dit file, which contains the AD database. The NTDS.dit file is encrypted by default, but can be configured to use reversible encryption, which allows an attacker to obtain the plaintext passwords of all AD domain users.

To exploit this vulnerability, an attacker must first gain access to the domain controller. Once access is obtained, the attacker can use a variety of tools to dump the NTDS.dit file and extract the plaintext passwords. This technique can be particularly effective if the domain administrator account is compromised, as it provides the attacker with full access to the AD domain and all its resources.

From a business perspective, this attack can be devastating as it can result in the compromise of sensitive data, including intellectual property, financial information, and personal data of employees and customers.

 

## Requirements

1. Access to the domain controller

1. Tools for dumping the NTDS.dit file and extracting passwords

 

## Defense

1. Ensure that reversible encryption is disabled for the NTDS.dit file

1. Use strong passwords and limit the number of domain administrators

1. Monitor for suspicious activity on the domain controller, such as unusual logins or file access

 

## Objectives

1. Dump the NTDS.dit file from the domain controller

1. Extract the plaintext passwords of AD domain users

1. Gain full access to the AD domain and its resources

 

# Instructions

1. This command allows for the use of encrypted passwords in the system.

 



**Code**: [[UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED]]



> When this command is set to true, users will be able to use encrypted passwords in the system. Encrypted passwords provide an added layer of security as they cannot be easily deciphered by unauthorized users. To use encrypted passwords, users will need to follow the specific instructions provided by the system. This command should only be used if encrypted passwords are supported by the system and if users are aware of how to use them.



**Command** ([[Check if password encryption is allowed]]):

```bash
UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Check if password encryption is allowed]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]
- [[NTDS Reversible Encryption]]


