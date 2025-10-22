---
id: 48a55ee3-12b6-4174-888f-b3f2406e102d
name: DNS/Passive DNS
type: sub-technique
mitre_id: T1596.001
mitre_url: null
created_at: '2023-04-06T00:31:25.618259+00:00'
updated_at: '2023-04-06T00:31:25.618259+00:00'
parent_technique: '[[Search Open Technical Databases|T1596 - Search Open Technical
  Databases]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
procedures:
- '[[Subdomain Enumeration using Subfinder]]'
- '[[Subdomain Enumeration with Aquatone Scan]]'
---

# DNS/Passive DNS

**MITRE ID**: T1596.001

**Parent Technique**: [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

This is a sub-technique of T1596 - Search Open Technical Databases.

## Summary

Adversaries may search DNS data for information about victims that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts.

Adversaries may s

## Description

Adversaries may search DNS data for information about victims that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts.

Adversaries may search DNS data to gather actionable information. Threat actors can query nameservers for a target organization directly, or search through centralized repositories of logged DNS query responses (known as passive DNS).(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Adversaries may also seek and target DNS misconfigurations/leaks that reveal information about internal networks. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[Subdomain Enumeration using Subfinder]]
- [[Subdomain Enumeration with Aquatone Scan]]
