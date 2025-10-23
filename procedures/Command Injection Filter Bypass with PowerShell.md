---
id: 3b504ce8-d9bb-4962-b2d8-c319984a4b51
name: Command Injection Filter Bypass with PowerShell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.395988+00:00'
updated_at: '2023-04-06T03:55:57.411955+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Bypass with $()]]'
- '[[Bypass with wildcards]]'
- '[[Command Injection]]'
- '[[Filter Bypasses]]'
---

# Command Injection Filter Bypass with PowerShell

## Summary

Command injection is a technique used by attackers to execute arbitrary commands on a targeted system. This specific procedure uses PowerShell to bypass filters that attempt to block certain characters or commands. By using wildcards and the $() syntax, an attacker can execute commands that would n

## Description

# Description

Command injection is a technique used by attackers to execute arbitrary commands on a targeted system. This specific procedure uses PowerShell to bypass filters that attempt to block certain characters or commands. By using wildcards and the $() syntax, an attacker can execute commands that would normally be blocked. This technique can be used to gain access to sensitive information, escalate privileges, or execute further attacks on the system.

Technical Explanation:
This procedure uses PowerShell to bypass filters that block certain characters or commands. The $() syntax allows the attacker to execute commands within a string. Wildcards are used to bypass filters that attempt to block specific file extensions or file names. The attacker can use this technique to execute arbitrary commands on the targeted system.

Business Value:
This procedure can be used by attackers to gain access to sensitive information, escalate privileges, or execute further attacks on the system. By bypassing filters that attempt to block certain characters or commands, an attacker can execute commands that would normally be blocked.

 

## Requirements

1. Access to a system with PowerShell installed

 

## Defense

1. Implement input validation and sanitize user input to prevent injection attacks

1. Implement proper filtering and blocking of characters and commands to prevent bypass attempts

1. Monitor system logs and network traffic for suspicious activity

 

## Objectives

1. Execute arbitrary commands on the targeted system

1. Bypass filters that attempt to block certain characters or commands

 

# Instructions

1. The first command will open notepad by using wildcards to bypass filters that block specific file names and extensions. The second command will open the calculator by using wildcards to bypass filters that block specific file names and extensions.

 



**Code**: [[powershell C:\*\*2\n??e*d.*? # notepad
@^p^o^w^e^r]]



> The attacker uses the $() syntax to execute arbitrary commands within a string. Wildcards are used to bypass filters that attempt to block specific file extensions or file names. The first command uses the wildcard *2 to bypass filters that block specific file names. The second command uses the wildcard *32 to bypass filters that block specific file names. The ? characters are used to match any single character. The e*d.*? matches any file name that starts with e, has a d in the middle, and ends with any extension that is three characters long.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Tags

- [[Bypass with $()]]
- [[Bypass with wildcards]]
- [[Command Injection]]
- [[Filter Bypasses]]


