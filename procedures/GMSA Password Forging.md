---
id: ebdcd7c0-2f72-4ebe-b00c-b9b8cf139ea2
name: GMSA Password Forging
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.594889+00:00'
updated_at: '2023-04-10T20:25:56.343182+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Forging Golden GMSA]]'
---

# GMSA Password Forging

## Summary

The GMSA Password Forging attack is a way to obtain the password for a Golden GMSA account. This account can be used to execute code on any computer in the domain and is often used by attackers to move laterally and escalate privileges. This attack involves changing the password of a GMSA account t

## Description

# Description

The GMSA Password Forging attack is a way to obtain the password for a Golden GMSA account. This account can be used to execute code on any computer in the domain and is often used by attackers to move laterally and escalate privileges. This attack involves changing the password of a GMSA account to a known value, which can then be used to create a Golden Ticket. This ticket can be used to authenticate to any computer in the domain as the GMSA account, without the need for valid credentials. 

Technical Explanation: The attack involves using the 'Managed Password Interval in Days' command to force the domain controller to reset the password of the GMSA account to a known value. Once the password is reset, the attacker can create a Golden Ticket, which can be used to authenticate to any computer in the domain as the GMSA account. This allows the attacker to move laterally and escalate privileges.

Business Value: An attacker who successfully forges a Golden GMSA account can gain access to sensitive information, execute code on any computer in the domain, and escalate privileges. This can lead to data theft, system compromise, and significant financial loss for the organization.

 

## Requirements

1. Domain access

1. Valid credentials to reset GMSA password

1. Knowledge of 'Managed Password Interval in Days' command

 

## Defense

1. Limit access to 'Managed Password Interval in Days' command

1. Monitor for unusual activity on GMSA accounts

1. Implement multi-factor authentication for domain administrators

 

## Objectives

1. Forge a Golden GMSA account

1. Move laterally across the domain

1. Escalate privileges

 

# Instructions

1. To manage the password interval for a gMSA, use the following command:
Set-ADServiceAccount -Identity <gMSA_Name> -ManagedPasswordIntervalInDays <Interval_In_Days>
This command sets the password interval for the specified gMSA to the specified number of days.


 



**Code**: [[ManagedPasswordIntervalInDays]]



> The ManagedPasswordIntervalInDays attribute specifies the number of days that a gMSA's password is valid before it must be automatically changed. This attribute can be set to any value between 1 and 999 days. When the password interval expires, the password is automatically changed by the Key Distribution Service (KDS). This ensures that the password is always strong and secure, without requiring manual intervention from an administrator. Note that you cannot manually reset a gMSA password, since the password is managed by the KDS.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Tags

- [[Active Directory Attacks]]
- [[Forging Golden GMSA]]


