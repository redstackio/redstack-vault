---
id: aa7569f9-cf41-4461-8580-31ab26856152
name: Commando VM
type: tool
verified: true
created_at: '2020-03-10T02:35:18.376822+00:00'
updated_at: '2023-05-30T01:08:36.241381+00:00'
commands:
- '[[Disable PowerShell Execution Policy Restrictions]]'
platforms:
- Windows
tags:
- '[[hacking]]'
- '[[Operating Systems]]'
---

# Commando VM

**Status**: ✓ Verified

## Overview

Fully customizable Windows-based pentesting virtual machine distribution from Mandiant/FireEye, specializing in Windows attacks. Commando is installed on top of a fully updated Windows 10 virtual machine via a PowerShell script. Commando includes most cross-platform tools from Kali (including Kali 

## Description

# Description

Fully customizable Windows-based pentesting virtual machine distribution from Mandiant/FireEye, specializing in Windows attacks. Commando is installed on top of a fully updated Windows 10 virtual machine via a PowerShell script. Commando includes most cross-platform tools from Kali (including Kali itself running via Hyper-V and Docker), frameworks like Impacket and PowerSploit, Active Directory tools like PowerView and BloodHound, popular wordlists, and multiple C2 frameworks.



Recommended VM Specs:

- a fully up-to-date copy of Windows 10

- 60 GB free hard drive space (consider 150-200GB if adding multiple builds of Visual Studio)

- 3+ CPU Processors

- 4GB RAM

- Nested virtualization (needed for Docker, but Commando will install OK without it)



# Installation

## Install on Windows

1. Create a new Windows 10 VM

2. Apply all available Windows updates

3. Disable Windows Defender Anti-Tamper Protection. [Click here for instructions](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/prevent-changes-to-security-settings-with-tamper-protection) 

4. Download the Commando installation script (install.ps1): [Download install.ps1 from GitHub](https://github.com/fireeye/commando-vm)

5. Open a new PowerShell session as Admin (right-click Start > Windows PowerShell (Admin))

6. Set PowerShell execution policy to unrestrcited, and select "A" or "Y" to accept



{{EMBEDDED_COMMAND_a57b7ff5-3ed0-4526-a454-b1514a7b9456}}

7. Create a new checkpoint for the virtual machine, in case the installation fails and the process must be restarted

8. Execute the installation script



After entering the user's password, the installer will proceed. Expect it to take over 2 hours, and it will restart multiple times. Upon completion, create a new checkpoint for the VM to use as a safe restore point. Having this checkpoint ensures a "clean" state exists, and is priceless for instances where Commando is exposed to malicious software.



## Platforms

- Windows

## Commands (1)

- [[Disable PowerShell Execution Policy Restrictions]]

## Tags

- [[hacking]]
- [[Operating Systems]]


