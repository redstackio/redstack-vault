---
id: 699af4f5-32a1-4e10-a320-a249ff3d16e0
name: Office Default Passwords for Excel Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.176757+00:00'
updated_at: '2023-04-10T20:36:54.436687+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Office - Attacks]]'
- '[[Office Default Passwords]]'
commands:
- '[[Download VelvetSweatshop]]'
- '[[Run VelvetSweatshop]]'
---

# Office Default Passwords for Excel Files

## Summary

This procedure involves attempting to access password-protected Excel files using known default passwords. This technique can be used by an attacker to gain access to sensitive information contained within the Excel files. 

To execute this procedure, the attacker would need to identify the target 

## Description

# Description

This procedure involves attempting to access password-protected Excel files using known default passwords. This technique can be used by an attacker to gain access to sensitive information contained within the Excel files. 

To execute this procedure, the attacker would need to identify the target Excel files and attempt to access them using a list of known default passwords. If successful, the attacker would gain access to the contents of the Excel files. 

This procedure can be used to gain access to sensitive financial, customer, or employee data.

 

## Requirements

1. Access to the target network

1. Knowledge of default passwords for Excel files

 

## Defense

1. Ensure that all default passwords for Excel files are changed

1. Implement two-factor authentication for accessing sensitive data

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Gain access to sensitive information contained within password-protected Excel files

 

# Instructions

1. To set a password for an Excel file, follow these steps:
1. Click on 'File' and then 'Save As'.
2. Click on 'Tools' and then 'General Options'.
3. In the 'Password to Open' field, enter the password you want to use.
4. In the 'Password to Modify' field, enter the password if you want to prevent others from modifying the file.
5. Click 'OK' and then 'Save'.

 



**Code**: [[VelvetSweatshop]]



> The 'Password to Open' field is used to set a password that is required to open the file. The 'Password to Modify' field is used to set a password that is required to modify the file. If you do not want to set a password for either of these fields, simply leave them blank. It is important to note that if you forget your password, there is no way to recover it, so make sure to choose a password that you can remember.



**Command** ([[Download VelvetSweatshop]]):

```bash
wget http://www.ifarchive.org/if-archive/games/zcode/VelvetSweatshop.z5
```





**Command** ([[Run VelvetSweatshop]]):

```bash
frotz VelvetSweatshop.z5
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[Download VelvetSweatshop]]
- [[Run VelvetSweatshop]]

## Tags

- [[Office - Attacks]]
- [[Office Default Passwords]]


