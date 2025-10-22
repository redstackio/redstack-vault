---
id: cc8280b8-3593-420e-9949-4f3d57fcbf1d
name: Pass-the-Ticket Sapphire Tickets Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.909937+00:00'
updated_at: '2023-04-10T20:26:34.653059+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Tickets]]'
- '[[Pass-the-Ticket Sapphire Tickets]]'
commands:
- '[[Request impersonation with domain admin privileges]]'
---

# Pass-the-Ticket Sapphire Tickets Attack

## Summary

The Pass-the-Ticket Sapphire Tickets attack is a technique used by attackers to impersonate a user or service account, and gain unauthorized access to network resources. This attack involves using a forged Kerberos ticket, known as a Sapphire Ticket, to authenticate to network resources. The attack

## Description

# Description

The Pass-the-Ticket Sapphire Tickets attack is a technique used by attackers to impersonate a user or service account, and gain unauthorized access to network resources. This attack involves using a forged Kerberos ticket, known as a Sapphire Ticket, to authenticate to network resources. The attacker can use this technique to move laterally within the network, escalate privileges, and gain access to sensitive data. The attack is particularly effective when the attacker has already compromised a domain user account with administrative privileges, as they can then use this account to generate the Sapphire Ticket.

## Requirements

1. Valid domain user account credentials

1. Access to a domain-joined machine

1. Tools for generating Kerberos tickets

## Defense

1. Implement strong password policies and multi-factor authentication to prevent compromise of domain user accounts

1. Monitor and analyze network traffic for signs of suspicious activity, such as unusual authentication requests or use of invalid Kerberos tickets

1. Regularly review and update access controls to limit the scope of potential attacks

## Objectives

1. Gain unauthorized access to network resources

1. Move laterally within the network

1. Escalate privileges

1. Access sensitive data

# Instructions

1. To use this command, run the ticketer.py script with the -request and -impersonate flags. Specify the domain admin account to impersonate with the 'domain_adm' argument. Provide the domain name with the 'domain' argument. Enter the credentials of a domain user with the 'user' and 'password' arguments. Use the 'aesKey' argument to specify the AES key for the service. Finally, provide the domain SID with the 'domain-sid' argument. The 'baduser' argument will be ignored.

**Code**: [[# baduser argument will be ignored
ticketer.py -re]]

> This command allows an attacker to impersonate a domain admin by mimicking the PAC field as close as possible to a legitimate one. The PAC (Privilege Attribute Certificate) is a field in the Kerberos ticket that contains authorization data for the user. By mimicking a legitimate PAC, the attacker can gain access to resources that are restricted to domain admins.

**Command** ([[Request impersonation with domain admin privileges]]):

```bash
ticketer.py -request -impersonate 'domain_adm' -domain 'lab.local' -user 'domain_user' -password 'password' -aesKey 'krbtgt/service AES key' -domain-sid 'S-1-5-21-...' 'baduser'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[Request impersonation with domain admin privileges]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Tickets]]
- [[Pass-the-Ticket Sapphire Tickets]]
