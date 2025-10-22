---
id: a0f808b6-1eac-4611-8485-f57bd8e7959b
name: Threat Intel Vendors
type: sub-technique
mitre_id: T1597.001
mitre_url: null
created_at: '2023-04-06T00:31:26.111239+00:00'
updated_at: '2023-04-06T00:31:26.111239+00:00'
parent_technique: '[[Search Closed Sources|T1597 - Search Closed Sources]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Threat Intel Vendors

**MITRE ID**: T1597.001

**Parent Technique**: [[Search Closed Sources|T1597 - Search Closed Sources]]

This is a sub-technique of T1597 - Search Closed Sources.

## Summary

Adversaries may search private data from threat intelligence vendors for information that can be used during targeting. Threat intelligence vendors may offer paid feeds or portals that offer more data than what is publicly reported. Although sensitive details (such as customer names and other identi

## Description

Adversaries may search private data from threat intelligence vendors for information that can be used during targeting. Threat intelligence vendors may offer paid feeds or portals that offer more data than what is publicly reported. Although sensitive details (such as customer names and other identifiers) may be redacted, this information may contain trends regarding breaches such as target industries, attribution claims, and successful TTPs/countermeasures.(Citation: D3Secutrity CTI Feeds)

Adversaries may search in private threat intelligence vendor data to gather actionable information. Threat actors may seek information/indicators gathered about their own campaigns, as well as those conducted by other adversaries that may align with their target industries, capabilities/objectives, or other operational concerns. Information reported by vendors may also reveal opportunities other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190) or [External Remote Services](https://attack.mitre.org/techniques/T1133)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
