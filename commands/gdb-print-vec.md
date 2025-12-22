---
id: cmd-gdb-print-vec
type: command
executor: gdb
data: 'p vec[2]'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.864Z'
platforms:
  - Linux
tags:
  - debugging
  - memory
verified: false
validated: true
submitted: true
---

# gdb-print-vec

## Command

```gdb
p vec[2]
```

## Description

In a GDB session attached to the Apache process, prints the second element of the iovec vector in the response brigade to inspect where the XSS payload is stored during request handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| vec[2] | Index of the array element containing iov_base and iov_len | Yes |

## Examples

### Basic Usage

```gdb
p vec[2]
```

### Advanced Usage

```gdb
attach <pid>\np vec[2]
```

## Expected Output

$1 = {iov_base = 0x7f5115c1b17b, iov_len = 27}

## Related

- [[commands/gdb-print-payload]]
- [[procedures/Observe-and-Verify-Reflected-XSS-in-Response]]
