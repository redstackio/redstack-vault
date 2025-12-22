---
id: cmd-gdb-print-payload
type: command
executor: gdb
data: p (char *)0x7f5115c1b17b
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.861Z'
platforms:
  - Linux
tags:
  - debugging
  - memory
  - xss
verified: false
validated: true
submitted: true
---

# gdb-print-payload

## Command

```gdb
p (char *)0x7f5115c1b17b
```

## Description

Casts a memory address to char* in GDB and prints the string contents, verifying the XSS payload stored in the brigade bucket during the exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 0x7f5115c1b17b | Memory address of iov_base from vec[2] | Yes |

## Examples

### Basic Usage

```gdb
p (char *)0x7f5115c1b17b
```

### Advanced Usage

```gdb
p (char *)<dynamic_address>
```

## Expected Output

$2 = "<script>alert(1)</script>\r\n"

## Related

- [[commands/gdb-print-vec]]
- [[procedures/Observe-and-Verify-Reflected-XSS-in-Response]]
