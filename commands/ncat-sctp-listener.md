---
id: 00324f00-9bda-4c76-9c38-efce10a913bf
name: ncat-sctp-listener
type: command
executor: bash
data: ncat --sctp -lvp $_PORT
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

# ncat-sctp-listener

## Command

```bash
ncat --sctp -lvp $_PORT
```

## Description

Starts an Ncat SCTP listener for stream control transmission protocol connections. SCTP provides multi-streaming but requires kernel support and is uncommon for shells.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | The port to listen on (e.g., 4242) | Yes |
| --sctp | Specifies SCTP protocol | Built-in |
| -l | Listen mode | Built-in |
| -v | Verbose output | Built-in |
| -p | Port specification | Built-in |

## Examples

### Basic Usage

```bash
ncat --sctp -lvp 4242
```

## Expected Output

Ncat: Version 7.94 ( https://nmap.org/ncat )
Listening on :::4242

(Upon connection: Accepts SCTP stream.)

## Related

- [[commands/ncat-tcp-listener]]
- [[procedures/linux-reverse-shell-persistence-via-ncat-systemd]]
