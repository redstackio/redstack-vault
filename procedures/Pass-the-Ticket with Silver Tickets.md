---
id: d642976d-6347-433e-a430-2e7e7ce408eb
name: Pass-the-Ticket with Silver Tickets
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.886202+00:00'
updated_at: '2023-04-10T20:26:29.249333+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Tickets]]'
- '[[Pass-the-Ticket Diamond Tickets]]'
commands:
- '[[Request Ticket from ticketer.py and Export it using Rubeus.exe]]'
---

# Pass-the-Ticket with Silver Tickets

## Summary

Pass-the-Ticket attacks occur when an attacker uses a Kerberos ticket to authenticate to a service as a legitimate user without the need for the user's password. Pass-the-Ticket with Silver Tickets is a technique used by attackers to forge a Kerberos ticket with Domain Admin privileges. This is ach

## Description

# Description

Pass-the-Ticket attacks occur when an attacker uses a Kerberos ticket to authenticate to a service as a legitimate user without the need for the user's password. Pass-the-Ticket with Silver Tickets is a technique used by attackers to forge a Kerberos ticket with Domain Admin privileges. This is achieved by forging a Ticket Granting Service (TGS) ticket for the krbtgt account, which is used to generate service tickets for any account within the domain. Once the attacker has the Silver Ticket, they can access any service within the domain as any user without being detected.

## Requirements

1. Valid domain credentials

1. Access to the domain controller

1. Mimikatz or other tool to generate Silver Tickets

## Defense

1. Implement multi-factor authentication to prevent credential theft

1. Monitor for unusual Kerberos ticket activity

1. Disable Kerberos ticket caching to limit the impact of stolen tickets

## Objectives

1. Forge a Silver Ticket for the krbtgt account

1. Gain Domain Admin privileges

1. Access any service within the domain as any user

# Instructions

1. Use the following commands to generate a silver ticket for a specific user and domain:

**Code**: [[ticketer.py -request -domain 'lab.local' -user 'do]]

> The above commands can be used to generate a silver ticket for a specific user and domain. The 'ticketer.py' command generates a silver ticket using the provided arguments such as domain name, user name, password, NT hash, AES key, domain SID, user ID, and group IDs. The 'Rubeus.exe' command is used to request a TGS ticket for the specified service using the provided credentials and ticket information. This ticket can then be used to access the service as the specified user. The 'Interesting services to target with a silver ticket' text provides a list of services that can be targeted using a silver ticket.

**Command** ([[Request Ticket from ticketer.py and Export it using Rubeus.exe]]):

```bash
ticketer.py -request -domain 'lab.local' -user 'domain_user' -password 'password' -nthash 'krbtgt/service NT hash' -aesKey 'krbtgt/service AES key' -domain-sid 'S-1-5-21-...' -user-id '1337' -groups '512,513,518,519,520' 'baduser'

Rubeus.exe diamond /domain:DOMAIN /user:USER /password:PASSWORD /dc:DOMAIN_CONTROLLER /enctype:AES256 /krbkey:HASH /ticketuser:USERNAME /ticketuserid:USER_ID /groups:GROUP_IDS
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[Request Ticket from ticketer.py and Export it using Rubeus.exe]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Tickets]]
- [[Pass-the-Ticket Diamond Tickets]]
