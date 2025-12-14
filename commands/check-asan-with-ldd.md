---
id: cmd-uuid-4
data: ldd squid | grep asan
tags:
  - verify
  - binary
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.208Z'
verified: false
validated: true
submitted: true
---
# check-asan-with-ldd

## Command

```bash
ldd squid | grep asan
```

## Description

Checks dynamic library dependencies of the Squid binary for AddressSanitizer linkage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| squid | Path to Squid executable | Yes |

## Examples

### Basic Usage

```bash
ldd squid | grep asan
```

### Advanced Usage

```bash
ldd /usr/local/sbin/squid | grep -i asan
```

## Expected Output

libasan.so.5 => /usr/lib/libasan.so.5 (if linked).

## Related

- [[Related Procedure: Verify-ASAN-Linkage-and-Monitor-Crash-with-GDB]]
