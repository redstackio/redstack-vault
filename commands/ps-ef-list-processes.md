---
id: cmd-001
data: ps -ef
tags:
  - recon
type: command
output: Output of all processes for reconnaissance
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.223Z'
verified: false
validated: true
submitted: true
---
# ps-ef-list-processes

## Command

```bash
ps -ef
```

## Description

Lists all running processes in full format, used in postinst for reconnaissance during package installation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -e | Show all processes | Yes |
| -f | Full format output | Yes |

## Examples

### Basic Usage

```bash
ps -ef
```

### Advanced Usage

```bash
ps -ef | grep build
```

## Expected Output

Full list of PIDs, users, commands; e.g., UID PID PPID C STIME TTY TIME CMD.

## Related

- [[commands/setpasswd-id-execute]]
