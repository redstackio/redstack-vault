---
data: ls -l /etc/cron.daily/zzz-backdoor
tags:
  - verification
type: command
output: '-rw-r--r-- 1 root root 123 May 1 06:30 /etc/cron.daily/zzz-backdoor'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.435Z'
id: f08687d0-acad-4af5-ae40-115245f9d14e
verified: false
validated: true
submitted: true
---
# ls-cron-backdoor

## Command

```bash
ls -l /etc/cron.daily/zzz-backdoor
```

## Description

Lists the backdoor file in long format to verify creation and root ownership post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Long format (permissions, owner) | Yes |
| `/etc/cron.daily/zzz-backdoor` | File path | Yes |

## Examples

### Basic Usage

```bash
ls -l /etc/cron.daily/zzz-backdoor
```

### Advanced Usage

```bash
ls -la /etc/cron.daily/
```

## Expected Output

File details, e.g., '-rw-r--r-- 1 root root 123 May 1 06:30 /etc/cron.daily/zzz-backdoor'.

## Related

- [[commands/cat-cron-backdoor]]
