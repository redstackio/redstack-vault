---
id: 18072241-fde6-446c-9347-0897b859e66d
name: Network Topology
type: sub-technique
mitre_id: T1590.004
mitre_url: null
created_at: '2023-04-06T00:31:25.880254+00:00'
updated_at: '2023-04-06T00:31:25.880254+00:00'
parent_technique: '[[Gather Victim Network Information|T1590 - Gather Victim Network
  Information]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Network Topology

**MITRE ID**: T1590.004

**Parent Technique**: [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

This is a sub-technique of T1590 - Gather Victim Network Information.

## Summary

Adversaries may gather information about the victim's network topology that can be used during targeting. Information about network topologies may include a variety of details, including the physical and/or logical arrangement of both external-facing and internal network environments. This informati

## Description

Adversaries may gather information about the victim's network topology that can be used during targeting. Information about network topologies may include a variety of details, including the physical and/or logical arrangement of both external-facing and internal network environments. This information may also include specifics regarding network devices (gateways, routers, etc.) and other infrastructure.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about network topologies may also be exposed to adversaries via online or other accessible data sets (ex: [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation: DNS Dumpster) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
