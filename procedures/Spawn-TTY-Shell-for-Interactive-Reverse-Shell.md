---
type: procedure
description: >-
  Upgrades a basic reverse shell to a fully interactive TTY shell on Linux
  systems, enabling stable command execution and user switching.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Unix Shell]]'
sub_techniques: []
tags:
  - reverse-shell
  - tty-shell
  - post-exploitation
  - linux
commands:
  - '[[commands/script-create-pty-bash]]'
  - '[[commands/su-switch-to-user]]'
platforms:
  - Linux
tools: []
validated: true
---

# Spawn-TTY-Shell-for-Interactive-Reverse-Shell

## Summary

This procedure upgrades a non-interactive reverse shell to a fully interactive pseudo-TTY (PTY) shell on Linux systems. It uses the 'script' utility to allocate a PTY and then allows switching to another user with 'su', providing stable interactivity for commands that require a terminal, such as sudo, vi, or file transfers. This is essential in post-exploitation scenarios where basic reverse shells lack proper terminal emulation.

## Description

In red team operations or penetration testing, reverse shells established via tools like netcat or Python often run without a proper PTY, leading to limitations like inability to use arrow keys, tab completion, or commands requiring tty (e.g., 'su: must be run from a terminal'). This procedure addresses that by invoking the 'script' command, which records a session but can be configured to discard output and spawn an interactive bash shell within a PTY. Optionally, it then uses 'su' to pivot to a target user if credentials are known, simulating physical console access. The technique assumes an existing reverse shell session and targets Unix-like environments with bash and script available. Success results in a resilient shell resistant to disconnection and capable of full system interaction.

## Requirements

1. An active reverse shell session on the target Linux system (e.g., via netcat, Python, or similar).
2. Bash and /usr/bin/script available on the target (standard on most Linux distributions).
3. Valid credentials (username and password) for the target user if performing user switching.
4. No sudo restrictions or PAM configurations blocking tty-less su attempts.

## Defense

- Enable process auditing (e.g., via auditd) to log executions of 'script' and 'su' in non-standard contexts, such as from network-initiated processes.
- Implement kernel-level restrictions like AppArmor or SELinux to limit shell spawning from untrusted sources.
- Monitor for anomalous shell behaviors, such as unexpected PTY allocations or su attempts from low-privilege processes, using tools like Sysdig or OSSEC.
- Enforce multi-factor authentication (MFA) for user switching and restrict su/sudo to physical consoles via PAM configurations.

## Objectives

1. Upgrade the reverse shell to support full terminal interactivity, resolving tty-related errors.
2. Enable seamless user context switching to escalate access or maintain persistence.
3. Provide a stable environment for further post-exploitation activities like file manipulation or privilege escalation.

## Instructions

### Step 1: Allocate PTY with Script Command

**Context**: This step creates a pseudo-terminal using the 'script' utility, which spawns a new bash shell. The '-q' flag suppresses messages, '-c' runs the specified command, and '/dev/null' discards any logging, ensuring a clean interactive session. This resolves common reverse shell limitations.

**Command** ([[commands/script-create-pty-bash]]):
```bash
/usr/bin/script -qc /bin/bash /dev/null
```

> Run this directly in the reverse shell. It should immediately provide a new bash prompt with full tty support. Verify by testing arrow keys for history or running 'stty -a' to check terminal settings.

### Step 2: Switch to Target User

**Context**: With the PTY now active, use 'su' to switch to a different user context. This requires entering the target user's password when prompted. Replace 'user' with the actual username (e.g., 'root' or a service account). This step is optional but enhances access if credentials are available.

**Command** ([[commands/su-switch-to-user]]):
```bash
su - user
```

> After execution, provide the password at the prompt. Success is indicated by a new shell prompt prefixed with the target username (e.g., 'user@hostname:~$'). If the password is incorrect, it will fail with 'su: Authentication failure'; retry with correct creds or skip if not needed.
