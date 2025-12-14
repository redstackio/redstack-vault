---
data: ./rename a b
tags:
  - race-condition
  - syscall
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.217Z'
id: a11eebc3-6c4d-4ec4-a396-22a6a077bd6d
verified: false
validated: true
submitted: true
---
# rename-swap

## Command

```bash
./rename a b
```

## Description

Runs the custom rename program to infinitely swap the names of files 'a' (symlink) and 'b' (directory) using the renameat2 syscall with RENAME_EXCHANGE flag, creating a TOCTOU race window for libcurl exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| a | Path to symlink (source) | Yes |
| b | Path to directory (target) | Yes |

## Examples

### Basic Usage

```bash
./rename a b
```

### Background Execution

```bash
./rename a b &
```

## Expected Output

No stdout output; the program runs in an infinite loop performing atomic swaps via syscall(SYS_renameat2, AT_FDCWD, argv[1], AT_FDCWD, argv[2], RENAME_EXCHANGE). Success indicated by process running without errors.

## Related

- [[commands/ps-aux]]
- [[procedures/Execute-Symlink-Swapping-with-Custom-Rename-Tool]]
