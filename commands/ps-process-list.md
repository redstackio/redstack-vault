---
id: cmd-ps-list-001
data: ps aux | grep root
tags:
  - process-enum
  - recon
type: command
output: 'root     1234  0.0  0.1  12345  6789 ?        S    12:00   0:00 /usr/sbin/sshd'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:27.937Z'
verified: false
validated: true
submitted: true
---
# ps-process-list

## Command

```bash
ps aux | grep root
```

## Description

Lists processes owned by root to identify hijackable sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `aux` | User-oriented format | Yes |
| `grep root` | Filter for root | Yes |

## Examples

### Basic Usage

```bash
ps aux | grep root
```

### Advanced Usage

```bash
ps aux | grep root | awk '{print $2}'
```

## Expected Output

PID list of root processes.

## Related

- [[commands/cat-proc-env]]
