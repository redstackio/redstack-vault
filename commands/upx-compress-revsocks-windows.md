---
id: 7c02a62f-2c95-4de9-af2e-c15abec07113
name: upx-compress-revsocks-windows
type: command
executor: bash
data: upx revsocks.exe
output: null
created_at: '2023-04-06T03:56:22.908058Z'
updated_at: '2023-04-10T20:25:18.397562Z'
platforms:
  - Windows
tags:
  - compression
  - evasion
verified: true
validated: true
---

# upx-compress-revsocks-windows

## Command

```bash
upx revsocks.exe
```

## Description

Compresses the Windows revsocks executable using UPX.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| revsocks.exe | Binary file | Yes |

## Examples

### Basic Usage

```bash
upx revsocks.exe
```

## Expected Output

File size         Method      Packed Size
revsocks.exe      UPX!        X -> Y (Z%)

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
