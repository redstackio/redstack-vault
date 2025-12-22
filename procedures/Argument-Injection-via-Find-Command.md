---
type: procedure
description: >-
  Demonstrates argument injection into the Unix 'find' command via PHP system()
  calls to execute arbitrary commands like reading sensitive files.
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
  - >-
    [[techniques/Command-and-Scripting-Interpreter/Command-Line-Interface|T1059.003
    - Windows Command Shell]]
sub_techniques: []
tags:
  - '[[tags/Argument-Injection]]'
  - '[[tags/FIND]]'
  - '[[tags/List-of-exposed-commands]]'
commands: []
platforms:
  - Linux
  - PHP
tools: []
validated: true
---

# Argument-Injection-via-Find-Command

## Summary

This procedure exploits argument injection vulnerabilities in applications that use the Unix 'find' command via system calls, such as in PHP scripts. By controlling the filename parameter passed to 'find', an attacker can inject find-specific options like '-exec' to execute arbitrary commands on the target system, such as reading sensitive files like /etc/passwd. This technique bypasses basic shell escaping like escapeshellcmd, as it targets the program's argument parsing rather than shell metacharacters.

## Description

Argument injection into the 'find' command occurs when user input is directly concatenated into the command line without proper validation or argument-level escaping. The 'find' utility interprets options like -iname for pattern matching, but injected flags such as -or or -exec can alter its behavior to run external commands. For example, in a PHP web application that searches for files based on user input, an attacker can supply a crafted filename to trigger command execution. This is particularly dangerous in environments with elevated privileges, allowing unauthorized access to system files, data exfiltration, or further compromise. The procedure assumes access to inject into a parameter used in a system('find ...') call and targets Linux/Unix systems where 'find' is available.

## Requirements

1. Ability to inject controlled input into a parameter that is passed to the 'find' command via system(), exec(), or similar functions in PHP or another scripting language.
2. Target system running Linux/Unix with the 'find' utility installed (standard on most distributions).
3. PHP runtime environment if exploiting via web application (version 5+ with system() enabled).
4. No need for direct shell access; injection can occur remotely via web forms or APIs.

## Defense

- Validate and sanitize all user inputs intended for command-line arguments; use whitelisting for allowed characters in filenames (e.g., alphanumeric only) rather than relying on escapeshellcmd, which does not prevent argument injection into tools like 'find'.
- Avoid constructing dynamic commands with user input; use safer APIs like find's built-in predicates or language-specific libraries (e.g., PHP's glob() or scandir()).
- Run applications with least privilege; disable dangerous functions like system(), exec(), and shell_exec() in PHP via disable_functions in php.ini.
- Monitor logs for anomalous 'find' executions, such as unusual -exec actions or access to sensitive paths like /etc/; implement command-line auditing with tools like auditd on Linux.

## Objectives

1. Inject crafted arguments into the 'find' command to execute arbitrary system commands.
2. Read sensitive files such as /etc/passwd to enumerate users and hashed passwords.
3. Escalate access or exfiltrate data by chaining additional commands in the injection payload.

## Instructions

### Step 1: Understand Safe Execution

**Context**: Review how the 'find' command should be executed safely using escapeshellcmd to escape shell metacharacters, though note this does not prevent find-specific argument injection.

**Code** ([[codes/PHP-Find-Command-Safe-Example]]):

```php
$file = "some_file";
system("find /tmp -iname " . escapeshellcmd($file));
```

> This step executes a benign search for a file named 'some_file' in /tmp. The escapeshellcmd() function prevents shell injection (e.g., ; rm -rf /), but allows find options to pass through unchanged. Expected output: No files found if 'some_file' doesn't exist, or a list of matching paths. Verify by checking for no unintended command execution (e.g., no output from /etc/passwd).

### Step 2: Inject Argument to Execute Command

**Context**: Craft an input that injects find options to run an arbitrary command, such as cat /etc/passwd, by appending flags like -or -exec ... ; -quit to the filename pattern. This tricks 'find' into evaluating the injected logic.

**Code** ([[codes/PHP-Find-Command-Argument-Injection-Read-Passwd]]):

```php
$file = "sth -or -exec cat /etc/passwd ; -quit";
system("find /tmp -iname " . escapeshellcmd($file));
```

> Submit the injected filename via the vulnerable input field (e.g., a web form parameter). The payload uses -or to short-circuit the search and -exec to run cat /etc/passwd, terminated by ; -quit to end the expression. Expected output: Contents of /etc/passwd displayed, including usernames and hashed passwords (e.g., root:x:0:0:root:/root:/bin/bash). If successful, no search results for 'sth' but the file contents appear. Decision point: If /etc/passwd is not readable, try less sensitive files like /etc/hosts; if blocked, encode the payload to evade filters.
