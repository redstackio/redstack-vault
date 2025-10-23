---
id: 1d6d135d-657e-41a5-a138-3ae8b0cd1379
name: SID Hijacking for Golden Ticket Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.249434+00:00'
updated_at: '2023-04-10T20:26:22.620442+00:00'
tags:
- '[[Active Directory Attacks]]'
- '[[Child Domain to Forest Compromise - SID Hijacking]]'
commands:
- '[[Convert target.domain.com\krbtgt to SID]]'
- '[[Lookup SID using Impacket]]'
---

# SID Hijacking for Golden Ticket Attack

## Summary

SID Hijacking is a technique that allows an attacker to elevate their privileges within a domain. In this specific scenario, the attacker has compromised a child domain and is attempting to move laterally to the parent domain. By using the Convert-NameToSid command, the attacker can obtain a SID (S

## Description

# Description

SID Hijacking is a technique that allows an attacker to elevate their privileges within a domain. In this specific scenario, the attacker has compromised a child domain and is attempting to move laterally to the parent domain. By using the Convert-NameToSid command, the attacker can obtain a SID (Security Identifier) of a user in the parent domain. They can then use this SID to create a new user object in the child domain with the same SID as the user in the parent domain. This new user object will have the same privileges as the user in the parent domain, allowing the attacker to move laterally to the parent domain. Once in the parent domain, the attacker can use a Golden Ticket attack to generate a forged Kerberos ticket and gain access to any resource in the domain. This attack is difficult to detect and can persist even after the initial compromise is mitigated.

 

## Requirements

1. Access to a compromised child domain

1. Knowledge of a user in the parent domain

 

## Defense

1. Implement proper access controls and segregation of duties to prevent attackers from moving laterally between domains

1. Monitor for unusual user creation or modification, especially for users with the same SID as a user in another domain

1. Implement multi-factor authentication and limit the use of Kerberos tickets to mitigate Golden Ticket attacks

 

## Objectives

1. Move laterally from a compromised child domain to the parent domain

1. Gain access to resources in the parent domain

 

# Instructions

1. This command helps to convert a username or group name to a Security Identifier (SID) for a specified domain. The SID is a unique value that identifies a security principal, such as a user, group, or computer account. To use this command, replace 'target.domain.com\krbtgt' with the username or group name you want to convert to a SID.

 



**Code**: [[$ Convert-NameToSid target.domain.com\krbtgt
S-1-5]]



> The 'Convert-NameToSid' command can be used to find the SID of a domain. The command takes a username or group name as an argument and returns the corresponding SID. This can be helpful in various scenarios, such as when you need to grant permissions to a user or group on a remote system. Additionally, the command can be used in combination with the Impacket tool 'lookupsid.py' to perform SID lookups on remote systems.



**Command** ([[Convert target.domain.com\krbtgt to SID]]):

```bash
$ Convert-NameToSid target.domain.com\krbtgt
S-1-5-21-2941561648-383941485-1389968811-502


```





**Command** ([[Lookup SID using Impacket]]):

```bash
lookupsid.py domain/user:password@10.10.10.10
```



2. This command is used to create a golden ticket and launch a Golden Ticket Attack on the parent domain. The /user argument specifies the user account that will be used to generate the ticket. The /krbtgt argument specifies the hash of the KRBTGT account. The /domain argument specifies the domain to attack. The /sid argument specifies the security identifier (SID) of the domain. The /sids argument specifies the SIDs of the groups to add to the ticket. The /ptt argument specifies that the ticket should be loaded into memory for immediate use.

 



**Code**: [[kerberos::golden /user:Administrator /krbtgt:HASH_]]



> A Golden Ticket Attack is a type of attack that allows an attacker to create a forged Kerberos ticket that grants them full access to a domain. This attack is possible because of a flaw in the way that Kerberos handles authentication. By creating a golden ticket, an attacker can bypass authentication and gain access to any resource on the domain. This command is typically used by attackers who have already gained access to a domain and want to escalate their privileges.

## Commands Used

- [[Convert target.domain.com\krbtgt to SID]]
- [[Lookup SID using Impacket]]

## Tags

- [[Active Directory Attacks]]
- [[Child Domain to Forest Compromise - SID Hijacking]]


