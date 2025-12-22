---
type: procedure
description: >-
  Technique to execute long-running commands in the background to evade timeouts
  in command injection scenarios.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - backgrounding-long-running-commands
  - command-injection
commands:
  - '[[commands/bash-nohup-background-sleep]]'
platforms:
  - Linux
  - Unix
tools: []
validated: true
---

# Background-Long-Running-Commands

## Summary

Backgrounding long-running commands is a technique used in command injection attacks to execute prolonged operations without interruption from process timeouts. By using tools like nohup and redirecting output, the command continues running in the background even after the injecting process terminates, allowing attackers to perform tasks such as data exfiltration or persistence establishment.

## Description

In scenarios where an attacker gains command execution via injection vulnerabilities (e.g., in web applications or scripts), the parent process may impose timeouts to limit damage. Backgrounding counters this by detaching the command from the session, making it immune to hangups and allowing it to persist. This is particularly useful for commands like network connections, file downloads, or simulations of long tasks. The technique relies on shell features available in Unix-like systems and maps to execution and evasion tactics in MITRE ATT&CK, as it obscures the command's visibility and prolongs its lifecycle.

## Requirements

1. Access to a shell or command injection point on a Unix-like target system (e.g., Linux).
2. Knowledge of the desired long-running command to execute.
3. No additional tools required beyond standard shell utilities like bash.

## Defense

- Implement strict input validation and sanitization to prevent command injection, using whitelisting for allowed inputs.
- Monitor system logs (e.g., via auditd or syslog) for suspicious background processes, unusual nohup usage, or detached jobs.
- Use process monitoring tools like ps or top to detect orphaned or long-running background tasks, and enforce timeouts at the application level.

## Objectives

1. Execute a long-running command detached from the injecting process to avoid timeouts.
2. Ensure the command runs silently without producing visible output or errors.
3. Verify the command persists after the injection session ends.

## Instructions

### Step 1: Identify the Long-Running Task

**Context**: Determine the command that needs to run for an extended period, such as a sleep simulation for testing or an actual payload like a reverse shell connection. This step ensures the command is suitable for backgrounding.

Replace the example with your actual command, but for demonstration, use sleep to simulate duration.

### Step 2: Execute the Backgrounded Command

**Context**: Use nohup to run the command immune to hangups, redirect output to null to suppress logging, and append & to background it. This detaches the process, allowing it to survive session termination.

**Command** ([[commands/bash-nohup-background-sleep]]):
```bash
nohup sleep 120 > /dev/null &
```

> This command starts a 2-minute sleep in the background. The nohup prevents termination on logout, > /dev/null discards output to avoid detection, and & backgrounds it. After execution, the shell returns a process ID (PID) for the job, confirming it started. Use jobs or ps to verify it's running.
