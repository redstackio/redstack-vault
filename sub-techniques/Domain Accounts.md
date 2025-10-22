---
id: 9a625ccc-1085-4bb7-8f78-6fcf4bbc215f
name: Domain Accounts
type: sub-technique
mitre_id: T1078.002
mitre_url: null
created_at: '2023-04-06T00:31:26.888893+00:00'
updated_at: '2023-04-06T00:31:26.888893+00:00'
parent_technique: '[[Valid Accounts|T1078 - Valid Accounts]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[AWS SSH Persistence with Authorized Keys]]'
---

# Domain Accounts

**MITRE ID**: T1078.002

**Parent Technique**: [[Valid Accounts|T1078 - Valid Accounts]]

This is a sub-technique of T1078 - Valid Accounts.

## Summary

Adversaries may obtain and abuse credentials of a domain account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion.(Citation: TechNet Credential Theft) Domain accounts are those managed by Active Directory Domain Services where access and permissions are con

## Description

Adversaries may obtain and abuse credentials of a domain account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion.(Citation: TechNet Credential Theft) Domain accounts are those managed by Active Directory Domain Services where access and permissions are configured across systems and services that are part of that domain. Domain accounts can cover users, administrators, and services.(Citation: Microsoft AD Accounts)

Adversaries may compromise domain accounts, some with a high level of privileges, through various means such as [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) or password reuse, allowing access to privileged resources of the domain.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[AWS SSH Persistence with Authorized Keys]]
