---
type: command
executor: bash
data: ./build-alpine -a i686
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - image-building
verified: true
validated: true
---

# Build-Alpine-Image-i686

## Command

```bash
./build-alpine -a i686
```

## Description

Builds a minimal Alpine Linux image for i686 architecture using the lxd-alpine-builder script, producing a tar.gz file importable into LXD.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a i686 | Architecture flag (i686 for 32-bit compatibility) | Yes |

## Examples

### Basic Usage

```bash
./build-alpine -a i686
```

### For x86_64

```bash
./build-alpine -a x86_64
```

## Expected Output

Building Alpine image...
Image built: alpine-i686.tar.gz

Tarball file generated in current directory.

## Related

- [[procedures/Linux-Privilege-Escalation-via-LXC-LXD-Alpine-Image]]
