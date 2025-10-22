---
id: c334a6c3-d0b1-4161-a32f-1e8f6cdc02e2
name: CDNs
type: sub-technique
mitre_id: T1596.004
mitre_url: null
created_at: '2023-04-06T00:31:26.567687+00:00'
updated_at: '2023-04-06T00:31:26.567687+00:00'
parent_technique: '[[Search Open Technical Databases|T1596 - Search Open Technical
  Databases]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# CDNs

**MITRE ID**: T1596.004

**Parent Technique**: [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

This is a sub-technique of T1596 - Search Open Technical Databases.

## Summary

Adversaries may search content delivery network (CDN) data about victims that can be used during targeting. CDNs allow an organization to host content from a distributed, load balanced array of servers. CDNs may also allow organizations to customize content delivery based on the requestor’s geograph

## Description

Adversaries may search content delivery network (CDN) data about victims that can be used during targeting. CDNs allow an organization to host content from a distributed, load balanced array of servers. CDNs may also allow organizations to customize content delivery based on the requestor’s geographical region.

Adversaries may search CDN data to gather actionable information. Threat actors can use online resources and lookup tools to harvest information about content servers within a CDN. Adversaries may also seek and target CDN misconfigurations that leak sensitive information not intended to be hosted and/or do not have the same protection mechanisms (ex: login portals) as the content hosted on the organization’s website.(Citation: DigitalShadows CDN) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [Drive-by Compromise](https://attack.mitre.org/techniques/T1189)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
