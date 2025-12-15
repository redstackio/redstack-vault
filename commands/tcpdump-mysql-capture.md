---
data: tcpdump -s 0 port 3306 -i eth0 -w infogramsteal.pcap
tags:
  - network
  - capture
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.667Z'
id: 2cc27719-9243-4c59-b031-3880326b56a5
verified: false
validated: true
submitted: true
---
# tcpdump-mysql-capture

## Command

```bash
tcpdump -s 0 port 3306 -i eth0 -w infogramsteal.pcap
```

## Description

This command captures all network traffic on MySQL port 3306 using the eth0 interface, saving full packets to a PCAP file for analysis of exfiltrated data from Infogram LFI exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s 0 | Capture full packet size (no truncation) | Yes |
| port 3306 | Filter for MySQL traffic | Yes |
| -i eth0 | Specify input interface | Yes |
| -w infogramsteal.pcap | Output file in PCAP format | Yes |

## Examples

### Basic Usage

```bash
tcpdump -s 0 port 3306 -i eth0 -w capture.pcap
```

### Advanced Usage

```bash
tcpdump -s 0 -i any port 3306 -w fullcapture.pcap -v
```

## Expected Output

Real-time display of captured packets (e.g., IP attacker > infogram: Flags [S.], seq 12345), with data written to infogramsteal.pcap. Stop with Ctrl+C.

## Related

- [[Related Procedure: Capture-MySQL-Traffic-with-tcpdump]]
