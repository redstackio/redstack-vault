---
id: 13dce5b7-adbd-4d11-bfe4-cd591b0d9729
name: Kerberos Constrained Delegation - Impersonation on Resource
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.749404+00:00'
updated_at: '2023-04-10T20:26:26.610750+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
sub_techniques:
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
- '[[Pass the Ticket|T1550.003 - Pass the Ticket]]'
- '[[Silver Ticket|T1558.002 - Silver Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Impersonate a domain user on a resource]]'
- '[[Kerberos Constrained Delegation]]'
---

# Kerberos Constrained Delegation - Impersonation on Resource

## Summary

This procedure allows an attacker to impersonate a domain user on a resource using Kerberos Constrained Delegation. By exploiting this feature, attackers can bypass the need for valid user credentials and gain access to resources that they would not normally have access to. This technique can be us

## Description

# Description

This procedure allows an attacker to impersonate a domain user on a resource using Kerberos Constrained Delegation. By exploiting this feature, attackers can bypass the need for valid user credentials and gain access to resources that they would not normally have access to. This technique can be used to elevate privileges, move laterally within a network, and access sensitive data.

To perform this attack, the attacker must have access to a user account that has been granted the 'Trust this computer for delegation' privilege. The attacker can then use this account to impersonate a domain user on a resource, without needing to know the user's password. This attack can be difficult to detect, as it does not require any malicious software to be installed on the target system.

The business value of this attack is that it allows attackers to gain access to sensitive data and systems, which can be used for financial gain or to disrupt business operations.

## Requirements

1. Access to a user account that has been granted the 'Trust this computer for delegation' privilege

## Defense

1. Disable the 'Trust this computer for delegation' privilege for all user accounts that do not require it

1. Monitor for suspicious activity, such as users accessing resources they would not normally have access to

1. Implement strong password policies to make it more difficult for attackers to obtain valid user credentials

## Objectives

1. Impersonate a domain user on a resource

1. Gain access to resources that the attacker would not normally have access to

1. Elevate privileges and move laterally within the network

# Instructions

1. This command impersonates the administrator account and accesses a remote share. To use this command, replace 'dc01.offense.local' with the name of the remote server and ensure that you have the necessary permissions to access the share.

**Code**: [[PS> [Reflection.Assembly]::LoadWithPartialName('Sy]]

> This command loads the 'System.IdentityModel' assembly, creates a new WindowsIdentity object for the 'administrator' account, impersonates the account, and then uses the 'ls' command to list the contents of the remote share '\\dc01.offense.local\c$'.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]
- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

### Sub-Techniques

- [[Kerberoasting|T1558.003 - Kerberoasting]]
- [[Pass the Ticket|T1550.003 - Pass the Ticket]]
- [[Silver Ticket|T1558.002 - Silver Ticket]]

## Tags

- [[Active Directory Attacks]]
- [[Impersonate a domain user on a resource]]
- [[Kerberos Constrained Delegation]]
