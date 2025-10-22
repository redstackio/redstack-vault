---
id: e44c338c-599a-466d-b254-df9f53220b63
name: Scan Databases
type: sub-technique
mitre_id: T1596.005
mitre_url: null
created_at: '2023-04-06T00:31:27.136946+00:00'
updated_at: '2023-04-06T00:31:27.136946+00:00'
parent_technique: '[[Search Open Technical Databases|T1596 - Search Open Technical
  Databases]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Scan Databases

**MITRE ID**: T1596.005

**Parent Technique**: [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

This is a sub-technique of T1596 - Search Open Technical Databases.

## Summary

Adversaries may search within public scan databases for information about victims that can be used during targeting. Various online services continuously publish the results of Internet scans/surveys, often harvesting information such as active IP addresses, hostnames, open ports, certificates, and 

## Description

Adversaries may search within public scan databases for information about victims that can be used during targeting. Various online services continuously publish the results of Internet scans/surveys, often harvesting information such as active IP addresses, hostnames, open ports, certificates, and even server banners.(Citation: Shodan)

Adversaries may search scan databases to gather actionable information. Threat actors can use online resources and lookup tools to harvest information from these services. Adversaries may seek information about their already identified targets, or use these datasets to discover opportunities for successful breaches. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
