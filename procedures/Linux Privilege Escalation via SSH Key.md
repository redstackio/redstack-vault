---
id: 8f008d9c-02dc-4bae-a955-24426ae60def
name: Linux Privilege Escalation via SSH Key
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.584197+00:00'
updated_at: '2023-04-10T20:34:23.019374+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[Sensitive files]]'
- '[[SSH Key]]'
---

# Linux Privilege Escalation via SSH Key

## Summary

This procedure involves searching for SSH keys on a Linux system, which can be used to escalate privileges and gain persistent access. SSH keys are often stored in sensitive files, such as authorized_keys or id_rsa, and can be easily located using a simple search command. Once found, an attacker ca

## Description

# Description

This procedure involves searching for SSH keys on a Linux system, which can be used to escalate privileges and gain persistent access. SSH keys are often stored in sensitive files, such as authorized_keys or id_rsa, and can be easily located using a simple search command. Once found, an attacker can use these keys to gain access to the system as a privileged user, and potentially move laterally throughout the network. This technique is commonly used by attackers to maintain access to compromised systems.

## Requirements

1. Access to a Linux system

1. Command-line access

1. Knowledge of Linux file system

## Defense

1. Regularly review and remove unused SSH keys

1. Implement multi-factor authentication for SSH access

1. Monitor for unauthorized SSH logins and unusual activity

## Objectives

1. Locate SSH keys on a Linux system

1. Escalate privileges and gain persistent access

# Instructions

1. To search for SSH keys on a system, run the following commands:
1. find / -name authorized_keys 2> /dev/null
2. find / -name id_rsa 2> /dev/null

The first command searches for authorized_keys files which are used for SSH public key authentication. The second command searches for id_rsa files which are private keys used for SSH authentication. The 'find' command searches the entire file system starting from the root directory ('/') and the '-name' option specifies the name of the file to search for. The '2> /dev/null' redirects error messages to the null device, which means they will not be displayed on the screen. This is useful to avoid seeing error messages for directories that the user does not have permission to access.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Tags

- [[Linux - Privilege Escalation]]
- [[Sensitive files]]
- [[SSH Key]]
