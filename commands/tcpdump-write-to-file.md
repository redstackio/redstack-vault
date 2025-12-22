---
id: b4e70500-ed15-48bb-9ae6-14906a28f7fb
name: tcpdump-write-to-file
type: command
executor: bash
data: tcpdump -w 0001.pcap -i eth0
output: null
created_at: '2023-04-06T03:56:23.097459+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
platforms:
  - Linux
tags:
  - network-sniffing
  - pcap-save
verified: true
validated: true
---

# tcpdump-write-to-file

## Command

```bash
tcpdump -w $_FILENAME.pcap -i $_INTERFACE
```

## Description

Writes captured packets to a PCAP file for later analysis, avoiding real-time display overhead.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -w $_FILENAME.pcap | Output file name | Yes |
| -i $_INTERFACE | Interface to capture | Yes |

## Examples

### Basic Usage

```bash
tcpdump -w capture.pcap -i eth0
```

### With Filter

```bash
tcpdump -w capture.pcap -i eth0 port 80
```

## Expected Output

No console output during capture; file grows in size. Stop with Ctrl+C.

## Related

- [[procedures/Network-Trace-Capture]]
- [[commands/tcpdump-print-ascii]]
