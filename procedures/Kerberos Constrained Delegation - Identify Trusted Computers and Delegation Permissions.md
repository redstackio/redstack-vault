---
id: 15ba2a49-99ff-4e31-a8a4-fe6091b8553a
name: Kerberos Constrained Delegation - Identify Trusted Computers and Delegation
  Permissions
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.668987+00:00'
updated_at: '2023-04-10T20:26:18.830970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Identify a Constrained Delegation]]'
- '[[Kerberos Constrained Delegation]]'
---

# Kerberos Constrained Delegation - Identify Trusted Computers and Delegation Permissions

## Summary

Kerberos Constrained Delegation is a feature in Active Directory that allows a service to impersonate a user to another service. This can be useful for delegation scenarios, but it can also be abused by attackers to gain access to sensitive resources. This procedure helps identify which computers a

## Description

# Description

Kerberos Constrained Delegation is a feature in Active Directory that allows a service to impersonate a user to another service. This can be useful for delegation scenarios, but it can also be abused by attackers to gain access to sensitive resources. This procedure helps identify which computers are trusted for delegation and what permissions they have.

To identify a constrained delegation, an attacker can use tools like Powerview or Bloodhound to query Active Directory for the relevant information. Once the trusted computers and their permissions are identified, an attacker can use this information to further their attack, such as performing lateral movement or privilege escalation.

The business value of this procedure is that it can help organizations identify potential weaknesses in their Active Directory environment and take steps to mitigate them before an attacker can exploit them.

## Requirements

1. Authenticated access to the target Active Directory environment

1. Tools like Powerview or Bloodhound to query Active Directory

## Defense

1. Monitor Active Directory for unusual activity, such as changes to delegation permissions

1. Enforce the principle of least privilege by limiting delegation permissions to only what is necessary

1. Implement strong password policies and multi-factor authentication to prevent credential theft

## Objectives

1. Identify trusted computers and delegation permissions in Active Directory

1. Understand the potential risks associated with Kerberos Constrained Delegation

1. Use the information gathered to perform further attacks, such as lateral movement or privilege escalation

# Instructions

1. This command will list all the trusted computers and delegation permissions for the current user.

**Code**: [[Get-DomainComputer -TrustedToAuth | select -exp dn]]

> The first part of the command 'Get-DomainComputer -TrustedToAuth' will list all the computers that the current user has trusted to authenticate against. The second part of the command 'Get-DomainComputer previous_result | select -exp msds-AllowedToDelegateTo' will list all the delegation permissions for the previous result. This can be useful for identifying potential attack vectors if any of the trusted computers have excessive delegation permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]

## Tags

- [[Active Directory Attacks]]
- [[Identify a Constrained Delegation]]
- [[Kerberos Constrained Delegation]]
