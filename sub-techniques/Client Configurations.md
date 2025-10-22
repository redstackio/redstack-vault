---
id: 8b912e9e-a0a1-425d-b53c-a2cd99af2601
name: Client Configurations
type: sub-technique
mitre_id: T1592.004
mitre_url: null
created_at: '2023-04-06T00:31:26.377135+00:00'
updated_at: '2023-04-06T00:31:26.377135+00:00'
parent_technique: '[[Gather Victim Host Information|T1592 - Gather Victim Host Information]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Client Configurations

**MITRE ID**: T1592.004

**Parent Technique**: [[Gather Victim Host Information|T1592 - Gather Victim Host Information]]

This is a sub-technique of T1592 - Gather Victim Host Information.

## Summary

Adversaries may gather information about the victim's client configurations that can be used during targeting. Information about client configurations may include a variety of details and settings, including operating system/version, virtualization, architecture (ex: 32 or 64 bit), language, and/or 

## Description

Adversaries may gather information about the victim's client configurations that can be used during targeting. Information about client configurations may include a variety of details and settings, including operating system/version, virtualization, architecture (ex: 32 or 64 bit), language, and/or time zone.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) (ex: listening ports, server banners, user agent strings) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Adversaries may also compromise sites then include malicious content designed to collect host information from visitors.(Citation: ATT ScanBox) Information about the client configurations may also be exposed to adversaries via online or other accessible data sets (ex: job postings, network maps, assessment reports, resumes, or purchase invoices). Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [Supply Chain Compromise](https://attack.mitre.org/techniques/T1195) or [External Remote Services](https://attack.mitre.org/techniques/T1133)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]
