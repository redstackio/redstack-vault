---
data: chroot /chroot
tags:
  - escape
  - chroot
type: command
output: Shell on host
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.859Z'
id: 0ec02114-f9a8-4673-8ca9-b3651d78b3f3
verified: false
validated: true
submitted: true
---
# chroot-to-host-root

## Command

```bash
chroot /chroot
```

## Description

Changes the root directory to the mounted host filesystem, escaping the container.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/chroot` | Path to mounted host root | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

New shell in host root FS.

## Related

- [[procedures/Escape-to-Host-via-Privileged-Pod]]
