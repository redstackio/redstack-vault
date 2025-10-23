---
id: 076b62c8-9a84-4a5b-8502-3bc7c1b46ae7
name: Command Injection Filter Bypass with $() and variable expansion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.374486+00:00'
updated_at: '2023-04-06T03:55:57.386961+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Bypass with $()]]'
- '[[Bypass with variable expansion]]'
- '[[Command Injection]]'
- '[[Filter Bypasses]]'
---

# Command Injection Filter Bypass with $() and variable expansion

## Summary

Command injection is a technique that allows an attacker to execute arbitrary commands on a targeted system. In this specific case, the attacker is bypassing a filter that is in place to prevent command injection by using $() and variable expansion. The attacker is able to execute a command that is

## Description

# Description

Command injection is a technique that allows an attacker to execute arbitrary commands on a targeted system. In this specific case, the attacker is bypassing a filter that is in place to prevent command injection by using $() and variable expansion. The attacker is able to execute a command that is stored in a variable by expanding the variable and then executing the command. This technique can be used to bypass security measures and gain access to sensitive information.

 

## Requirements

1. Access to a system with a command injection vulnerability

 

## Defense

1. Implement input validation and sanitization to prevent command injection attacks

1. Limit the privileges of the user executing the command to prevent unauthorized access

1. Use security tools such as intrusion detection systems to detect and prevent command injection attacks

 

## Objectives

1. Execute arbitrary commands on a targeted system

1. Bypass security measures

 

# Instructions

1. 1. Set the variable 'test' to the desired command
2. Use variable expansion to bypass the filter and execute the command
3. The 'cat' command is used to display the contents of the executed command

 



**Code**: [[/???/??t /???/p??s??

test=/ehhh/hmtc/pahhh/hmsswd]]



> The attacker sets the variable 'test' to the desired command and then uses variable expansion to bypass the filter. The '${test//hhh\/hm/}' expression replaces all occurrences of 'hhh/hm' with '/' in the 'test' variable. The '${test//hh??hm/}' expression replaces all occurrences of 'hh' followed by any two characters and then 'hm' with '/' in the 'test' variable. The resulting command is then executed using the 'cat' command.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Bypass with $()]]
- [[Bypass with variable expansion]]
- [[Command Injection]]
- [[Filter Bypasses]]


