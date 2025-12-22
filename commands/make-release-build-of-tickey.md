---
id: 0557a344-6f6f-4ba0-a084-ad672430d89b
name: make-release-build-of-tickey
type: command
executor: bash
data: make CONF=Release
output: null
created_at: '2023-04-06T03:56:08.565585+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - build
  - compilation
verified: true
validated: true
---

# Make Release Build of Tickey

## Command

```bash
make CONF=Release
```

## Description

Compiles the Tickey tool in release configuration using the Makefile, optimizing for production use and generating the executable binary.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CONF=Release | Build configuration flag for release mode (optimized, no debug symbols) | Yes |

## Examples

### Basic Usage

```bash
make CONF=Release
```

### Clean Build

```bash
make clean && make CONF=Release
```

## Expected Output

make -C src CONF=Release
[compilation logs...]
gcc ... -o tickey ...

## Related

- [[procedures/extract-ccache-tickets-from-linux-keyring-with-tickey]]
- [[tools/tickey]]
