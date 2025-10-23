---
id: 306b0a1e-aac9-4c28-b9f3-4509526d72db
name: Windows Vault Credential Theft with Mimikatz
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.578124+00:00'
updated_at: '2023-04-10T20:37:18.013424+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Credentials in Registry|T1214 - Credentials in Registry]]'
tags:
- '[[Credential Manager & DPAPI]]'
- '[[Vault]]'
- '[[Windows - Mimikatz]]'
commands:
- '[[Vault Credentials Exported]]'
---

# Windows Vault Credential Theft with Mimikatz

## Summary

Windows Vault Credential Theft with Mimikatz is a technique used by attackers to steal credentials from the Windows Credential Manager Vault. This technique is often used as a post-exploitation technique after an attacker has gained access to a system. Mimikatz is a popular tool used by attackers t

## Description

# Description

Windows Vault Credential Theft with Mimikatz is a technique used by attackers to steal credentials from the Windows Credential Manager Vault. This technique is often used as a post-exploitation technique after an attacker has gained access to a system. Mimikatz is a popular tool used by attackers to extract plaintext passwords, hashes, and Kerberos tickets from memory. The Windows Credential Manager Vault is a secure storage area for user and system credentials that is encrypted with the Data Protection API (DPAPI). Mimikatz can be used to extract the DPAPI keys used to encrypt the Vault, which can then be used to decrypt and extract credentials stored within it. This technique can be used to obtain domain credentials, which can be used to move laterally within a network or elevate privileges.

 

## Requirements

1. Access to a Windows system

1. Mimikatz tool

 

## Defense

1. Implement strong password policies and use multi-factor authentication to protect against password theft

1. Monitor systems for signs of Mimikatz usage and other credential dumping techniques

1. Encrypt sensitive data and use access controls to restrict access to sensitive information

 

## Objectives

1. Steal credentials from the Windows Credential Manager Vault

1. Extract plaintext passwords, hashes, and Kerberos tickets

1. Obtain domain credentials for lateral movement or privilege escalation

 

# Instructions

1. To retrieve Windows credentials from the Vault, use the following command:

 



**Code**: [[vault::cred /in:C:\Users\demo\AppData\Local\Micros]]



> The 'vault::cred' command is used to access the Windows Credential Manager Vault. The '/in' argument specifies the path to the Vault. This command will retrieve all stored credentials in the Vault and display them in the console.



**Command** ([[Vault Credentials Exported]]):

```bash
vault::cred /in:C:\Users\demo\AppData\Local\Microsoft\Vault\"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Credentials in Registry|T1214 - Credentials in Registry]]

## Commands Used

- [[Vault Credentials Exported]]

## Tags

- [[Credential Manager & DPAPI]]
- [[Vault]]
- [[Windows - Mimikatz]]


