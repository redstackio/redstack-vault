---
id: 281d023c-d79b-46ef-91e5-9e4f40e06c61
name: Azure Password Spraying
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.854072+00:00'
updated_at: '2023-04-10T20:19:42.141558+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Cloud - Azure]]'
- '[[Enumerate valid emails]]'
- '[[Enumeration]]'
- '[[Password spraying]]'
commands:
- '[[MSOLSpray User Authentication]]'
---

# Azure Password Spraying

## Summary

Azure Password Spraying is a technique used by attackers to gain access to Azure accounts. It involves guessing passwords for a large number of accounts using a small set of commonly used passwords. This technique can be used to identify accounts with weak passwords and gain access to sensitive dat

## Description

# Description

Azure Password Spraying is a technique used by attackers to gain access to Azure accounts. It involves guessing passwords for a large number of accounts using a small set of commonly used passwords. This technique can be used to identify accounts with weak passwords and gain access to sensitive data. Attackers can use this technique to gain access to cloud-based email accounts, which can contain sensitive information such as financial data, intellectual property, and personal information. This technique is commonly used in conjunction with other techniques to gain access to an organization's cloud-based resources.

## Requirements

1. Access to the Azure portal

1. A list of valid email addresses

## Defense

1. Enforce strong password policies to prevent password spraying attacks

1. Implement multi-factor authentication to protect against unauthorized access to Azure accounts

1. Monitor Azure logs for suspicious activity and investigate any anomalies

## Objectives

1. Gain access to Azure accounts

1. Identify accounts with weak passwords

1. Access sensitive data stored in cloud-based email accounts

# Instructions

1. To perform an Office 365 user password spraying attack using MSOLSpray, follow the below instructions:

**Code**: [[PS> . C:\Tools\MSOLSpray\MSOLSpray.ps1
PS> Invoke-]]

> 1. Download the MSOLSpray.ps1 script from https://github.com/dafthack/MSOLSpray.
2. Open PowerShell and navigate to the directory where the script is saved.
3. Run the command '.\MSOLSpray.ps1' to load the script.
4. Run the command 'Invoke-MSOLSpray -UserList C:\Tools\validemails.txt -Password <PASSWORD> -Verbose', replacing <PASSWORD> with the password to be used for the attack.
5. The script will attempt to authenticate to Office 365 using the supplied credentials and perform a password spraying attack against the user list provided in the 'validemails.txt' file.
6. If successful, the script will output the usernames and passwords that were found.

**Command** ([[MSOLSpray User Authentication]]):

```bash
. C:\Tools\MSOLSpray\MSOLSpray.ps1
Invoke-MSOLSpray -UserList C:\Tools\validemails.txt -Password <PASSWORD> -Verbose
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[MSOLSpray User Authentication]]

## Tags

- [[Cloud - Azure]]
- [[Enumerate valid emails]]
- [[Enumeration]]
- [[Password spraying]]
