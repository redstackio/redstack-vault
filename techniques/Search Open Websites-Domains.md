---
id: 30e70a34-a8bd-49b8-b12d-27ae6a74e747
name: Search Open Websites/Domains
type: technique
mitre_id: T1593
mitre_url: null
created_at: '2023-04-06T00:31:26.654481+00:00'
updated_at: '2023-04-06T03:56:21.759464+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
procedures:
- '[[Azure O365 Email Enumeration]]'
- '[[Passive Recon and Information Gathering]]'
---

# Search Open Websites/Domains

**MITRE ID**: T1593

## Description

Adversaries may search freely available websites and/or domains for information about victims that can be used during targeting. Information about victims may be available in various online sites, such as social media, new sites, or those hosting information about business operations such as hiring or requested/rewarded contracts.(Citation: Cyware Social Media)(Citation: SecurityTrails Google Hacking)(Citation: ExploitDB GoogleHacking)

Adversaries may search in different online sites depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Phishing](https://attack.mitre.org/techniques/T1566)).

## Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

## Related Procedures (2)

- [[Azure O365 Email Enumeration]]
- [[Passive Recon and Information Gathering]]
