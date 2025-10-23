---
id: c01689bc-3c3b-4c24-ae4d-c6e2e5754341
name: Command Injection with $@
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.330801+00:00'
updated_at: '2023-04-06T03:55:57.343205+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Bypass Blacklisted words]]'
- '[[Bypass with $@]]'
- '[[Command Injection]]'
- '[[Filter Bypasses]]'
---

# Command Injection with $@

## Summary

Command injection is a technique used by attackers to execute arbitrary commands on a target system. In this specific case, the attacker is attempting to bypass blacklisted words by using the $@ syntax. This technique allows the attacker to pass arguments to a command, even if those arguments conta

## Description

# Description

Command injection is a technique used by attackers to execute arbitrary commands on a target system. In this specific case, the attacker is attempting to bypass blacklisted words by using the $@ syntax. This technique allows the attacker to pass arguments to a command, even if those arguments contain spaces or other special characters that would normally be interpreted by the shell. By using this technique, the attacker can execute arbitrary commands and potentially gain full control of the target system.

From a technical perspective, this attack works by taking advantage of the way that shells parse command-line arguments. When a command is executed, the shell splits the command line into individual arguments based on whitespace. By using the $@ syntax, the attacker can pass an array of arguments to the command, which will be treated as separate arguments by the shell, even if they contain spaces or other special characters.

The business value of this attack is significant, as it can allow an attacker to gain full control of a target system and potentially access sensitive data or disrupt critical operations.

 

## Requirements

 

## Defense

1. Implement input validation and filtering to prevent the injection of malicious commands

1. Use an application firewall to block known attack patterns and prevent command injection attacks

1. Limit the privileges of user accounts to prevent attackers from gaining full control of the system

 

## Objectives

1. Execute arbitrary commands on a target system

1. Bypass blacklisted words in command input

 

# Instructions

1. To execute this command, simply copy and paste it into the command prompt or shell on the target system.

 



**Code**: [[who$@ami

echo $0
-> /usr/bin/zsh
echo whoami|$0]]



> The command works by injecting the 'whoami' command into the system using the $@ syntax. The $@ syntax allows the attacker to pass arguments to the command, even if those arguments contain spaces or other special characters that would normally be interpreted by the shell. The 'echo $0' command is used to determine which shell is being used, and the 'echo whoami|$0' command is used to execute the 'whoami' command within that shell.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Bypass Blacklisted words]]
- [[Bypass with $@]]
- [[Command Injection]]
- [[Filter Bypasses]]


