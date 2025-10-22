---
id: 7842cbab-3dfe-47d5-9d3c-53d9495d2d5a
name: Windows - PowerShell Constrained Language Mode Check
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.470722+00:00'
updated_at: '2023-04-10T20:37:07.123835+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Constrained Language Mode]]'
- '[[Powershell]]'
- '[[Windows - Defenses]]'
commands:
- '[[Check PowerShell Language Mode]]'
---

# Windows - PowerShell Constrained Language Mode Check

## Summary

The PowerShell Constrained Language Mode Check procedure is used to determine if the PowerShell environment is running in Constrained Language Mode. Constrained Language Mode is a PowerShell language mode that restricts the ability to run PowerShell commands or scripts to a limited set of commands.

## Description

# Description

The PowerShell Constrained Language Mode Check procedure is used to determine if the PowerShell environment is running in Constrained Language Mode. Constrained Language Mode is a PowerShell language mode that restricts the ability to run PowerShell commands or scripts to a limited set of commands. This mode can help protect against malicious scripts and commands. However, it can also limit the functionality of legitimate PowerShell scripts and commands. This procedure can be used to check if Constrained Language Mode is enabled and to determine if it is causing any issues with legitimate scripts or commands.

## Requirements

1. Access to a PowerShell environment

## Defense

1. Ensure that Constrained Language Mode is enabled on all systems as a best practice

1. Monitor PowerShell activity for any suspicious behavior

1. Consider using additional security measures such as PowerShell logging or script block logging

## Objectives

1. Determine if PowerShell is running in Constrained Language Mode

1. Identify any issues with legitimate scripts or commands caused by Constrained Language Mode

# Instructions

1. To check the language mode of PowerShell, use the $ExecutionContext.SessionState.LanguageMode property.

**Code**: [[$ExecutionContext.SessionState.LanguageMode]]

> The $ExecutionContext.SessionState.LanguageMode property is used to determine if PowerShell is running in FullLanguage mode or ConstrainedLanguage mode. FullLanguage mode allows the use of all PowerShell language features, while ConstrainedLanguage mode restricts the use of certain PowerShell language features to enhance security. This command checks if PowerShell is currently running in ConstrainedLanguage mode.

**Command** ([[Check PowerShell Language Mode]]):

```bash
$ExecutionContext.SessionState.LanguageMode
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Check PowerShell Language Mode]]

## Tags

- [[Constrained Language Mode]]
- [[Powershell]]
- [[Windows - Defenses]]
