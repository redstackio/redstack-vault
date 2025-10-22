---
id: 5285b0b0-cb40-4a05-a831-4aeaf801a15d
name: Identify Business Tempo
type: sub-technique
mitre_id: T1591.003
mitre_url: null
created_at: '2023-04-06T00:31:25.739294+00:00'
updated_at: '2023-04-06T00:31:25.739294+00:00'
parent_technique: '[[Gather Victim Org Information|T1591 - Gather Victim Org Information]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Identify Business Tempo

**MITRE ID**: T1591.003

**Parent Technique**: [[Gather Victim Org Information|T1591 - Gather Victim Org Information]]

This is a sub-technique of T1591 - Gather Victim Org Information.

## Summary

Adversaries may gather information about the victim's business tempo that can be used during targeting. Information about an organization’s business tempo may include a variety of details, including operational hours/days of the week. This information may also reveal times/dates of purchases and shi

## Description

Adversaries may gather information about the victim's business tempo that can be used during targeting. Information about an organization’s business tempo may include a variety of details, including operational hours/days of the week. This information may also reveal times/dates of purchases and shipments of the victim’s hardware and software resources.

Adversaries may gather this information in various ways, such as direct elicitation via [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about business tempo may also be exposed to adversaries via online or other accessible data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation: ThreatPost Broadvoice Leak) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Supply Chain Compromise](https://attack.mitre.org/techniques/T1195) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199))

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
