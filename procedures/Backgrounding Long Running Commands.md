---
id: 2f2d69f8-c9ba-4ce0-9414-d4ee04a7c788
name: Backgrounding Long Running Commands
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.568345+00:00'
updated_at: '2023-04-06T03:55:57.581554+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Backgrounding long running commands]]'
- '[[Command Injection]]'
commands:
- '[[Sleep for 2 minutes]]'
---

# Backgrounding Long Running Commands

## Summary

Backgrounding long running commands is a technique used to bypass time-outs of injected processes. The attacker can use this technique to run a command that takes a long time to complete, without the risk of it being killed by the process injecting it. This technique is commonly used in command inj

## Description

# Description

Backgrounding long running commands is a technique used to bypass time-outs of injected processes. The attacker can use this technique to run a command that takes a long time to complete, without the risk of it being killed by the process injecting it. This technique is commonly used in command injection attacks.

 

## Requirements

1. Access to a vulnerable system with a command injection vulnerability.

 

## Defense

1. Use input validation and sanitization techniques to prevent command injection vulnerabilities.

1. Monitor system logs for suspicious activity, such as long running commands or backgrounded processes.

1. Implement network segmentation and access controls to limit the impact of a successful command injection attack.

 

## Objectives

1. Execute a long running command without the risk of it being killed by the process injecting it.

 

# Instructions

1. To background a long running command, use the following command:

nohup <command> > /dev/null &

Replace <command> with the command you want to run in the background.

 



**Code**: [[nohup sleep 120 > /dev/null &]]



> The 'nohup' command is used to run a command immune to hangups, with output to a non-tty. The 'sleep' command is used to simulate a long running command. The '>/dev/null' part of the command is used to redirect the output to a null device, which means that the output will not be saved anywhere. Finally, the '&' symbol is used to background the command. This will allow the command to continue running even after the process that injected it has timed out.



**Command** ([[Sleep for 2 minutes]]):

```bash
nohup sleep 120 > /dev/null &
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Commands Used

- [[Sleep for 2 minutes]]

## Tags

- [[Backgrounding long running commands]]
- [[Command Injection]]


