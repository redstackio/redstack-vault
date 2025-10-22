---
id: 73a52261-7b06-4830-93d5-8c2571e4e18b
name: Active Directory Trust Ticket Forgery with Mimikatz
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.322967+00:00'
updated_at: '2023-04-10T20:26:18.480256+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Kerberoasting|T1208 - Kerberoasting]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Create a forged trust ticket (inter-realm TGT) using Mimikatz]]'
- '[[Forest to Forest Compromise - Trust Ticket]]'
commands:
- '[[Kerberos Golden Ticket]]'
- '[[Kerberos Golden Ticket]]'
---

# Active Directory Trust Ticket Forgery with Mimikatz

## Summary

Active Directory trust ticket forgery is a technique used by attackers to gain unauthorized access to resources across different domains or forests. This procedure involves creating a forged trust ticket using Mimikatz, a popular post-exploitation tool. The attacker can use the forged ticket to obt

## Description

# Description

Active Directory trust ticket forgery is a technique used by attackers to gain unauthorized access to resources across different domains or forests. This procedure involves creating a forged trust ticket using Mimikatz, a popular post-exploitation tool. The attacker can use the forged ticket to obtain a valid TGT for a trusted domain, which can then be used to authenticate to other systems within that domain. This technique can be used to escalate privileges and move laterally across a network.

From a technical standpoint, this procedure involves extracting the domain's krbtgt hash, which is used to encrypt Kerberos tickets. The attacker then uses Mimikatz to create a forged trust ticket using the krbtgt hash, which can be used to obtain a TGT for the trusted domain. This TGT can be used to authenticate to other systems within the trusted domain.

The business value of this procedure is that it allows attackers to move laterally across a network, gain access to sensitive resources, and escalate privileges.

## Requirements

1. Valid domain credentials with privileges to extract krbtgt hash

1. Access to a system where Mimikatz can be run

## Defense

1. Implement least privilege access controls to limit the potential impact of an attacker who has obtained a forged trust ticket

1. Monitor for suspicious activity, such as unusual authentication requests or changes to trust relationships

1. Regularly review and update trust relationships between domains and forests

## Objectives

1. Gain unauthorized access to resources across different domains or forests

1. Escalate privileges and move laterally across a network

# Instructions

1. Use Mimikatz to create a Kerberos Golden Ticket for a specific domain and target service account using the following command:
kerberos::golden /domain:<domain_name> /sid:<domain_SID> /rc4:<NTLM_hash_of_the_KrBTGT_account> /user:<target_service_account> /service:krbtgt /target:<target_domain_name> /ticket:<path_to_save_ticket_file>

**Code**: [[mimikatz(commandline) # kerberos::golden /domain:d]]

> This command creates a Kerberos Golden Ticket, which is a forged TGT (Ticket Granting Ticket) that can be used to impersonate any domain user, and provides full access to the domain. The command requires the domain name, domain SID, NTLM hash of the KrBTGT account, target service account, target domain name, and a path to save the ticket file. The command uses the Mimikatz tool, which is a post-exploitation tool that allows extracting plaintexts passwords, hash, PIN codes and kerberos tickets from memory. This command can be used for privilege escalation, persistence, and lateral movement.

**Command** ([[Kerberos Golden Ticket]]):

```bash
mimikatz(commandline) # kerberos::golden /domain:domain.local /sid:S-1-5-21... /rc4:HASH_TRUST$ /user:Administrator /service:krbtgt /target:external.com /ticket:c:\temp\trust.kirbi
```

**Command** ([[Kerberos Golden Ticket]]):

```bash
mimikatz(commandline) # kerberos::golden /domain:dollarcorp.moneycorp.local /sid:S-1-5-21-1874506631-3219952063-538504511 /sids:S-1-5-21-280534878-1496970234-700767426-519 /rc4:e4e47c8fc433c9e0f3b17ea74856ca6b /user:Administrator /service:krbtgt /target:moneycorp.local /ticket:c:\ad\tools\mcorp-ticket.kirbi
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Kerberoasting|T1208 - Kerberoasting]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[Kerberos Golden Ticket]]
- [[Kerberos Golden Ticket]]

## Tags

- [[Active Directory Attacks]]
- [[Create a forged trust ticket (inter-realm TGT) using Mimikatz]]
- [[Forest to Forest Compromise - Trust Ticket]]
