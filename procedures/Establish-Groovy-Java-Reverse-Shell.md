---
id: 33037ce2-b247-428f-a332-e6672b4ea0b6
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.698569+00:00'
updated_at: '2023-04-10T20:25:30.872881+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - >-
    [[techniques/Standard Non-Application Layer Protocol|T1095 - Standard
    Non-Application Layer Protocol]]
sub_techniques: []
tags:
  - '[[tags/Groovy]]'
  - '[[tags/Reverse Shell]]'
  - '[[tags/Reverse Shell Cheat Sheet]]'
commands:
  - '[[commands/groovy-execute-reverse-shell-file]]'
platforms:
  - Linux
  - Windows
  - macOS
tools:
  - '[[tools/Groovy]]'
validated: true
---

# Establish-Groovy-Java-Reverse-Shell

## Summary

This procedure demonstrates how to establish a reverse shell on a compromised system using Groovy to execute a Java-based TCP reverse shell payload. The payload connects back to an attacker-controlled listener, providing command execution capabilities with the privileges of the compromised process. It is useful in post-exploitation scenarios where Java is available via Groovy, allowing bypass of some scripting restrictions.

## Description

The Groovy Java Reverse Shell leverages Groovy's ability to run Java code directly to create a TCP-based reverse connection from the target to the attacker's machine. Once connected, the attacker receives a shell session (cmd.exe on Windows or equivalent) for remote command execution. This technique is effective in environments with Groovy installed, such as Java web applications or development servers, and uses standard TCP for communication, making it stealthy but detectable via network monitoring. The payload handles input/output streams between the local process and the remote socket, enabling interactive command execution. Prerequisites include write access on the target to save the script and an active listener on the attacker's side.

## Requirements

1. Groovy installed on the compromised system (version 2.0 or later).
2. Java Runtime Environment (JRE) available, as Groovy depends on it.
3. Write access to a directory on the target to save the script file.
4. Attacker machine with a listener (e.g., netcat) running on the specified host and port.
5. Network connectivity from target to attacker (outbound TCP allowed).

## Defense

- Implement network segmentation and egress filtering to block unauthorized outbound connections to attacker IPs/ports.
- Monitor for unusual TCP connections from internal systems to external hosts using tools like Zeek or Suricata.
- Deploy EDR solutions to detect Groovy script execution and anomalous process behavior (e.g., Java processes spawning shells).
- Enable application whitelisting to restrict Groovy execution in production environments.

## Objectives

1. Establish a persistent command and control channel via TCP reverse connection.
2. Gain interactive shell access on the compromised system for command execution.
3. Enable data exfiltration or further post-exploitation activities through the shell.

## Instructions

### Step 1: Prepare the Reverse Shell Payload

**Context**: Create a Groovy script file containing the Java reverse shell code. This step involves writing the payload to a file on the target system, substituting the attacker's host and port.

Reference the payload code: [[codes/Java-TCP-Reverse-Shell]]

Save the code to a file named `revshell.groovy` using a text editor or echo command on the target.

**Expected Output**: A file `revshell.groovy` created with the exact payload code, customized with the attacker's IP and port.

### Step 2: Set Up Listener on Attacker Machine

**Context**: Before executing the payload, start a listener to catch the incoming connection. This ensures the reverse shell can connect successfully.

Use netcat or a similar tool on the attacker machine:

```bash
nc -lvnp $_ATTACKER_PORT
```

**Expected Output**: Listener starts, waiting for connections on the specified port.

### Step 3: Execute the Groovy Script

**Context**: Run the Groovy script on the target to initiate the reverse connection. This executes the Java code within Groovy, spawning a shell process and forwarding I/O over TCP.

**Command** ([[commands/groovy-execute-reverse-shell-file]]):

```bash
groovy revshell.groovy
```

> This command invokes Groovy to interpret and execute the script, establishing the socket connection and process streams. If successful, the target will connect back to the listener, providing a shell prompt.

**Expected Output**: No visible output on the target if successful; on the attacker side, a new connection appears in the listener with a shell prompt (e.g., `C:\Windows\system32>` on Windows).
