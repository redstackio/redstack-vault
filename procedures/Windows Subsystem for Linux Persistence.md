---
id: 4987b561-b8e4-4376-9196-f3d420f12bce
name: Windows Subsystem for Linux Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.332211+00:00'
updated_at: '2023-04-10T20:37:23.949761+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Create or Modify System Process|T1543 - Create or Modify System Process]]'
- '[[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]'
sub_techniques:
- '[[Create Cloud Instance|T1578.002 - Create Cloud Instance]]'
- '[[Windows Service|T1543.003 - Windows Service]]'
tags:
- '[[Elevated]]'
- '[[Windows - Persistence]]'
- '[[Windows Subsystem for Linux]]'
commands:
- '[[List and install online packages]]'
- '[[Run the machine as root]]'
- '[[Use a local package]]'
---

# Windows Subsystem for Linux Persistence

## Summary

Windows Subsystem for Linux (WSL) is a compatibility layer for running Linux binary executables natively on Windows 10. Attackers can use WSL to execute Linux binaries and scripts, which can help them evade defenses and maintain persistence on a compromised system. By installing and running Kali Li

## Description

# Description

Windows Subsystem for Linux (WSL) is a compatibility layer for running Linux binary executables natively on Windows 10. Attackers can use WSL to execute Linux binaries and scripts, which can help them evade defenses and maintain persistence on a compromised system. By installing and running Kali Linux on Windows using WSL, attackers can leverage a wide range of offensive tools to perform reconnaissance, lateral movement, and data exfiltration. Technical details on how to install and use Kali Linux on Windows using WSL can be found in the commands section below. From a business perspective, this technique allows attackers to maintain long-term access to a compromised system, potentially leading to data theft, ransomware, or other malicious activities.

## Requirements

1. Access to a Windows 10 system with WSL enabled

1. Installation of Kali Linux on Windows using WSL

1. Knowledge of Linux command line and Kali Linux tools

## Defense

1. Disable WSL if not needed for business purposes

1. Monitor for suspicious activity related to WSL, such as unusual network traffic or file access patterns

1. Implement least privilege access controls to limit the ability of attackers to install and use Kali Linux on Windows using WSL

## Objectives

1. Maintain persistence on a compromised Windows system

1. Execute Linux binaries and scripts natively on a Windows system

1. Leverage Kali Linux tools for reconnaissance, lateral movement, and data exfiltration

# Instructions

1. To install and run Kali Linux on Windows using WSL, follow these steps:

1. List and install online packages by running the following commands:

wsl --list --online
wsl --install -d kali-linux

2. Use a local package by running the following commands:

wsl --set-default-version 2
curl.exe --insecure -L -o debian.appx https://aka.ms/wsl-debian-gnulinux
Add-AppxPackage .\debian.appx

3. Run the machine as root by running the following command:

wsl kali-linux --user root

**Code**: [[# List and install online packages
wsl --list --on]]

> The `wsl` command is used to manage the Windows Subsystem for Linux. The `--list --online` options list all the available distributions that can be installed. The `--install -d kali-linux` option installs the Kali Linux distribution. The `--set-default-version 2` option sets the default version of WSL to version 2. The `curl.exe` command is used to download the Debian package file. The `Add-AppxPackage` command installs the Debian package. The `kali-linux` command is used to run the Kali Linux distribution. The `--user root` option runs the distribution as the root user.

**Command** ([[List and install online packages]]):

```bash
wsl --list --online
wsl --install -d kali-linux
```

**Command** ([[Use a local package]]):

```bash
wsl --set-default-version 2
curl.exe --insecure -L -o debian.appx https://aka.ms/wsl-debian-gnulinux
Add-AppxPackage .\debian.appx
```

**Command** ([[Run the machine as root]]):

```bash
wsl kali-linux --user root
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Create or Modify System Process|T1543 - Create or Modify System Process]]
- [[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]

### Sub-Techniques

- [[Create Cloud Instance|T1578.002 - Create Cloud Instance]]
- [[Windows Service|T1543.003 - Windows Service]]

## Commands Used

- [[List and install online packages]]
- [[Run the machine as root]]
- [[Use a local package]]

## Tags

- [[Elevated]]
- [[Windows - Persistence]]
- [[Windows Subsystem for Linux]]
