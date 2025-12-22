---
id: proc-uuid-001
name: Spoof-Bluetooth-Address-and-Name-Using-Golang-and-BlueZ
tags:
  - bluetooth
  - spoofing
type: procedure
tools:
  - '[[tools/Golang]]'
  - '[[tools/BlueZ]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/go-build-chgbtaddr]]'
  - '[[commands/chgbtaddr-spoof-address]]'
  - '[[commands/sudo-systemctl-restart-bluetooth]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:31:52.369Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---
# Spoof-Bluetooth-Address-and-Name-Using-Golang-and-BlueZ

## Summary

This procedure spoofs the Bluetooth address and name of a Raspberry Pi to impersonate a legitimate paired device, such as a Surface Laptop 4, enabling subsequent unauthorized reconnection attacks on Sony WH-1000XM5 headphones.

## Description

The attack targets the Bluetooth stack on Linux using BlueZ and a custom Golang script to modify the MAC address and hostname. By matching the identity of a previously paired device, the attacker can exploit the headphones' failure to perform proper SSP authentication during reconnection. Prerequisites include a Raspberry Pi with Bluetooth adapter and knowledge of the target's Bluetooth MAC and name. Expected outcomes include the attacker's device appearing as the legitimate one in Bluetooth scans.

## Requirements

1. Raspberry Pi OS (Bullseye or later) with BlueZ 5.55 and kernel 6.1
2. Golang installed for compiling the spoofing script
3. Root access for service restarts and address changes
4. Target device's Bluetooth MAC address (e.g., 00:11:22:33:44:55) and name (e.g., 'Surface Laptop 4')

## Defense

Defensive measures and detection strategies:

- Monitor Bluetooth logs for unusual address changes (e.g., via `bluetoothctl` or dmesg)
- Enforce strict pairing modes and disable auto-reconnect on IoT devices
- Use Bluetooth monitoring tools like Wireshark to detect spoofed connections

## Objectives

1. Change Bluetooth MAC to spoof legitimate device
2. Update device name to match target
3. Apply changes via service restart for persistence

## Instructions

### Step 1: Prepare and Compile Spoofing Script

**Context**: Create and build the Golang script (main.go) to change the Bluetooth MAC address.

**Command** ([[commands/go-build-chgbtaddr]]):
```bash
go build main.go -o chgbtaddr
```

> Compiles the source code into an executable. Expected output: Generates 'chgbtaddr' binary file.

### Step 2: Execute Address Spoofing

**Context**: Run the compiled tool to set the spoofed MAC address.

**Command** ([[commands/chgbtaddr-spoof-address]]):
```bash
./chgbtaddr -addr 00:11:22:33:44:55
```

> Updates the Bluetooth adapter's MAC. Expected output: Confirmation of address change.

### Step 3: Update Device Name and Restart Service

**Context**: Edit /etc/machine-info to set PRETTY_HOSTNAME (e.g., 'Surface Laptop 4'), then restart BlueZ to apply all changes.

**Command** ([[commands/sudo-systemctl-restart-bluetooth]]):
```bash
sudo systemctl restart bluetooth.service
```

> Applies name and address modifications. Expected output: Service restarted successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques


## Commands Used

- [[commands/go-build-chgbtaddr]]
- [[commands/chgbtaddr-spoof-address]]
- [[commands/sudo-systemctl-restart-bluetooth]]

## Tools Used

- [[tools/Golang]]
- [[tools/BlueZ]]

## Tags

- [[bluetooth]]
- [[spoofing]]
