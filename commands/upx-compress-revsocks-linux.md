---
id: 563063ce-17c2-4ac4-b029-5c9e209756c6
name: upx-compress-revsocks-linux
type: command
executor: bash
data: upx --brute revsocks
output: null
created_at: '2023-04-06T03:56:22.907722Z'
updated_at: '2023-04-10T20:25:18.397562Z'
platforms:
  - Linux
tags:
  - compression
  - evasion
verified: true
validated: true
---

# upx-compress-revsocks-linux

## Command

```bash
upx --brute revsocks
```

## Description

Compresses the Linux revsocks binary using UPX with brute force optimization for maximum size reduction and evasion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --brute | Aggressive compression | No |
| revsocks | Binary file | Yes |

## Examples

### Basic Usage

```bash
upx --brute revsocks
```

## Expected Output

File size         Method      Packed Size
revsocks          UPX!        X -> Y (Z%)

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
