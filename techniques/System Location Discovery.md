---
id: 60c80af9-3ead-4f59-ac40-727ea549e3db
name: System Location Discovery
type: technique
mitre_id: T1614
mitre_url: null
created_at: '2023-04-06T00:31:26.911505+00:00'
updated_at: '2023-04-06T00:31:27.869465+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
---

# System Location Discovery

**MITRE ID**: T1614

## Description

Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from [System Location Discovery](https://attack.mitre.org/techniques/T1614) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings.(Citation: FBI Ragnar Locker 2020)(Citation: Sophos Geolocation 2016)(Citation: Bleepingcomputer RAT malware 2020) Windows API functions such as <code>GetLocaleInfoW</code> can also be used to determine the locale of the host.(Citation: FBI Ragnar Locker 2020) In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance.(Citation: AWS Instance Identity Documents)(Citation: Microsoft Azure Instance Metadata 2021)

Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.(Citation: Securelist Trasparent Tribe 2020)(Citation: Sophos Geolocation 2016)

## Tactics

- [[Discovery|TA0007 - Discovery]]
