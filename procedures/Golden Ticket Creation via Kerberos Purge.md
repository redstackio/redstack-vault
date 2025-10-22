---
id: a140cb8b-262c-4ef0-aaba-b22d8312c0ce
name: Golden Ticket Creation via Kerberos Purge
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.451339+00:00'
updated_at: '2023-04-10T20:37:25.722827+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Domain]]'
- '[[Golden Ticket]]'
- '[[Windows - Persistence]]'
commands:
- '[[Generate Golden Kerberos Ticket]]'
- '[[Purge Kerberos tickets]]'
- '[[Request TGT with Golden Ticket]]'
---

# Golden Ticket Creation via Kerberos Purge

## Summary

This procedure involves using Kerberos Purge to obtain domain administrator credentials, which can then be used to create a Golden Ticket. A Golden Ticket is a forged Kerberos ticket that grants the attacker unlimited access to the domain. Kerberos Purge works by deleting all tickets for a specific

## Description

# Description

This procedure involves using Kerberos Purge to obtain domain administrator credentials, which can then be used to create a Golden Ticket. A Golden Ticket is a forged Kerberos ticket that grants the attacker unlimited access to the domain. Kerberos Purge works by deleting all tickets for a specific user, forcing the user to request new tickets. If the attacker can intercept these requests, they can obtain the user's TGT, which can be used to create a Golden Ticket. This technique can be used to maintain persistence in the domain, as well as to move laterally and access sensitive information.

## Requirements

1. Valid domain credentials

1. Access to a domain controller

1. Kerberos Purge tool

## Defense

1. Implement strong password policies and ensure that all domain users change their passwords regularly

1. Monitor the domain for unusual activity, such as multiple requests for new tickets from the same user

1. Implement network segmentation to prevent lateral movement within the domain

## Objectives

1. Obtain domain administrator credentials

1. Create a Golden Ticket for persistent access to the domain

1. Move laterally and access sensitive information

# Instructions

1. This command is used to purge Kerberos tickets and create a Golden Ticket. The 'kerberos::purge' command is used to delete all Kerberos tickets from the current user's session. The 'kerberos::golden' command is used to create a Golden Ticket with the specified user, domain, SID, krbtgt hash, ticket file, and pass-the-ticket (PTT) flag. The arguments for the 'kerberos::golden' command are as follows:

- /user: The user account for which the Golden Ticket is being created.
- /domain: The domain for which the Golden Ticket is being created.
- /sid: The Security Identifier (SID) of the domain for which the Golden Ticket is being created.
- /krbtgt: The hash of the krbtgt account for the domain.
- /ticket: The name of the ticket file to be created.
- /ptt: Pass-the-ticket flag, which is used to inject the ticket into the current session.

Note: This command should only be used for authorized penetration testing purposes.

**Code**: [[kerberos::purge
kerberos::golden /user:evil /domai]]

> The 'kerberos::purge' command is used to delete all Kerberos tickets from the current user's session. This can be useful in situations where a user has obtained a Kerberos ticket for a specific service and wants to remove it from their session. The 'kerberos::golden' command is used to create a Golden Ticket, which is a forged Kerberos ticket that grants the attacker full access to the domain. This can be used to bypass authentication and gain access to sensitive resources in the domain. It is important to note that the 'kerberos::golden' command should only be used for authorized penetration testing purposes.

**Command** ([[Purge Kerberos tickets]]):

```bash
kerberos::purge
```

**Command** ([[Generate Golden Kerberos Ticket]]):

```bash
kerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tck /ptt
```

**Command** ([[Request TGT with Golden Ticket]]):

```bash
kerberos::tgt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Ticket|T1097 - Pass the Ticket]]
- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[Generate Golden Kerberos Ticket]]
- [[Purge Kerberos tickets]]
- [[Request TGT with Golden Ticket]]

## Tags

- [[Domain]]
- [[Golden Ticket]]
- [[Windows - Persistence]]
