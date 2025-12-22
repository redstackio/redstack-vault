---
data: df -h
tags:
  - disk-usage
type: command
output: 'Filesystem usage report, e.g., /dev/sdb 100.0G 40.9G 59.1G 41% /etc/hosts'
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.611Z'
id: 5dbc77f6-eea7-42fc-aede-079769fe3030
verified: false
validated: true
submitted: true
---
# df-check-usage

## Command

```bash
df -h
```

## Description

Reports disk space usage of filesystems in human-readable format, useful for baselining before exhaustion attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -h | Human-readable output (e.g., GB) | No |

## Examples

### Basic Usage

```bash
df -h
```

### Advanced Usage

```bash
df -h /etc/hosts
```

## Expected Output

Table of filesystems with size, used, avail, %use, mount point.

## Related

- [[commands/df-check-kubelet]]
- [[procedures/Exec-Into-Pod-and-Baseline-Disk]]
