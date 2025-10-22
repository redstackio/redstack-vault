---
id: bc5f5ee1-ed1f-46dd-adbc-e325223e3da3
name: Local Accounts
type: sub-technique
mitre_id: T1078.003
mitre_url: null
created_at: '2023-04-06T00:31:27.239366+00:00'
updated_at: '2023-04-06T00:31:27.239366+00:00'
parent_technique: '[[Valid Accounts|T1078 - Valid Accounts]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Local Accounts

**MITRE ID**: T1078.003

**Parent Technique**: [[Valid Accounts|T1078 - Valid Accounts]]

This is a sub-technique of T1078 - Valid Accounts.

## Summary

Adversaries may obtain and abuse credentials of a local account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or 

## Description

Adversaries may obtain and abuse credentials of a local account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service.

Local Accounts may also be abused to elevate privileges and harvest credentials through [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). Password reuse may allow the abuse of local accounts across a set of machines on a network for the purposes of Privilege Escalation and Lateral Movement. 

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
