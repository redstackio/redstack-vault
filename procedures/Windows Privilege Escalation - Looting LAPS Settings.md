---
id: 211b7714-6a0d-4ca2-957d-0f8e47e597cd
name: Windows Privilege Escalation - Looting LAPS Settings
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.901096+00:00'
updated_at: '2023-04-10T20:37:54.569224+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
- '[[Credentials in Registry|T1214 - Credentials in Registry]]'
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[LAPS Settings]]'
- '[[Windows - Privilege Escalation]]'
---

# Windows Privilege Escalation - Looting LAPS Settings

## Summary

This procedure involves extracting the Local Administrator Password Solution (LAPS) policy settings from Active Directory. LAPS is a Microsoft tool used to manage the local administrator password on domain joined computers. By extracting the LAPS settings, an attacker can obtain the password for th

## Description

# Description

This procedure involves extracting the Local Administrator Password Solution (LAPS) policy settings from Active Directory. LAPS is a Microsoft tool used to manage the local administrator password on domain joined computers. By extracting the LAPS settings, an attacker can obtain the password for the local administrator account on a target system. The attacker can then use this password to escalate their privileges on the target system and potentially move laterally within the network.

Technical Explanation: The LAPS password is stored in the Active Directory attribute ms-Mcs-AdmPwd. An attacker can use LDAP queries to extract this attribute and obtain the LAPS password. The extracted password can then be used to escalate privileges on the target system.

Business Value: By obtaining the LAPS password, an attacker can gain access to sensitive data and systems within an organization. This can lead to data theft, financial loss, and damage to the organization's reputation.

## Requirements

1. Access to Active Directory

1. LDAP queries

1. Knowledge of the LAPS password format

## Defense

1. Implement strict access controls to Active Directory to prevent unauthorized access

1. Implement monitoring and alerting for LDAP queries to detect suspicious activity

1. Implement a strong password policy and regularly rotate local administrator passwords to mitigate the risk of LAPS password theft

## Objectives

1. Obtain the LAPS password for a target system

1. Escalate privileges on the target system using the LAPS password

1. Move laterally within the network

# Instructions

1. To extract AdmPwd policy settings, follow these steps:
1. Open the Registry Editor by typing 'regedit' in the Windows search bar and pressing Enter.
2. Navigate to the following path: HKLM\Software\Policies\Microsoft Services\AdmPwd
3. Look for the desired policy setting and note its value.
4. Close the Registry Editor.

**Code**: [[HKLM\Software\Policies\Microsoft Services\AdmPwd]]

> The AdmPwd policy settings are used to manage the local administrator password solution (LAPS) in a Windows environment. These settings allow administrators to configure the password length, complexity, expiration, and other security-related policies for the local administrator account on Windows machines. By extracting these policy settings, administrators can review and audit the current configuration to ensure compliance with security policies and best practices.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]
- [[Credentials in Registry|T1214 - Credentials in Registry]]
- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Tags

- [[EoP - Looting for passwords]]
- [[LAPS Settings]]
- [[Windows - Privilege Escalation]]
