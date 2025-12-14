---
data: gcc dirty.c -o dirty_sock
tags:
  - compile
  - exploit
type: command
executor: bash
platforms:
  - Linux
id: afcbef94-f2cf-4b52-9dd4-7a3a139efb6d
created_at: '2025-12-14T17:30:47.102Z'
updated_at: '2025-12-14T17:30:47.102Z'
verified: false
validated: true
submitted: true
---
# gcc-compile-dirty-sock

## Command

```bash
gcc dirty.c -o dirty_sock
```

## Description

Compiles the dirty_sock exploit source code (dirty.c) into an executable binary using gcc, enabling local privilege escalation on vulnerable Ubuntu systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `dirty.c` | Source file | Yes |
| `-o dirty_sock` | Output binary name | Yes |

## Examples

### Basic Usage

```bash
gcc dirty.c -o dirty_sock
```

### Advanced Usage

```bash
gcc -O2 dirty.c -o dirty_sock
```

## Expected Output

No output if successful; binary created. Error if gcc missing or syntax issues.

## Related

- [[commands/run-dirty-sock-exploit]]
- [[procedures/Exploit-Dirty-Sock-for-Root-Access]]
