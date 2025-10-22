---
id: 6a1c9729-03ec-4f1f-98fa-0d6ae5eaabe7
name: DPAPI Credential Theft with Hekatomb
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.325320+00:00'
updated_at: '2023-04-10T20:37:12.933432+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Data Protection API]]'
- '[[Hekatomb - Steal all credentials on domain]]'
- '[[Windows - DPAPI]]'
commands:
- '[[Install Hekatomb and Perform Hashes]]'
---

# DPAPI Credential Theft with Hekatomb

## Summary

DPAPI is a key-based encryption technology used to encrypt data in Windows, including user credentials. Hekatomb is a tool that can be used to steal all credentials on a domain by extracting DPAPI hashes from the system. This technique can be used by an attacker to gain access to sensitive informat

## Description

# Description

DPAPI is a key-based encryption technology used to encrypt data in Windows, including user credentials. Hekatomb is a tool that can be used to steal all credentials on a domain by extracting DPAPI hashes from the system. This technique can be used by an attacker to gain access to sensitive information and escalate privileges on a target network. 

Technical Explanation: Hekatomb uses the DPAPIck library to extract DPAPI hashes from the system. These hashes can then be used to crack passwords and gain access to user accounts. 

Business Value: This technique can be used by attackers to gain access to sensitive information, such as financial data or intellectual property, and to escalate privileges on a target network.

## Requirements

1. Access to a Windows system with DPAPI hashes

1. Hekatomb tool

## Defense

1. Implement strong password policies and multi-factor authentication to make it more difficult to crack passwords

1. Monitor for unusual account activity and investigate any suspicious behavior

1. Disable or restrict access to tools that can be used to extract DPAPI hashes

## Objectives

1. Steal all credentials on a target domain

1. Escalate privileges on a target network

# Instructions

1. To extract the NTLM hash of the specified domain user, first install the Hekatomb tool using pip3. Then, run the command 'hekatomb -hashes :<hash type> <domain>/<username>@<ip address> -debug -dnstcp', replacing the hash type, domain, username, and IP address with the appropriate values. The tool will perform a DNS request to the specified IP address to extract the hash.

**Code**: [[pip3 install hekatomb
hekatomb -hashes :ed0052e5a6]]

> The '-hashes' option specifies the type of hash to extract. The ':ed' prefix indicates an NTLM hash. The '<domain>/<username>@<ip address>' argument specifies the domain, username, and IP address of the user whose hash is being extracted. The '-debug' option enables verbose output, while the '-dnstcp' option forces the tool to use TCP instead of UDP for the DNS request.

**Command** ([[Install Hekatomb and Perform Hashes]]):

```bash
pip3 install hekatomb
hekatomb -hashes :ed0052e5a66b1c8e942cc9481a50d56 DOMAIN.local/administrator@10.0.0.1 -debug -dnstcp
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Install Hekatomb and Perform Hashes]]

## Tags

- [[Data Protection API]]
- [[Hekatomb - Steal all credentials on domain]]
- [[Windows - DPAPI]]
