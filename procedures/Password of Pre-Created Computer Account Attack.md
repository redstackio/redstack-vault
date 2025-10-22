---
id: bf89f1ce-c7d1-4d67-bfcb-c357616d641e
name: Password of Pre-Created Computer Account Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.471172+00:00'
updated_at: '2023-04-10T20:26:27.409776+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Password of Pre-Created Computer Account]]'
commands:
- '[[Join computer to domain and assign pre-Windows 2000 name]]'
---

# Password of Pre-Created Computer Account Attack

## Summary

The Password of Pre-Created Computer Account Attack is a technique used to gain access to a domain controller by compromising a pre-created computer account's password. This technique can be used to elevate privileges and move laterally across the network. Attackers can use this technique to dump c

## Description

# Description

The Password of Pre-Created Computer Account Attack is a technique used to gain access to a domain controller by compromising a pre-created computer account's password. This technique can be used to elevate privileges and move laterally across the network. Attackers can use this technique to dump credentials from the domain controller and gain access to sensitive data. This attack can be executed by assigning a pre-Windows 2000 computer account or provisioning a machine with a default password.

## Requirements

1. Access to the network

1. Knowledge of the pre-created computer account's name

1. Tools for password cracking

## Defense

1. Monitor and detect unauthorized access attempts

1. Ensure strong password policies are in place

1. Enable multi-factor authentication for user accounts

## Objectives

1. Gain access to a domain controller

1. Elevate privileges

1. Move laterally across the network

1. Dump credentials from the domain controller

1. Gain access to sensitive data

# Instructions

1. Set-ADComputer -Identity <ComputerName> -SamAccountName <SamAccountName>

**Code**: [[Assign this computer account as a pre-Windows 2000]]

> The -SamAccountName parameter specifies the pre-Windows 2000 computer account name. This should be in the format of NetBIOSDomainName\ComputerName$. The -Identity parameter specifies the distinguished name (DN), GUID, security identifier (SID), or SAM account name of the computer account to modify.

**Command** ([[Join computer to domain and assign pre-Windows 2000 name]]):

```bash
netdom.exe join /domain:contoso.com /ou:OU=Desktops,OU=Computers,DC=contoso,DC=com /preW2K:CONTOSO\Win10Comp$

```

2. To provision a machine with a default password, run the following command from a domain-joined device connected to the domain:

djoin /PROVISION /DOMAIN <fqdn> /MACHINE <machine_name> /SAVEFILE C:\temp\<machine_name>.txt /DEFPWD /PRINTBLOB /NETBIOS <machine_name>

Replace <fqdn> with the fully qualified domain name of the domain, and <machine_name> with the name of the machine you want to provision.

**Code**: [[# Create a machine with default password
# must be]]

> This command provisions a new machine and joins it to the specified domain. The /DEFPWD switch sets the machine's password to a default value, which should be changed immediately after provisioning. The /PRINTBLOB switch outputs the machine account password blob to the console, which can be used to automate the provisioning of additional machines. The /NETBIOS switch sets the NetBIOS name of the machine to the specified value.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Join computer to domain and assign pre-Windows 2000 name]]

## Tags

- [[Active Directory Attacks]]
- [[Password of Pre-Created Computer Account]]
