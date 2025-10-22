---
id: d0bb4013-5469-455d-97f3-1c4eeedc3bb5
name: LFI to RCE via FindFirstFile
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.529690+00:00'
updated_at: '2023-04-10T20:22:14.885842+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[File Inclusion]]'
- '[[LFI to RCE via upload (FindFirstFile)]]'
---

# LFI to RCE via FindFirstFile

## Summary

This procedure involves exploiting a local file inclusion (LFI) vulnerability that allows an attacker to upload a malicious file and execute remote code. The vulnerability is caused by a lack of input validation in the application's file inclusion functionality. By using the FindFirstFile function 

## Description

# Description

This procedure involves exploiting a local file inclusion (LFI) vulnerability that allows an attacker to upload a malicious file and execute remote code. The vulnerability is caused by a lack of input validation in the application's file inclusion functionality. By using the FindFirstFile function and carefully crafted input, an attacker can bypass the application's security controls and upload a malicious file. Once the file is uploaded, the attacker can execute arbitrary code on the target system.

Technical Explanation: The FindFirstFile function is used to search for a file or directory on a file system. If the function is called with a path that includes user-controlled input, an attacker can manipulate the input to include a path to their malicious file. The application will then include the malicious file in its execution flow, allowing the attacker to execute arbitrary code on the target system.

Business Value: An attacker can use this procedure to gain unauthorized access to a system and steal sensitive data, install malware or ransomware, or use the target system as a foothold to launch further attacks.

## Requirements

1. Access to the target system

1. Knowledge of the application's file inclusion functionality

1. Ability to craft malicious input

## Defense

1. Implement input validation to prevent user-controlled input from being used in file inclusion functionality.

1. Monitor file system activity for suspicious behavior, such as new files being created or modified.

1. Implement least privilege access controls to limit the impact of a successful attack.

## Objectives

1. Upload and execute malicious code on the target system

1. Gain unauthorized access to sensitive data

1. Use the target system as a foothold to launch further attacks

# Instructions

1. The FindFirstFile function is used to search for a file or directory on a file system.

> To exploit the LFI vulnerability, an attacker would call the FindFirstFile function with a path that includes user-controlled input. The function will then search for the file or directory specified in the input. If the input is carefully crafted, the function will include the attacker's malicious file in its execution flow, allowing the attacker to execute arbitrary code on the target system.

2. Masks are used to match multiple files or directories based on a pattern.

**Code**: [[&lt;&lt; * &gt;&gt; ?]]

> An attacker can use masks as wildcards to match multiple files or directories when calling the FindFirstFile function. By using carefully crafted masks, an attacker can include their malicious file in the search results, allowing them to execute arbitrary code on the target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]

## Tags

- [[File Inclusion]]
- [[LFI to RCE via upload (FindFirstFile)]]
