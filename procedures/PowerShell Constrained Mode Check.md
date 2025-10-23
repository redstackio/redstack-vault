---
id: d46c4f92-fb7c-4824-aca1-278c7b4f8555
name: PowerShell Constrained Mode Check
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.993289+00:00'
updated_at: '2023-04-10T20:37:00.424076+00:00'
tags:
- '[[Constrained Mode]]'
- '[[Powershell]]'
commands:
- '[[Bypass PowerShell Version 2]]'
- '[[Check Execution Context Language Mode]]'
---

# PowerShell Constrained Mode Check

## Summary

PowerShell Constrained Mode is a method of limiting the capabilities of PowerShell to only allow certain commands to be run. This can be useful in environments where there is a need to restrict access to certain PowerShell functionality. However, attackers can use PowerShell to execute malicious co

## Description

# Description

PowerShell Constrained Mode is a method of limiting the capabilities of PowerShell to only allow certain commands to be run. This can be useful in environments where there is a need to restrict access to certain PowerShell functionality. However, attackers can use PowerShell to execute malicious code, so it's important to ensure that PowerShell is running in Constrained Mode to prevent this. This procedure checks whether PowerShell is running in Constrained Mode or not.

 

## Requirements

1. Access to PowerShell.

 

## Defense

1. Ensure that PowerShell is running in Constrained Mode to limit the capabilities of attackers.

1. Implement security measures such as application whitelisting to prevent unauthorized code execution.

1. Use PowerShell logging and monitoring to detect and respond to any malicious activity.

 

## Objectives

1. To determine whether PowerShell is running in Constrained Mode or not.

 

# Instructions

1. To check if you are in a constrained mode, run the following command in PowerShell:

$ExecutionContext.SessionState.LanguageMode

This command will return either FullLanguage or ConstrainedLanguage as the result. FullLanguage mode allows the execution of all PowerShell commands and scripts, while ConstrainedLanguage mode restricts the use of certain commands and language features.

To bypass ConstrainedLanguage mode, you can use the following command:

powershell -version 2

 



**Code**: [[# Check if we are in a constrained mode
# Values c]]



> The $ExecutionContext.SessionState.LanguageMode variable returns the current PowerShell language mode. This mode determines which commands and language features are available for use. FullLanguage mode allows the use of all PowerShell commands and language features, while ConstrainedLanguage mode restricts the use of certain commands and language features. The 'powershell -version 2' command can be used to bypass ConstrainedLanguage mode and execute scripts with FullLanguage mode.



**Command** ([[Check Execution Context Language Mode]]):

```bash
$ExecutionContext.SessionState.LanguageMode
```





**Command** ([[Bypass PowerShell Version 2]]):

```powershell
powershell -version 2
```



## Commands Used

- [[Bypass PowerShell Version 2]]
- [[Check Execution Context Language Mode]]

## Tags

- [[Constrained Mode]]
- [[Powershell]]


