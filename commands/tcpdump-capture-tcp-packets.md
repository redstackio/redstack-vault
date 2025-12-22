---
id: 57f825a1-2578-43a7-a091-6e609515d8d9
name: tcpdump-capture-tcp-packets
type: command
executor: bash
data: tcpdump -i eth0 tcp
output: null
created_at: '2023-04-06T03:56:23.097593+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
platforms:
  - Linux
tags:
  - network-sniffing
  - tcp-filter
verified: true
validated: true
---

# tcpdump-capture-tcp-packets

## Command

```bash
tcpdump -i $_INTERFACE tcp
```

## Description

This command captures only TCP packets on the specified network interface, useful for focusing on reliable, connection-oriented traffic where sensitive data may be exchanged.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_INTERFACE | Network interface to listen on (e.g., eth0, wlan0) | Yes |
| tcp | Filter to TCP protocol only | Yes |

## Examples

### Basic Usage

```bash
tcpdump -i eth0 tcp
```

### With Output Limit

```bash
tcpdump -i eth0 -c 100 tcp
```

## Expected Output

Real-time display of TCP packets:

14:23:45.123456 IP 192.168.1.100.12345 > 192.168.1.200.80: Flags [S], seq 123456789, win 65535, length 0

## Related

- [[procedures/Network-Trace-Capture]]
- [[commands/tcpdump-write-to-file]]
