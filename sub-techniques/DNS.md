---
id: 43ed01a8-5797-4855-97fa-f272d04eb4fa
name: DNS
type: sub-technique
mitre_id: T1590.002
mitre_url: null
created_at: '2023-04-06T00:31:25.535375+00:00'
updated_at: '2023-04-06T00:31:25.535375+00:00'
parent_technique: '[[Gather Victim Network Information|T1590 - Gather Victim Network
  Information]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
procedures:
- '[[Subdomain Enumeration with Subbrute]]'
---

# DNS

**MITRE ID**: T1590.002

**Parent Technique**: [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

This is a sub-technique of T1590 - Gather Victim Network Information.

## Summary

Adversaries may gather information about the victim's DNS that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts. DNS, MX, TXT, and SPF 

## Description

Adversaries may gather information about the victim's DNS that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts. DNS, MX, TXT, and SPF records may also reveal the use of third party cloud and SaaS providers, such as Office 365, G Suite, Salesforce, or Zendesk.(Citation: Sean Metcalf Twitter DNS Records)

Adversaries may gather this information in various ways, such as querying or otherwise collecting details via [DNS/Passive DNS](https://attack.mitre.org/techniques/T1596/001). DNS information may also be exposed to adversaries via online or other accessible data sets (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)).(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596), [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593), or [Active Scanning](https://attack.mitre.org/techniques/T1595)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Subdomain Enumeration with Subbrute]]
