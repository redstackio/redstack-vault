---
id: 618e52d4-4010-497a-844c-94296a9f9434
name: Flare VM
type: tool
verified: true
created_at: '2020-03-10T22:47:47.725281+00:00'
updated_at: '2023-05-30T01:06:14.563920+00:00'
commands:
- '[[Disable PowerShell Execution Policy Restrictions]]'
platforms:
- Windows
tags:
- '[[hacking]]'
- '[[Operating Systems]]'
---

# Flare VM

**Status**: ✓ Verified

## Overview

Fully customizable Windows-based security distribution for malware analysis, incident response, penetration testing, reverse engineering, etc. Flare is installed on top of a fully updated Windows 10 virtual machine via a PowerShell script. Flare includes popular debuggers like x64dbg/Olly and WinDb

## Description

# Description

Fully customizable Windows-based security distribution for malware analysis, incident response, penetration testing, reverse engineering, etc. Flare is installed on top of a fully updated Windows 10 virtual machine via a PowerShell script. Flare includes popular debuggers like x64dbg/Olly and WinDbg, disassemblers like Cutter and Ghidra, malware dumping tools, and more. See [Flare ](https://github.com/fireeye/flare-vm)[VM](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/prevent-changes-to-security-settings-with-tamper-protection)['s GitHub page](https://github.com/fireeye/flare-vm/blob/master/install.ps1) for a full list of default packages.

Recommended VM Specs:

- a fully up-to-date copy of Windows 10

- 60 GB free hard drive space (consider 150-200GB if adding multiple builds of Visual Studio)

- 3+ CPU Processors

- 4GB RAM

# Installation

## Install on Windows

1. Create a new Windows 10 VM

2. Apply all available Windows updates

3. Disable Windows Defender Anti-Tamper Protection. [Click here for instructions](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/prevent-changes-to-security-settings-with-tamper-protection)

4. 4. Download the Flare installation script (install.ps1): [ Download install.ps1 from GitHub](https://github.com/fireeye/flare-vm/blob/master/install.ps1)

5. Open a new PowerShell session as Admin (right-click Start > Windows PowerShell (Admin))
6. Set PowerShell execution policy to unrestrcited, and select "A" or "Y" to accept

7. Create a new checkpoint for the virtual machine, in case the installation fails and the process must be restarted
8. Execute the installation script

After entering the user's password, the installer will proceed. Expect it to take over an hour, and it will restart multiple times. Upon completion, create a new checkpoint for the VM to use as a safe restore point. Having this checkpoint ensures a "clean" state exists, and is priceless for instances where Flare is exposed to malicious software.

## Platforms

- Windows

## Commands (1)

- [[Disable PowerShell Execution Policy Restrictions]]

## Tags

- [[hacking]]
- [[Operating Systems]]
