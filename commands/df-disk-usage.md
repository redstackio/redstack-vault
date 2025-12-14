---
id: cmd-df-usage-001
data: df
tags:
  - verification
  - disk
type: command
output: |-
  Filesystem 1K-blocks Used Available Use% Mounted on
  /dev/root      123456 123456      0 100% /
executor: bash
platforms:
  - Embedded Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.944Z'
verified: false
validated: true
submitted: true
---
# df-disk-usage

## Command

```bash
df
```

## Description

Displays disk space usage for filesystems on Linux, used here to verify exhaustion of /tmp and /var partitions after uploads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard invocation shows all filesystems | No |

## Examples

### Basic Usage

```bash
df
```

### Advanced Usage

```bash
df -h /tmp
``` for human-readable output focused on /tmp.

## Expected Output

Table showing filesystems, e.g., /dev/root at 100% used for /tmp and /var mounts.

## Related

- [[Related Procedure|procedures/Verify-Disk-Exhaustion-Impact]]
