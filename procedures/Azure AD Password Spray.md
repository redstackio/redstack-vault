---
id: 48c3d668-8ab8-47cb-b94c-c70bb6812cf3
name: Azure AD Password Spray
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:16.028114+00:00'
updated_at: '2023-05-23T16:41:08.041642+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
platforms:
- Cloud
tags:
- '[[Azure AD]]'
- '[[Cloud - Azure]]'
- '[[Password Spray]]'
commands:
- '[[Clone MSOLSpray repository from GitHub]]'
- '[[Import MSOLSpray PowerShell module]]'
- '[[Spray passwords using MSOLSpray]]'
---

# Azure AD Password Spray

**Status**: ✓ Verified

## Summary

A password spray attack is a type of brute force attack that targets a large number of user accounts with a few commonly used passwords. In the context of Azure AD, this type of attack can be used to gain access to sensitive data and resources by compromising user accounts. Attackers can use the MS

## Description

# Description

A password spray attack is a type of brute force attack that targets a large number of user accounts with a few commonly used passwords. In the context of Azure AD, this type of attack can be used to gain access to sensitive data and resources by compromising user accounts. Attackers can use the MSOLSpray tool to automate the process of password spraying against Azure AD accounts. This attack can be particularly effective against organizations with weak password policies and a large number of user accounts.

 

## Requirements

1. Valid Azure AD credentials

1. Access to the MSOLSpray tool

 

## Defense

1. Enforce strong password policies and multi-factor authentication to make password spraying attacks more difficult

1. Monitor for failed login attempts and unusual login activity

1. Implement rate limiting and account lockout policies to prevent brute force attacks

 

## Objectives

1. Gain unauthorized access to sensitive data and resources

1. Compromise user accounts

 

# Instructions

1. To use MSOLSpray, first clone the repository from GitHub and import the PowerShell module. Then, use the Invoke-MSOLSpray command with the appropriate arguments to perform the password spray attack. The UserList argument should be a file containing a list of usernames in the format "user@domain.com", and the Password argument should be a single password that will be used for the attack. The Force argument can be used to continue the attack even if multiple account lockouts are detected, and the URL argument can be used to specify the URL to spray against.

 



**Code**: [[git clone https://github.com/dafthack/MSOLSpray
Im]]



> 1. Download the MSOLSpray.ps1 script from https://github.com/dafthack/MSOLSpray.
2. Open PowerShell and navigate to the directory where the script is saved.
3. Run the command '.\MSOLSpray.ps1' to load the script.
4.  Run the command 'Invoke-MSOLSpray -UserList C:\Tools\validemails.txt  -Password <PASSWORD> -Verbose', replacing <PASSWORD> with  the password to be used for the attack.
5. The script will attempt to  authenticate to Office 365 using the supplied credentials and perform a  password spraying attack against the user list provided in the  'validemails.txt' file.
6. If successful, the script will output the usernames and passwords that were found.



**Command** ([[Clone MSOLSpray repository from GitHub]]):

```bash
git clone https://github.com/dafthack/MSOLSpray
```





**Command** ([[Import MSOLSpray PowerShell module]]):

```bash
Import-Module .\MSOLSpray.ps1
```





**Command** ([[Spray passwords using MSOLSpray]]):

```bash
Invoke-MSOLSpray -UserList .\userlist.txt -Password Winter2020
Invoke-MSOLSpray -UserList .\users.txt -Password d0ntSprayme!
```



## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[Clone MSOLSpray repository from GitHub]]
- [[Import MSOLSpray PowerShell module]]
- [[Spray passwords using MSOLSpray]]

## Tags

- [[Azure AD]]
- [[Cloud - Azure]]
- [[Password Spray]]


