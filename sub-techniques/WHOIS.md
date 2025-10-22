---
id: 0fd6cca6-7142-4c35-8cb4-966887a8f381
name: WHOIS
type: sub-technique
mitre_id: T1596.002
mitre_url: null
created_at: '2023-04-06T00:31:25.602335+00:00'
updated_at: '2023-04-06T00:31:25.602335+00:00'
parent_technique: '[[Search Open Technical Databases|T1596 - Search Open Technical
  Databases]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# WHOIS

**MITRE ID**: T1596.002

**Parent Technique**: [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

This is a sub-technique of T1596 - Search Open Technical Databases.

## Summary

Adversaries may search public WHOIS data for information about victims that can be used during targeting. WHOIS data is stored by regional Internet registries (RIR) responsible for allocating and assigning Internet resources such as domain names. Anyone can query WHOIS servers for information about 

## Description

Adversaries may search public WHOIS data for information about victims that can be used during targeting. WHOIS data is stored by regional Internet registries (RIR) responsible for allocating and assigning Internet resources such as domain names. Anyone can query WHOIS servers for information about a registered domain, such as assigned IP blocks, contact information, and DNS nameservers.(Citation: WHOIS)

Adversaries may search WHOIS data to gather actionable information. Threat actors can use online resources or command-line utilities to pillage through WHOIS data for information about potential victims. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
