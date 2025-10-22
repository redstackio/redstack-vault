---
id: 3ea05c77-3ec2-4394-8f3b-ae261ce1aa91
name: Logon Script (Windows)
type: sub-technique
mitre_id: T1037.001
mitre_url: null
created_at: '2023-04-06T00:31:27.128610+00:00'
updated_at: '2023-04-06T00:31:27.128610+00:00'
parent_technique: '[[Logon Scripts|T1037 - Logon Scripts]]'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Logon Script (Windows)

**MITRE ID**: T1037.001

**Parent Technique**: [[Logon Scripts|T1037 - Logon Scripts]]

This is a sub-technique of T1037 - Logon Scripts.

## Summary

Adversaries may use Windows logon scripts automatically executed at logon initialization to establish persistence. Windows allows logon scripts to be run whenever a specific user or group of users log into a system.(Citation: TechNet Logon Scripts) This is done via adding a path to a script to the <

## Description

Adversaries may use Windows logon scripts automatically executed at logon initialization to establish persistence. Windows allows logon scripts to be run whenever a specific user or group of users log into a system.(Citation: TechNet Logon Scripts) This is done via adding a path to a script to the <code>HKCU\Environment\UserInitMprLogonScript</code> Registry key.(Citation: Hexacorn Logon Scripts)

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. 

## Tactics

This sub-technique is used in the following tactics:

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
