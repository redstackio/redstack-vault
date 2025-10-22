---
id: 1e06b09b-b153-4e43-aeb1-804e6faa5b18
name: Kerberoasting
type: sub-technique
mitre_id: T1558.003
mitre_url: null
created_at: '2023-04-06T00:31:27.175477+00:00'
updated_at: '2023-04-06T00:31:27.175477+00:00'
parent_technique: '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
  Tickets]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Active Directory ACL Abuse via Kerberoasting and AS-REP Roasting]]'
- '[[Active Directory Assessment and Privilege Escalation]]'
- '[[CCACHE Ticket Reuse from Keyring with Tickey]]'
- '[[CCACHE Ticket Reuse from Keytab]]'
- '[[CCACHE Ticket Reuse from /tmp]]'
- '[[Golden Certificate Domain Persistence]]'
- '[[Golden Ticket Creation via Kerberos Purge]]'
- '[[Kerberos Bronze Bit Attack]]'
- '[[Kerberos Bronze Bit Attack Procedure]]'
- '[[Kerberos Clock Synchronization Attack]]'
- '[[Kerberos Clock Synchronization Attack]]'
- '[[Kerberos Constrained Delegation - Impersonation on Resource]]'
- '[[Kerberos S4U2self Privilege Escalation]]'
- '[[NTLM Reflection SMB Relay Attack]]'
- '[[OAuth Token Theft via Redirect URI]]'
- '[[Pass-the-Ticket with Silver Tickets]]'
- '[[RODC Key List Extraction and Golden Ticket Creation]]'
- '[[samAccountName Spoofing Attack]]'
- '[[User Certificate and TGT Persistence via Domain Request]]'
---

# Kerberoasting

**MITRE ID**: T1558.003

**Parent Technique**: [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

This is a sub-technique of T1558 - Steal or Forge Kerberos Tickets.

## Summary

Adversaries may abuse a valid Kerberos ticket-granting ticket (TGT) or sniff network traffic to obtain a ticket-granting service (TGS) ticket that may be vulnerable to [Brute Force](https://attack.mitre.org/techniques/T1110).(Citation: Empire InvokeKerberoast Oct 2016)(Citation: AdSecurity Cracking 

## Description

Adversaries may abuse a valid Kerberos ticket-granting ticket (TGT) or sniff network traffic to obtain a ticket-granting service (TGS) ticket that may be vulnerable to [Brute Force](https://attack.mitre.org/techniques/T1110).(Citation: Empire InvokeKerberoast Oct 2016)(Citation: AdSecurity Cracking Kerberos Dec 2015) 

Service principal names (SPNs) are used to uniquely identify each instance of a Windows service. To enable authentication, Kerberos requires that SPNs be associated with at least one service logon account (an account specifically tasked with running a service(Citation: Microsoft Detecting Kerberoasting Feb 2018)).(Citation: Microsoft SPN)(Citation: Microsoft SetSPN)(Citation: SANS Attacking Kerberos Nov 2014)(Citation: Harmj0y Kerberoast Nov 2016)

Adversaries possessing a valid Kerberos ticket-granting ticket (TGT) may request one or more Kerberos ticket-granting service (TGS) service tickets for any SPN from a domain controller (DC).(Citation: Empire InvokeKerberoast Oct 2016)(Citation: AdSecurity Cracking Kerberos Dec 2015) Portions of these tickets may be encrypted with the RC4 algorithm, meaning the Kerberos 5 TGS-REP etype 23 hash of the service account associated with the SPN is used as the private key and is thus vulnerable to offline [Brute Force](https://attack.mitre.org/techniques/T1110) attacks that may expose plaintext credentials.(Citation: AdSecurity Cracking Kerberos Dec 2015)(Citation: Empire InvokeKerberoast Oct 2016) (Citation: Harmj0y Kerberoast Nov 2016)

This same behavior could be executed using service tickets captured from network traffic.(Citation: AdSecurity Cracking Kerberos Dec 2015)

Cracked hashes may enable [Persistence](https://attack.mitre.org/tactics/TA0003), [Privilege Escalation](https://attack.mitre.org/tactics/TA0004), and [Lateral Movement](https://attack.mitre.org/tactics/TA0008) via access to [Valid Accounts](https://attack.mitre.org/techniques/T1078).(Citation: SANS Attacking Kerberos Nov 2014)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 19 procedures using this sub-technique:

- [[Active Directory ACL Abuse via Kerberoasting and AS-REP Roasting]]
- [[Active Directory Assessment and Privilege Escalation]]
- [[CCACHE Ticket Reuse from Keyring with Tickey]]
- [[CCACHE Ticket Reuse from Keytab]]
- [[CCACHE Ticket Reuse from /tmp]]
- [[Golden Certificate Domain Persistence]]
- [[Golden Ticket Creation via Kerberos Purge]]
- [[Kerberos Bronze Bit Attack]]
- [[Kerberos Bronze Bit Attack Procedure]]
- [[Kerberos Clock Synchronization Attack]]
- [[Kerberos Clock Synchronization Attack]]
- [[Kerberos Constrained Delegation - Impersonation on Resource]]
- [[Kerberos S4U2self Privilege Escalation]]
- [[NTLM Reflection SMB Relay Attack]]
- [[OAuth Token Theft via Redirect URI]]
- [[Pass-the-Ticket with Silver Tickets]]
- [[RODC Key List Extraction and Golden Ticket Creation]]
- [[samAccountName Spoofing Attack]]
- [[User Certificate and TGT Persistence via Domain Request]]
