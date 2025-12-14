---
id: cmd-uuid-002
data: './chgbtaddr -addr 00:11:22:33:44:55'
tags:
  - bluetooth
  - spoofing
type: command
output: Bluetooth address updated successfully
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.321Z'
verified: false
validated: true
submitted: true
---
# chgbtaddr-spoof-address

## Command

```bash
./chgbtaddr -addr 00:11:22:33:44:55
```

## Description

Executes the compiled Golang tool to change the Raspberry Pi's Bluetooth MAC address to a spoofed value, impersonating a target device's identity for Bluetooth attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -addr | New Bluetooth MAC address (e.g., 00:11:22:33:44:55) | Yes |

## Examples

### Basic Usage

```bash
./chgbtaddr -addr 00:11:22:33:44:55
```

### Advanced Usage

Not applicable; single parameter tool.

## Expected Output

Confirmation message indicating the Bluetooth address has been successfully updated.

## Related

- [[commands/go-build-chgbtaddr]]
- [[procedures/Spoof-Bluetooth-Address-and-Name-Using-Golang-and-BlueZ]]
