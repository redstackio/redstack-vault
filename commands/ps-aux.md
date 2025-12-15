---
id: c1d2e3f4-g5h6-7891-cdef-012345678901
data: ps aux
tags:
  - recon
  - processes
type: command
output: Output of running processes on the server
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:14.493Z'
verified: false
validated: true
submitted: true
---
# ps aux

## Command

```bash
ps aux
```

## Description

Lists all running processes on a Unix-like system with detailed information, used here to demonstrate RCE by capturing server state for exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| a | Show processes for all users | Yes (implicit) |
| u | Display user-oriented format | Yes (implicit) |
| x | Include processes without controlling ttys | Yes (implicit) |

## Examples

### Basic Usage

```bash
ps aux
```

### Advanced Usage

```bash
ps aux | grep imgur
```

## Expected Output

A table of processes including USER, PID, %CPU, %MEM, VSZ, RSS, TTY, STAT, START, TIME, COMMAND.

## Related

- [[commands/ps-aux-exfil]]
