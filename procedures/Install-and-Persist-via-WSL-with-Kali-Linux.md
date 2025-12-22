---
id: 4987b561-b8e4-4376-9196-f3d420f12bce
name: Install-and-Persist-via-WSL-with-Kali-Linux
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.332211+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Create-or-Modify-System-Process|T1543 - Create or Modify System
    Process]]
sub_techniques:
  - '[[sub-techniques/Windows-Service|T1543.003 - Windows Service]]'
tags:
  - '[[tags/Elevated]]'
  - '[[tags/Windows - Persistence]]'
  - '[[tags/Windows Subsystem for Linux]]'
commands:
  - '[[commands/wsl-list-online-distributions]]'
  - '[[commands/wsl-install-kali-linux]]'
  - '[[commands/wsl-set-default-version-2]]'
  - '[[commands/curl-download-wsl-debian]]'
  - '[[commands/add-wsl-debian-package]]'
  - '[[commands/wsl-run-kali-as-root]]'
platforms:
  - Windows
tools: []
validated: true
---

# Install-and-Persist-via-WSL-with-Kali-Linux

## Summary

This procedure demonstrates how to install and configure Windows Subsystem for Linux (WSL) with Kali Linux on a Windows 10 or later system to establish persistence, evade detection, and gain elevated access for executing Linux-based offensive tools. By leveraging WSL, attackers can run native Linux binaries and scripts on Windows, blending Windows and Linux attack techniques while maintaining long-term access through the installed distribution.

## Description

Windows Subsystem for Linux (WSL) provides a compatibility layer that allows Linux distributions to run natively on Windows without virtualization overhead. In an attack scenario, this enables persistence by installing a full Kali Linux environment, which can host persistent scripts, backdoors, or tools that survive reboots. Once installed, attackers can execute reconnaissance, lateral movement, and exfiltration using familiar Linux commands, potentially evading Windows-specific defenses like antivirus that may not monitor WSL processes effectively. This technique is particularly useful in hybrid environments where attackers need to bridge Windows and Linux toolchains. The procedure covers both online installation from Microsoft Store distributions and offline/local package methods for scenarios with limited internet access. Prerequisites include administrative privileges on the target Windows system, as installation modifies system processes and services.

## Requirements

1. Administrative access to a Windows 10 (version 2004 or later) or Windows 11 system with WSL feature enabled (via 'Turn Windows features on or off' or PowerShell).
2. Internet access for online installation (optional for local package method).
3. PowerShell execution policy set to allow scripts (e.g., Set-ExecutionPolicy RemoteSigned).
4. Basic knowledge of Windows command-line and Linux basics for post-installation use.

## Defense

- Disable WSL if not required for legitimate business use via Group Policy or by removing the 'Windows Subsystem for Linux' feature in Windows settings.
- Monitor for WSL-related activity using Windows Event Logs (e.g., Event ID 13 for WSL process creation) and network traffic from wsl.exe or lxssmanager.exe.
- Implement application whitelisting (e.g., AppLocker) to restrict installation of Linux distributions and monitor PowerShell executions involving wsl or Add-AppxPackage.
- Regularly audit installed WSL distributions with 'wsl --list' and remove unauthorized ones.

## Objectives

1. Install Kali Linux via WSL to create a persistent Linux execution environment on Windows.
2. Configure WSL for elevated (root) access to facilitate privilege escalation and evasion.
3. Enable execution of Linux tools for further offensive operations while maintaining access across system reboots.

## Instructions

### Step 1: List Available Online Distributions

**Context**: Begin by querying the available WSL distributions online to confirm Kali Linux is accessible, ensuring the target system can connect to Microsoft's distribution repository.

**Command** ([[commands/wsl-list-online-distributions]]):
```powershell
wsl --list --online
```

> This command fetches and displays a list of installable Linux distributions from the Microsoft Store. It verifies network connectivity and availability without making changes. Expected output includes 'kali-linux' in the list if available.

### Step 2: Install Kali Linux Online

**Context**: Install the Kali Linux distribution directly from the online repository, which sets up the WSL environment and downloads the necessary files for persistence.

**Command** ([[commands/wsl-install-kali-linux]]):
```powershell
wsl --install -d kali-linux
```

> This installs Kali Linux as a WSL distribution, creating a new instance that persists on the system. The process may prompt for a username/password setup on first launch. Success is indicated by a completion message and the distribution appearing in 'wsl --list'.

### Step 3: Set Default WSL Version to 2 (For Local Install)

**Context**: If using a local package, configure WSL to use version 2 for better performance and compatibility, as version 1 has limitations in file system integration.

**Command** ([[commands/wsl-set-default-version-2]]):
```powershell
wsl --set-default-version 2
```

> This sets the default WSL version globally. Verify with 'wsl --status'. If the version is already 2, no change occurs; otherwise, it prepares the system for version 2 distributions.

### Step 4: Download Debian Appx Package (Fallback for Kali)

**Context**: For offline or restricted environments, download a base Debian package (compatible with Kali setup) as a fallback, since direct Kali offline packages may not be available.

**Command** ([[commands/curl-download-wsl-debian]]):
```powershell
curl.exe --insecure -L -o debian.appx https://aka.ms/wsl-debian-gnulinux
```

> This uses curl to fetch the Debian WSL package, ignoring SSL issues with --insecure. The file debian.appx is saved locally. Success: File downloaded without errors (check file size ~500MB).

### Step 5: Install Local Debian Package

**Context**: Install the downloaded package to add the Linux distribution to WSL, providing a base for further Kali tool installation inside the distro.

**Command** ([[commands/add-wsl-debian-package]]):
```powershell
Add-AppxPackage .\debian.appx
```

> This PowerShell cmdlet installs the .appx package as a WSL distribution. It may require running PowerShell as administrator. Expected output: Installation progress and success confirmation; verify with 'wsl --list'.

### Step 6: Run Kali Linux as Root

**Context**: Launch the installed Kali distribution with root privileges to bypass user-level restrictions and establish elevated persistence for executing tools.

**Command** ([[commands/wsl-run-kali-as-root]]):
```powershell
wsl kali-linux --user root
```

> This starts the Kali WSL instance directly as the root user, dropping into a Linux shell. No password is required for root in default setups. Success: Root shell prompt (root@kali:~#) for running Linux commands.
