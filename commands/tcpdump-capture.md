---
id: cmd-003
data: tcpdump -i any -w capture.pcap host demo.stripo.email
tags:
  - network
  - capture
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T09:01:21.506Z'
verified: false
validated: true
submitted: true
---
# Tcpdump Capture

## Command

```bash
tcpdump -i any -w capture.pcap host demo.stripo.email
```

## Description

Captures network traffic for a specific host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Interface | Yes |
| `-w` | Output file | Yes |
| `host` | Filter | Yes |

## Examples

### Basic Usage

```bash
tcpdump -i any -w out.pcap host target
```

## Expected Output

PCAP file with captured packets.

## Related

- [[procedures/Exploit-for-Request-Hijacking]]
