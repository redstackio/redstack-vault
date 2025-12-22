---
data: ./rename a b
tags:
  - swap
  - race
type: command
executor: bash
platforms:
  - Linux
id: 66c6e1cb-7385-42e9-8b66-3ac1ce9d0c7c
created_at: '2025-12-14T17:24:19.390Z'
updated_at: '2025-12-14T17:24:19.390Z'
verified: false
validated: true
submitted: true
---
# run-rename-swap

## Command

```bash
./rename a b
```

## Description

Executes the custom rename program to infinitely swap names of 'a' (symlink) and 'b' (directory) using renameat2 with RENAME_EXCHANGE, creating the race window for libcurl exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| a | First file path (symlink) | Yes |
| b | Second file path (directory) | Yes |

## Examples

### Basic Usage

```bash
./rename symlink target_dir
```

### Advanced Usage

```bash
# Run in background for persistence
./rename a b &
```

## Expected Output

No stdout; process loops indefinitely, atomically exchanging file names (monitor with watch -n 0.1 'ls -l a b').

## Related

- [[tools/rename-custom-swapper]]
- [[procedures/Execute-Continuous-File-Swapping]]
