---
id: cmd-011
data: make -j$(nproc)
tags:
  - build
  - compile
type: command
output: 'Compiled binaries, e.g., libcurl.la'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.050Z'
verified: false
validated: true
submitted: true
---
# make-parallel-build

## Command

```bash
make -j$(nproc)
```

## Description

Compiles cURL using all CPU cores for speed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-j$(nproc)` | Parallel jobs | Yes |

## Examples

### Basic Usage

```bash
make -j$(nproc)
```

## Expected Output

Build complete; binaries in src/.

## Related

- [[commands/echo-build-status]]
