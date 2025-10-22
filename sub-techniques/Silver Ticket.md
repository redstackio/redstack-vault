---
id: 0ce6db6e-eb9e-4b79-81ff-28f37811ab3e
name: Silver Ticket
type: sub-technique
mitre_id: T1558.002
mitre_url: null
created_at: '2023-04-06T00:31:26.990310+00:00'
updated_at: '2023-04-06T00:31:26.990310+00:00'
parent_technique: '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
  Tickets]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Active Directory ACL Abuse via Kerberoasting and AS-REP Roasting]]'
- '[[CCACHE Ticket Reuse from /tmp]]'
- '[[HTML GET CSRF Payload with User Interaction]]'
- '[[HTML GET CSRF Payload with User Interaction]]'
- '[[Kerberos Constrained Delegation - Impersonation on Resource]]'
- '[[Kerberos Unconstrained Delegation with SpoolService Abuse]]'
- '[[OAuth Token Theft via Redirect URI]]'
---

# Silver Ticket

**MITRE ID**: T1558.002

**Parent Technique**: [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

This is a sub-technique of T1558 - Steal or Forge Kerberos Tickets.

## Summary

Adversaries who have the password hash of a target service account (e.g. SharePoint, MSSQL) may forge Kerberos ticket granting service (TGS) tickets, also known as silver tickets. Kerberos TGS tickets are also known as service tickets.(Citation: ADSecurity Silver Tickets)

Silver tickets are more li

## Description

Adversaries who have the password hash of a target service account (e.g. SharePoint, MSSQL) may forge Kerberos ticket granting service (TGS) tickets, also known as silver tickets. Kerberos TGS tickets are also known as service tickets.(Citation: ADSecurity Silver Tickets)

Silver tickets are more limited in scope in than golden tickets in that they only enable adversaries to access a particular resource (e.g. MSSQL) and the system that hosts the resource; however, unlike golden tickets, adversaries with the ability to forge silver tickets are able to create TGS tickets without interacting with the Key Distribution Center (KDC), potentially making detection more difficult.(Citation: ADSecurity Detecting Forged Tickets)

Password hashes for target services may be obtained using [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) or [Kerberoasting](https://attack.mitre.org/techniques/T1558/003).

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 7 procedures using this sub-technique:

- [[Active Directory ACL Abuse via Kerberoasting and AS-REP Roasting]]
- [[CCACHE Ticket Reuse from /tmp]]
- [[HTML GET CSRF Payload with User Interaction]]
- [[HTML GET CSRF Payload with User Interaction]]
- [[Kerberos Constrained Delegation - Impersonation on Resource]]
- [[Kerberos Unconstrained Delegation with SpoolService Abuse]]
- [[OAuth Token Theft via Redirect URI]]
