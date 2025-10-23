---
id: f39e8828-e3db-4d37-aae7-20a57c32baf4
name: Command Injection with Filter Bypass using Single Quote
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.257560+00:00'
updated_at: '2023-04-06T03:55:57.271520+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Bypass Blacklisted words]]'
- '[[Bypass with single quote]]'
- '[[Command Injection]]'
- '[[Filter Bypasses]]'
---

# Command Injection with Filter Bypass using Single Quote

## Summary

Command Injection is a type of attack where an attacker can execute arbitrary commands on a target system by injecting malicious inputs in the command-line interface. In this case, the attacker is bypassing a filter that blocks blacklisted words with a single quote. The single quote is used to esca

## Description

# Description

Command Injection is a type of attack where an attacker can execute arbitrary commands on a target system by injecting malicious inputs in the command-line interface. In this case, the attacker is bypassing a filter that blocks blacklisted words with a single quote. The single quote is used to escape the filter and execute the command. This technique can be used to gain unauthorized access, escalate privileges, or exfiltrate sensitive data.

 

## Requirements

1. Access to a vulnerable application or system

1. Knowledge of the filter bypass technique

 

## Defense

1. Sanitize user inputs by removing or encoding special characters

1. Implement a whitelist approach instead of a blacklist approach for input validation

1. Monitor system logs for suspicious activities and commands

 

## Objectives

1. Execute arbitrary commands on the target system

1. Bypass the filter that blocks blacklisted words

1. Gain unauthorized access, escalate privileges, or exfiltrate sensitive data

 

# Instructions

1. Execute the command using Invoke-Expression in PowerShell

 



**Code**: [[w'h'o'am'i]]



> The single quote is used to escape the filter and execute the command. The command 'whoami' is being executed in this case.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Bypass Blacklisted words]]
- [[Bypass with single quote]]
- [[Command Injection]]
- [[Filter Bypasses]]


