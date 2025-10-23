---
id: 27bc6fa5-4c43-453f-b47a-f75e6a53d40e
name: Windows - EoP Looting for Passwords via Key Manager
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.263837+00:00'
updated_at: '2023-04-10T20:37:51.603899+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials in Registry|T1214 - Credentials in Registry]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Passwords stored in Key Manager]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Open Windows Credential Manager]]'
---

# Windows - EoP Looting for Passwords via Key Manager

## Summary

Elevation of Privilege (EoP) attacks are commonly used by attackers to gain higher privileges on a compromised system. One method of EoP is looting for passwords stored in the Key Manager. The Key Manager is a secure storage area for sensitive information such as passwords, certificates, and privat

## Description

# Description

Elevation of Privilege (EoP) attacks are commonly used by attackers to gain higher privileges on a compromised system. One method of EoP is looting for passwords stored in the Key Manager. The Key Manager is a secure storage area for sensitive information such as passwords, certificates, and private keys. Attackers can use tools like 'Display Stored Passwords' to extract these passwords and escalate their privileges. This attack can lead to complete compromise of the system and sensitive data.

Technical Explanation: The Key Manager is a secure storage area in Windows that allows programs to store sensitive information such as passwords, certificates, and private keys. The Key Manager is protected by a master key that is generated when a user creates a password. This master key is used to encrypt all sensitive data stored in the Key Manager. Attackers can use tools like 'Display Stored Passwords' to extract these passwords and escalate their privileges.

Business Value: Attackers can use this method to gain access to sensitive data and systems, causing significant damage to the business. This attack can lead to data theft, system compromise, and reputational damage.

 

## Requirements

1. Access to a compromised Windows system

1. Administrative privileges on the compromised system

1. Use of 'Display Stored Passwords' tool

 

## Defense

1. Implement strong password policies and multi-factor authentication to reduce the risk of password theft

1. Monitor the Key Manager for suspicious activity and changes

1. Regularly update and patch Windows systems to prevent known vulnerabilities

 

## Objectives

1. To escalate privileges on a compromised system

1. To gain access to sensitive data and systems

 

# Instructions

1. To display stored passwords, run the following command in Command Prompt or PowerShell:

 



**Code**: [[rundll32 keymgr,KRShowKeyMgr]]



> This command will launch the Windows Credential Manager GUI, which displays all passwords and login information that are stored on the local machine. This can be useful for retrieving forgotten passwords or managing saved login information.



**Command** ([[Open Windows Credential Manager]]):

```bash
rundll32 keymgr,KRShowKeyMgr
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials in Registry|T1214 - Credentials in Registry]]

## Commands Used

- [[Open Windows Credential Manager]]

## Tags

- [[EoP - Looting for passwords]]
- [[Passwords stored in Key Manager]]
- [[Windows - Privilege Escalation]]


