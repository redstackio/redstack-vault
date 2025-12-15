---
id: cmd-uuid-4
data: 'tcpdump -nni venet0 -e icmp[icmptype] == 8'
tags:
  - network
  - icmp
  - capture
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.005Z'
verified: false
validated: true
submitted: true
---
# tcpdump-icmp-listen

## Command

```bash
tcpdump -nni venet0 -e icmp[icmptype] == 8
```

## Description

Captures ICMP echo request packets (type 8) on a Linux network interface to verify remote command execution via ping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -nni | No DNS, interface venet0, non-promiscuous | Yes |
| -e | Print link-level header | Yes |
| icmp[icmptype] == 8 | Filter for echo requests | Yes |

## Examples

### Basic Usage

```bash
tcpdump -nni venet0 -e icmp[icmptype] == 8
```

### Advanced Usage

```bash
tcpdump -nni any -e icmp[icmptype] == 8 -w capture.pcap
```

## Expected Output

IP target_ip > listener_ip: ICMP echo request, id X, seq Y, length Z (packet details with source from exploited server).

## Related

- [[procedures/Verify-RCE-with-ICMP-Listener]]
