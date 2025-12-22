---
id: c01689bc-3c3b-4c24-ae4d-c6e2e5754341
name: Command-Injection-Bypass-Using-$@-Syntax
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.330801+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Unix Shell|T1059.004 - Unix Shell]]'
tags:
  - '[[tags/Bypass Blacklisted words]]'
  - '[[tags/Bypass with $@]]'
  - '[[tags/Command Injection]]'
  - '[[tags/Filter Bypasses]]'
commands: []
platforms:
  - Linux
  - Unix
tools: []
validated: true
---

# Command-Injection-Bypass-Using-$-Syntax

## Summary

This procedure demonstrates a command injection technique that bypasses input filters blacklisting specific words like 'whoami' by using the shell's $@ variable syntax to split and reconstruct malicious commands. It is useful in scenarios where an application executes user input as shell commands without proper sanitization, allowing attackers to execute arbitrary commands on Unix-like systems.

## Description

Command injection vulnerabilities occur when an application passes unsanitized user input to system shell commands, enabling attackers to append or modify the executed command. This specific bypass leverages the $@ special variable in Unix shells (e.g., zsh, bash), which expands to all positional parameters as separate words. By inserting $@ into the input, attackers can evade filters that detect complete blacklisted terms (e.g., 'whoami') by breaking them across the expansion point, such as 'who$@ami', which may reconstruct to 'whoami' if $@ expands appropriately or if the filter processes it literally. This technique is particularly effective against naive regex-based filters that do not account for shell variable expansions. The target environment is typically web applications or scripts that invoke shell commands with user-supplied arguments, leading to potential remote code execution (RCE) and system compromise.

## Requirements

1. Access to an input field or parameter that is directly interpolated into a shell command without quoting or validation (e.g., via a vulnerable web form or API endpoint).
2. The target system must use a Unix-like shell (e.g., bash, zsh) where $@ is supported.
3. Knowledge of blacklisted words in the application's input filter (e.g., 'whoami', 'id').
4. Network access to the vulnerable application if it's remote.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization, using whitelisting instead of blacklisting, and avoid direct shell execution of user input (use APIs or parameterized calls instead).
- Employ web application firewalls (WAFs) to detect anomalous shell metacharacters, variable expansions like $@, and injection patterns.
- Run applications with least privilege, isolating them in containers or non-privileged users to limit damage from successful injections.
- Enable logging of all shell executions and monitor for unexpected commands or processes spawned from the application.

## Objectives

1. Identify and confirm the shell environment to tailor the injection payload.
2. Bypass input filters blocking direct command execution.
3. Execute arbitrary commands to enumerate the system or escalate access.
4. Achieve remote code execution leading to potential persistence or data exfiltration.

## Instructions

### Step 1: Identify the Target Shell

**Context**: Determine the shell interpreter used by the vulnerable application to ensure compatibility with $@ expansion and craft the payload accordingly. This step reveals the shell path, which can be piped into for execution.

**Command**:
```bash
echo $0
```

> This command outputs the current shell name or path (e.g., '/usr/bin/zsh'). Use this information to verify Unix shell usage and prepare the injection. If the output indicates a different shell, adjust the payload syntax.

### Step 2: Test Basic Injection with $@ Bypass

**Context**: Inject a split command using $@ to bypass filters. For example, if 'whoami' is blacklisted, use 'who$@ami' where $@ may expand or be ignored by the filter, allowing reconstruction in the shell.

**Code** ([[codes/Bypass-Blacklist-Command-Injection-With-$@]]):

> Execute the injection payload in the vulnerable input field. The code snippet demonstrates the bypass: input 'who$@ami' to attempt execution of 'whoami'. Expected output is the current user if successful, confirming injection. If $@ expands to empty, it becomes 'whoami'; otherwise, test variations based on positional parameters.

### Step 3: Execute Reconstructed Command via Piped Shell

**Context**: Use the identified shell to pipe and execute the full command, ensuring the injection runs in the correct interpreter. This verifies RCE and allows further enumeration.

**Command**:
```bash
echo whoami | $0
```

> This pipes 'whoami' to the shell from Step 1 (e.g., zsh). Replace 'whoami' with other commands like 'id' or 'ls /'. Success is indicated by the command's output (e.g., username or process list) instead of an error or filtered response.
