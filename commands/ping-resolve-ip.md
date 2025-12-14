---
id: cmd-ping-resolve
data: ping zomato.com
tags:
  - recon
type: command
output: PING zomato.com (52.77.124.190) 56(84) bytes of data.
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.247Z'
verified: false
validated: true
submitted: true
---
# ping-resolve-ip

## Command

```bash
ping zomato.com
```

## Description

Resolves the domain to IP and tests connectivity via ICMP echoes, useful for initial target identification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | Target domain to ping | Yes |

## Examples

### Basic Usage

```bash
ping zomato.com
```

### Advanced Usage

```bash
ping -c 4 zomato.com
```

## Expected Output

Displays resolved IP 52.77.124.190 and round-trip times.

## Related

- [[commands/nmap-host-scan]]
