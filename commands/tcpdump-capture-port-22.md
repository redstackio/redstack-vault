---
id: 16efebfe-0c63-428b-973a-5b7fc74655cb
name: tcpdump-capture-port-22
type: command
executor: bash
data: tcpdump -i eth0 port 22
output: null
created_at: '2023-04-06T03:56:23.097642+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
platforms:
  - Linux
tags:
  - network-sniffing
  - ssh-capture
verified: true
validated: true
---

# tcpdump-capture-port-22

## Command

```bash
tcpdump -i $_INTERFACE port $_PORT
```

## Description

Captures traffic on a specific port (default 22 for SSH), ideal for monitoring secure shell connections or identifying authentication attempts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_INTERFACE | Interface to capture from (e.g., eth0) | Yes |
| port $_PORT | Port number to filter (e.g., 22) | Yes |

## Examples

### Basic Usage

```bash
tcpdump -i eth0 port 22
```

### Quiet Mode

```bash
tcpdump -q -i eth0 port 22
```

## Expected Output

Packet headers for port 22 traffic:

14:23:45.123456 IP 192.168.1.100.54321 > 192.168.1.200.22: Flags [S], seq 0, win 29200

## Related

- [[procedures/Network-Trace-Capture]]
- [[commands/tcpdump-capture-tcp-packets]]
