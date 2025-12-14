---
id: cmd-uuid-003
data: sudo systemctl restart bluetooth.service
tags:
  - bluetooth
  - service
type: command
output: 'Bluetooth service restarted, applying configuration changes'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.317Z'
verified: false
validated: true
submitted: true
---
# sudo-systemctl-restart-bluetooth

## Command

```bash
sudo systemctl restart bluetooth.service
```

## Description

Restarts the BlueZ Bluetooth service on Linux systems like Raspberry Pi OS to apply changes to device name, address, or configuration after spoofing modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| bluetooth.service | The systemd service unit for the Bluetooth stack | Yes |

## Examples

### Basic Usage

```bash
sudo systemctl restart bluetooth.service
```

### Advanced Usage

```bash
sudo systemctl restart bluetooth.service && bluetoothctl show
```

## Expected Output

System message: 'bluetooth.service: Succeeded.' Service restarts without errors, loading new configurations.

## Related

- [[commands/chgbtaddr-spoof-address]]
- [[procedures/Spoof-Bluetooth-Address-and-Name-Using-Golang-and-BlueZ]]
