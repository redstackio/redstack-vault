---
id: 0271c0a0-7a8f-4b56-8e98-8528ff0175cb
type: command
executor: bash
data: sudo systemctl enable --now $FULL_PATH_TO_FILE
output: null
created_at: '2019-10-16T23:21:22.688202+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - persistence
  - systemd
verified: true
validated: true
---

# systemctl-enable-and-start-service-by-file

## Command

```bash
sudo systemctl enable --now $FULL_PATH_TO_FILE
```

## Description

This command enables a specified systemd service unit file to start automatically on system boot and immediately starts the service using the --now flag. It is useful in post-exploitation scenarios for establishing persistence by linking a custom malicious service file to the system's startup targets, allowing payloads to execute reliably after reboots.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $FULL_PATH_TO_FILE | Full path to the .service unit file (e.g., /tmp/malicious.service or /etc/systemd/system/payload.service) | Yes |
| sudo | Elevates privileges to root, required for enabling and starting system services | Yes |
| enable | Enables the service by creating symlinks in the appropriate systemd targets | Built-in |
| --now | Immediately starts the service after enabling it, without waiting for a reboot | No (but recommended for immediate testing and activation) |

## Examples

### Basic Usage

```bash
sudo systemctl enable --now /tmp/root.service
```

### Advanced Usage

```bash
sudo systemctl enable --now /etc/systemd/system/custom-payload.service --no-block
```

The --no-block option allows the command to return immediately without waiting for the service to fully start.

## Expected Output

When successful, the command outputs confirmation of symlink creation for boot-time execution:

```
Created symlink /etc/systemd/system/multi-user.target.wants/root.service → /tmp/root.service.
Created symlink /etc/systemd/system/root.service → /tmp/root.service.
```

If the service starts successfully, you may see additional logs via `journalctl -u root.service` showing the service's initialization.

## Related

- [[procedures/Create-Systemd-Service-for-Persistence]]
- [[commands/systemctl-link-service-unit-file]]
- [[tools/systemctl]]
