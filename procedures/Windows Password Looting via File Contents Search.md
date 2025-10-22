---
id: 4cf7f908-3886-4738-b0f2-ab3b4f906c4f
name: Windows Password Looting via File Contents Search
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.926838+00:00'
updated_at: '2023-04-10T20:37:46.581014+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[Password Filter DLL|T1174 - Password Filter DLL]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Search for file contents]]'
- '[[Windows - Privilege Escalation]]'
---

# Windows Password Looting via File Contents Search

## Summary

This procedure involves searching for password files on a compromised Windows system. By searching for file contents, the attacker can identify files that contain password information. This technique can be used as part of an escalation of privileges attack, allowing the attacker to gain access to 

## Description

# Description

This procedure involves searching for password files on a compromised Windows system. By searching for file contents, the attacker can identify files that contain password information. This technique can be used as part of an escalation of privileges attack, allowing the attacker to gain access to sensitive information and potentially gain further access to the system.

To execute this procedure, the attacker must have already compromised the system and have the necessary permissions to search for files. This technique is often used in combination with other techniques such as the use of password filter DLLs.

This procedure can be valuable to an attacker as it can provide access to sensitive information such as user credentials, which can be used to move laterally across the network or gain further access to the compromised system.

## Requirements

1. Access to a compromised Windows system

1. Sufficient permissions to search for files

## Defense

1. Implement strong access controls and permissions to limit the ability of attackers to search for files containing sensitive information

1. Monitor for suspicious file access and search activity on systems

1. Implement multi-factor authentication to reduce the risk of password-based attacks

## Objectives

1. Identify files containing password information

1. Escalate privileges on the compromised system

1. Gain access to sensitive information

# Instructions

1. This command searches for files containing the word 'password' in the C drive and its subdirectories. It then appends the results to a file called 'results.txt'.

**Code**: [[cd C:\ & findstr /SI /M "password" *.xml *.ini *.t]]

> The 'cd C:\' command changes the current directory to the root of the C drive. The 'findstr /SI /M "password" *.xml *.ini *.txt' command searches for files with the extension .xml, .ini, or .txt that contain the word 'password'. The '/SI' switch makes the search case-insensitive and the '/M' switch displays only the file names that contain the search string. The 'findstr /si password *.xml *.ini *.txt *.config 2>nul >> results.txt' command searches for the same string in files with the extension .config and appends the results to the 'results.txt' file. The 'findstr /spin "password" *.*' command searches for the string 'password' in all files in the current directory and its subdirectories. The '/s' switch searches in subdirectories, the '/p' switch skips files with non-printable characters, and the '/i' switch makes the search case-insensitive.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[Password Filter DLL|T1174 - Password Filter DLL]]

## Tags

- [[EoP - Looting for passwords]]
- [[Search for file contents]]
- [[Windows - Privilege Escalation]]
