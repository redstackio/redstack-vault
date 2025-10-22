---
id: a264143b-c7cd-4f33-8855-2068bab0b911
name: Active Directory Credential Dumping via Vssadmin
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.882957+00:00'
updated_at: '2023-04-10T20:26:12.406050+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Credentials in Files|T1081 - Credentials in Files]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
- '[[Using vssadmin]]'
---

# Active Directory Credential Dumping via Vssadmin

## Summary

Active Directory (AD) is a critical component of many corporate environments, often containing sensitive information such as user credentials. Attackers may attempt to dump AD credentials using various techniques, such as using vssadmin. Vssadmin is a command-line tool that can be used to create an

## Description

# Description

Active Directory (AD) is a critical component of many corporate environments, often containing sensitive information such as user credentials. Attackers may attempt to dump AD credentials using various techniques, such as using vssadmin. Vssadmin is a command-line tool that can be used to create and manage volume shadow copies. By creating a volume shadow copy of the system, an attacker can then copy the NTDS.dit file, which contains hashed passwords for all AD accounts. These hashes can then be cracked offline to obtain plaintext passwords, giving the attacker access to sensitive information and potentially allowing them to move laterally within the network.

Technical Explanation: Vssadmin can be used to create a volume shadow copy of the system, which can then be accessed to copy the NTDS.dit file. This file contains hashed passwords for all AD accounts, which can be cracked offline to obtain plaintext passwords.

Business Value: By obtaining AD credentials, an attacker can gain access to sensitive information and potentially move laterally within the network, causing significant damage to the organization.

## Requirements

1. Access to a system with vssadmin installed

1. Access to the NTDS.dit file

## Defense

1. Limit access to the NTDS.dit file to only authorized personnel

1. Monitor for suspicious use of vssadmin

1. Implement strong password policies to make cracking the hashed passwords more difficult

## Objectives

1. Dump AD credentials for lateral movement within the network

1. Gain access to sensitive information

# Instructions

1. This command creates a volume shadow copy and copies specific files to a specified location. 

The 'vssadmin create shadow' command creates a shadow copy of the specified volume. The '/for' parameter specifies the volume to create the shadow copy for. 

The 'copy' command is used to copy files from the specified source to the specified destination. The '\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1' path is used to access the shadow copy. The 'C:\ShadowCopy' path is used to specify the destination folder. The files being copied are 'NTDS.dit' and 'SYSTEM'.

**Code**: [[vssadmin create shadow /for=C:\ncopy \\?\GLOBALROO]]

> This command can be used to create a backup of the 'NTDS.dit' and 'SYSTEM' files on a Windows system. By creating a shadow copy of the volume and then copying the files to a specified location, a backup copy of these critical files can be made without interrupting the normal operation of the system. This can be useful for disaster recovery scenarios or for forensic analysis of a system.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Credentials in Files|T1081 - Credentials in Files]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]
- [[Using vssadmin]]
