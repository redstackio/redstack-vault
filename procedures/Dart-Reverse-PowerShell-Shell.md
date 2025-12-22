---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/PowerShell|T1059.001 - PowerShell]]'
tags:
  - '[[tags/Dart]]'
  - '[[tags/Reverse Shell]]'
commands:
  - '[[commands/nc-tcp-listener]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Dart-Reverse-PowerShell-Shell

## Summary

This procedure uses a Dart script to establish a reverse PowerShell shell on a Windows target system. The script runs on the target, connects back to an attacker-controlled listener, and allows remote execution of PowerShell commands for post-exploitation activities such as command execution, file manipulation, and lateral movement.

## Description

In a typical red team engagement, after initial access to a Windows target, this procedure deploys a lightweight Dart-based reverse shell payload. The Dart script initiates a TCP connection to the attacker's listener, spawns a PowerShell process on the target, and relays commands received over the socket to PowerShell's stdin while streaming stdout back. This provides interactive shell access without relying on common tools like Netcat. The technique is useful in environments where Dart runtime is available or can be sideloaded, and it maps to MITRE ATT&CK Execution tactics by leveraging PowerShell as the interpreter. Prerequisites include network outbound access from the target to the attacker's IP/port and Dart SDK installed on the target.

## Requirements

1. Dart SDK installed on the target Windows system (version 2.0+ for dart:io support).
2. Outbound network access from the target to the attacker's IP and port (e.g., TCP 4444).
3. Attacker machine with a TCP listener (e.g., Netcat) ready to receive the connection.
4. Initial access to the target to deploy and execute the Dart script (e.g., via file upload or existing shell).

## Defense

- Restrict Dart runtime installation and execution on endpoints using application whitelisting (e.g., AppLocker or WDAC).
- Monitor for unusual outbound TCP connections from non-standard processes like dart.exe to high ports.
- Enable PowerShell logging (Module, ScriptBlock, and Transcription) to detect interactive command execution from spawned processes.
- Network segmentation to block lateral connections and use EDR tools to alert on process injection or socket usage by scripting interpreters.

## Objectives

1. Establish persistent interactive access to the target via PowerShell.
2. Execute remote commands for reconnaissance, privilege escalation, or data exfiltration.
3. Maintain command and control (C2) over the compromised Windows host.

## Instructions

### Step 1: Prepare the Listener on Attacker Machine

**Context**: Set up a TCP listener to receive the incoming reverse shell connection from the target. This allows sending commands and receiving output.

**Command** ([[commands/nc-tcp-listener]]):
```bash
nc -lvnp $_ATTACKER_PORT
```

> This command starts a Netcat listener on the specified port. Replace $_ATTACKER_PORT with your chosen port (e.g., 4444). Expected output includes a message like "Listening on [0.0.0.0] (family 0, port 4444)" confirming the listener is active. Once the target connects, you'll see a new connection and can type commands directly.

### Step 2: Customize and Deploy the Dart Payload on Target

**Context**: Edit the Dart script with the attacker's IP and port, then save it as a .dart file on the target system. This payload will be executed to initiate the reverse connection.

**Code Reference** ([[codes/Dart-Reverse-PowerShell-Payload]]):

The code connects to the listener and spawns PowerShell locally on the target.

> Manually replace the hardcoded IP ("10.0.0.1") and port (4242) in the script with your attacker's details (e.g., attacker's IP and 4444). Save as reverse_shell.dart on the target via your initial access method (e.g., upload using existing shell or SMB). Expected: File saved without errors, ready for execution.

### Step 3: Execute the Dart Script on Target

**Context**: Run the Dart script on the target to establish the reverse shell. This spawns PowerShell and connects back to your listener.

**Instructions**: From an existing shell or command prompt on the target, execute:
```bash
dart run reverse_shell.dart
```

> This compiles and runs the script inline. Expected: No output if successful (silent connection); check your listener for incoming connection. If Dart is not in PATH, use the full path to dart.exe. Success is indicated by the listener showing a new connection and accepting input (e.g., type 'whoami' to test).

### Step 4: Interact with the Shell

**Context**: Use the established connection to send PowerShell commands and receive output for further operations.

**Instructions**: In the Netcat listener terminal, enter PowerShell commands directly (e.g., 'Get-Process' or 'dir C:\'). The script relays input to PowerShell stdin and stdout back over the socket.

> Expected: Real-time command execution and output mirroring a local PowerShell session. For example, 'whoami' should return the current user on the target. If the connection drops, re-execute the script on target.
