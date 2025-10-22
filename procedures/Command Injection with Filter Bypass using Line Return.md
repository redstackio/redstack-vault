---
id: 5bd56b39-1cc4-49de-88a6-83f6adf39caf
name: Command Injection with Filter Bypass using Line Return
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.134465+00:00'
updated_at: '2023-04-06T03:55:57.148451+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Bypass with a line return]]'
- '[[Command Injection]]'
- '[[Filter Bypasses]]'
commands:
- '[[View Password File]]'
---

# Command Injection with Filter Bypass using Line Return

## Summary

Command Injection with Filter Bypass using Line Return is a technique used to bypass input validation filters and execute arbitrary commands on a target system. This technique involves inserting a line return character (%0A) into the injected command, which can bypass certain input validation filte

## Description

# Description

Command Injection with Filter Bypass using Line Return is a technique used to bypass input validation filters and execute arbitrary commands on a target system. This technique involves inserting a line return character (%0A) into the injected command, which can bypass certain input validation filters. The attacker can then execute any command on the target system, including reading or writing files, stealing data, or creating new user accounts. This technique can be used to gain unauthorized access to a target system and carry out malicious activities.

## Requirements

1. Access to a vulnerable web application or other input validation filter

1. Knowledge of the target system's operating system and commands

## Defense

1. Implement input validation filters to prevent command injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Limit user privileges to prevent attackers from executing arbitrary commands

## Objectives

1. Execute arbitrary commands on a target system

1. Bypass input validation filters

# Instructions

1. Inject the following command into the vulnerable input field:

**Code**: [[something%0Acat%20/etc/passwd]]

> This command injects a line return character (%0A) into the 'something' command, which can bypass input validation filters and execute the 'cat /etc/passwd' command on the target system. This command reads the contents of the password file and returns them to the attacker.

**Command** ([[View Password File]]):

```bash
something
cat /etc/passwd
```

2. Inject the following command into the vulnerable input field:

**Code**: [[;cat>/tmp/hi<<EOF%0ahello%0aEOF
;cat</tmp/hi
hello]]

> This command injects a command that creates a file on the target system. The command creates a file called 'hi' in the '/tmp' directory and writes the text 'hello' to the file. The attacker can then use the 'cat' command to read the contents of the file and confirm that it was successfully created.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Commands Used

- [[View Password File]]

## Tags

- [[Bypass with a line return]]
- [[Command Injection]]
- [[Filter Bypasses]]
