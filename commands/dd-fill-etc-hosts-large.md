---
data: dd if=/dev/zero of=/etc/hosts count=1000000 bs=10M
tags:
  - disk-exhaustion
type: command
output: Records in/out until disk full
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.580Z'
id: 3c183c74-3c82-42a1-a953-7a14d926a2b3
verified: false
validated: true
submitted: true
---
# dd-fill-etc-hosts-large

## Command

```bash
dd if=/dev/zero of=/etc/hosts count=1000000 bs=10M
```

## Description

Large-scale write to fully exhaust disk with 10TB of data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| if=/dev/zero | Zeros input | Yes |
| of=/etc/hosts | Target file | Yes |
| count=1000000 | Blocks count | Yes |
| bs=10M | 10MB block size | Yes |

## Examples

### Basic Usage

```bash
dd if=/dev/zero of=/etc/hosts count=1000000 bs=10M
```

## Expected Output

Progressive records until interruption or full.

## Related

- [[commands/dd-fill-etc-hosts]]
- [[procedures/Overwrite-Etc-Hosts-with-Dd]]
