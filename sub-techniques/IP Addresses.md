---
id: da0ccd1d-2851-4efb-8423-6d3b33a61a26
name: IP Addresses
type: sub-technique
mitre_id: T1590.005
mitre_url: null
created_at: '2023-04-06T00:31:25.521937+00:00'
updated_at: '2023-04-06T00:31:25.521937+00:00'
parent_technique: '[[Gather Victim Network Information|T1590 - Gather Victim Network
  Information]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# IP Addresses

**MITRE ID**: T1590.005

**Parent Technique**: [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

This is a sub-technique of T1590 - Gather Victim Network Information.

## Summary

Adversaries may gather the victim's IP addresses that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses. Information about assigned IP addresses may include a variety of details, such as which IP addresses are in use. IP 

## Description

Adversaries may gather the victim's IP addresses that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses. Information about assigned IP addresses may include a variety of details, such as which IP addresses are in use. IP addresses may also enable an adversary to derive other details about a victim, such as organizational size, physical location(s), Internet service provider, and or where/how their publicly-facing infrastructure is hosted.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about assigned IP addresses may also be exposed to adversaries via online or other accessible data sets (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)).(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
