---
id: 5def7b2c-b500-4da4-9010-ef4eca42b821
name: Windows - Guest Credential Default Password
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.651568+00:00'
updated_at: '2023-04-10T20:38:07.306348+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Credentials in Files|T1081 - Credentials in Files]]'
tags:
- '[[Get credentials]]'
- '[[Guest Credential]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Extracted Credentials]]'
---

# Windows - Guest Credential Default Password

## Summary

This procedure involves obtaining the default guest account password for a Windows system. The default guest account password is often left unchanged by system administrators, making it an easy target for attackers. Once the password is obtained, an attacker can use it to gain access to the system 

## Description

# Description

This procedure involves obtaining the default guest account password for a Windows system. The default guest account password is often left unchanged by system administrators, making it an easy target for attackers. Once the password is obtained, an attacker can use it to gain access to the system and potentially escalate privileges. The technical process involves finding the guest account and then using a tool or script to guess the password. The business value of this procedure is that it allows an attacker to gain unauthorized access to sensitive information and systems.

 

## Requirements

1. Access to the targeted Windows system

1. Ability to run scripts or tools on the system

 

## Defense

1. Change the default guest account password to a strong, unique password

1. Monitor for failed login attempts and other signs of unauthorized access

1. Implement multi-factor authentication to prevent password guessing attacks

 

## Objectives

1. Obtain the default guest account password

1. Gain unauthorized access to the system

1. Potentially escalate privileges

 

# Instructions

1. To change the password for the Guest account, use the following command: net user guest *

 



**Code**: [[Username: Guest
Password: [EMPTY]
NT Hash: 31d6cfe]]



> The 'net user' command is used to manage user accounts in Windows. The 'guest' argument specifies the username for which the password is to be changed. The '*' character prompts the user to enter a new password. Once the new password is entered, it will replace the empty default password for the Guest account.



**Command** ([[Extracted Credentials]]):

```bash
Username: Guest
Password: [EMPTY]
NT Hash: 31d6cfe0d16ae931b73c59d7e0c089c0
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Credentials in Files|T1081 - Credentials in Files]]

## Commands Used

- [[Extracted Credentials]]

## Tags

- [[Get credentials]]
- [[Guest Credential]]
- [[Windows - Using credentials]]


