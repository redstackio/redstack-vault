---
id: f4aa874a-477b-43e4-bb72-d6fc7048f90f
name: Pass the Ticket
type: sub-technique
mitre_id: T1550.003
mitre_url: null
created_at: '2023-04-06T00:31:26.401860+00:00'
updated_at: '2023-04-06T00:31:26.401860+00:00'
parent_technique: '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication
  Material]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[IIS Machine Key Cookie Decryption and Encryption]]'
- '[[IIS Machine Key Cookie Decryption and Encryption]]'
- '[[IIS Machine Key Cookie Decryption and Encryption]]'
- '[[Kerberos Clock Synchronization Attack]]'
- '[[Kerberos Constrained Delegation - Impersonation on Resource]]'
- '[[Pass-the-Golden-Ticket Attack using Meterpreter]]'
- '[[PrivExchange Attack with NTLM Relay]]'
---

# Pass the Ticket

**MITRE ID**: T1550.003

**Parent Technique**: [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

This is a sub-technique of T1550 - Use Alternate Authentication Material.

## Summary

Adversaries may “pass the ticket” using stolen Kerberos tickets to move laterally within an environment, bypassing normal system access controls. Pass the ticket (PtT) is a method of authenticating to a system using Kerberos tickets without having access to an account's password. Kerberos authentica

## Description

Adversaries may “pass the ticket” using stolen Kerberos tickets to move laterally within an environment, bypassing normal system access controls. Pass the ticket (PtT) is a method of authenticating to a system using Kerberos tickets without having access to an account's password. Kerberos authentication can be used as the first step to lateral movement to a remote system.

When preforming PtT, valid Kerberos tickets for [Valid Accounts](https://attack.mitre.org/techniques/T1078) are captured by [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). A user's service tickets or ticket granting ticket (TGT) may be obtained, depending on the level of access. A service ticket allows for access to a particular resource, whereas a TGT can be used to request service tickets from the Ticket Granting Service (TGS) to access any resource the user has privileges to access.(Citation: ADSecurity AD Kerberos Attacks)(Citation: GentilKiwi Pass the Ticket)

A [Silver Ticket](https://attack.mitre.org/techniques/T1558/002) can be obtained for services that use Kerberos as an authentication mechanism and are used to generate tickets to access that particular resource and the system that hosts the resource (e.g., SharePoint).(Citation: ADSecurity AD Kerberos Attacks)

A [Golden Ticket](https://attack.mitre.org/techniques/T1558/001) can be obtained for the domain using the Key Distribution Service account KRBTGT account NTLM hash, which enables generation of TGTs for any account in Active Directory.(Citation: Campbell 2014)

Adversaries may also create a valid Kerberos ticket using other user information, such as stolen password hashes or AES keys. For example, "overpassing the hash" involves using a NTLM password hash to authenticate as a user (i.e. [Pass the Hash](https://attack.mitre.org/techniques/T1550/002)) while also using the password hash to create a valid Kerberos ticket.(Citation: Stealthbits Overpass-the-Hash)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures

There are 7 procedures using this sub-technique:

- [[IIS Machine Key Cookie Decryption and Encryption]]
- [[IIS Machine Key Cookie Decryption and Encryption]]
- [[IIS Machine Key Cookie Decryption and Encryption]]
- [[Kerberos Clock Synchronization Attack]]
- [[Kerberos Constrained Delegation - Impersonation on Resource]]
- [[Pass-the-Golden-Ticket Attack using Meterpreter]]
- [[PrivExchange Attack with NTLM Relay]]
