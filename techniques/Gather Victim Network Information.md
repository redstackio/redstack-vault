---
id: f319a0f8-077f-4133-9c46-8954b033527c
name: Gather Victim Network Information
type: technique
mitre_id: T1590
mitre_url: null
created_at: '2023-04-06T00:31:26.622185+00:00'
updated_at: '2023-04-06T03:56:37.807452+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
procedures:
- '[[Azure Subdomain Enumeration]]'
- '[[DNS Reconnaissance with ADIDNS Search Commands]]'
- '[[Network Discovery - Spyse Reverse IP Lookup]]'
- '[[Spyse DNS Enumeration Procedure]]'
- '[[Spyse Subdomain Enumeration]]'
- '[[SSRF Enumeration via HTTP URL Scheme]]'
- '[[Subdomain Enumeration and Takeover using Hostile Subdomain Bruteforcer]]'
- '[[Subdomain Enumeration using AltDNS]]'
- '[[Subdomain Enumeration using Nmap and CRTSH Scan]]'
- '[[Subdomain Enumeration with Aquatone]]'
- '[[Subdomain Enumeration with DNS Dumpster]]'
- '[[Subdomain Enumeration with Findomain]]'
- '[[Subdomain Enumeration with Subbrute]]'
- '[[Sublist3r Subdomain Enumeration]]'
- '[[Web Enumeration and Backup File Discovery]]'
---

# Gather Victim Network Information

**MITRE ID**: T1590

## Description

Adversaries may gather information about the victim's networks that can be used during targeting. Information about networks may include a variety of details, including administrative data (ex: IP ranges, domain names, etc.) as well as specifics regarding its topology and operations.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about networks may also be exposed to adversaries via online or other accessible data sets (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)).(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

## Related Procedures (15)

- [[Azure Subdomain Enumeration]]
- [[DNS Reconnaissance with ADIDNS Search Commands]]
- [[Network Discovery - Spyse Reverse IP Lookup]]
- [[Spyse DNS Enumeration Procedure]]
- [[Spyse Subdomain Enumeration]]
- [[SSRF Enumeration via HTTP URL Scheme]]
- [[Subdomain Enumeration and Takeover using Hostile Subdomain Bruteforcer]]
- [[Subdomain Enumeration using AltDNS]]
- [[Subdomain Enumeration using Nmap and CRTSH Scan]]
- [[Subdomain Enumeration with Aquatone]]
- [[Subdomain Enumeration with DNS Dumpster]]
- [[Subdomain Enumeration with Findomain]]
- [[Subdomain Enumeration with Subbrute]]
- [[Sublist3r Subdomain Enumeration]]
- [[Web Enumeration and Backup File Discovery]]
