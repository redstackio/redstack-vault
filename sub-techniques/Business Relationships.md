---
id: 6ee5cde0-2afe-49e2-80b5-52d6d7f3a39f
name: Business Relationships
type: sub-technique
mitre_id: T1591.002
mitre_url: null
created_at: '2023-04-06T00:31:26.328469+00:00'
updated_at: '2023-04-06T00:31:26.328469+00:00'
parent_technique: '[[Gather Victim Org Information|T1591 - Gather Victim Org Information]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Business Relationships

**MITRE ID**: T1591.002

**Parent Technique**: [[Gather Victim Org Information|T1591 - Gather Victim Org Information]]

This is a sub-technique of T1591 - Gather Victim Org Information.

## Summary

Adversaries may gather information about the victim's business relationships that can be used during targeting. Information about an organization’s business relationships may include a variety of details, including second or third-party organizations/domains (ex: managed service providers, contracto

## Description

Adversaries may gather information about the victim's business relationships that can be used during targeting. Information about an organization’s business relationships may include a variety of details, including second or third-party organizations/domains (ex: managed service providers, contractors, etc.) that have connected (and potentially elevated) network access. This information may also reveal supply chains and shipment paths for the victim’s hardware and software resources.

Adversaries may gather this information in various ways, such as direct elicitation via [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about business relationships may also be exposed to adversaries via online or other accessible data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation: ThreatPost Broadvoice Leak) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Supply Chain Compromise](https://attack.mitre.org/techniques/T1195), [Drive-by Compromise](https://attack.mitre.org/techniques/T1189), or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
