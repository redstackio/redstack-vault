---
id: 4a9593ba-f0d1-4059-9928-1c773a178401
name: Powershell Execution Policy for PowerView Commands
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.967799+00:00'
updated_at: '2023-04-10T20:37:00.752574+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]'
tags:
- '[[Execution Policy]]'
- '[[Powershell]]'
commands:
- '[[Change execution policy]]'
- '[[Run PowerView PowerShell script]]'
---

# Powershell Execution Policy for PowerView Commands

## Summary

The Powershell Execution Policy is a security feature that determines the conditions under which PowerShell loads configuration files and runs scripts. In this procedure, we will be discussing the Execution Policy required for running PowerView commands. PowerView is a popular PowerShell tool used 

## Description

# Description

The Powershell Execution Policy is a security feature that determines the conditions under which PowerShell loads configuration files and runs scripts. In this procedure, we will be discussing the Execution Policy required for running PowerView commands. PowerView is a popular PowerShell tool used for reconnaissance and exploitation. By setting the Execution Policy to allow signed scripts, we can ensure that only trusted scripts are executed on a system. This procedure is useful for both red and blue teams in assessing and securing a network.

From a technical perspective, the Execution Policy is a setting in PowerShell that determines the level of security surrounding script execution. By default, PowerShell will not run scripts, but rather only allow interactive commands. This is a security feature to prevent malicious scripts from running on a system. However, in order to run scripts such as PowerView, the Execution Policy must be changed. Setting the Execution Policy to allow signed scripts means that only scripts that are signed by a trusted publisher will be allowed to run. This ensures that only trusted scripts are executed, preventing malicious code from running on the system.

From a business perspective, this procedure ensures that PowerShell scripts are executed in a secure manner, preventing unauthorized access to sensitive data or systems. By requiring signed scripts, organizations can ensure that only trusted scripts are executed, reducing the risk of a security breach.

 

## Requirements

1. Admin access to the system

1. PowerShell installed on the system

1. PowerView commands installed on the system

 

## Defense

1. Ensure that the Execution Policy is set to allow only signed scripts

1. Verify that scripts are signed by a trusted publisher before execution

1. Monitor PowerShell logs for any suspicious activity

 

## Objectives

1. To ensure that the Execution Policy is set to allow signed scripts for PowerView commands

1. To ensure that only trusted PowerShell scripts are executed on the system

1. To reduce the risk of a security breach through the execution of malicious code

 

# Instructions

1. To use PowerView, run the following commands:

 



**Code**: [[powershell -EncodedCommand $encodedCommand
powersh]]



> 1. powershell -EncodedCommand $encodedCommand - Encoded command to load the PowerView module
2. powershell -ep bypass ./PowerView.ps1 - Loads the PowerView module
3. Set-Executionpolicy -Scope CurrentUser -ExecutionPolicy UnRestricted - Changes the execution policy to allow running the PowerView module
4. Set-ExecutionPolicy Bypass -Scope Process - Changes the execution policy to allow running the PowerView module



**Command** ([[Run PowerView PowerShell script]]):

```powershell
powershell -EncodedCommand $encodedCommand
powershell -ep bypass ./PowerView.ps1
```





**Command** ([[Change execution policy]]):

```bash
Set-Executionpolicy -Scope CurrentUser -ExecutionPolicy UnRestricted
Set-ExecutionPolicy Bypass -Scope Process
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]

## Commands Used

- [[Change execution policy]]
- [[Run PowerView PowerShell script]]

## Tags

- [[Execution Policy]]
- [[Powershell]]


