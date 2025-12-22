---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - '[[tags/Chaining commands]]'
  - '[[tags/Command Injection]]'
  - '[[tags/Exploits]]'
commands:
  - '[[commands/bash-list-directory-contents]]'
  - '[[commands/bash-chain-commands-with-and]]'
  - '[[commands/bash-chain-commands-with-or]]'
  - '[[commands/bash-chain-commands-with-pipe]]'
  - '[[commands/powershell-chain-commands-with-operators]]'
platforms:
  - Linux
  - Windows
tools: []
verified: true
validated: true
---

# Command-Injection-Chaining-Commands

## Summary

This procedure demonstrates how to chain multiple commands in command injection attacks using operators in Bash and PowerShell, allowing attackers to execute arbitrary sequences of actions on a vulnerable system to bypass restrictions, escalate privileges, or exfiltrate data.

## Description

Command injection vulnerabilities occur when user input is not properly sanitized and is passed directly to system shells, enabling attackers to append or chain additional commands. Chaining allows combining multiple operations, such as reconnaissance followed by privilege escalation, into a single injection point. This is particularly effective in web applications or scripts that execute system commands based on input. In a typical scenario, an attacker identifies an input field (e.g., a ping utility form) that runs a command like `ping $_HOST`, and injects chaining operators to execute additional payloads. The technique targets environments running Bash on Linux/Unix or PowerShell on Windows, assuming low-privilege initial access via the injection vector. Success leads to multi-step execution without repeated injections, increasing stealth and efficiency.

## Requirements

1. Access to a vulnerable application or system that executes unsanitized user input as system commands (e.g., web form invoking `system()` in PHP).
2. Knowledge of the target shell (Bash for Linux/Unix, PowerShell for Windows) and basic syntax for chaining operators.
3. Network access to the target if the injection is remote (e.g., via HTTP POST).
4. Tools like Burp Suite or curl for testing injections in web contexts.

## Defense

Defensive measures and detection strategies:

- Strictly validate and sanitize all user inputs using whitelists, avoiding direct shell execution; use parameterized APIs or libraries like `escapeshellarg()` in PHP.
- Implement web application firewalls (WAFs) to detect common injection patterns like `;`, `&&`, `|`, and `||`.
- Enable command logging and monitoring (e.g., auditd on Linux, PowerShell transcription on Windows) to identify anomalous chained executions.
- Run applications in least-privilege containers or sandboxes to limit impact of injected commands.

## Objectives

1. Execute arbitrary commands on a vulnerable system by injecting chained sequences.
2. Bypass security measures that might block single commands.
3. Escalate privileges through combined reconnaissance and exploitation steps.
4. Exfiltrate data by chaining listing commands with output redirection to attacker-controlled endpoints.

## Instructions

### Step 1: Identify the Injection Point and Test Basic Execution

**Context**: Locate a vulnerable input field that passes data to a shell command (e.g., a diagnostic tool). Test with a simple command to confirm injection works before chaining.

**Command** ([[commands/bash-list-directory-contents]]):
```bash
ls
```

> This command lists files in the current directory. In an injection like `ping $_HOST; ls`, it verifies execution post-original command. Expected output: A list of files and directories, confirming shell access.

### Step 2: Chain Commands in Bash Using Logical Operators

**Context**: Use Bash operators to execute multiple commands sequentially or conditionally, injecting after the original server command (e.g., `ping 127.0.0.1; $_INJECTED`).

**Command** ([[commands/bash-chain-commands-with-and]]):
```bash
original_cmd_by_server && ls
```

> Executes `ls` only if the original command succeeds. Useful for conditional escalation, e.g., check access then download payload. Expected output: Directory listing if original succeeds; nothing if it fails.

**Command** ([[commands/bash-chain-commands-with-or]]):
```bash
original_cmd_by_server || ls
```

> Runs `ls` only if the original fails, helpful for fallback actions like error-based exfiltration. Expected output: Directory listing on failure.

**Command** ([[commands/bash-chain-commands-with-pipe]]):
```bash
original_cmd_by_server | ls
```

> Pipes output of original to `ls`, which may garble results but can chain for data processing (e.g., filter then exfil). Expected output: Processed or combined stdout.

For multi-line chaining in Bash, separate with newlines:

**Code** ([[codes/bash-multi-line-command-chain]]):
```bash
original_cmd_by_server
ls
```

> This executes commands sequentially across lines, ideal for longer payloads in injection fields supporting multi-line input. Expected output: Results from each command in sequence.

### Step 3: Chain Commands in PowerShell

**Context**: On Windows targets, inject into PowerShell executions using operators like semicolon for unconditional chaining or ampersand for conditional.

**Code** ([[codes/powershell-command-chaining-operators]]):
```powershell
original_cmd_by_server; ls
original_cmd_by_server && ls
original_cmd_by_server | ls
original_cmd_by_server || ls   # Only if the first cmd fail
```

> Inject this snippet to run multiple commands. Semicolon runs regardless; `&&` on success; `|` pipes output; `||` on failure. Replace `ls` with actual payloads like `whoami`. Expected output: Sequential or conditional command results, e.g., user info after listing.
