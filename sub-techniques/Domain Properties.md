---
id: 5c789445-8831-45b4-ac26-9f52d7684cae
name: Domain Properties
type: sub-technique
mitre_id: T1590.001
mitre_url: null
created_at: '2023-04-06T00:31:27.079540+00:00'
updated_at: '2023-04-06T00:31:27.079540+00:00'
parent_technique: '[[Gather Victim Network Information|T1590 - Gather Victim Network
  Information]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Domain Properties

**MITRE ID**: T1590.001

**Parent Technique**: [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

This is a sub-technique of T1590 - Gather Victim Network Information.

## Summary

Adversaries may gather information about the victim's network domain(s) that can be used during targeting. Information about domains and their properties may include a variety of details, including what domain(s) the victim owns as well as administrative data (ex: name, registrar, etc.) and more dir

## Description

Adversaries may gather information about the victim's network domain(s) that can be used during targeting. Information about domains and their properties may include a variety of details, including what domain(s) the victim owns as well as administrative data (ex: name, registrar, etc.) and more directly actionable information such as contacts (email addresses and phone numbers), business addresses, and name servers.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about victim domains and their properties may also be exposed to adversaries via online or other accessible data sets (ex: [WHOIS](https://attack.mitre.org/techniques/T1596/002)).(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Where third-party cloud providers are in use, this information may also be exposed through publicly available API endpoints, such as GetUserRealm and autodiscover in Office 365 environments.(Citation: Azure Active Directory Reconnaisance)(Citation: Office 265 Azure Domain Availability) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596), [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593), or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
