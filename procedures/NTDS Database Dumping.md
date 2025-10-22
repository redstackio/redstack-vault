---
id: e211bc1d-6b1c-4821-8250-5c298c92c5b2
name: NTDS Database Dumping
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.804864+00:00'
updated_at: '2023-04-10T20:25:54.215105+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
---

# NTDS Database Dumping

## Summary

NTDS database dumping is a technique used to extract password hashes from an Active Directory domain controller. This technique is commonly used by attackers to obtain credentials that can be used to move laterally within the network. The NTDS database is a critical component of Active Directory an

## Description

# Description

NTDS database dumping is a technique used to extract password hashes from an Active Directory domain controller. This technique is commonly used by attackers to obtain credentials that can be used to move laterally within the network. The NTDS database is a critical component of Active Directory and contains valuable information such as user and computer account details, group membership information, and password hashes. This procedure involves extracting the NTDS.dit file from the domain controller and then using a tool such as Mimikatz to extract password hashes from the database. 

From a technical perspective, the NTDS database is a binary file that is stored on the domain controller. The database contains a table of all objects in the domain, including user accounts, computer accounts, and security groups. Password hashes are stored in the database and can be extracted using a variety of tools and techniques. 

The business value of this procedure is that it allows attackers to obtain valuable credentials that can be used to move laterally within the network and gain access to sensitive data and systems.

## Requirements

1. Domain administrator privileges

1. Access to the domain controller

1. Tools such as Mimikatz or similar password dumping tools

## Defense

1. Limit domain administrator privileges to only those who need them

1. Implement strong password policies and multi-factor authentication

1. Monitor for suspicious activity, such as unusual file access or unusual network traffic

## Objectives

1. Extract password hashes from the NTDS database

1. Gain access to user and computer account details

1. Move laterally within the network

# Instructions

1. To get the current location of the NTDS database file, run the following command:

**Code**: [[reg query HKLM\SYSTEM\CurrentControlSet\Services\N]]

> This command queries the registry for the current location of the NTDS database file. The location is stored in the 'DSA Database file' value under the 'HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters' key.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]
