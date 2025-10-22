---
id: 1510742e-fdf0-4ea5-a365-be76f069fd87
name: Scanning IP Blocks
type: sub-technique
mitre_id: T1595.001
mitre_url: null
created_at: '2023-04-06T00:31:27.034648+00:00'
updated_at: '2023-04-06T00:31:27.034648+00:00'
parent_technique: '[[Active Scanning|T1595 - Active Scanning]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Scanning IP Blocks

**MITRE ID**: T1595.001

**Parent Technique**: [[Active Scanning|T1595 - Active Scanning]]

This is a sub-technique of T1595 - Active Scanning.

## Summary

Adversaries may scan victim IP blocks to gather information that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses.

Adversaries may scan IP blocks in order to [Gather Victim Network Information](https://attack.mitre.org/

## Description

Adversaries may scan victim IP blocks to gather information that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses.

Adversaries may scan IP blocks in order to [Gather Victim Network Information](https://attack.mitre.org/techniques/T1590), such as which IP addresses are actively in use as well as more detailed information about hosts assigned these addresses. Scans may range from simple pings (ICMP requests and responses) to more nuanced scans that may reveal host software/versions via server banners or other network artifacts.(Citation: Botnet Scan) Information from these scans may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
