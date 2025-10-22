---
id: 01ff2956-e878-4635-8205-f37c355d3b68
name: Software Discovery
type: technique
mitre_id: T1518
mitre_url: null
created_at: '2023-04-06T00:31:27.081717+00:00'
updated_at: '2023-04-06T03:56:38.978335+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[AMSI Provider Enumeration]]'
- '[[Detection of .NET Serialization Attacks]]'
- '[[Discovery of Local MSSQL Server Instances]]'
- '[[Linux - SSH Key Predictable PRNG Privilege Escalation]]'
- '[[MSSQL Server Version Query]]'
- '[[Reflection Method with WMF5 Autologging Bypass]]'
- '[[Server Side Template Injection - Expression Language EL Properties Information
  Disclosure]]'
---

# Software Discovery

**MITRE ID**: T1518

## Description

Adversaries may attempt to get a listing of software and software versions that are installed on a system or in a cloud environment. Adversaries may use the information from [Software Discovery](https://attack.mitre.org/techniques/T1518) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable to [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068).

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (7)

- [[AMSI Provider Enumeration]]
- [[Detection of .NET Serialization Attacks]]
- [[Discovery of Local MSSQL Server Instances]]
- [[Linux - SSH Key Predictable PRNG Privilege Escalation]]
- [[MSSQL Server Version Query]]
- [[Reflection Method with WMF5 Autologging Bypass]]
- [[Server Side Template Injection - Expression Language EL Properties Information Disclosure]]
