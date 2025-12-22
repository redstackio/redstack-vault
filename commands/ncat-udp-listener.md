---
id: 236ee5f6-f7cd-4b1b-8c5d-8b9c25248e8b
name: ncat-udp-listener
type: command
executor: bash
data: ncat --udp -lvp $_PORT
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - listener
  - reverse-shell
verified: true
validated: true
---

# ncat-udp-listener

## Command

```bash
ncat --udp -lvp $_PORT
```

## Description

Starts an Ncat UDP listener for incoming datagram-based connections. Less reliable for interactive shells than TCP but useful for certain payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | The port to listen on (e.g., 4242) | Yes |
| --udp | Specifies UDP protocol | Built-in |
| -l | Listen mode | Built-in |
| -v | Verbose output | Built-in |
| -p | Port specification | Built-in |

## Examples

### Basic Usage

```bash
ncat --udp -lvp 4242
```

## Expected Output

Ncat: Version 7.94 ( https://nmap.org/ncat )
Listening on :::4242

(Handles UDP packets; verbose shows incoming data.)

## Related

- [[commands/ncat-tcp-listener]]
- [[procedures/linux-reverse-shell-persistence-via-ncat-systemd]]
