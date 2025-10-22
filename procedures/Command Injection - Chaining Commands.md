---
id: c3e19bb7-ce91-4e1f-8b9a-b3860007f54f
name: Command Injection - Chaining Commands
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.061542+00:00'
updated_at: '2023-04-06T03:55:57.084922+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Chaining commands]]'
- '[[Command Injection]]'
- '[[Exploits]]'
commands:
- '[[List Directory Contents]]'
- '[[List files in current directory]]'
- '[[Pipe Commands Together]]'
- '[[Run Second Command Only If First Fails]]'
- '[[Run Two Commands Together]]'
---

# Command Injection - Chaining Commands

## Summary

Command injection is a technique used by attackers to execute arbitrary commands on a vulnerable system. Chaining commands is a method used to execute multiple commands in sequence, allowing the attacker to perform multiple actions on the system. This can be used to bypass security measures, escala

## Description

# Description

Command injection is a technique used by attackers to execute arbitrary commands on a vulnerable system. Chaining commands is a method used to execute multiple commands in sequence, allowing the attacker to perform multiple actions on the system. This can be used to bypass security measures, escalate privileges, or exfiltrate data. 

In technical terms, command injection occurs when an attacker is able to inject their own commands into a system command that is being executed. This can happen when the system does not properly validate user input, allowing the attacker to inject additional commands. Chaining commands is a technique used to execute multiple commands in sequence, allowing the attacker to perform multiple actions on the system.

From a business perspective, command injection attacks can result in data theft, system downtime, and reputational damage. It is important for organizations to ensure that their systems are properly patched and configured to prevent these types of attacks.

## Requirements

1. Access to a vulnerable system

1. Knowledge of the system and its vulnerabilities

## Defense

1. Validate user input to prevent injection attacks

1. Ensure that systems are properly patched and configured

1. Implement security measures such as firewalls and intrusion detection systems

## Objectives

1. Execute arbitrary commands on a vulnerable system

1. Bypass security measures

1. Escalate privileges

1. Exfiltrate data

# Instructions

1. To chain commands in PowerShell, use the semicolon, ampersand, pipe, or double pipe operators. The semicolon executes both commands, regardless of the success or failure of the first command. The ampersand executes both commands, but only if the first command succeeds. The pipe sends the output of the first command to the input of the second command. The double pipe executes the second command only if the first command fails.

**Code**: [[original_cmd_by_server; ls
original_cmd_by_server ]]

> For example, to list the contents of a directory and then execute a command, you could use the following command:

ls; whoami

This would list the contents of the current directory and then display the current user. If you only wanted to execute the second command if the first command succeeded, you could use the following command:

ls && whoami

This would only execute the second command if the first command succeeded.

**Command** ([[List Directory Contents]]):

```bash
ls
```

**Command** ([[Run Two Commands Together]]):

```bash
original_cmd_by_server && ls
```

**Command** ([[Pipe Commands Together]]):

```bash
original_cmd_by_server | ls
```

**Command** ([[Run Second Command Only If First Fails]]):

```bash
original_cmd_by_server || ls
```

2. To chain commands in Bash, you can simply separate them with a newline character. This will execute each command in sequence.

**Code**: [[original_cmd_by_server
ls]]

> For example, to list the contents of a directory and then execute a command, you could use the following command:

original_cmd_by_server
ls

This would list the contents of the current directory and then display the output of the original command.

**Command** ([[List files in current directory]]):

```bash
ls
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Commands Used

- [[List Directory Contents]]
- [[List files in current directory]]
- [[Pipe Commands Together]]
- [[Run Second Command Only If First Fails]]
- [[Run Two Commands Together]]

## Tags

- [[Chaining commands]]
- [[Command Injection]]
- [[Exploits]]
