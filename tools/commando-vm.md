---
id: aa7569f9-cf41-4461-8580-31ab26856152
name: commando-vm
type: tool
verified: true
created_at: '2020-03-10T02:35:18.376822+00:00'
updated_at: '2023-05-30T01:08:36.241381+00:00'
platforms:
  - Windows
tags:
  - hacking
  - operating-systems
url: 'https://github.com/fireeye/commando-vm'
commands:
  - '[[commands/set-powershell-execution-policy-unrestricted]]'
validated: true
---

# Commando VM

**Status**: ✓ Verified

## Overview

Commando VM is a fully customizable Windows-based penetration testing virtual machine distribution developed by Mandiant (formerly FireEye). It specializes in Windows attacks and is built on top of a fully updated Windows 10 virtual machine. The distribution includes cross-platform tools from Kali Linux (running via Hyper-V and Docker), frameworks like Impacket and PowerSploit, Active Directory tools such as PowerView and BloodHound, popular wordlists, and multiple command-and-control (C2) frameworks.

## Description

Commando VM provides a comprehensive environment for offensive security operations focused on Windows ecosystems. It is installed via a PowerShell script that automates the setup of hundreds of tools, ensuring compatibility with Windows-specific attack techniques. The VM supports nested virtualization for running additional environments like Kali Linux inside it, making it ideal for red teaming, adversary emulation, and security research targeting Active Directory and enterprise Windows networks.

## Features

- Pre-configured Windows 10 base with all updates applied
- Integration of Kali Linux tools via Hyper-V and Docker
- Active Directory exploitation tools (PowerView, BloodHound, Rubeus)
- Post-exploitation frameworks (Impacket, PowerSploit, Empire)
- Wordlists and cracking utilities (Hashcat, John the Ripper)
- C2 frameworks (Covenant, Sliver, Cobalt Strike compatibility)
- Customizable installation with optional components like Visual Studio builds

## Installation

### Requirements

- A fully up-to-date Windows 10 virtual machine
- 60 GB free hard drive space (150-200 GB recommended if installing Visual Studio)
- 3+ CPU cores
- 4 GB RAM minimum
- Nested virtualization enabled (for Docker and Hyper-V support, though installation works without it)
- Administrative privileges on the host hypervisor (e.g., VMware, VirtualBox, Hyper-V)

### Install Commands

1. Create a new Windows 10 VM and apply all Windows updates.

2. Disable Windows Defender Tamper Protection. Refer to [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/prevent-changes-to-security-settings-with-tamper-protection) for instructions.

3. Download the installation script from the [GitHub repository](https://github.com/fireeye/commando-vm).

4. Open PowerShell as Administrator and set the execution policy:

   [[commands/set-powershell-execution-policy-unrestricted]]

5. Create a VM checkpoint before proceeding.

6. Run the installation script:

   ```powershell
   .\install.ps1
   ```

The installation process requires entering the user's password and may take over 2 hours, including multiple restarts. After completion, create another checkpoint as a clean restore point.

## Basic Usage

Once installed, launch the VM and access tools via the Start Menu shortcuts or command line. For example, to start a PowerShell session with pentesting tools loaded:

```powershell
powershell.exe
```

Explore installed tools in directories like `C:\Commando` or use the included launcher scripts.

### Common Options

Commando VM does not have CLI options itself but integrates with tools that do. Refer to individual tool documentation for usage.

## Examples

### Example 1: Basic Launch

Boot the VM and open a terminal to verify installation:

```powershell
Get-ExecutionPolicy  # Should return 'Unrestricted'
```

### Example 2: Tool Access

Navigate to installed tools:

```powershell
cd C:\tools\impacket
python examples\GetPac.py domain/user:password@target
```

## Related Commands

- [[commands/set-powershell-execution-policy-unrestricted]]

## References

- Official GitHub: https://github.com/fireeye/commando-vm
- Mandiant Blog: https://www.mandiant.com/resources/blog/introducing-commando-vm

*Last updated: 2023-05-30T01:08:36.241381+00:00*
