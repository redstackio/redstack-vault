---
id: 65c32c92-2cea-4725-995b-881359b2dde3
name: Shadow Credential Harvesting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.239601+00:00'
updated_at: '2023-04-10T20:26:25.573402+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Shadow Credentials]]'
---

# Shadow Credential Harvesting

## Summary

Shadow credentials are Active Directory user accounts that have been previously used to authenticate on a device, but are no longer in use. These accounts can be harvested and used by an attacker to gain access to other devices and systems within the network. 

To harvest shadow credentials, an att

## Description

# Description

Shadow credentials are Active Directory user accounts that have been previously used to authenticate on a device, but are no longer in use. These accounts can be harvested and used by an attacker to gain access to other devices and systems within the network. 

To harvest shadow credentials, an attacker can use techniques such as credential dumping to extract password hashes from the Security Account Manager (SAM) database. The harvested hashes can then be cracked to obtain the plaintext password, which can be used to authenticate as the user and gain access to their associated resources. 

The business value of this attack is that it allows an attacker to move laterally within a network, potentially gaining access to sensitive data or systems.

 

## Requirements

1. Access to the target network.

1. Tools for dumping credentials and cracking password hashes.

 

## Defense

1. Implement strong password policies and regularly rotate passwords.

1. Monitor for unusual authentication activity, such as authentication attempts from inactive user accounts.

1. Use multi-factor authentication to prevent unauthorized access even if credentials are compromised.

 

## Objectives

1. Harvest shadow credentials from the target network.

1. Use the harvested credentials to move laterally within the network and access sensitive data or systems.

 

# Instructions

1. This command is used to manage the key credentials for a user object in Active Directory. It allows administrators to add, remove, or view the key credentials associated with a user account.
To add a new key credential, use the 'Add-ADUserKeyCredential' cmdlet. To remove a key credential, use the 'Remove-ADUserKeyCredential' cmdlet. To view the key credentials associated with a user account, use the 'Get-ADUserKeyCredential' cmdlet.

 



**Code**: [[msDS-KeyCredentialLink]]



> The 'msDS-KeyCredentialLink' attribute is used to store the link between a user object and its associated key credentials. This attribute is managed automatically by Active Directory and cannot be edited by user objects themselves. This is a security measure to prevent users from tampering with their own key credentials and potentially compromising the security of the domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Tags

- [[Active Directory Attacks]]
- [[Shadow Credentials]]


