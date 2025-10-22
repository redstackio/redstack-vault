---
id: ee76c610-ab99-4145-97c4-650f47710634
name: Network Logon Script
type: sub-technique
mitre_id: T1037.003
mitre_url: null
created_at: '2023-04-06T00:31:26.904637+00:00'
updated_at: '2023-04-06T00:31:26.904637+00:00'
parent_technique: '[[Logon Scripts|T1037 - Logon Scripts]]'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Network Logon Script

**MITRE ID**: T1037.003

**Parent Technique**: [[Logon Scripts|T1037 - Logon Scripts]]

This is a sub-technique of T1037 - Logon Scripts.

## Summary

Adversaries may use network logon scripts automatically executed at logon initialization to establish persistence. Network logon scripts can be assigned using Active Directory or Group Policy Objects.(Citation: Petri Logon Script AD) These logon scripts run with the privileges of the user they are a

## Description

Adversaries may use network logon scripts automatically executed at logon initialization to establish persistence. Network logon scripts can be assigned using Active Directory or Group Policy Objects.(Citation: Petri Logon Script AD) These logon scripts run with the privileges of the user they are assigned to. Depending on the systems within the network, initializing one of these scripts could apply to more than one or potentially all systems.  

Adversaries may use these scripts to maintain persistence on a network. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary.

## Tactics

This sub-technique is used in the following tactics:

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
