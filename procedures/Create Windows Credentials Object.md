---
id: f0b44a88-1014-49eb-9295-cb48a1efedc3
name: Create Windows Credentials Object
type: procedure
verified: false
submitted: false
created_at: '2020-03-13T23:31:09.355485+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Valid Accounts|T1078 - Valid Accounts]]'
platforms:
- Windows
tags:
- '[[authentication]]'
commands:
- '[[Create a Windows PSCredential Object]]'
- '[[Create a Windows Secure String]]'
---

# Create Windows Credentials Object

## Summary

Create a PSCredential object from a username and password. Many PowerShell commands support a "Credential" argument, allowing the execution of commands as other users, or  to authenticate in instances where credentials aren't passed on in the existing session. 

## Description

# Description

Create a PSCredential object from a username and password. Many PowerShell commands support a "Credential" argument, allowing the execution of commands as other users, or  to authenticate in instances where credentials aren't passed on in the existing session.



# Instructions

1. Create a secure string using a password





**Command** ([[Create a Windows Secure String]]):

```bash
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
```





2. Create a PSCredential object, using the secure string created in step 1 ($Pass variable).





**Command** ([[Create a Windows PSCredential Object]]):

```bash
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_USER", $Pass
```



Note: when specifying a domain, the username format is: "$_DOMAIN\$_USER", eg "megabank\dave".

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Create a Windows PSCredential Object]]
- [[Create a Windows Secure String]]

## Tags

- [[authentication]]


