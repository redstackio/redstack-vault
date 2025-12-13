---
data: make TARGET=linux2628
tags:
  - compile
type: command
executor: bash
platforms:
  - Linux
id: b8dc964e-e71b-41ee-9099-2e8b545e79c8
created_at: '2025-12-13T09:01:22.106Z'
updated_at: '2025-12-13T09:01:22.106Z'
verified: false
validated: true
submitted: true
---
# make Compile HAProxy

## Command

```bash
make TARGET=linux2628
```

## Description

Compiles HAProxy source code for Linux kernel 2.6.28+.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `TARGET` | Specifies the build target platform | Yes |

## Examples

### Basic Usage

```bash
make TARGET=linux2628
```

## Expected Output

Compiled HAProxy binary in the current directory.

## Related

- [[procedures/Compile-and-Setup-HAProxy-Frontend-Proxy]]
- [[tools/make]]
