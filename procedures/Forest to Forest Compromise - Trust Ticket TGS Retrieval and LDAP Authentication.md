---
id: 9e9de362-1ec8-447e-ac28-0f0cef43f41b
name: Forest to Forest Compromise - Trust Ticket TGS Retrieval and LDAP Authentication
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.350064+00:00'
updated_at: '2023-04-10T20:26:01.146181+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Indirect Command Execution|T1202 - Indirect Command Execution]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Forest to Forest Compromise - Trust Ticket]]'
- '[[Use the Trust Ticket file to get a ST for the targeted service]]'
---

# Forest to Forest Compromise - Trust Ticket TGS Retrieval and LDAP Authentication

## Summary

This procedure involves using a Trust Ticket file to get a TGS ticket for the targeted service. The TGS ticket can then be retrieved and used for LDAP authentication. The Trust Ticket file is a file that contains the encrypted hash of the trust password between two Active Directory forests. This pr

## Description

# Description

This procedure involves using a Trust Ticket file to get a TGS ticket for the targeted service. The TGS ticket can then be retrieved and used for LDAP authentication. The Trust Ticket file is a file that contains the encrypted hash of the trust password between two Active Directory forests. This procedure can be used to move laterally within a network and gain access to sensitive information. To execute this attack, an attacker needs to have access to a Trust Ticket file and knowledge of the targeted service.

Technical Explanation: The Trust Ticket file contains the encrypted hash of the trust password between two Active Directory forests. By cracking this hash, an attacker can get the trust password and use it to create a TGS ticket for the targeted service. The TGS ticket can then be retrieved and used for LDAP authentication. The KirbiKator tool can be used to inject the TGS ticket and access the targeted service.

Business Value: This procedure can be used by attackers to gain access to sensitive information and move laterally within a network. By compromising the trust relationship between two Active Directory forests, attackers can gain access to resources that they would not normally have access to, such as sensitive data or critical systems.

## Requirements

1. Access to a Trust Ticket file

1. Knowledge of the targeted service

## Defense

1. Limit the number of users who have access to Trust Ticket files

1. Use strong passwords for trust relationships

1. Implement network segmentation to limit lateral movement

## Objectives

1. Gain access to sensitive information

1. Move laterally within a network

# Instructions

1. To retrieve a TGS ticket and use it for LDAP authentication, follow these steps:
1. Run the command '.\asktgs.exe c:\temp\trust.kirbi CIFS/machine.domain.local' to retrieve a TGS ticket for the CIFS service on the machine.domain.local host.
2. Run the command '.\Rubeus.exe asktgs /ticket:c:\ad\tools\mcorp-ticket.kirbi /service:LDAP/mcorp-dc.moneycorp.local /dc:mcorp-dc.moneycorp.local /ptt' to use the TGS ticket for LDAP authentication against the mcorp-dc.moneycorp.local domain controller.

**Code**: [[.\asktgs.exe c:\temp\trust.kirbi CIFS/machine.doma]]

> The first command retrieves a TGS ticket for the CIFS service on the machine.domain.local host and saves it to the trust.kirbi file in the c:\temp directory. The second command uses the TGS ticket stored in the c:\ad\tools\mcorp-ticket.kirbi file to authenticate against the LDAP service on the mcorp-dc.moneycorp.local domain controller. The /service argument specifies the LDAP service and the /dc argument specifies the domain controller to use for authentication. The /ptt argument tells Rubeus to import the ticket into the current user's session so it can be used for subsequent operations.

2. To use this command, first obtain a valid .kirbi ticket. Then, use the KirbiKator tool to inject the ticket into the current session. Finally, use the 'ls' command to access the targeted service with the spoofed rights.

**Code**: [[kirbikator lsa .\ticket.kirbi
ls \\machine.domain.]]

> The 'kirbikator' command is used to inject a Kerberos ticket into the current session. The 'lsa' option specifies that the ticket should be injected into the Local Security Authority Subsystem Service (LSASS) process. The '.\ticket.kirbi' argument specifies the location of the .kirbi ticket on the local system. The 'ls' command is used to list the contents of a directory. The '\\machine.domain.local\c$' argument specifies the location of the directory to be listed, using the UNC path format. By injecting the Kerberos ticket into the LSASS process, the 'ls' command will be executed with the spoofed rights of the user associated with the ticket, allowing access to resources that would otherwise be inaccessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Indirect Command Execution|T1202 - Indirect Command Execution]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Tags

- [[Active Directory Attacks]]
- [[Forest to Forest Compromise - Trust Ticket]]
- [[Use the Trust Ticket file to get a ST for the targeted service]]
