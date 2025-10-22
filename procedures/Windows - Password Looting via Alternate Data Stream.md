---
id: c06117f5-6877-4f7b-8d11-befb305db0f2
name: Windows - Password Looting via Alternate Data Stream
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.351701+00:00'
updated_at: '2023-04-10T20:37:36.624830+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[File Permissions Modification|T1222 - File Permissions Modification]]'
- '[[Image File Execution Options Injection|T1183 - Image File Execution Options Injection]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Password in Alternate Data Stream]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Get-Item and Get-Content for Flag.txt]]'
---

# Windows - Password Looting via Alternate Data Stream

## Summary

This technique involves looting for passwords by accessing the Alternate Data Stream (ADS) of a file. An ADS is a feature of the NTFS file system that allows data to be hidden and associated with a file without changing the file itself. By placing a password in an ADS, an attacker can bypass passwo

## Description

# Description

This technique involves looting for passwords by accessing the Alternate Data Stream (ADS) of a file. An ADS is a feature of the NTFS file system that allows data to be hidden and associated with a file without changing the file itself. By placing a password in an ADS, an attacker can bypass password checks and gain access to the system. This technique requires the attacker to have already escalated privileges on the system. The attacker can use this technique to gain access to sensitive information, such as user credentials, stored on the system.

## Requirements

1. Administrator or SYSTEM privileges on the target system

1. Access to a file with an Alternate Data Stream containing a password

## Defense

1. Implement proper access controls to prevent unauthorized access to sensitive files.

1. Monitor for suspicious activity, such as changes to file permissions or creation of Alternate Data Streams.

1. Implement password policies that require strong, unique passwords and prevent the use of easily guessable passwords.

## Objectives

1. Gain access to sensitive information, such as user credentials, stored on the system.

# Instructions

1. To retrieve the content of the flag file, use the 'Get-Item' and 'Get-Content' commands with the appropriate arguments.
First, use 'Get-Item' to retrieve the flag file with all its streams:

Get-Item -path flag.txt -Stream *

This will return an object with all the streams associated with the flag file. Next, use 'Get-Content' to retrieve the content of the 'Flag' stream:

Get-Content -path flag.txt -Stream Flag

**Code**: [[PS > Get-Item -path flag.txt -Stream *
PS > Get-Co]]

> The 'Get-Item' command is used to retrieve an item (file, folder, etc.) from a specified path. In this case, we are retrieving the flag file with all its streams. The '-path' parameter specifies the path to the file, and the '-Stream *' parameter specifies that all streams associated with the file should be retrieved.

The 'Get-Content' command is used to retrieve the content of a file. In this case, we are retrieving the content of the 'Flag' stream of the flag file. The '-path' parameter specifies the path to the file, and the '-Stream Flag' parameter specifies that we want to retrieve the 'Flag' stream specifically.

**Command** ([[Get-Item and Get-Content for Flag.txt]]):

```powershell
PS > Get-Item -path flag.txt -Stream *
PS > Get-Content -path flag.txt -Stream Flag
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[File Permissions Modification|T1222 - File Permissions Modification]]
- [[Image File Execution Options Injection|T1183 - Image File Execution Options Injection]]

## Commands Used

- [[Get-Item and Get-Content for Flag.txt]]

## Tags

- [[EoP - Looting for passwords]]
- [[Password in Alternate Data Stream]]
- [[Windows - Privilege Escalation]]
