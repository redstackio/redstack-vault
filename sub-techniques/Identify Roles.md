---
id: 13088a21-5478-4b35-aeaa-dfd87b05a377
name: Identify Roles
type: sub-technique
mitre_id: T1591.004
mitre_url: null
created_at: '2023-04-06T00:31:26.942466+00:00'
updated_at: '2023-04-06T00:31:26.942466+00:00'
parent_technique: '[[Gather Victim Org Information|T1591 - Gather Victim Org Information]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Identify Roles

**MITRE ID**: T1591.004

**Parent Technique**: [[Gather Victim Org Information|T1591 - Gather Victim Org Information]]

This is a sub-technique of T1591 - Gather Victim Org Information.

## Summary

Adversaries may gather information about identities and roles within the victim organization that can be used during targeting. Information about business roles may reveal a variety of targetable details, including identifiable information for key personnel as well as what data/resources they have a

## Description

Adversaries may gather information about identities and roles within the victim organization that can be used during targeting. Information about business roles may reveal a variety of targetable details, including identifiable information for key personnel as well as what data/resources they have access to.

Adversaries may gather this information in various ways, such as direct elicitation via [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about business roles may also be exposed to adversaries via online or other accessible data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation: ThreatPost Broadvoice Leak) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
