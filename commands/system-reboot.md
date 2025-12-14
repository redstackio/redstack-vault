---
data: reboot
tags:
  - reboot
  - restart
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.176Z'
id: 603eeee6-10c7-47e2-94c4-047d7004d330
verified: false
validated: true
submitted: true
---
# system-reboot

## Command

```bash
reboot
```

## Description

Restarts the Linux system, triggering systemd to reload and start services like the modified nordvpnd.service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| reboot | System restart command | Yes |

## Examples

### Basic Usage

```bash
sudo reboot
```

### Advanced Usage

```bash
sudo reboot --force
```

## Expected Output

System initiates shutdown and reboot; services reload on startup.

## Related

- [[procedures/Trigger-Malicious-Service-Execution-via-Reboot]]
