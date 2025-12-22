---
id: 08a6132e-8a6a-4541-87fe-987825226d21
type: command
executor: bash
data: sudo systemctl link $FULL_PATH_TO_FILE
output: null
created_at: '2019-10-16T23:21:22.677582+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - persistence
  - systemd
verified: true
validated: true
---

# systemctl-link-service-unit-file

## Command

```bash
sudo systemctl link $FULL_PATH_TO_FILE
```

## Description

This command creates symlinks from the specified unit file to the appropriate directories in /etc/systemd/system, allowing the service to be enabled and managed by systemd without relocating the original file. Use this when staging custom services from temporary locations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $FULL_PATH_TO_FILE | Full path to the .service unit file (e.g., /tmp/root.service) | Yes |
| sudo | Elevates privileges (required for linking) | Yes |

## Examples

### Basic Usage

```bash
sudo systemctl link /tmp/root.service
```

### Advanced Usage

```bash
sudo systemctl link /path/to/custom.service --no-pager
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
bob@ubuntu18:/tmp$ sudo systemctl link /tmp/root.service

Created symlink /etc/systemd/system/root.service → /tmp/root.service.
```

## Related

- [[procedures/Create-Systemd-Service-for-Persistence]]
- [[commands/systemctl-enable-and-start-service-by-file]]
