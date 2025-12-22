---
id: cmd-uuid-001
data: go build main.go -o chgbtaddr
tags:
  - bluetooth
  - spoofing
type: command
output: Generates executable file chgbtaddr
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.327Z'
verified: false
validated: true
submitted: true
---
# go-build-chgbtaddr

## Command

```bash
go build main.go -o chgbtaddr
```

## Description

Compiles a Golang script (main.go) designed for Bluetooth MAC address spoofing into an executable binary named chgbtaddr, used on Raspberry Pi to prepare for device impersonation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| main.go | Source code file containing Bluetooth spoofing logic | Yes |
| -o chgbtaddr | Output executable name | Yes |

## Examples

### Basic Usage

```bash
go build main.go -o chgbtaddr
```

### Advanced Usage

```bash
go build -ldflags="-s -w" main.go -o chgbtaddr
```

## Expected Output

Successful compilation with no errors, producing the 'chgbtaddr' executable file in the current directory.

## Related

- [[commands/chgbtaddr-spoof-address]]
- [[procedures/Spoof-Bluetooth-Address-and-Name-Using-Golang-and-BlueZ]]
