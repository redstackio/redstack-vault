---
data: nc -v -u -l 12346
tags:
  - listener
  - udp
type: command
output: >-
  Connection from [Imgur IP] 12346 udp accepted; e.g.,
  TESTUDPPACKEToctettsize0blksize512timeout6
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.994Z'
id: ca3c80a8-56a8-49f6-b6e4-f6c0c4ce0836
verified: false
validated: true
submitted: true
---
# nc-listen-udp-verbose

## Command

```bash
nc -v -u -l 12346
```

## Description

Listen for incoming UDP packets on port 12346 with verbose output to capture TFTP or other UDP-based SSRF payloads from Imgur.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | Yes |
| `-u` | UDP mode | Yes |
| `-l` | Listen mode | Yes |
| `12346` | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
nc -v -u -l 12346
```

### Advanced Usage

```bash
nc -v -u -l 12346 -w 5
```

> With short timeout for UDP.

## Expected Output

UDP packet data received, such as TFTP options string.

## Related

- [[commands/nc-listen-tcp-verbose]]
- [[procedures/Demonstrate-UDP-SSRF-with-TFTP-and-Netcat]]
