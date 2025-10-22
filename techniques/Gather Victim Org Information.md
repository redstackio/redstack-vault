---
id: 3a960175-dd97-493b-98c0-d79c2a652496
name: Gather Victim Org Information
type: technique
mitre_id: T1591
mitre_url: null
created_at: '2023-04-06T00:31:26.583820+00:00'
updated_at: '2023-04-06T00:31:27.810401+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Gather Victim Org Information

**MITRE ID**: T1591

## Description

Adversaries may gather information about the victim's organization that can be used during targeting. Information about an organization may include a variety of details, including the names of divisions/departments, specifics of business operations, as well as the roles and responsibilities of key employees.

Adversaries may gather this information in various ways, such as direct elicitation via [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about an organization may also be exposed to adversaries via online or other accessible data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation: ThreatPost Broadvoice Leak)(Citation: SEC EDGAR Search) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]
