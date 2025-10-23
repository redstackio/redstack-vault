---
id: 4b3093a3-c7bc-475c-954e-783bb15a00df
name: LFI to RCE via uploaded file
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.483121+00:00'
updated_at: '2023-04-10T20:22:14.540060+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[User Execution|T1204 - User Execution]]'
sub_techniques:
- '[[Malicious File|T1204.002 - Malicious File]]'
- '[[Malicious Image|T1204.003 - Malicious Image]]'
tags:
- '[[File Inclusion]]'
- '[[LFI to RCE via upload]]'
---

# LFI to RCE via uploaded file

## Summary

This procedure involves exploiting a Local File Inclusion (LFI) vulnerability to achieve Remote Code Execution (RCE) by uploading a file with a malicious payload. LFI vulnerabilities occur when an application allows user input to be included in a file path without proper validation. Attackers can e

## Description

# Description

This procedure involves exploiting a Local File Inclusion (LFI) vulnerability to achieve Remote Code Execution (RCE) by uploading a file with a malicious payload. LFI vulnerabilities occur when an application allows user input to be included in a file path without proper validation. Attackers can exploit these vulnerabilities to include and execute arbitrary files, such as a malicious PHP file, which can then be used to execute code on the target system. By uploading a file with a malicious payload, attackers can bypass any input validation and execute arbitrary code on the target system. This procedure can be used to gain unauthorized access to sensitive data, escalate privileges or perform other malicious activities.

 

## Requirements

1. Access to an application with a LFI vulnerability

1. Ability to upload files to the target system

 

## Defense

1. Validate user input and sanitize any input that is included in a file path.

1. Implement proper access controls to prevent unauthorized access to sensitive data.

1. Monitor system logs for any suspicious activity, such as unusual file uploads or system commands.

 

## Objectives

1. Gain unauthorized access to sensitive data

1. Escalate privileges

1. Execute arbitrary code on the target system

 

# Instructions

1. Upload a file with a malicious payload, such as a PHP file with a system command to execute arbitrary code.

 



**Code**: [[<?php system($_GET['c']); ?>]]



> The payload can be injected into a file that is uploaded to the target system. The payload should contain a system command that can be executed by the server. The command can be executed by accessing the uploaded file with the appropriate parameter, such as file.png?c=command.

2. Execute the uploaded file by accessing it through the application.

 



**Code**: [[http://example.com/index.php?page=path/to/uploaded]]



> The uploaded file can be executed by accessing it through the application. The URL should include the path to the uploaded file.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[User Execution|T1204 - User Execution]]

### Sub-Techniques

- [[Malicious File|T1204.002 - Malicious File]]
- [[Malicious Image|T1204.003 - Malicious Image]]

## Tags

- [[File Inclusion]]
- [[LFI to RCE via upload]]


