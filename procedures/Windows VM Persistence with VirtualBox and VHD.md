---
id: 9a91e47a-a9d7-496d-8e79-7024a7448c98
name: Windows VM Persistence with VirtualBox and VHD
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.300194+00:00'
updated_at: '2023-04-10T20:37:27.519252+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]'
sub_techniques:
- '[[Print Processors|T1547.012 - Print Processors]]'
- '[[Registry Run Keys / Startup Folder|T1547.001 - Registry Run Keys / Startup Folder]]'
tags:
- '[[Elevated]]'
- '[[Virtual Machines]]'
- '[[Windows - Persistence]]'
---

# Windows VM Persistence with VirtualBox and VHD

## Summary

This procedure involves creating a Windows virtual machine using VirtualBox and mounting a VHD file for persistence. The virtual machine can be used to execute malicious code or maintain access to a compromised network. The VHD file is mounted as a secondary hard drive and a malicious executable is

## Description

# Description

This procedure involves creating a Windows virtual machine using VirtualBox and mounting a VHD file for persistence. The virtual machine can be used to execute malicious code or maintain access to a compromised network. The VHD file is mounted as a secondary hard drive and a malicious executable is added to the startup folder to ensure it is executed on boot. This technique can evade detection by security solutions that are not configured to monitor virtual machines.

From a technical perspective, this procedure involves creating a new virtual machine in VirtualBox and attaching a VHD file as a secondary hard drive. The VHD file contains a malicious executable that is added to the startup folder of the virtual machine. When the virtual machine is started, the malicious executable is executed, providing persistence on the compromised system.

From a business perspective, this technique can be used by attackers to maintain access to a compromised network or execute malicious code on a victim's machine. By evading detection by security solutions, attackers can remain undetected for longer periods of time, potentially causing more damage to the victim's organization.

 

## Requirements

1. Access to a Windows virtual machine

1. VirtualBox installed on the host system

1. A VHD file containing a malicious executable

 

## Defense

1. Monitor virtual machines for suspicious activity, such as network traffic or unusual behavior

1. Implement network segmentation to limit the impact of a compromised virtual machine

1. Regularly update security solutions to detect and prevent new attack techniques

 

## Objectives

1. Create a persistent backdoor on a compromised system

1. Maintain access to a compromised network

 

# Instructions

1. To create a virtual machine with VirtualBox and mount a VHD file, follow these steps:
1. Download VirtualBox from the official website.
2. Run the downloaded file and perform a silent install to avoid creating desktop and quick launch icons.
3. Disable notifications by running the command in \Program Files\Oracle\VirtualBox\VBoxManage.exe.
4. Download the VHD file from the network location to your local machine.
5. Create a new VM by running the command in VBoxManage.exe, specifying the name, operating system type, and registering it.
6. Add a network card in NAT mode, configure memory, video RAM, audio, graphics controller, and description.
7. Mount the VHD file by running the command in VBoxManage.exe, specifying the storage controller, storage attachment, comment, type, medium, and port.
8. Start the VM by running the command in VBoxManage.exe, specifying the name and type.
9. Optionally, add a shared folder by running the command in VBoxManage.exe, specifying the name, host path, and automount.
10. Mount the shared folder in the VM by running the commands sudo mkdir /mnt/c and sudo mount -t vboxsf shadow_c /mnt/c.

 



**Code**: [[# download virtualbox
Invoke-WebRequest "https://d]]



> This script automates the process of creating a virtual machine with VirtualBox and mounting a VHD file. It downloads VirtualBox from the official website, disables notifications, downloads the VHD file from a network location, creates a new VM, adds a network card in NAT mode, configures memory, video RAM, audio, graphics controller, and description, mounts the VHD file, and starts the VM. Additionally, it provides instructions and explanations for each step to help the user understand the process.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]

### Sub-Techniques

- [[Print Processors|T1547.012 - Print Processors]]
- [[Registry Run Keys / Startup Folder|T1547.001 - Registry Run Keys / Startup Folder]]

## Tags

- [[Elevated]]
- [[Virtual Machines]]
- [[Windows - Persistence]]


