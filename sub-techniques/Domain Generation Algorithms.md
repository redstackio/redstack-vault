---
id: a013d4a9-d67c-4198-9f59-faf23ac94699
name: Domain Generation Algorithms
type: sub-technique
mitre_id: T1568.002
mitre_url: null
created_at: '2023-04-06T00:31:25.570217+00:00'
updated_at: '2023-04-06T00:31:25.570217+00:00'
parent_technique: '[[Dynamic Resolution|T1568 - Dynamic Resolution]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[DNS Beacon Payload with Cobalt Strike]]'
- '[[DNS Rebinding Protection Bypass via CNAME]]'
- '[[Git Index File Recovery]]'
---

# Domain Generation Algorithms

**MITRE ID**: T1568.002

**Parent Technique**: [[Dynamic Resolution|T1568 - Dynamic Resolution]]

This is a sub-technique of T1568 - Dynamic Resolution.

## Summary

Adversaries may make use of Domain Generation Algorithms (DGAs) to dynamically identify a destination domain for command and control traffic rather than relying on a list of static IP addresses or domains. This has the advantage of making it much harder for defenders to block, track, or take over th

## Description

Adversaries may make use of Domain Generation Algorithms (DGAs) to dynamically identify a destination domain for command and control traffic rather than relying on a list of static IP addresses or domains. This has the advantage of making it much harder for defenders to block, track, or take over the command and control channel, as there potentially could be thousands of domains that malware can check for instructions.(Citation: Cybereason Dissecting DGAs)(Citation: Cisco Umbrella DGA)(Citation: Unit 42 DGA Feb 2019)

DGAs can take the form of apparently random or “gibberish” strings (ex: istgmxdejdnxuyla.ru) when they construct domain names by generating each letter. Alternatively, some DGAs employ whole words as the unit by concatenating words together instead of letters (ex: cityjulydish.net). Many DGAs are time-based, generating a different domain for each time period (hourly, daily, monthly, etc). Others incorporate a seed value as well to make predicting future domains more difficult for defenders.(Citation: Cybereason Dissecting DGAs)(Citation: Cisco Umbrella DGA)(Citation: Talos CCleanup 2017)(Citation: Akamai DGA Mitigation)

Adversaries may use DGAs for the purpose of [Fallback Channels](https://attack.mitre.org/techniques/T1008). When contact is lost with the primary command and control server malware may employ a DGA as a means to reestablishing command and control.(Citation: Talos CCleanup 2017)(Citation: FireEye POSHSPY April 2017)(Citation: ESET Sednit 2017 Activity)

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures

There are 3 procedures using this sub-technique:

- [[DNS Beacon Payload with Cobalt Strike]]
- [[DNS Rebinding Protection Bypass via CNAME]]
- [[Git Index File Recovery]]
