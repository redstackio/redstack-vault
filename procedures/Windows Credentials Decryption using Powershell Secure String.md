---
id: c946f6fa-d806-48f1-8beb-8c53e9fbd75e
name: Windows Credentials Decryption using Powershell Secure String
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.188811+00:00'
updated_at: '2023-04-10T20:38:06.232039+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
- '[[Credentials in Registry|T1214 - Credentials in Registry]]'
tags:
- '[[Powershell Remoting Protocol]]'
- '[[Powershell Secure String]]'
- '[[Windows - Using credentials]]'
---

# Windows Credentials Decryption using Powershell Secure String

## Summary

Windows Credentials Decryption using Powershell Secure String is a technique used by attackers to obtain and decrypt stored Windows credentials on a compromised system. This technique involves using the Powershell Remoting Protocol to remotely execute Powershell scripts that decrypt the Secure Stri

## Description

# Description

Windows Credentials Decryption using Powershell Secure String is a technique used by attackers to obtain and decrypt stored Windows credentials on a compromised system. This technique involves using the Powershell Remoting Protocol to remotely execute Powershell scripts that decrypt the Secure String which contains the stored credentials. This technique is commonly used by attackers who have already gained access to a system and are looking to escalate privileges or move laterally across a network.

From a technical perspective, this technique involves using the ConvertTo-SecureString cmdlet in Powershell to encrypt the credentials and then storing the encrypted string in a file or registry. The attacker can then use the ConvertFrom-SecureString cmdlet to decrypt the string using a key and obtain the plain-text credentials.

The business value of this technique is that it allows attackers to gain access to sensitive information such as usernames and passwords, which can be used to further compromise the system or other systems on the network.

## Requirements

1. Access to a compromised system with stored Windows credentials

1. Knowledge of the Powershell Remoting Protocol

1. Knowledge of Powershell cmdlets for Secure String encryption and decryption

## Defense

1. Encrypt stored Windows credentials using a strong encryption algorithm

1. Limit access to files or registry keys containing encrypted credentials

1. Monitor for suspicious Powershell activity, such as the use of Secure String cmdlets

## Objectives

1. Obtain stored Windows credentials

1. Escalate privileges or move laterally across a network

# Instructions

1. This command is used to decrypt a secure string using an AES key. The command requires two inputs: the AES key and the secure string to be decrypted. The AES key should be provided as an array of bytes. The secure string should be provided as a string. The command uses the ConvertTo-SecureString cmdlet to create a secure object using the provided string and AES key. The SecureStringToBSTR method is then used to convert the secure object to an unmanaged BSTR string. Finally, the PtrToStringAuto method is used to convert the BSTR string to a managed string.

**Code**: [[$aesKey = (49, 222, 253, 86, 26, 137, 92, 43, 29, ]]

> The $aesKey variable should be an array of bytes representing the AES key used to encrypt the secure string. The $secureObject variable should be a secure string that was encrypted using the same AES key. The $decrypted variable will contain the decrypted string.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]
- [[Credentials in Registry|T1214 - Credentials in Registry]]

## Tags

- [[Powershell Remoting Protocol]]
- [[Powershell Secure String]]
- [[Windows - Using credentials]]
