---
id: e8805cff-13b4-4b11-9926-4405e1e6dcb3
name: Pass-the-Ticket Silver Ticket Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.853736+00:00'
updated_at: '2023-04-10T20:36:11.322271+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Tickets]]'
- '[[Pass-the-Ticket Silver Tickets]]'
---

# Pass-the-Ticket Silver Ticket Creation

## Summary

Pass-the-Ticket Silver Tickets is a technique used by attackers to gain access to a network by using a forged Kerberos ticket. This technique is often used after an attacker has already gained initial access to a network through other means. The attacker uses a tool like Mimikatz to extract the Ker

## Description

# Description

Pass-the-Ticket Silver Tickets is a technique used by attackers to gain access to a network by using a forged Kerberos ticket. This technique is often used after an attacker has already gained initial access to a network through other means. The attacker uses a tool like Mimikatz to extract the Kerberos ticket from memory, and then uses that ticket to create a new ticket granting ticket (TGT) with elevated privileges. This new TGT allows the attacker to access resources they would not normally have access to, and move laterally through the network.

## Requirements

1. Valid credentials for a domain user account

1. Access to a computer on the domain

1. Mimikatz or similar tool for extracting Kerberos tickets

## Defense

1. Implementing least privilege access controls can limit the impact of Pass-the-Ticket attacks

1. Enforcing strong password policies and multi-factor authentication can prevent attackers from obtaining valid domain credentials

1. Monitoring for anomalous activity such as unusual logins or unexpected privilege escalation can help detect and respond to Pass-the-Ticket attacks

## Objectives

1. Gain access to a network using a forged Kerberos ticket

1. Create a new TGT with elevated privileges

1. Access resources that would not normally be accessible

# Instructions

1. To create a Kerberos Golden Ticket, use the 'kerberos::golden' command in Mimikatz with the required arguments. The '/user' argument specifies the user account for which the ticket is being created, the '/domain' argument specifies the domain name, the '/sid' argument specifies the domain security identifier (SID), the '/target' argument specifies the target host name, the '/rc4' argument specifies the NT hash of the target machine, and the '/service' argument specifies the service name. Once the ticket is created, use the 'misc::convert' command to convert the ticket to a cache file. Finally, set the 'KRB5CCNAME' environment variable to point to the cache file and use the 'psexec.py' tool to execute commands on the target host.

**Code**: [[# Create a ticket for the service
mimikatz $ kerbe]]

> This command is used to create a Kerberos Golden Ticket, which is a forged Kerberos ticket that can be used to gain unauthorized access to a network. The ticket can be used to authenticate to any service on the target host as any user in the domain. This attack is possible due to a weakness in the Kerberos protocol that allows an attacker to create a valid ticket without knowing the user's password. Organizations can mitigate this attack by implementing strong password policies, limiting the use of privileged accounts, and monitoring for suspicious activity on the network.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Tickets]]
- [[Pass-the-Ticket Silver Tickets]]
