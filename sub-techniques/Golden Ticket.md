---
id: d313cf93-3145-4df6-a53a-ba92d4fa066a
name: Golden Ticket
type: sub-technique
mitre_id: T1558.001
mitre_url: null
created_at: '2023-04-06T00:31:26.370519+00:00'
updated_at: '2023-04-06T00:31:26.370519+00:00'
parent_technique: '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
  Tickets]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[CCACHE Ticket Reuse from Keyring with Tickey]]'
- '[[Golden Ticket Attack with Mimikatz]]'
- '[[HTML GET CSRF Payload with User Interaction]]'
- '[[HTML GET CSRF Payload with User Interaction]]'
- '[[Kerberos Bronze Bit Attack]]'
- '[[NTLM Reflection SMB Relay Attack]]'
- '[[Pass-the-Golden-Ticket Attack using Meterpreter]]'
- '[[RODC Key List Extraction and Golden Ticket Creation]]'
---

# Golden Ticket

**MITRE ID**: T1558.001

**Parent Technique**: [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

This is a sub-technique of T1558 - Steal or Forge Kerberos Tickets.

## Summary

Adversaries who have the KRBTGT account password hash may forge Kerberos ticket-granting tickets (TGT), also known as a golden ticket.(Citation: AdSecurity Kerberos GT Aug 2015) Golden tickets enable adversaries to generate authentication material for any account in Active Directory.(Citation: CERT-

## Description

Adversaries who have the KRBTGT account password hash may forge Kerberos ticket-granting tickets (TGT), also known as a golden ticket.(Citation: AdSecurity Kerberos GT Aug 2015) Golden tickets enable adversaries to generate authentication material for any account in Active Directory.(Citation: CERT-EU Golden Ticket Protection) 

Using a golden ticket, adversaries are then able to request ticket granting service (TGS) tickets, which enable access to specific resources. Golden tickets require adversaries to interact with the Key Distribution Center (KDC) in order to obtain TGS.(Citation: ADSecurity Detecting Forged Tickets)

The KDC service runs all on domain controllers that are part of an Active Directory domain. KRBTGT is the Kerberos Key Distribution Center (KDC) service account and is responsible for encrypting and signing all Kerberos tickets.(Citation: ADSecurity Kerberos and KRBTGT) The KRBTGT password hash may be obtained using [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) and privileged access to a domain controller.

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 8 procedures using this sub-technique:

- [[CCACHE Ticket Reuse from Keyring with Tickey]]
- [[Golden Ticket Attack with Mimikatz]]
- [[HTML GET CSRF Payload with User Interaction]]
- [[HTML GET CSRF Payload with User Interaction]]
- [[Kerberos Bronze Bit Attack]]
- [[NTLM Reflection SMB Relay Attack]]
- [[Pass-the-Golden-Ticket Attack using Meterpreter]]
- [[RODC Key List Extraction and Golden Ticket Creation]]
