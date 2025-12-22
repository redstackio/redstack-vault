---
data: mount /dev/sda9 /h
tags:
  - mount
type: command
executor: bash
platforms:
  - Linux
id: 1017e4ad-274e-40f6-aa44-de9bfac2dfea
created_at: '2025-12-14T04:08:48.072Z'
updated_at: '2025-12-14T04:08:48.072Z'
verified: false
validated: true
submitted: true
---
# Mount Host Storage Volume

## Command

```bash
mount /dev/sda9 /h
```

## Description

Mounts host block device to container directory for filesystem access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /dev/sda9 | Host device | Yes |
| /h | Mount point | Yes |

## Examples

### Basic Usage

```bash
mount /dev/sda9 /h
```

## Expected Output

Mount successful; ls /h shows host files.

## Related

- [[commands/mkdir-host-mount-point]]
