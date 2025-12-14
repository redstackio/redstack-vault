---
id: cmd-uuid-2
data: ltrace ping 0x7f.1 2>&1 | grep 0x7f.1
tags:
  - os-resolution
  - inet_aton
type: command
output: 'inet_aton("0x7f.1", { 0x100007f }) = 1'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.674Z'
verified: false
validated: true
submitted: true
---
# ltrace-ping-hex-ip

## Command

```bash
ltrace ping 0x7f.1 2>&1 | grep 0x7f.1
```

## Description

Traces system calls during ping to show OS-level resolution of hexadecimal IP to 127.0.0.1 via inet_aton, contrasting Ruby Resolv failure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 0x7f.1 | Hex IP for 127.0.0.1 | Yes |

## Examples

### Basic Usage

```bash
ltrace ping 0x7f.1 2>&1 | grep 0x7f.1
```

## Expected Output

inet_aton("0x7f.1", { 0x100007f }) = 1

## Related

- [[commands/ltrace-ping-decimal-ip]]
- [[procedures/Bypass-SSRF-Filters-with-Hex-and-Decimal-IPs]]
