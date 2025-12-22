---
id: cmd-cat-proc-001
data: 'cat /proc/[pid]/environ'
tags:
  - process-read
  - recon
type: command
output: |-
  HOME=/root
  PATH=/usr/bin:SUDO_UID=0
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:27.925Z'
verified: false
validated: true
submitted: true
---
# cat-proc-env

## Command

```bash
cat /proc/[pid]/environ
```

## Description

Reads environment variables from a process PID to find exploitable data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/proc/[pid]/environ` | Proc path | Yes |

## Examples

### Basic Usage

```bash
cat /proc/1234/environ
```

### Advanced Usage

```bash
cat /proc/$(pgrep sshd)/environ
```

## Expected Output

Null-separated env vars.

## Related

- [[commands/ps-process-list]]
