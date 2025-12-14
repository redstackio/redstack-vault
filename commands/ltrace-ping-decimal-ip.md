---
id: cmd-uuid-4
data: ltrace ping 2130706433 2>&1 | grep 2130706433
tags:
  - os-resolution
  - inet_aton
type: command
output: 'inet_aton("2130706433", { 0x100007f }) = 1'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.667Z'
verified: false
validated: true
submitted: true
---
# ltrace-ping-decimal-ip

## Command

```bash
ltrace ping 2130706433 2>&1 | grep 2130706433
```

## Description

Traces ping to demonstrate OS resolution of decimal IP to localhost, enabling SSRF despite Resolv failure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 2130706433 | Decimal IP for 127.0.0.1 | Yes |

## Examples

### Basic Usage

```bash
ltrace ping 2130706433 2>&1 | grep 2130706433
```

## Expected Output

inet_aton("2130706433", { 0x100007f }) = 1

## Related

- [[commands/ltrace-ping-hex-ip]]
- [[procedures/Bypass-SSRF-Filters-with-Hex-and-Decimal-IPs]]
