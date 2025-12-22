---
id: cmd-uuid-2
data: 'CFLAGS="-O0 -g -fsanitize=address" CXXFLAGS="${CFLAGS}" ./configure'
tags:
  - build
  - debug
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.216Z'
verified: false
validated: true
submitted: true
---
# configure-squid-with-asan

## Command

```bash
CFLAGS="-O0 -g -fsanitize=address" CXXFLAGS="${CFLAGS}" ./configure
```

## Description

Configures Squid build environment with AddressSanitizer flags for detecting heap overflows during compilation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -O0 | Disable optimization | Yes |
| -g | Include debug symbols | Yes |
| -fsanitize=address | Enable ASAN | Yes |

## Examples

### Basic Usage

```bash
CFLAGS="-O0 -g -fsanitize=address" CXXFLAGS="${CFLAGS}" ./configure
```

### Advanced Usage

```bash
export CFLAGS="-O0 -g -fsanitize=address"; CXXFLAGS="$CFLAGS" ./configure --prefix=/usr/local
```

## Expected Output

Configure script runs successfully, detecting compiler support for ASAN.

## Related

- [[Related Procedure: Build-and-Run-Squid-with-AddressSanitizer]]
