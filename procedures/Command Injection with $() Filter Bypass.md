---
id: f455998b-31e9-48c7-9de1-b6d2f3ae1aac
name: Command Injection with $() Filter Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.353378+00:00'
updated_at: '2023-04-06T03:55:57.365339+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Bypass with $()]]'
- '[[Command Injection]]'
- '[[Filter Bypasses]]'
---

# Command Injection with $() Filter Bypass

## Summary

Command injection is a technique that allows an attacker to execute arbitrary commands on a targeted system. By injecting malicious commands into an existing command, an attacker can bypass filters and execute unauthorized actions. The $() filter bypass is a common technique used to bypass filters 

## Description

# Description

Command injection is a technique that allows an attacker to execute arbitrary commands on a targeted system. By injecting malicious commands into an existing command, an attacker can bypass filters and execute unauthorized actions. The $() filter bypass is a common technique used to bypass filters that block traditional command injection techniques. This technique allows an attacker to execute arbitrary commands by wrapping them in $() characters. This can be used to bypass filters that block traditional command injection techniques.

 

## Requirements

1. Access to a vulnerable system

1. Knowledge of the target system's command syntax

 

## Defense

1. Input validation and sanitization can be used to prevent command injection attacks.

1. Limiting the privileges of the user executing the command can minimize the impact of a successful command injection attack.

1. Monitoring system logs for suspicious activity can help detect and respond to command injection attacks.

 

## Objectives

1. Execute arbitrary commands on the target system

1. Bypass filters that block traditional command injection techniques

 

# Instructions

1. To execute arbitrary commands using the $() filter bypass, follow these steps:
1. Identify a vulnerable command on the target system.
2. Inject malicious commands into the existing command using the $() syntax.
3. Execute the modified command to execute the injected commands.

 



**Code**: [[who$()ami
who$(echo am)i
who`echo am`i]]



> The $() filter bypass allows an attacker to execute arbitrary commands by wrapping them in $() characters. This technique can be used to bypass filters that block traditional command injection techniques. In this example, the 'whoami' command is executed using the $() filter bypass. The 'echo' command is also used to inject the string 'am' into the command. The output of the command is the current user on the target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Bypass with $()]]
- [[Command Injection]]
- [[Filter Bypasses]]


