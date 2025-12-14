---
data: gcc test.c
tags:
  - compilation
  - malware
type: command
output: Executable binary 'a.out'
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:59.001Z'
id: 51f257d4-9125-46a5-b628-5821a90e39d9
verified: false
validated: true
submitted: true
---
# compile-test-binary

## Command

```bash
gcc test.c
```

## Description

Compiles the C source file 'test.c' into a default executable 'a.out' using GCC, preparing a malicious binary for use in privilege escalation exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `test.c` | Input C source file | Yes |
| (implicit `-o a.out`) | Output executable name | No |

## Examples

### Basic Usage

```bash
gcc test.c
```

### Advanced Usage

Specify output: `gcc test.c -o malicious`

## Expected Output

'a.out' executable created. Verify: `ls -l a.out` shows file with execute permissions.

## Related

- [[procedures/Compile-Malicious-Executable]]
- [[procedures/Develop-Malicious-Binary]]
