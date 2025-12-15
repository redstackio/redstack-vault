---
data: df -h /var/lib/kubelet
tags:
  - disk-usage
  - dos
type: command
output: 'Disk usage, e.g., decreasing available space to 0%'
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.585Z'
id: 678b432d-edf5-4ec2-9cfd-144b1b460b5a
verified: false
validated: true
submitted: true
---
# df-check-kubelet

## Command

```bash
df -h /var/lib/kubelet
```

## Description

Checks disk usage specifically for the kubelet directory, confirming exhaustion from pod actions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -h | Human-readable | Yes |
| /var/lib/kubelet | Path to check | Yes |

## Examples

### Basic Usage

```bash
df -h /var/lib/kubelet
```

## Expected Output

Usage stats showing % full increasing to 100%.

## Related

- [[procedures/Confirm-Host-Disk-Exhaustion]]
