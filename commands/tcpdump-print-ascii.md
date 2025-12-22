---
id: a8449923-df5f-44c3-b4e0-663f2cb5f558
name: tcpdump-print-ascii
type: command
executor: bash
data: tcpdump -A -i eth0
output: null
created_at: '2023-04-06T03:56:23.097531+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
platforms:
  - Linux
tags:
  - network-sniffing
  - ascii-payload
verified: true
validated: true
---

# tcpdump-print-ascii

## Command

```bash
tcpdump -A -i $_INTERFACE
```

## Description

Displays packet payloads in ASCII format for real-time readability, helping spot cleartext data like usernames or passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -A | Print packet contents in ASCII | Yes |
| -i $_INTERFACE | Capture interface | Yes |

## Examples

### Basic Usage

```bash
tcpdump -A -i eth0
```

### Limited Packets

```bash
tcpdump -A -c 10 -i eth0
```

## Expected Output

ASCII representation of payloads:

GET /login HTTP/1.1
Host: example.com
Username: admin

## Related

- [[procedures/Network-Trace-Capture]]
- [[commands/tcpdump-write-to-file]]
