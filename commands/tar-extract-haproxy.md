---
data: tar zxvf haproxy-1.5.3.tar.gz
tags:
  - extract
type: command
executor: bash
platforms:
  - Linux
id: 16d6204a-d677-4b09-9257-aba8a7c26f28
created_at: '2025-12-13T09:01:22.115Z'
updated_at: '2025-12-13T09:01:22.115Z'
verified: false
validated: true
submitted: true
---
# tar Extract HAProxy

## Command

```bash
tar zxvf haproxy-1.5.3.tar.gz
```

## Description

Extracts the gzipped tarball of HAProxy source code, preparing for compilation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `z` | Decompress gzip | Yes |
| `x` | Extract | Yes |
| `v` | Verbose | No |
| `f` | File | Yes |

## Examples

### Basic Usage

```bash
tar zxvf haproxy-1.5.3.tar.gz
```

## Expected Output

Extracted directory haproxy-1.5.3 with source files.

## Related

- [[procedures/Compile-and-Setup-HAProxy-Frontend-Proxy]]
- [[tools/tar]]
