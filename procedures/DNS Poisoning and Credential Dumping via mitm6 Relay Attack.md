---
id: 3ee7dc2f-2eee-4075-b2a7-ff4751f2081f
name: DNS Poisoning and Credential Dumping via mitm6 Relay Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.649147+00:00'
updated_at: '2023-04-10T20:25:58.604862+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Exfiltration Over Web Service|T1567 - Exfiltration Over Web Service]]'
- '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
sub_techniques:
- '[[Exfiltration to Code Repository|T1567.001 - Exfiltration to Code Repository]]'
- '[[Reversible Encryption|T1556.005 - Reversible Encryption]]'
tags:
- '[[Active Directory Attacks]]'
- '[[DNS Poisonning - Relay delegation with mitm6]]'
- '[[Man-in-the-Middle attacks & relaying]]'
---

# DNS Poisoning and Credential Dumping via mitm6 Relay Attack

## Summary

This attack involves DNS poisoning and a mitm6 relay attack to steal user credentials and gain access to an Active Directory environment. The attacker first poisons the DNS cache of a target system, causing it to send DNS requests to a server controlled by the attacker. The attacker then performs a

## Description

# Description

This attack involves DNS poisoning and a mitm6 relay attack to steal user credentials and gain access to an Active Directory environment. The attacker first poisons the DNS cache of a target system, causing it to send DNS requests to a server controlled by the attacker. The attacker then performs a mitm6 relay attack, intercepting authentication requests and relaying them to the target server while capturing the user's credentials. Once the attacker has obtained valid credentials, they can use them to access the target's network and escalate privileges. This attack can be used to gain access to sensitive data and compromise the security of an organization.

 

## Requirements

1. Access to a target system

1. Ability to poison DNS cache

1. Ability to perform mitm6 relay attack

 

## Defense

1. Implement DNSSEC to prevent DNS poisoning

1. Use multi-factor authentication to prevent credential theft

1. Monitor network traffic for signs of DNS poisoning or mitm6 relay attacks

 

## Objectives

1. Steal user credentials

1. Gain unauthorized access to an Active Directory environment

 

# Instructions

1. 1. Clone the MITM6 repository and install it.
2. Use MITM6 to intercept traffic and filter requests based on the domain name.
3. Use NTLMRelayx to relay authentication requests to the target domain controller.
4. Grant delegation rights to the attacker and perform a Resource-Based Constrained Delegation (RBCD).
5. Use GetST.py to obtain a valid Service Ticket (ST).
6. Set the KRB5CCNAME environment variable to the administrator's credentials cache.
7. Use secretsdump.py to dump the target domain's credentials.

 



**Code**: [[git clone https://github.com/fox-it/mitm6.git 
cd ]]



> - The 'git clone' command clones the MITM6 repository and the 'pip install' command installs the necessary dependencies.
- The 'mitm6' command is used to intercept traffic and filter requests based on the domain name.
- The 'ntlmrelayx.py' command is used to relay authentication requests to the target domain controller. The '-ip' option specifies the interface to run the relay on, the '-t' option specifies the target domain controller, and the '-wh' option specifies the WPAD host to serve.
- The 'getST.py' command is used to obtain a valid Service Ticket (ST) for the target domain.
- The 'export' command sets the KRB5CCNAME environment variable to the administrator's credentials cache.
- The 'secretsdump.py' command is used to dump the target domain's credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Exfiltration|TA0010 - Exfiltration]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Exfiltration Over Web Service|T1567 - Exfiltration Over Web Service]]
- [[Modify Authentication Process|T1556 - Modify Authentication Process]]

### Sub-Techniques

- [[Exfiltration to Code Repository|T1567.001 - Exfiltration to Code Repository]]
- [[Reversible Encryption|T1556.005 - Reversible Encryption]]

## Tags

- [[Active Directory Attacks]]
- [[DNS Poisonning - Relay delegation with mitm6]]
- [[Man-in-the-Middle attacks & relaying]]


