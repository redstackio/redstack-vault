---
id: 7c1f090d-5489-4810-b2e9-c18ec271dd1d
name: Forest to Forest Trust Ticket Hash Dump
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.270608+00:00'
updated_at: '2023-04-10T20:36:12.823821+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Forest to Forest Compromise - Trust Ticket]]'
---

# Forest to Forest Trust Ticket Hash Dump

## Summary

The Forest to Forest Trust Ticket Hash Dump procedure is an attack that can be used to compromise a target Active Directory environment. This procedure is used to dump the hash of a trust ticket from a target domain. With this hash, an attacker can forge a trust ticket and use it to authenticate to

## Description

# Description

The Forest to Forest Trust Ticket Hash Dump procedure is an attack that can be used to compromise a target Active Directory environment. This procedure is used to dump the hash of a trust ticket from a target domain. With this hash, an attacker can forge a trust ticket and use it to authenticate to the target domain. This procedure is typically used in conjunction with other techniques to move laterally within the target environment.

Technical Explanation: The trust ticket is a cryptographic ticket that is used to authenticate between domains in a forest. The procedure involves dumping the hash of the trust ticket from a target domain controller using a tool such as Mimikatz. The hash can then be used to create a forged trust ticket, which can be used to authenticate to the target domain. This procedure requires administrative access to the target domain controller.

Business Value: This procedure allows an attacker to move laterally within a target environment, potentially gaining access to sensitive information and systems.

 

## Requirements

1. Administrative access to the target domain controller

1. Mimikatz or similar tool for dumping the hash

 

## Defense

1. Monitor and restrict administrative access to domain controllers

1. Implement strong password policies and multi-factor authentication

1. Regularly monitor for unusual authentication activity

 

## Objectives

1. Dump the hash of a trust ticket from a target domain

1. Forge a trust ticket using the dumped hash

1. Authenticate to the target domain using the forged trust ticket

 

# Instructions

1. Use the following command to dump the hash of the target domain:

mimikatz.exe "lsadump::dcsync /user:<username> /domain:<target_domain> /dc:<dc_ip>"

 



**Code**: [[currentdomain\targetdomain$]]



> This command will use Mimikatz to execute the 'lsadump::dcsync' command and dump the hash of the specified user in the target domain. Replace '<username>' with the name of the user whose hash you want to dump, '<target_domain>' with the name of the target domain, and '<dc_ip>' with the IP address of the domain controller in the target domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]

## Tags

- [[Active Directory Attacks]]
- [[Forest to Forest Compromise - Trust Ticket]]


